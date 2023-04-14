
const menuBtn = document.querySelector(".menu-btn");
const mainMenu = document.querySelector(".main-menu");

menuBtn.addEventListener("click", function() {
  mainMenu.classList.toggle("show");
  menuBtn.querySelector("i").classList.toggle("fa-bars");
  menuBtn.querySelector("i").classList.toggle("fa-times");
});
