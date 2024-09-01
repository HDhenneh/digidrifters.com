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
