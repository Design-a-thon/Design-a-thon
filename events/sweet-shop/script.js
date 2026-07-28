const menuButton = document.getElementById("menu-button");
const menu = document.getElementById("menu");

menuButton.addEventListener("click", () => {
    menu.classList.toggle("active");
});

const images = [
    "../../assets/images/event/examples/sweet1.jpg",
    "../../assets/images/event/examples/sweet2.jpg",
    "../../assets/images/event/examples/sweet3.jpg",
    "../../assets/images/event/examples/sweet4.jpg",
    "../../assets/images/event/examples/sweet5.jpg",
    "../../assets/images/event/examples/sweet6.jpg",
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