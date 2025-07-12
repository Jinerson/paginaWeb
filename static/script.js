const link_registro = document.querySelector('.link-registro.registrar');
const link_login = document.querySelector('.link-registro.ingresar');
const wrapper = document.querySelector('.wrapper');

link_registro.addEventListener('click', () => {
    wrapper.classList.add('active');
});

link_login.addEventListener('click', () => {
    wrapper.classList.add('active');
});

