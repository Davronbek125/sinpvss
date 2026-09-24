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
    if (dots) dots.forEach(dot => dot.classList.remove('active'));
    
    slides[n].classList.add('active');
    if (dots && dots[n]) dots[n].classList.add('active');
}

// Modal / Contact Form Redirection
function openModal() {
    if (window.location.pathname.includes('_ru')) {
        window.location.href = "index_ru.html#contact-form";
    } else {
        window.location.href = "index.html#contact-form";
    }
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
    const targetTab = document.getElementById(tabName);
    if (targetTab) {
        targetTab.style.display = "block";
    }
    if (evt && evt.currentTarget) {
        evt.currentTarget.className += " active";
    }
}

// Lightbox Logic
function openLightbox(imageSrc) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    if (lightbox && lightboxImg) {
        lightbox.style.display = "block";
        lightboxImg.src = imageSrc;
        lightboxImg.alt = "Hujjat rasmi";
    }
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    if (lightbox) {
        lightbox.style.display = "none";
    }
}

// Contact Form Submission (Telegram & Email via send.php)
function sendToTelegram(e) {
    e.preventDefault();
    
    const nameEl = document.getElementById('name');
    const phoneEl = document.getElementById('phone');
    const serviceEl = document.getElementById('service');
    const messageEl = document.getElementById('message');
    const statusDiv = document.getElementById('formStatus');
    const submitBtn = e.target.querySelector('button[type="submit"]');
    
    const isRu = window.location.pathname.includes('_ru');
    
    const name = nameEl ? nameEl.value.trim() : '';
    const phone = phoneEl ? phoneEl.value.trim() : '';
    const service = serviceEl ? serviceEl.value.trim() : '';
    const message = messageEl ? messageEl.value.trim() : '';
    
    if (!name || !phone) {
        if (statusDiv) {
            statusDiv.innerHTML = isRu ? "Пожалуйста, заполните обязательные поля!" : "Iltimos, ism va telefon raqamingizni kiriting!";
            statusDiv.style.color = "#dc2626";
        }
        return;
    }
    
    if (statusDiv) {
        statusDiv.innerHTML = isRu ? "Отправка заявки..." : "Arizangiz yuborilmoqda...";
        statusDiv.style.color = "#0245cc";
    }
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.style.opacity = "0.7";
    }
    
    const formData = new FormData();
    formData.append('name', name);
    formData.append('phone', phone);
    formData.append('service', service);
    formData.append('message', message);
    
    fetch('send.php', {
        method: 'POST',
        body: formData
    })
    .then(async response => {
        let data = {};
        try {
            data = await response.json();
        } catch (e) {}
        if (response.ok || data.success || data.telegram) {
            return data;
        }
        throw new Error(data.message || 'Server javob bermadi');
    })
    .then(data => {
        if (data.success || data.telegram) {
            if (statusDiv) {
                statusDiv.innerHTML = isRu 
                    ? "✓ Ваша заявка успешно отправлена! Скоро мы свяжемся с вами." 
                    : "✓ Arizangiz muvaffaqiyatli qabul qilindi! Tez orada mutaxassislarimiz siz bilan bog'lanishadi.";
                statusDiv.style.color = "#16a34a";
            }
            const form = document.getElementById('tgForm');
            if (form) form.reset();
        } else {
            throw new Error(data.message || 'Xatolik yuz berdi');
        }
    })
    .catch(error => {
        console.error('Send error:', error);
        if (statusDiv) {
            statusDiv.innerHTML = isRu 
                ? "Произошла ошибка при отправке. Пожалуйста, позвоните нам напрямую." 
                : "Xatolik yuz berdi. Iltimos, bizga to'g'ridan-to'g'ri telefon orqali bog'laning.";
            statusDiv.style.color = "#dc2626";
        }
    })
    .finally(() => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.style.opacity = "1";
        }
    });
}


