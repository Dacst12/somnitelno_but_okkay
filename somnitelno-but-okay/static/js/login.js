const loginButton = document.querySelector('.enter-account');
const loginFormContainer = document.querySelector('.login-menu');
const header = document.querySelector('header');
const main = document.querySelector('main');
const footer = document.querySelector('footer');

loginButton.addEventListener('click', function(event) {
  if (loginFormContainer.style.display === 'block') {
    return; 
  }

  event.stopPropagation(); 

  loginFormContainer.style.display = 'block';
  header.classList.remove('active');
  body.classList.remove('active');
  burger.classList.remove('active');
  document.body.style.overflow = 'visible';
  header.classList.add('blur');
  main.classList.add('blur');
  footer.classList.add('blur');

  document.addEventListener('click', function closeMenu(event) {
    if (loginFormContainer.style.display === 'block') {
      if (!loginFormContainer.contains(event.target) && event.target !== loginFormContainer) {
        loginFormContainer.style.display = 'none';
        header.classList.remove('blur');
        main.classList.remove('blur');
        footer.classList.remove('blur');
        document.removeEventListener('click', closeMenu);
      }
    }
  });
});

const loginSubmitButton = document.querySelector('.entrance');
loginSubmitButton.addEventListener('click', function(event) {
  loginFormContainer.style.display = 'none';
  header.classList.remove('blur');
  main.classList.remove('blur');
  footer.classList.remove('blur');
});