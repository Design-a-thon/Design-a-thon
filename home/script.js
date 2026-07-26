const menuButton = document.getElementById("menu-button");
const menu = document.getElementById("menu");

menuButton.addEventListener("click", () => {
    menu.classList.toggle("active");
});

const floatImg1 = document.getElementById("float-img1");
const floatImg2 = document.getElementById("float-img2");
const floatImg3 = document.getElementById("float-img3");

const images1 = [
    "../assets/images/homepage/about/Website Float 1-1.png",
    "../assets/images/homepage/about/Website Float 1-2.png"
];
const images2 = [
    "../assets/images/homepage/about/Website Float 2-1.png",
    "../assets/images/homepage/about/Website Float 2-2.png"
];
const images3 = [
    "../assets/images/homepage/about/Website Float 3-1.png",
    "../assets/images/homepage/about/Website Float 3-2.png"
];

let index = 0;

setInterval(() => {
    index = (index + 1) % images1.length;
    floatImg1.src = images1[index];
    floatImg2.src = images2[index];
    floatImg3.src = images3[index];
}, 1200);