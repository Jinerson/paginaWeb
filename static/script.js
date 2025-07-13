const link_registro = document.querySelector('.link-registro.registrar');
const link_login = document.querySelector('.link-registro.ingresar');
const wrapper = document.querySelector('.wrapper');
const btn_popup = document.querySelector('.btonEntrarRegistro');
const iconClose = document.querySelector('.icon-close');

link_registro.addEventListener('click', () => {
    wrapper.classList.add('active');
});

link_login.addEventListener('click', () => {
    wrapper.classList.remove('active');
});

btn_popup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});