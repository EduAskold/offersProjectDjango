function showFinder(){
    const finderForm = document.querySelector('#form-finder')
    const companyForm = document.querySelector('#form-company')
    const companyText = document.querySelector('.company-text')
    const searchingWorkerText = document.querySelector('.searching-worker-text')
    companyForm.style.animation = 'hide 300ms 0ms linear forwards'
    setTimeout(() => {
        companyForm.style.display = 'none'
        finderForm.style.display = 'flex'
        finderForm.style.animation = 'show 300ms 0ms linear forwards'
        companyForm.style.animation = 'none'
        setTimeout(() => {
            finderForm.style.animation = 'none'
        }, 300);
    }, 300);
    companyText.style.color = 'white'
    searchingWorkerText.style.color = 'mediumslateblue'
}
function showCompany(){
    const finderForm = document.querySelector('#form-finder')
    const companyForm = document.querySelector('#form-company')
    const companyText = document.querySelector('.company-text')
    const searchingWorkerText = document.querySelector('.searching-worker-text')
    finderForm.style.animation = 'hide 300ms 0ms linear forwards'
    setTimeout(() => {
        finderForm.style.display = 'none'
        companyForm.style.display = 'flex'
        companyForm.style.animation = 'show 300ms 0ms linear forwards'
        finderForm.style.animation = 'none'
        setTimeout(() => {
            companyForm.style.animation = 'none'
        }, 300);
    }, 300);
    companyText.style.color = 'mediumslateblue'
    searchingWorkerText.style.color = 'white'
}
function getFile(selector){
    const input = document.querySelector(selector);
    input.style.backgroundColor = 'green';
}