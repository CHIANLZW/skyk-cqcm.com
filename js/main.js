document.querySelectorAll('.tab-btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    const tab = btn.dataset.tab;
    document.querySelectorAll('.tab-btn').forEach((b) => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach((p) => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(`tab-${tab}`).classList.add('active');
  });
});

const navToggle = document.querySelector('.nav-toggle');
const mainNav = document.querySelector('.main-nav');
const backdrop = document.createElement('div');
backdrop.className = 'nav-backdrop';
document.body.appendChild(backdrop);

const mobileBar = document.querySelector('.mobile-bar');
const mobileMq = window.matchMedia('(max-width: 900px)');

function syncMobileLayout() {
  document.body.classList.toggle('has-mobile-bar', mobileMq.matches && !!mobileBar);
  if (!mobileMq.matches) setNavOpen(false);
}

function setNavOpen(open) {
  mainNav.classList.toggle('open', open);
  navToggle.setAttribute('aria-expanded', open);
  backdrop.classList.toggle('visible', open);
  document.body.style.overflow = open ? 'hidden' : '';
}

navToggle.addEventListener('click', () => {
  setNavOpen(!mainNav.classList.contains('open'));
});

backdrop.addEventListener('click', () => setNavOpen(false));

mainNav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => setNavOpen(false));
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') setNavOpen(false);
});

mobileMq.addEventListener('change', syncMobileLayout);
syncMobileLayout();

function handleSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const data = Object.fromEntries(new FormData(form));
  alert(`感谢您的咨询，${data.name}！\n我们已收到您的信息，将尽快与您联系。`);
  form.reset();
  return false;
}

const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
  header.style.boxShadow = window.scrollY > 20 ? '0 2px 20px rgba(0,0,0,0.08)' : 'none';
}, { passive: true });
