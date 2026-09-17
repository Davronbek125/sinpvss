# SINOV SERTIFIQAT SERVIS (sinovss.uz) — MODERNIZATSIYA VA QAYTA ISHLAB CHIQISH BO‘YICHA TO‘LIQ TEXNIK TOPSHIRIQ (SPECIFICATION)

Ushbu hujjat **https://www.sinovss.uz** saytini **https://uztest.uz** andozasida zamonaviy, ishonchli va yuqori konversiyali qilib modernizatsiya qilish bo‘yicha to‘liq texnik ko‘rsatma (blueprint) hisoblanadi.

---

## 1. LOYIHA HAQIDA VA ASOSIY MAQSAD

* **Tashkilot nomi:** «SINOV SERTIFIQAT SERVIS» MChJ.
* **Faoliyat yo‘nalishi:** Qurilish materiallari va konstruksiyalarini akkreditatsiyalangan sinov laboratoriyasida sinovdan o‘tkazish (O‘zDSt ISO/IEC 17025) hamda O‘zbekiston Milliy sertifikatlashtirish tizimida mahsulotlarni sertifikatlash.
* **Asosiy vazifa:** 
  1. Hozirgi `sinovss.uz`ning eskirgan shakli (dizayni)ni `uztest.uz` kabi zamonaviy, nufuzli davlat va xalqaro andozalarga mos shaklga o‘tkazish.
  2. Ranglar gammasini eskirgan qizil/ko‘kdan zamonaviy korporativ to‘q ko‘k (Navy Blue) va oqqa o‘zgartirish.
  3. Xodimlar qismida faqat haqiqiy xodim: **Д.Я. Мадримова — Директор** ma’lumotini rasmiy shaklda joylashtirish.
  4. Qolgan barcha ma’lumotlar, akkreditatsiyalar, mahsulotlar va rekvizitlarni to‘liq saqlash.

---

## 2. MANBALAR VA MA’LUMOTLAR TAQSIMOTI

| Ma’lumot turi | Qayerdan olinadi? | Aniq tafsilotlar |
| :--- | :--- | :--- |
| **Dizayn, shakl va bloklar** | `https://uztest.uz` | Split-ekranli slayder, statistika hisoblagichlari, interaktiv tablar, nufuzli Header/Footer |
| **Ranglar palitrasi** | `uztest.uz` andozasida | `#003399` (To‘q ko‘k), `#0077CC` (Moviy), `#FFFFFF` (Oq), `#F4F7FA` (Yumshoq fon) |
| **Xizmatlar va Akkreditatsiya** | `https://www.sinovss.uz` | № O'ZAK.MS.0029 (Sertifikatlashtirish), № O'ZAK.SL.0154 (Laboratoriya) |
| **Mahsulotlar katalogi** | `https://www.sinovss.uz/cert.html` | G‘isht, beton, quruq qorishmalar, shag‘al, qum, marmar, temir-beton konstruksiyalar |
| **Hujjatlar va fayllar** | `https://www.sinovss.uz/` | `zayavka.pdf`, `jalob.docx`, `2-УТВЕРЖДАЮ.docx`, `sxema.jpg`, `akk.jpg` |
| **Jamoa / Xodimlar** | `https://www.sinovss.uz/` | Faqat: **Д.Я. Мадримова — Директор** (rasmi: `img/women.jpg`) |
| **Tashkilot rekvizitlari** | `https://www.sinovss.uz/` | Xorazm viloyati, Tuproqqal’a tumani, Xalqlar do‘stligi ko‘chasi, 10/3-uy. Tel: `+998 88 100 28 69, +998 99 335 07 70` |

---

## 3. TEXNOLOGIK STEK (TECH STACK)

* **Platforma:** WordPress (Eng so‘nggi barqaror versiya).
* **Mavzu (Theme):** `Hello Elementor` (Ultra-yengil, ortiqcha shablon kodlarisiz).
* **Vizual konstruktor:** `Elementor Pro` + `Jeg Elementor Kit (JKit)`.
* **Ko‘p tillilik (Multilingual):** `Polylang` (UZ va RU tillari uchun).
* **Formalar va Ariza qabuli:** `Fluent Forms` yoki `Elementor Forms`.
* **Xabarnomalar:** Telegram Bot API (har bir arizani Telegram guruhga yuborish).
* **Kesh va tezlik:** `LiteSpeed Cache` / `WP Rocket` + WebP rasm konvertatsiyasi.

---

## 4. DIZAYN TIZIMI VA RANGLAR (DESIGN SYSTEM)

