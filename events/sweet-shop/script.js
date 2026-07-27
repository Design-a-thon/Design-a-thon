const menuButton = document.getElementById("menu-button");
const menu = document.getElementById("menu");

menuButton.addEventListener("click", () => {
    menu.classList.toggle("active");
});

const images = [
    "../../assets/images/event/sweet-shop/examples/sweet1.png",
    "../../assets/images/event/sweet-shop/examples/sweet2.png",
    "../../assets/images/event/sweet-shop/examples/sweet3.png",
    "../../assets/images/event/sweet-shop/examples/sweet4.jpg",
    "../../assets/images/event/sweet-shop/examples/sweet5.png",
];

let startIndex = 0;

const carouselImages = document.querySelectorAll(".carousel-img");

function updateCarousel() {
    carouselImages.forEach((img, i) => {
        img.src = images[(startIndex + i) % images.length];
    });
}

function changeSlide(direction) {
    startIndex += direction;

    if (startIndex < 0) {
        startIndex = images.length - 1;
    }

    if (startIndex >= images.length) {
        startIndex = 0;
    }

    updateCarousel();
}