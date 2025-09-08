// static/filter.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('filterForm');
    const resultDiv = document.getElementById('result');

    // Hero image elements
    const heroSelect = document.getElementById('hero');
    const heroImage = document.getElementById('heroImage');
    const seasonSelect = document.getElementById('season');
    const statSelect = document.getElementById('stat');

    // --- CHART.js setup ---
    let chartInstance = null;
    function updateChart(seasons, values, hero, stat) {
        const ctx = document.getElementById('statChart').getContext('2d');
        if (chartInstance) {
            chartInstance.destroy();
        }
        chartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: seasons,
                datasets: [{
                    label: `${hero} - ${stat} per Season`,
                    data: values,
                    borderColor: '#0d6efd',
                    backgroundColor: 'rgba(0, 0, 255, 0.1)',
                    tension: 0.3
                }]
            },
            options: {
                    plugins: {
                        legend: {
                            labels: {
                                usePointStyle: true,   // use line/circle instead of box
                                pointStyle: 'line'     // looks like a line instead of a box
                            }
                        },
                    },
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return value.toLocaleString(); // commas
                            }
                        }
                    }
                }
            }
        });
    }

    // --- Update hero image when selection changes ---
    heroSelect.addEventListener('change', function() {
        if (heroSelect.value) {
            heroImage.src = `/static/images/${heroSelect.value}.png`;
            heroImage.style.display = 'inline-block';
        } else {
            heroImage.style.display = 'none';
        }
        updateDependentFilters();
    });

    // --- Update dependent filters (season & stat) based on hero ---
    function updateDependentFilters() {
        const hero = heroSelect.value;
        if (!hero) return;

        fetch(`/filter_options?hero=${encodeURIComponent(hero)}`)
            .then(response => response.json())
            .then(data => {
                // Seasons
                seasonSelect.innerHTML = "";
                data.seasons.forEach(season => {
                    const opt = document.createElement("option");
                    opt.value = season;
                    opt.textContent = season;
                    seasonSelect.appendChild(opt);
                });

                // Stats
                statSelect.innerHTML = "";
                data.stats.forEach(stat => {
                    const opt = document.createElement("option");
                    opt.value = stat;
                    opt.textContent = stat;
                    statSelect.appendChild(opt);
                });
            })
            .catch(err => console.error("Error fetching dependent filters:", err));
    }

    // --- Form submission using AJAX (updates both text + chart) ---
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent page reload

        const hero = heroSelect.value;
        const season = seasonSelect.value;
        const stat = statSelect.value;

        // Update text result
        fetch(`/filter?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.text())
            .then(data => {
                resultDiv.textContent = data;
            })
            .catch(err => {
                resultDiv.textContent = 'Error fetching data';
                console.error(err);
            });

        // Update chart
        fetch(`/chart_data?hero=${encodeURIComponent(hero)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.json())
            .then(data => {
                updateChart(data.seasons, data.values, hero, stat);
            })
            .catch(err => console.error("Error fetching chart data:", err));
    });

    // --- Initialize on page load ---
    if (heroSelect.value) {
        heroImage.src = `/static/images/${heroSelect.value}.png`;
        heroImage.style.display = 'inline-block';
        updateDependentFilters();
    }
});
