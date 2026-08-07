/* ==========================================================
    CUSTOM CURSOR
========================================================== */

const cursor = document.getElementById("cursor");
const ring = document.getElementById("cursor-ring");

let mouseX = window.innerWidth / 2;
let mouseY = window.innerHeight / 2;

let ringX = mouseX;
let ringY = mouseY;

document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

function animateCursor() {

    cursor.style.left = mouseX + "px";
    cursor.style.top = mouseY + "px";

    ringX += (mouseX - ringX) * 0.15;
    ringY += (mouseY - ringY) * 0.15;

    ring.style.left = ringX + "px";
    ring.style.top = ringY + "px";

    requestAnimationFrame(animateCursor);
}

animateCursor();


/* ==========================================================
    PARTICLE BACKGROUND
========================================================== */

const canvas = document.getElementById("bg");
const ctx = canvas.getContext("2d");

let width;
let height;

let particles = [];

const colors = [
    "0,212,255",
    "123,47,255",
    "26,110,255"
];

function resizeCanvas() {

    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;

}

window.addEventListener("resize", () => {

    resizeCanvas();
    createParticles();

});

resizeCanvas();


/* ==========================================================
    PARTICLES
========================================================== */

class Particle {

    constructor() {

        this.reset();

    }

    reset() {

        this.x = Math.random() * width;
        this.y = Math.random() * height;

        this.radius = Math.random() * 2 + 1;

        this.speedX = (Math.random() - 0.5) * 0.45;
        this.speedY = (Math.random() - 0.5) * 0.45;

        this.color =
            colors[Math.floor(Math.random() * colors.length)];

    }

    move() {

        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x < 0) this.x = width;
        if (this.x > width) this.x = 0;

        if (this.y < 0) this.y = height;
        if (this.y > height) this.y = 0;

    }

    draw() {

        ctx.beginPath();

        ctx.arc(
            this.x,
            this.y,
            this.radius,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = `rgba(${this.color},0.75)`;

        ctx.fill();

    }

}


/* ==========================================================
    CREATE PARTICLES
========================================================== */

function createParticles() {

    particles = [];

    const amount = Math.min(
        Math.floor(width * height / 18000),
        90
    );

    for (let i = 0; i < amount; i++) {

        particles.push(
            new Particle()
        );

    }

}

createParticles();


/* ==========================================================
    CONNECT LINES
========================================================== */

function drawConnections() {

    for (let i = 0; i < particles.length; i++) {

        for (let j = i + 1; j < particles.length; j++) {

            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;

            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 140) {

                const opacity = (140 - distance) / 140;

                ctx.beginPath();

                ctx.moveTo(
                    particles[i].x,
                    particles[i].y
                );

                ctx.lineTo(
                    particles[j].x,
                    particles[j].y
                );

                ctx.strokeStyle =
                    `rgba(0,212,255,${opacity * 0.12})`;

                ctx.lineWidth = 1;

                ctx.stroke();

            }

        }

    }

}


/* ==========================================================
    MOUSE GLOW
========================================================== */

function drawMouseGlow() {

    const gradient =
        ctx.createRadialGradient(
            mouseX,
            mouseY,
            0,
            mouseX,
            mouseY,
            180
        );

    gradient.addColorStop(
        0,
        "rgba(0,212,255,.10)"
    );

    gradient.addColorStop(
        1,
        "rgba(0,212,255,0)"
    );

    ctx.fillStyle = gradient;

    ctx.fillRect(
        0,
        0,
        width,
        height
    );

}


/* ==========================================================
    MAIN LOOP
========================================================== */

function animate() {

    ctx.clearRect(
        0,
        0,
        width,
        height
    );

    drawMouseGlow();

    particles.forEach((particle) => {

        particle.move();
        particle.draw();

    });

    drawConnections();

    requestAnimationFrame(animate);

}

animate();


/* ==========================================================
    BUTTON EFFECT
========================================================== */

document
.querySelectorAll(".btn")
.forEach(button => {

    button.addEventListener("mouseenter", () => {

        button.style.transform =
            "translateY(-4px) scale(1.03)";

    });

    button.addEventListener("mouseleave", () => {

        button.style.transform =
            "translateY(0) scale(1)";

    });

});


