const menuButton = document.getElementById("menu-button");
const menu = document.getElementById("menu");

menuButton.addEventListener("click", () => {
    menu.classList.toggle("active");
});

const track = document.getElementById("carousel-track");
const images = document.querySelectorAll(".carousel-img");

function getVisible() {
    return window.innerWidth <= 900 ? 1 : 3;
}

let index = 0;

function getSlideWidth() {
    return images[0].getBoundingClientRect().width + 25;
}

function moveCarousel() {
    track.style.transition = "transform 0.5s ease";
    track.style.transform = `translateX(-${index * getSlideWidth()}px)`;

    updateButtons();
}

function updateButtons() {
    document.getElementById("prev").disabled = index === 0;
    document.getElementById("next").disabled =
        index === images.length - getVisible();
}

document.getElementById("next").onclick = () => {
    if (index < images.length - getVisible()) {
        index++;
        moveCarousel();
    }
};

document.getElementById("prev").onclick = () => {
    if (index > 0) {
        index--;
        moveCarousel();
    }
};

window.addEventListener("resize", () => {
    moveCarousel();
});

updateButtons();