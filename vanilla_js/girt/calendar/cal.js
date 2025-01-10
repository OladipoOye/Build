console.log('ok');
let monthIndex = 1;
window.addEventListener('load',showMonth(monthIndex));

// Next/previous controls
function plusMonth(n) {
  showMonth(monthIndex += n);}

// Thumbnail image controls
function currentSlide(n) {
  showMonth(monthIndex = n);}

function showMonth(n) {
  //console.log(n);
  let i;
  const months = document.getElementsByClassName("fullDiv");
  //let dots = document.getElementsByClassName("dot");
  if (n > months.length) {monthIndex = 1}
  if (n < 1) {monthIndex = months.length}
  for (i = 0; i < months.length; i++) {
    months[i].style.display = "none";}
  console.log(monthIndex);
  months[monthIndex-1].style.display = "flex";}

// for the modals
const Modal_box = document.getElementById("Modal_box");
const modal_img = document.getElementById("modal_img");
//const logo = document.getElementById("logo");
const cap = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
    Modal_box.style.display = "none";}

// for clicks on 8th october 
const term = document.getElementById("ms");
term.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "First Social<br>+<br>Michaelmas Term Start";}

// for clicks on 16th october 
const fw = document.getElementById("fw");
fw.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Freshers Welcome formal";}

// for clicks on 6th December 
const me = document.getElementById("me");
me.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Michaelmas Term End";}

// for clicks on 25th December 
const mas = document.getElementById("mas");
mas.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Merry Christmas";}

// for clicks on 8th December 
const ch = document.getElementById("ch");
ch.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/xo.png";
    cap.innerHTML = "The Annual Christmas Quiz Night";}

// for clicks on 21st of January 
const lents = document.getElementById("ls");
lents.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Lent Term Start";}

// for clicks on 21st of March 
const le = document.getElementById("le");
le.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Lent Term End";}

// for clicks on 29th of April
const es = document.getElementById("es");
es.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Easter Term Start";}


// for clicks on 8th october 
const ee = document.getElementById("ee");
ee.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = "../resources/b-two.png";
    cap.innerHTML = "Easter Term End";}