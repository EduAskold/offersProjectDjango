function showVacancie(){
    const vacanceName = document.querySelector('#vacancie_company');
    const descriptionName = document.querySelector('#description_company');
    const descriptionBlock = document.querySelector('.company-description-page');
    const vacanceBlock = document.querySelector('.company-vacancies-page');
    descriptionBlock.style.display = 'none';
    vacanceBlock.style.display = 'flex';
    vacanceName.classList.add('selected')
    descriptionName.classList.remove('selected')
}
function showDescription(){
    const vacanceName = document.querySelector('#vacancie_company');
    const descriptionName = document.querySelector('#description_company');
    const descriptionBlock = document.querySelector('.company-description-page');
    const vacanceBlock = document.querySelector('.company-vacancies-page');
    descriptionBlock.style.display = 'flex';
    vacanceBlock.style.display = 'none';
    vacanceName.classList.remove('selected')
    descriptionName.classList.add('selected')
}