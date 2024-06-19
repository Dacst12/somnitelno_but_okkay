let setBtn = document.querySelector('.settings-btn');
let changeWnd = document.querySelector('.change-em-pass');


setBtn.onclick = function() {
    if (this.innerHTML === 'Закрыть настройки аккаунта') {
        this.innerHTML = 'Открыть настройки профиля';
    } else {
        this.innerHTML = 'Закрыть настройки аккаунта';
    }
    if (changeWnd.classList.contains('active')) {
        changeWnd.classList.remove('active');
        setBtn.classList.remove('active');
    } else {
        changeWnd.classList.add('active');
        setBtn.classList.add('active');
    }
}