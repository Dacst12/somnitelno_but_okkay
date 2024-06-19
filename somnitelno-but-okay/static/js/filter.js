let selectedAccountType = null;
let selectedLevel = null;
let selectedExperience = null;
let selectedDirection=null;
let mobileFilter = document.querySelectorAll('.mobile-filter');
let filter = document.querySelector('.left-filter');
let closeButton = document.querySelector('.close-button');
let perfomers = document.querySelector('.perfomers');
let employers = document.querySelector('.employers');
let employersWnd = document.querySelector('.portfolio-employer');
let perfomersWnd = document.querySelector('.portfolio-perfomers');
let leftFilter = document.querySelector('.left-filter');


function handleButtonClick(group, value) {
  if (group === 'account') {
    selectedAccountType = value;
    updateSelectedButton(value, 'account');
    
  } 
  else if (group === 'level') {
    selectedLevel = value;
    updateSelectedButton(value, 'level');
  }
}

function handleExperienceChange() {
  selectedExperience = document.getElementById('experienceRange').value;
}


function updateSelectedButton(value, group) {
  const selectedButton = document.querySelector('.' + group + '-list-item button.' + value + ' span');
  if (selectedButton) {
    const buttons = document.querySelectorAll('.' + group + '-list-item button span');
    buttons.forEach(button => {
      button.classList.remove('active');
    });
    selectedButton.classList.add('active');
  }
}


for (mobileFilterBtn of mobileFilter) {
  mobileFilterBtn.onclick = function() {
      filter.classList.add('active');
      body.classList.add('active');
  };
}

closeButton.onclick = function () {
  filter.classList.remove('active');
  body.classList.remove('active');
};


perfomers.onclick = function() {
  perfomers.classList.add('active');
  perfomers.classList.add('curent-portfolio');
  employers.classList.remove('curent-portfolio');
  employers.classList.remove('active');
  employersWnd.style.display = 'none';
  perfomersWnd.style.display = 'flex';
  leftFilter.classList.remove('employer');
}

employers.onclick = function() {
  employers.classList.add('active');
  employers.classList.add('curent-portfolio');
  perfomers.classList.remove('curent-portfolio');
  perfomers.classList.remove('active');
  perfomersWnd.style.display = 'none';
  employersWnd.style.display = 'flex';
  leftFilter.classList.add('employer');
}