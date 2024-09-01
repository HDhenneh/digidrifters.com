// Array of 10 popular websites
const popularSites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.amazon.com",
    "https://www.netflix.com",
    "https://www.linkedin.com"
];

// Function to shuffle an array
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// Shuffle the sites array
const shuffledSites = shuffle(popularSites);

// Set the iframe src to a random site from the shuffled array
document.getElementById("random-site-iframe").src = shuffledSites[0];

// Portal button click event to navigate to a random site from a different list
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