// the main image toggling
const girt = document.getElementById('girt')
girt.addEventListener('click', togg_2)
function togg_2() {
    setTimeout( ()=> {
    if (ui.src.match("b-one")) { ui.src = "./resources/g-one.png"}
    else {ui.src = "./resources/b-one.png"}}, 200)}

// for the Girton printing
window.onload = setTimeout(amend(), 1000);
    
function amend(){
    girt.innerHTML = ''
    let xd=null
    let wr = 0
    clearInterval(xd);
    xd = setInterval(write, 150);
    function write() {
        if (wr < 18)
            {switch (wr) 
                {case 0: 
                    console.log('Ok')
                    break;
                case 1:
                    girt.innerHTML += 'T'
                    break;
                case 2:
                    girt.innerHTML += 'he'
                    break;
                case 3:
                    girt.innerHTML += ' '
                    break;
                case 4:
                    girt.innerHTML += 'Gi'
                    break;
                case 5:
                    girt.innerHTML += 'rt'
                    break;
                case 6:
                    girt.innerHTML += 'on'
                    break;
                case 7:
                    girt.innerHTML += ' '
                    break;
                case 8:
                    girt.innerHTML += 'En'
                    break;
                case 9:
                    girt.innerHTML += 'gi'
                    break;
                case 10:
                    girt.innerHTML += 'ne'
                    break;
                case 11:
                    girt.innerHTML += 'er'
                    break;
                case 12:
                    girt.innerHTML += 'ing'
                    break;
                case 13:
                    girt.innerHTML += ' '
                    break;
                case 14:
                    girt.innerHTML += 'So'
                    break;
                case 15:
                    girt.innerHTML += 'ci'
                    break;
                case 16:
                    girt.innerHTML += 'et'
                    break;
                case 17:
                    girt.innerHTML += 'y'
                    break;
                default:
                    console.log('just cause')
                    break;}
            wr++}
            else{clearInterval(xd)}
    }};

// for the modals
const Modal_box = document.getElementById("Modal_box");
const modal_img = document.getElementById("modal_img");
const logo = document.getElementById("logo");
const cap = document.getElementById("caption");
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
    Modal_box.style.display = "none";}

// for clicks on logo
logo.onclick = function(){
    Modal_box.style.display = "block";
    modal_img.src = logo.src;
    cap.innerHTML = "The original logo";}