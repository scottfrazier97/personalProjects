// static/filter.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('filterForm');
    const resultDiv = document.getElementById('result');

    // Hero image elements
    const heroSelect = document.getElementById('hero');
    const heroImage = document.getElementById('heroImage');

    // Update hero image when selection changes
    heroSelect.addEventListener('change', function() {
        if (heroSelect) {
            heroImage.src = `/static/images/${heroSelect.value}.png`;
            heroImage.style.display = 'inline-block';
        } else {
            heroImage.style.display = 'none';
        }
    });

    // Form submission using AJAX to stay on same page
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent page reload

        const hero = heroSelect.value;
        const season = document.getElementById('season').value;
        const stat = document.getElementById('stat').value;

        // Optional debug logs
        //console.log("Submitting filter:", hero, season, stat);

        // Fetch stats from Flask route
        fetch(`/filter?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.text())
            .then(data => {
                resultDiv.textContent = data;
            })
            .catch(err => {
                resultDiv.textContent = 'Error fetching data';
                console.error(err);
            });
    });

    // Optionally trigger image display on initial load
    if (heroSelect.value) {
        heroImage.src = `/static/images/${heroSelect.value}.png`;
        heroImage.style.display = 'inline-block';
    }
});
