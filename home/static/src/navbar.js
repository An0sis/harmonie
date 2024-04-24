var navbar = document.getElementById('navbar');
var logo = document.getElementById('logo');
var logo_temp = document.getElementById('logo_temp');

function toggleNavbar() {
    console.log('logo clicked');
    if (navbar.classList.contains('close')) {
        navbar.classList.remove('close');
    } else {
        navbar.classList.add('close');
    }
}

logo.addEventListener('click', toggleNavbar);
logo_temp.addEventListener('click', toggleNavbar);

document.addEventListener('click', function(event) {
    var isClickInside = navbar.contains(event.target) || logo.contains(event.target) || logo_temp.contains(event.target);

    if (!isClickInside && !navbar.classList.contains('close')) {
        navbar.classList.add('close');
    }
});