```css
:root {
  /* Asosiy ranglar */
  --primary-navy: #003399;      /* Asosiy to‘q ko‘k (UzTest sarlavhalar va header) */
  --primary-dark: #0b2265;      /* Chuqur ko‘k (tugmalar hover holati va footer) */
  --accent-blue: #0077cc;       /* Yorqin moviy (tugmalar, aktiv linklar) */
  --accent-light: #e8f1fd;      /* Ochiq havorang (kartalar va tablar foni) */

  /* Fon va neytral ranglar */
  --bg-white: #ffffff;          /* Asosiy toza oq */
  --bg-light: #f8fafc;          /* Seksiyalar ajratuvchi yumshoq fon */
  --border-color: #e2e8f0;      /* Kartalar va jadvallar chegarasi */

  /* Matn ranglari */
  --text-primary: #0f172a;      /* Bosh matnlar (yuqori kontrast) */
  --text-secondary: #475569;    /* Qo‘shimcha tavsiflar va sanalar */
  --text-muted: #94a3b8;        /* Ikkinchi darajali belgilar */

  /* Shriftlar */
  --font-heading: 'Roboto Condensed', sans-serif;
  --font-body: 'Roboto', sans-serif;
}
```

---

## 5. SAHIFALAR VA BLOKLAR STRUKTURASI (WIREFRAME)

### 5.1. Header (Yuqori qism — UzTest andozasida)
1. **Top-bar (Kichik yuqori qator):**
   * Ish vaqti: `Dushanba - Juma: 09:00 - 17:00 | Shanba: 09:00 - 14:00`
   * Telefon: `+998 88 100 28 69, +998 99 335 07 70`
   * Email: `info@sinovss.uz`
   * Til tanlash: `[UZ] [RU]`
2. **Asosiy Navigatsiya paneli:**
   * Logotip: «SINOV SERTIFIQAT SERVIS» (vektor/yuqori sifatli).
   * Menyu bandlari:
     * *Bosh sahifa*
     * *Sertifikatlashtirish*
     * *Sinov laboratoriyasi*
     * *Xizmatlar va narxlar*
     * *Hujjatlar va Ochiq ma’lumotlar*
     * *Aloqa*
   * Tugma: **«Ariza qoldirish»** (Modal oynani ochadi).

---

### 5.2. Bosh sahifa bloklari ketma-ketligi (Homepage Blocks)

#### 1-Blok: Hero Slider (Katta asosiy slayder)
* **1-slayd:**
  * Kichik sarlavha: `AKKREDITATSIYALANGAN SINOV LABORATORIYASI (O'ZAK.SL.0154)`
  * Asosiy sarlavha: **Qurilish materiallari va konstruksiyalarini sifatli sinovdan o‘tkazish**
  * Tavsif: O‘zbekistonda ishlab chiqarilayotgan va chetdan keltirilayotgan qurilish materiallarining xavfsizlik va sifat standartlariga muvofiqligini sinash.
  * Tugmalar: `[Ariza topshirish]` (ko‘k fon) va `[Laboratoriya haqida]` (shaffof hoshiyali).
* **2-slayd:**
  * Kichik sarlavha: `SERTIFIKATLASHTIRISH ORGANI (O'ZAK.MS.0029)`
  * Asosiy sarlavha: **Qurilish mahsulotlarini milliy tizimda sertifikatlash**
  * Tavsif: Mahsulot partiyalariga va seriyali ishlab chiqarishga muvofiqlik sertifikatlarini rasmiylashtirish.
  * Tugmalar: `[Sertifikatlash sxemalari]` va `[Arizani yuklab olish]`.

#### 2-Blok: Jonli Statistika (Fun Facts Counters)
* Kartalar (4 ta ustun):
  * **10+ yil** — Sohadagi muvaffaqiyatli faoliyat tajribasi
  * **15+** — Akkreditatsiyalangan qurilish materiallari yo‘nalishlari
  * **100%** — O‘zDSt ISO/IEC 17025 talablariga to‘liq muvofiqlik
  * **Tezkor** — Qisqa muddatlarda rasmiy sinov bayonnomalari

#### 3-Blok: Sinov va Sertifikatlash mahsulotlari (Interaktiv Tablar)
* `sinovss.uz/cert.html`dagi ro‘yxat asosida 4 ta toifaga ajratiladi:
  * **1-Tab (Devorbop materiallar):** Keramika g‘ishtlari, beton devor toshlari, yacheykali beton bloklari.
  * **2-Tab (Qorishmalar va bog‘lovchilar):** Og‘ir va mayda donali betonlar, qurilish eritmalari, quruq qurilish aralashmalari.
  * **3-Tab (Qazilma va pardozlash toshlari):** Tabiiy tosh buyumlari (mramor, granit), maydalangan qum, tabiiy qum, shag‘al.
  * **4-Tab (Konstruksiya va plitalar):** Keramika plitalari, beton yo‘lka (bruschatka) plitalari, temir-beton buyumlari.
* *Har bir toifada:* Qisqa ta’rif + «Sinovga ariza berish» tugmasi.

