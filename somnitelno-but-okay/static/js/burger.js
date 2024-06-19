let burger = document.querySelector('.burger');
let body = document.querySelector('body');


burger.onclick = function(evt) {
    evt.preventDefault();
    if (burger.classList.contains('active')) {
        header.classList.remove('active');
        body.classList.remove('active');
        burger.classList.remove('active');
        document.body.style.overflow = 'visible';
    } else {
        header.classList.add('active');
        body.classList.add('active');
        burger.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
};

