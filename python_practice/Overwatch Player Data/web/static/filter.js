// static/filter.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('filterForm');
    const resultDiv = document.getElementById('result');

    const heroSelect = document.getElementById('hero');
    const seasonSelect = document.getElementById('season');
    const statSelect = document.getElementById('stat');
    const heroImage = document.getElementById('heroImage');

    // Helper: update hero image
    function updateHeroImage() {
        if (heroSelect.value) {
            heroImage.src = `/static/images/${heroSelect.value}.png`;
            heroImage.style.display = 'inline-block';
        } else {
            heroImage.style.display = 'none';
        }
    }

    // Helper: fetch dependent options
    function updateOptions() {
    const hero = heroSelect.value;
    const seasonSelect = document.getElementById('season');
    const statSelect = document.getElementById('stat');

    fetch(`/options?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(seasonSelect.value)}`)
        .then(response => response.json())
        .then(data => {
            // Update seasons
            const currentSeason = seasonSelect.value;
            seasonSelect.innerHTML = "";
            data.seasons.forEach(s => {
                const opt = document.createElement("option");
                opt.value = s;
                opt.textContent = s;
                seasonSelect.appendChild(opt);
            });
            // Restore previous season only if still valid
            if (data.seasons.includes(currentSeason)) {
                seasonSelect.value = currentSeason;
            }

            // Update stats
            const currentStat = statSelect.value;
            statSelect.innerHTML = "";
            data.stats.forEach(st => {
                const opt = document.createElement("option");
                opt.value = st;
                opt.textContent = st;
                statSelect.appendChild(opt);
            });
            // Restore previous stat only if still valid
            if (data.stats.includes(currentStat)) {
                statSelect.value = currentStat;
            }
        })
        .catch(err => console.error("Error updating options:", err));
}


    // Update hero image + options when hero changes
    heroSelect.addEventListener('change', function() {
        updateHeroImage();
        updateOptions();
    });

    // Update options when season changes
    seasonSelect.addEventListener('change', updateOptions);

    // Handle form submission (AJAX)
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent reload

        const hero = heroSelect.value;
        const season = seasonSelect.value;
        const stat = statSelect.value;

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

    // On initial load
    if (heroSelect.value) {
        updateHeroImage();
        updateOptions();
    }
});