// Mobile Menu Logic
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');
const navBtn = document.querySelector('.nav-btn');
const mobileDropdowns = document.querySelectorAll('.dropdown');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = navLinks ? navLinks.classList.toggle('active') : false;
        if (navBtn) navBtn.classList.toggle('active');
        if (isOpen) {
            mobileMenuBtn.innerHTML = '&#10005;'; // ✕ icon
            mobileMenuBtn.setAttribute('aria-expanded', 'true');
        } else {
            mobileMenuBtn.innerHTML = '&#9776;'; // ☰ icon
            mobileMenuBtn.setAttribute('aria-expanded', 'false');
            mobileDropdowns.forEach(d => d.classList.remove('active'));
        }
    });
}

// Mobile Dropdown Tap Logic (Accordion toggle on mobile)
mobileDropdowns.forEach(dropdown => {
    const parentLink = dropdown.querySelector('a');
    if (parentLink) {
        parentLink.addEventListener('click', (e) => {
            if (window.innerWidth <= 992) {
                e.preventDefault();
                e.stopPropagation();
                const wasActive = dropdown.classList.contains('active');
                mobileDropdowns.forEach(d => d.classList.remove('active'));
                if (!wasActive) {
                    dropdown.classList.add('active');
                }
            }
        });
    }
});

// Auto-close mobile menu when clicking sub-links or regular nav links
const clickableNavLinks = document.querySelectorAll('.nav-links a:not(.dropdown > a), .dropdown-content a');
clickableNavLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 992 && navLinks) {
            navLinks.classList.remove('active');
            if (navBtn) navBtn.classList.remove('active');
            if (mobileMenuBtn) {
                mobileMenuBtn.innerHTML = '&#9776;';
                mobileMenuBtn.setAttribute('aria-expanded', 'false');
            }
            mobileDropdowns.forEach(d => d.classList.remove('active'));
        }
    });
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 992 && navLinks && navLinks.classList.contains('active')) {
        const navContainer = document.querySelector('.main-nav');
        if (navContainer && !navContainer.contains(e.target)) {
            navLinks.classList.remove('active');
            if (navBtn) navBtn.classList.remove('active');
            if (mobileMenuBtn) {
                mobileMenuBtn.innerHTML = '&#9776;';
                mobileMenuBtn.setAttribute('aria-expanded', 'false');
            }
            mobileDropdowns.forEach(d => d.classList.remove('active'));
        }
    }
});





// Smart Sticky Nav Logic (Faqat PC versiya uchun, mobil uchun menyu yuqoriga qadab qo'yilgan)
let lastScrollTop = 0;
const nav = document.querySelector('.main-nav');
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    if (!nav) return;
    
    // Mobil qurilmalarda menyu qalqib/yashirinmasdan yuqoriga qadab turadi (PCga tegmaydi)
    if (window.innerWidth <= 992) {
        nav.classList.remove('fixed-nav', 'hide-nav');
        document.body.style.paddingTop = '0px';
        return;
    }

    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Height of the white header (approx 140px)
    let headerHeight = header ? header.offsetHeight : 140;

    if (scrollTop > headerHeight) {
        // Fix the nav to the top of the window
        nav.classList.add('fixed-nav');
        document.body.style.paddingTop = nav.offsetHeight + 'px';
        
        if (scrollTop > lastScrollTop) {
            // Scrolling down -> hide nav
            nav.classList.add('hide-nav');
        } else {
            // Scrolling up -> show nav
            nav.classList.remove('hide-nav');
        }
    } else {
        // At the very top -> normal flow, visible
        nav.classList.remove('fixed-nav');
        nav.classList.remove('hide-nav');
        document.body.style.paddingTop = '0px';
    }
    lastScrollTop = scrollTop;
});

// Scroll Animations (Fade-Up)
const faders = document.querySelectorAll('.fade-up');
if (faders.length > 0) {
    const appearOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };
    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        });
    }, appearOptions);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
}