/* ==========================================================
    HERO CARD TILT
========================================================== */

const heroCard =
    document.querySelector(".hero-card");

heroCard.addEventListener("mousemove", (e) => {

    const rect =
        heroCard.getBoundingClientRect();

    const x =
        (e.clientX - rect.left) / rect.width - 0.5;

    const y =
        (e.clientY - rect.top) / rect.height - 0.5;

    heroCard.style.transform = `
        perspective(1000px)
        rotateY(${x * 8}deg)
        rotateX(${-y * 8}deg)
        translateY(-4px)
    `;

});

heroCard.addEventListener("mouseleave", () => {

    heroCard.style.transform = `
        perspective(1000px)
        rotateX(0deg)
        rotateY(0deg)
        translateY(0)
    `;

});

/* ===========================
   REGISTER PAGE
=========================== */

const password =
document.querySelector("#password");

const toggle =
document.querySelector(".toggle-password");

const bar =
document.querySelector("#strengthBar");

if(password){

    toggle.addEventListener("click",()=>{

        password.type =
        password.type==="password"
        ?"text"
        :"password";

        toggle.textContent =
        password.type==="password"
        ?"👁"
        :"🙈";

    });

    password.addEventListener("input",()=>{

        const value=password.value;

        let score=0;

        if(value.length>=8) score++;
        if(/[A-Z]/.test(value)) score++;
        if(/[0-9]/.test(value)) score++;
        if(/[^A-Za-z0-9]/.test(value)) score++;

        const widths=[
            "0%",
            "25%",
            "50%",
            "75%",
            "100%"
        ];

        const colors=[
            "#444",
            "#ff5f73",
            "#ffb347",
            "#00D4FF",
            "#00E5A0"
        ];

        bar.style.width=widths[score];
        bar.style.background=colors[score];

    });

}

/* ==========================================================
   DISMISS ALERT
========================================================== */

document.querySelectorAll(".close").forEach(button => {

    button.addEventListener("click", () => {

        const alert = button.closest(".alert");

        if (!alert) return;

        alert.style.transition = "opacity .25s ease";
        alert.style.opacity = "0";

        setTimeout(() => alert.remove(), 250);

    });

});


/* ==========================================================
   LANG TOGGLE
========================================================== */
window.AA = window.AA || {};
AA.translations = {
    en: {},
    fa: {},
};
AA.currentLang = localStorage.getItem('aa_lang') || 'en';
AA.applyLang = function (lang) {
    AA.currentLang = lang; localStorage.setItem('aa_lang', lang);
    const t = AA.translations[lang], html = document.documentElement;
    html.setAttribute('dir', lang === 'fa' ? 'rtl' : 'ltr');
    html.setAttribute('lang', lang === 'fa' ? 'fa' : 'en');
    document.querySelectorAll('[data-i18n]').forEach(el => { const k = el.getAttribute('data-i18n'); if (t[k] !== undefined) el.innerHTML = t[k]; });
    document.body.style.opacity = '0'; document.body.style.transition = 'opacity .2s';
    requestAnimationFrame(() => { document.body.style.opacity = '1'; });
    const btnEN = document.getElementById('btnEN'), btnFA = document.getElementById('btnFA'), slider = document.getElementById('langSlider');
    if (lang === 'en') { btnEN.classList.add('active'); btnFA.classList.remove('active'); slider.style.transform = 'translateX(0)'; slider.style.width = btnEN.offsetWidth + 'px'; }
    else { btnFA.classList.add('active'); btnEN.classList.remove('active'); slider.style.transform = `translateX(${btnEN.offsetWidth}px)`; slider.style.width = btnFA.offsetWidth + 'px'; }
};
AA.toggleLang = function () { AA.applyLang(AA.currentLang === 'en' ? 'fa' : 'en'); };
window.addEventListener('load', () => {
    const btnEN = document.getElementById('btnEN'), slider = document.getElementById('langSlider');
    if (btnEN && slider) slider.style.width = btnEN.offsetWidth + 'px';
    AA.applyLang(AA.currentLang);
});
