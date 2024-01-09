
const header = document.querySelector(".navbar")
const footer = document.querySelector("#footer")

window.onscroll = function() {
    var top = window.scrollY;
    if(top >=0) {
        header.classList.add('navbarDark')
    }
    else {
        header.classList.remove('navbarDark')
    }
}