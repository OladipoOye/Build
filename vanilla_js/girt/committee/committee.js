let slideIndex = 1;
window.addEventListener('load',showSlides(slideIndex))

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);}

function showSlides(n) {
  //console.log(n);
  let i;
  const slides = document.getElementsByClassName("mySlides");
  //let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  //for (i = 0; i < dots.length; i++) {
  //  dots[i].className = dots[i].className.replace(" active", "");}
  console.log(slideIndex);
  slides[slideIndex-1].style.display = "block";}
  //dots[slideIndex-1].className += " active";