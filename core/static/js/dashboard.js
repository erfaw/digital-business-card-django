
/*
const DEFAULTS = {
  name: 'علی ستارزاده', title: 'بنیان‌گذار و مدیرعامل', dept: 'مهندسی · محصول · چشم‌انداز',
  company: 'فناوری', tagline: 'کمال آن چیزی‌ست که ارائه می‌دهیم',
  email: 'sodeep@aa-tech.io', phone: '+49 30 1234 5678',
  website: 'aa-tech.io', websiteUrl: 'https://aa-tech.io',
  linkedin: 'linkedin.com/in/sodeep', linkedinUrl: 'https://linkedin.com/in/sodeep',
  location: 'برلین، آلمان', response: 'ظرف ۲۴ ساعت'
};
*/
const DEFAULTS = {
    name: '', title: '', dept: '',
    company: '', tagline: '',
    email: '', phone: '',
    website: '', websiteUrl: '',
    linkedin: '', linkedinUrl: '',
    location: '', response: ''
};
const STORAGE_KEY = 'aa_card_data';
const fields = Object.keys(DEFAULTS);
let dirty = false;

function load() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? { ...DEFAULTS, ...JSON.parse(raw) } : { ...DEFAULTS };
    } catch (e) { return { ...DEFAULTS }; }
}

function fillForm(data) {
    fields.forEach(k => {
        const el = document.getElementById('f_' + k);
        if (el) el.value = data[k];
    });
}

function updatePreview() {
    const v = id => document.getElementById('f_' + id).value || DEFAULTS[id];
    document.getElementById('p_name').textContent = v('name');
    document.getElementById('p_title').textContent = v('title');
    document.getElementById('p_dept').textContent = v('dept');
    document.getElementById('p_company').textContent = v('company');
    document.getElementById('p_tagline').textContent = v('tagline');
    document.getElementById('p_email').textContent = v('email');
    document.getElementById('p_website').textContent = v('website');
    document.getElementById('p_website2').textContent = v('website');
    document.getElementById('p_phone').textContent = v('phone');

    document.getElementById('l_email').textContent = v('email');
    document.getElementById('l_phone').textContent = v('phone');
    document.getElementById('l_website').textContent = v('website');
    document.getElementById('l_linkedin').textContent = v('linkedin');
    document.getElementById('l_location').textContent = v('location');
}

function setDirty(state) {
    dirty = state;
    const pill = document.getElementById('statusPill'), text = document.getElementById('statusText');
    if (state) { pill.classList.add('unsaved'); text.textContent = 'تغییرات ذخیره‌نشده'; }
    else { pill.classList.remove('unsaved'); text.textContent = 'همه چیز ذخیره شده'; }
}

function showToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('show');
    clearTimeout(showToast._tm);
    showToast._tm = setTimeout(() => t.classList.remove('show'), 2200);
}

function currentFormData() {
    const data = {};
    fields.forEach(k => { data[k] = document.getElementById('f_' + k).value.trim() || DEFAULTS[k]; });
    return data;
}

function save() {
    const data = currentFormData();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    setDirty(false);
    showToast('ذخیره شد ✓');
}

function reset() {
    if (!confirm("All changes will be erased. continue?")) return;
    localStorage.removeItem(STORAGE_KEY);
    fillForm(DEFAULTS);
    updatePreview();
    setDirty(false);
    showToast("Done!");
}

function exportJson() {
    const data = currentFormData();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'Digital-Business-Card.json'; a.click();
    URL.revokeObjectURL(url);
}

function embedSnippet(data) {
    return `<script>
(function(){
  var d=${JSON.stringify(data, null, 2)};
  var m={
    '[data-i18n="card_name"]':d.name,
    '[data-i18n="card_title"]':d.title,
    '[data-i18n="card_dept"]':d.dept,
    '[data-i18n="card_company"]':d.company,
    '[data-i18n="back_tagline"]':d.tagline,
    '[data-i18n="ei1_v"]':d.name,
    '[data-i18n="ei3_v"]':d.location,
    '[data-i18n="ei4_v"]':d.response
  };
  Object.keys(m).forEach(function(sel){
    document.querySelectorAll(sel).forEach(function(el){el.textContent=m[sel];});
  });
  document.querySelectorAll('a[href^="mailto:"]').forEach(function(el){
    el.href='mailto:'+d.email;
    var val=el.querySelector('.cl-val');if(val)val.textContent=d.email;
  });
  document.querySelectorAll('a[href^="tel:"]').forEach(function(el){
    el.href='tel:'+d.phone.replace(/\\s+/g,'');
    var val=el.querySelector('.cl-val');if(val)val.textContent=d.phone;
  });
  document.querySelectorAll('.contact-row').forEach(function(el){
    if(el.textContent.indexOf('@')>-1)el.lastChild.textContent=' '+d.email;
  });
})();
<\/script>`;
}

async function copyEmbed() {
    const data = currentFormData();
    const code = embedSnippet(data);
    try {
        await navigator.clipboard.writeText(code);
        showToast('کد جاسازی کپی شد ✓');
    } catch (e) {
        prompt('کد را کپی کنید:', code);
    }
}

document.addEventListener('input', e => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
        updatePreview();
        setDirty(true);
    }
});

document.getElementById('previewCard').addEventListener('click', function () {
    this.classList.toggle('flipped');
});

document.getElementById('btnSave').addEventListener('click', save);
document.getElementById('btnReset').addEventListener('click', reset);
document.getElementById('btnExport').addEventListener('click', exportJson);
document.getElementById('btnCopy').addEventListener('click', copyEmbed);

window.addEventListener('beforeunload', e => {
    if (dirty) { e.preventDefault(); e.returnValue = ''; }
});

(function init() {
    const data = load();
    fillForm(data);
    updatePreview();
    setDirty(false);
})();

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
