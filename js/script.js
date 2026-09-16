document.addEventListener('DOMContentLoaded', () => {
    console.log('SINOV SERTIFIQAT SERVIS - Sayt yuklandi');

    initSlider();
});

// Slider Logic
let slideIndex = 0;
let slides, dots;

function initSlider() {
    slides = document.querySelectorAll('.slide');
    dots = document.querySelectorAll('.dot');
    if (slides.length > 0) {
        showSlide(slideIndex);
        // Optional: auto slide every 5 seconds
        setInterval(() => {
            moveSlide(1);
        }, 5000);
    }
}

function moveSlide(n) {
    slideIndex += n;
    if (slideIndex >= slides.length) slideIndex = 0;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    showSlide(slideIndex);
}

function currentSlide(n) {
    slideIndex = n;
    showSlide(slideIndex);
}

function showSlide(n) {
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));
    
    slides[n].classList.add('active');
    dots[n].classList.add('active');
}

// Modal Placeholder
function openModal() {
    window.location.href = "index.html#contact-form";
}

// Stats Counter Animation
const counters = document.querySelectorAll('.stat-number');
const speed = 200; // The lower the slower

const animateCounters = () => {
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const inc = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target;
            }
        };
        updateCount();
    });
}

// Start animation when scrolled into view (simple version)
let animated = false;
window.addEventListener('scroll', () => {
    const statsSection = document.querySelector('.stats-section');
    if (statsSection && !animated) {
        const sectionPos = statsSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight;
        if (sectionPos < screenPos) {
            animateCounters();
            animated = true;
        }
    }
});

// Tabs Logic
function openTab(evt, tabName) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab-btn");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Lightbox Logic
function openLightbox(imageSrc) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    
    // Check if the image source exists (for placeholder sake, we will just show the modal)
    // In a real scenario, this would load the actual image.
    lightbox.style.display = "block";
    lightboxImg.src = imageSrc;
    lightboxImg.alt = "Akkreditatsiya hujjati";
}

function closeLightbox() {
    document.getElementById('lightbox').style.display = "none";
}

// Telegram Integration
function sendToTelegram(e) {
    e.preventDefault();
    
    // Replace these placeholders with your actual Bot Token and Chat ID
    const botToken = '<BOT_TOKEN>';
    const chatId = '<CHAT_ID>';
    
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    const service = document.getElementById('service').value;
    const message = document.getElementById('message').value;
    
    const currentTime = new Date().toLocaleString();
    
    const text = `🔔 YANGI ARIZA (sinovss.uz):\n━━━━━━━━━━━━━━━━━━━━\n👤 Buyurtmachi: ${name}\n📞 Telefon: ${phone}\n🏗 Xizmat turi: ${service}\n📝 Izoh: ${message}\n📅 Vaqt: ${currentTime}`;
    
    const statusDiv = document.getElementById('formStatus');
    statusDiv.innerHTML = "Yuborilmoqda...";
    statusDiv.style.color = "var(--primary-navy)";
    
    if(botToken === '<BOT_TOKEN>') {
        statusDiv.innerHTML = "Xatolik: Telegram bot ulanganicha yo'q. (Placeholder o'zgartirilmagan)";
        statusDiv.style.color = "red";
        return;
    }

    const url = `https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatId}&text=${encodeURIComponent(text)}`;

    fetch(url)
        .then(response => {
            if(response.ok) {
                statusDiv.innerHTML = "Arizangiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz.";
                statusDiv.style.color = "green";
                document.getElementById('tgForm').reset();
            } else {
                statusDiv.innerHTML = "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.";
                statusDiv.style.color = "red";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            statusDiv.innerHTML = "Xatolik yuz berdi. Internet ulanishini tekshiring.";
            statusDiv.style.color = "red";
        });
}