#### 4-Blok: Akkreditatsiya va Davlat guvohnomalari
* Hozirgi `sinovss.uz`dagi `img/akk.jpg`, `img/guvohnoma.jpg`, `img/guvohnomauz.jpg`, `img/sxem.jpg` rasmlari.
* Chiroyli ramkada Lightbox (bosganda ekranda kattalashib ochiladigan) qilib qo‘yiladi.
* Pastida `[Akkreditatsiya doirasini yuklab olish (PDF)]` havolasi.

#### 5-Blok: Rahbariyat / Xodimlar (Team Showcase)
* Foydalanuvchi ko‘rsatmasi bo‘yicha **faqat mavjud xodim**:
  * **F.I.Sh:** Д.Я. Мадримова
  * **Lavozimi:** Директор
  * **Fotosurat:** `img/women.jpg` (zamonaviy neytral fonli ramkada)
  * **Kompaniya:** ООО «SINOV SERTIFIQAT SERVIS»
* Karta dizayni: Markazlashtirilgan, nufuzli korporativ karta.

#### 6-Blok: Ariza topshirish va Qayta aloqa formasi
* Sarlavha: **Sertifikatlashtirish yoki sinov uchun ariza qoldiring**
* Kichik matn: *Mutaxassislarimiz 15 daqiqa ichida siz bilan bog‘lanib, sinov muddati va narxlar bo‘yicha ma’lumot beradi.*
* Maydonlar:
  1. *F.I.Sh / Korxona nomi* (Majburiy)
  2. *Telefon raqami* (`+998` maskasi bilan, majburiy)
  3. *Xizmat turi* (Sertifikatlashtirish / Laboratoriya sinovi tanlovi)
  4. *Xabar / Mahsulot tavsifi*
  5. *«Arizani yuborish»* tugmasi.

#### 7-Blok: Interaktiv Lokatsiya va Aloqa (Footer tepasida)
* Xorazm viloyati, Tuproqqal’a tumani xaritasi (Yandex/Google Map iframe).
* Manzil, telefon, ish vaqtlari aniq ko‘rsatilgan vizual kartochka.

#### 8-Blok: Footer (Pastki qism)
* Rasmiy ma’lumotlar, litsenziyalar ro‘yxati, tezkor havolalar, mualliflik huquqi (`© 2026 sinovss.uz. Barcha huquqlar himoyalangan.`).

---

## 6. TELEGRAM BILDIRISHNOMA INTEGRATSIYASI (KODLASH UCHUN QO‘LLANMA)

Sayt shakllari to‘ldirilganda ma’lumotlar quyidagi parametrlar asosida Telegram botga uzatiladi:

* **Endpoint:** `https://api.telegram.org/bot<BOT_TOKEN>/sendMessage`
* **Format:** HTML / Markdown
* **Xabar shabloni:**
```text
🔔 YANGI ARIZA (sinovss.uz):
━━━━━━━━━━━━━━━━━━━━
👤 Buyurtmachi: {name}
📞 Telefon: {phone}
🏗 Xizmat turi: {service_type}
📝 Izoh: {message}
📅 Vaqt: {current_time}
```

---

## 7. ISHLAB CHIQUVCHI (DEVELOPER) UCHUN QADAMMA-QADAM KO‘RSATMALAR

1. **Tayyorgarlik:**
   * `sinovss.uz` dagi mavjud barcha rasmlarni (`img/` papkasi) va hujjatlarni (`docs/` papkasi: `zayavka.pdf`, `jalob.docx`, `2-УТВЕРЖДАЮ.docx`) to‘liq yuklab olib, loyiha media-bazasiga kiritish.
2. **WordPress sozlamalari:**
   * Elementor global ranglari (`#003399`, `#0077CC`, `#FFFFFF`, `#F8FAFC`) va `Roboto` shriftini kiritish.
3. **Header/Footer yaratish:**
   * Elementor Theme Builder orqali Header va Footerni yaratish.
4. **Bosh sahifani yig‘ish:**
   * Yuqoridagi 8 ta blok ketma-ketligida sahifani Elementor orqali to‘liq terish.
5. **Ichki sahifalar:**
   * `cert.html` -> `/sertifikatlashtirish/`
   * `isp.html` -> `/sinov-laboratoriyasi/`
   * `price.html` -> `/narxlar/`
   * Barcha sahifalardagi yuklab olinuvchi PDF/Word fayllar havolalarini yangi joylashuvga to‘g‘rilash.
6. **Xodimlar tekshiruvi:**
   * Faqat «Д.Я. Мадримова — Директор» kartasi mavjudligini tasdiqlash.
7. **Sinov:**
   * Smartfon ekranida (375px - 430px) qulaylikni tekshirish, arizani Telegramga yuborib test qilish.
