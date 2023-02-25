window.onscroll = function() {stickyNavigation()};
var navigationBar = document.getElementById("navigationBar");
var offeset = navigationBar.offsetTop;

function stickyNavigation() {
    if(window.offeset>= offeset) {
        navigationBar.classList.add("sticky");
    } else {
        navigationBar.classList.remove("sticky");
    }
}