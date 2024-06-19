var showMoreButton = document.querySelector('.show-more-button');
var elementsBlock = document.querySelector('.curent-portfolio');
var elementsToShow = 10;
var currentVisibleIndex = 10;

function showMore() {
    for (var i = currentVisibleIndex; i < currentVisibleIndex + elementsToShow; i++) {
        if (i < elementsBlock.children.length) {
            elementsBlock.children[i].style.display = 'flex';
        }
    }
    currentVisibleIndex += elementsToShow;

    if (currentVisibleIndex >= elementsBlock.children.length) {
        showMoreButton.style.display = 'none'; 
    }

    for (var i = currentVisibleIndex; i < elementsBlock.children.length; i++) {
        elementsBlock.children[i].style.display = 'none'; 
    }
}

for (var i = elementsToShow; i < elementsBlock.children.length; i++) {
    elementsBlock.children[i].style.display = 'none';
}

showMoreButton.addEventListener('click', showMore);