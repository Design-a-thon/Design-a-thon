const menuButton = document.getElementById("menu-button");
const menu = document.getElementById("menu");

menuButton.addEventListener("click", () => {
    menu.classList.toggle("active");
});

const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Please fill in all fields.");
        return;
    }

    // TODO: Replace with backend/Firebase authentication
    console.log("Login attempt:");
    console.log("Email:", email);
    console.log("Password:", password);

});


const googleButton = document.getElementById("google-login");

googleButton.addEventListener("click", () => {

    // TODO: Replace with Google OAuth/Firebase Auth

    console.log("Google login clicked");


});


const forgotPassword = document.querySelector(".forgot-password");

forgotPassword.addEventListener("click", (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;

    if (!email) {
        alert("Enter your email first.");
        return;
    }

    // TODO: Firebase password reset

    console.log("Password reset requested for:", email);
});