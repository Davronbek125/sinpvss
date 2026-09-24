<?php
/**
 * SINOV SERTIFIQAT SERVIS (sinovss.uz)
 * Arizalarni Telegram va Email pochtaga yuborish skripti
 */

ini_set('display_errors', 0);
error_reporting(0);

header('Content-Type: application/json; charset=utf-8');

// =========================================================================
// 1. SOZLAMALAR (TELEGRAM BOT VA EMAIL)
// =========================================================================

// BotFather bergan bot tokenini shu yerga yozing:
$botToken = '8762355210:AAEkU1XXw_mPDaUaAwLX36_qDZ8be2k-b4M';

// Xabarlar borishi kerak bo'lgan Telegram guruh yoki kanal Chat ID sini yozing:
// (Guruh ID lari odatda -100 bilan boshlanadi, masalan: '-1001234567890')
$chatId = '-1004301229429';

// Buyurtma nusxasi boradigan elektron pochta manzili:
$adminEmail = 'elyormadirimov@gmail.com';

// =========================================================================
// 2. SO'ROVNI TEKSHIRISH VA MA'LUMOTLARNI QABUL QILISH
// =========================================================================

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode([
        'success' => false,
        'message' => 'Faqat POST so\'rovlar qabul qilinadi.'
    ]);
    exit;
}

// JSON yoki FormData orqali kelgan ma'lumotlarni o'qish
$input = $_POST;
if (empty($input)) {
    $rawInput = file_get_contents('php://input');
    $input = json_decode($rawInput, true) ?? [];
}

$name    = isset($input['name']) ? trim(strip_tags($input['name'])) : '';
$phone   = isset($input['phone']) ? trim(strip_tags($input['phone'])) : '';
$service = isset($input['service']) ? trim(strip_tags($input['service'])) : 'Ko\'rsatilmadi';
$message = isset($input['message']) ? trim(strip_tags($input['message'])) : 'Izoh qoldirilmadi';

if (empty($name) || empty($phone)) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'message' => 'Ism va telefon raqami kiritilishi shart!'
    ]);
    exit;
}

// Vaqt mintaqasi (Toshkent vaqti)
date_default_timezone_set('Asia/Tashkent');
$currentTime = date('d.m.Y H:i:s');
$userIp = $_SERVER['REMOTE_ADDR'] ?? 'Noma\'lum';

$telegramSuccess = false;
$mailSuccess = false;

// =========================================================================
// 3. TELEGRAMGA YUBORISH
// =========================================================================

try {
    if (!empty($botToken) && !empty($chatId)) {
        $tgMessage = "🔔 <b>YANGI ARIZA (sinovss.uz)</b>\n";
        $tgMessage .= "━━━━━━━━━━━━━━━━━━━━\n";
        $tgMessage .= "👤 <b>Mijoz:</b> " . htmlspecialchars($name, ENT_QUOTES, 'UTF-8') . "\n";
        $tgMessage .= "📞 <b>Telefon:</b> " . htmlspecialchars($phone, ENT_QUOTES, 'UTF-8') . "\n";
        $tgMessage .= "🏗 <b>Xizmat:</b> " . htmlspecialchars($service, ENT_QUOTES, 'UTF-8') . "\n";
        $tgMessage .= "📝 <b>Izoh:</b> " . htmlspecialchars($message, ENT_QUOTES, 'UTF-8') . "\n";
        $tgMessage .= "━━━━━━━━━━━━━━━━━━━━\n";
        $tgMessage .= "📅 <b>Vaqt:</b> {$currentTime}\n";
        $tgMessage .= "🌐 <b>IP:</b> {$userIp}";

        $tgUrl = "https://api.telegram.org/bot{$botToken}/sendMessage";
        $postFields = [
            'chat_id'    => $chatId,
            'text'       => $tgMessage,
            'parse_mode' => 'HTML',
            'disable_web_page_preview' => true
        ];

        if (function_exists('curl_init')) {
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $tgUrl);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postFields));
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_TIMEOUT, 10);
            $tgResponse = curl_exec($ch);
            curl_close($ch);
            
            $tgResDecoded = json_decode($tgResponse, true);
            if (isset($tgResDecoded['ok']) && $tgResDecoded['ok'] === true) {
                $telegramSuccess = true;
            }
        } else {
            $context = stream_context_create([
                'http' => [
                    'method'  => 'POST',
                    'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                    'content' => http_build_query($postFields),
                    'timeout' => 10
                ]
            ]);
            $tgResponse = @file_get_contents($tgUrl, false, $context);
            if ($tgResponse) {
                $tgResDecoded = json_decode($tgResponse, true);
                if (isset($tgResDecoded['ok']) && $tgResDecoded['ok'] === true) {
                    $telegramSuccess = true;
                }
            }
        }
    }
} catch (\Throwable $e) {
    $telegramSuccess = false;
}

