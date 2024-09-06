document.getElementById('random-btn').addEventListener('click', function() {
    const websites = [
        'https://www.google.com',
        'https://www.facebook.com',
        'https://www.youtube.com',
        'https://www.twitter.com',
        'https://www.reddit.com',
        'https://www.wikipedia.org',
        'https://www.instagram.com',
        'https://www.amazon.com',
        'https://www.linkedin.com',
        'https://www.netflix.com'
    ];

    // Select a random website from the array
    const randomSite = websites[Math.floor(Math.random() * websites.length)];
    window.location.href = randomSite; // Redirect to the random website
});
