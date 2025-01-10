// the on scroll effects
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('show');}
        else entry.target.classList.remove('show');})
});
const hiddenEls = document.querySelectorAll('.hidden');
hiddenEls.forEach((el) => observer.observe(el));
// The toggle functions

const i = document.querySelector('.i')
i.addEventListener('click', togg)
const ui = document.getElementById('ui');

function togg() {
    if (i.className == 'i is-active') {closeNav()}
    else {openNav()}
    i.classList.toggle('is-active');};

// the on load page transitions
//window.onload = () => {
    //const transitionEl = document.querySelector('.transition')
    //const anchors = document.querySelectorAll('a');
        //setTimeout(() => {
        //    transitionEl.classList.remove('is-active')
        //}, 500)
    
        //for (let i =0; i< anchors.length; i++) {
        //    const anchor = anchors[i];
        //    if (anchor.className == "closebtn") {return;}
        //    else{
        //        anchor.addEventListener('click', e => {
        //            e.preventDefault();
        //            let target = e.target.href;
        //            console.log(target)- keep commented
        //
        //            transitionEl.classList.add('is-active')
        //
        //            setTimeout(() => {
        //                window.location.href = target;
        //            }, 500);
        //    })}
        //}};
// opening the nav bar
function openNav(){
    document.getElementById('sideNav').style.width = '22%';
    document.getElementById('main').style.marginLeft = '22%';}
    //document.body.style.backgroundColor = 'rgba(0,0,0,0.4)'}}

function closeNav(){
    document.getElementById('sideNav').style.width = '0px';
    document.getElementById('main').style.marginLeft = '0px';}
    //document.body.style.backgroundColor = 'white'}