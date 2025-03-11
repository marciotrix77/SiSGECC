const menuLateral = document.querySelector('.menu-lateral');
const menuToggle = document.querySelector('.menu-toggle');

menuToggle.addEventListener('click', () => {
    menuLateral.classList.toggle('recolhido');
});