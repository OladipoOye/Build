console.log("Ok");
// for the modals
const Modal_box = document.getElementById("Modal_box");
const modal_img = document.getElementById("modal_img");
const cap = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
    Modal_box.style.display = "none";}

modal_img.onclick = function() {
    window.open("https://drive.google.com/drive/folders/19XqVvOfII4WbUhDT9d_Q_vlWQromYunE?usp=sharing")}

// for clicks on first
const first = document.getElementById("first");
first.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.innerHTML = "<h1> <br> <br> <br> <br> <br>First year </h1>";
    cap.innerHTML = "For the young ones";}

// for clicks on second
const second = document.getElementById("second");
second.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.innerHTML = "<h1> <br> <br> <br> <br> <br>Second year </h1>";
    cap.innerHTML = "The seconds";}

// for clicks on third
const third = document.getElementById("third");
third.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.innerHTML = "<h1> <br> <br> <br> <br> <br>Third year</h1>";
    cap.innerHTML = "The penultimate";}

// for clicks on fourth
const fourth = document.getElementById("fourth");
fourth.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.innerHTML = "<h1> <br> <br> <br> <br> <br>Fourth year</h1>";
    cap.innerHTML = "The final strecth";}

// for clicks on fifth
const fifth = document.getElementById("fifth");
fifth.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.innerHTML = "<h1> <br> <br> <br> <br> <br>Chemical Engineering</h1>";
    cap.innerHTML = "The myth";}

// for clicks on sixth
const sixth = document.getElementById("sixth");
sixth.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.innerHTML = "<h1> <br> <br> <br> <br> <br>Post graduates</h1>";
    cap.innerHTML = "Life after";}