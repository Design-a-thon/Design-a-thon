const menuButton = document.getElementById("menu-button");
const menu = document.getElementById("menu");

menuButton.addEventListener("click", () => {
    menu.classList.toggle("active");
});

const username = document.getElementById("username");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");

const registerForm = document.getElementById("registerForm");
const googleRegister = document.getElementById("googleRegister");