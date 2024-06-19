const registerButton = document.querySelector('.register-account');
const registerFormContainer = document.querySelector('.register-menu');

registerButton.addEventListener('click', function(event) {
  if (registerFormContainer.style.display === 'block') {
    return; 
  }

  loginFormContainer.style.display = 'none';

  event.stopPropagation(); 

  registerFormContainer.style.display = 'block';
  header.classList.add('blur');
  main.classList.add('blur');
  footer.classList.add('blur');


  document.addEventListener('click', function closeRegisterMenu(event) {
    if (!registerFormContainer.contains(event.target) && event.target !== registerFormContainer) {
      registerFormContainer.style.display = 'none';
      header.classList.remove('blur');
      main.classList.remove('blur');
      footer.classList.remove('blur');
      document.removeEventListener('click', closeRegisterMenu);
    }
  });
});

const registerSubmitButton = document.querySelector('.register-button');
registerSubmitButton.addEventListener('click', function(event) {
  registerFormContainer.style.display = 'none';
  header.classList.remove('blur');
  main.classList.remove('blur');
  footer.classList.remove('blur');
});