// =========================================================================
// 4. EMAIL POCHTAGA YUBORISH
// =========================================================================

try {
    if (!empty($adminEmail) && function_exists('mail')) {
        $mailSubject = "=?UTF-8?B?" . base64_encode("Yangi ariza: {$name} (sinovss.uz)") . "?=";
        
        $mailBody = '
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Yangi ariza</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; }
                .card { max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; }
                .header { background: #0245cc; color: #ffffff; padding: 20px; text-align: center; }
                .header h2 { margin: 0; font-size: 20px; }
                .content { padding: 25px; }
                .row { margin-bottom: 15px; border-bottom: 1px solid #edf2f7; padding-bottom: 10px; }
                .row:last-child { border-bottom: none; }
                .label { font-size: 13px; color: #64748b; font-weight: bold; text-transform: uppercase; margin-bottom: 4px; }
                .value { font-size: 16px; color: #0f172a; }
                .footer { background: #f8fafc; padding: 15px; text-align: center; font-size: 12px; color: #94a3b8; }
            </style>
        </head>
        <body>
            <div class="card">
                <div class="header">
                    <h2>🔔 SINOV SERTIFIQAT SERVIS - Yangi ariza</h2>
                </div>
                <div class="content">
                    <div class="row">
                        <div class="label">Mijoz / Tashkilot:</div>
                        <div class="value">' . htmlspecialchars($name, ENT_QUOTES, 'UTF-8') . '</div>
                    </div>
                    <div class="row">
                        <div class="label">Telefon raqami:</div>
                        <div class="value"><a href="tel:' . htmlspecialchars($phone, ENT_QUOTES, 'UTF-8') . '">' . htmlspecialchars($phone, ENT_QUOTES, 'UTF-8') . '</a></div>
                    </div>
                    <div class="row">
                        <div class="label">Xizmat turi:</div>
                        <div class="value">' . htmlspecialchars($service, ENT_QUOTES, 'UTF-8') . '</div>
                    </div>
                    <div class="row">
                        <div class="label">Izoh / Mahsulot tavsifi:</div>
                        <div class="value">' . nl2br(htmlspecialchars($message, ENT_QUOTES, 'UTF-8')) . '</div>
                    </div>
                    <div class="row">
                        <div class="label">Kelgan vaqti:</div>
                        <div class="value">' . $currentTime . '</div>
                    </div>
                </div>
                <div class="footer">
                    Xat avtomatik ravishda <b>sinovss.uz</b> sayti orqali yuborildi.
                </div>
            </div>
        </body>
        </html>';

        $headers = [];
        $headers[] = 'MIME-Version: 1.0';
        $headers[] = 'Content-type: text/html; charset=UTF-8';
        $headers[] = 'From: SINOV SERTIFIQAT SERVIS <no-reply@sinovss.uz>';
        $headers[] = 'X-Mailer: PHP/' . phpversion();

        $mailSuccess = @mail($adminEmail, $mailSubject, $mailBody, implode("\r\n", $headers));
    }
} catch (\Throwable $e) {
    $mailSuccess = false;
}

// =========================================================================
// 5. JAVOB QAYTARISH
// =========================================================================

$isSuccess = $telegramSuccess || $mailSuccess;

http_response_code(200);
echo json_encode([
    'success'  => $isSuccess,
    'telegram' => $telegramSuccess,
    'email'    => $mailSuccess,
    'message'  => $isSuccess ? 'Arizangiz muvaffaqiyatli qabul qilindi!' : 'Xatolik yuz berdi'
]);
exit;
