const sliderContainer = document.querySelector('.slider-container');
const bubbles = document.querySelectorAll('.glass-bubble');
let currentSlide = 0;

function slideHero() {
    currentSlide = (currentSlide + 1) % bubbles.length;
    const slideWidth = bubbles[0].offsetWidth + 40; // Width + margin
    sliderContainer.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}

// Slide every 3 seconds
setInterval(slideHero, 3000);

// Random site button logic remains the same
document.getElementById("portal-button").addEventListener("click", function() {
    const randomSites = [
        "https://www.stumbleupon.com",
        "https://www.reddit.com/r/random",
        "https://en.wikipedia.org/wiki/Special:Random",
        "https://www.boredpanda.com/",
        "https://www.randomwebsite.com/cgi-bin/random.pl",
        "https://theuselessweb.com/",
        "https://www.thisiscolossal.com/"
    ];

    const randomIndex = Math.floor(Math.random() * randomSites.length);
    const randomSite = randomSites[randomIndex];
    window.location.href = randomSite;
});
