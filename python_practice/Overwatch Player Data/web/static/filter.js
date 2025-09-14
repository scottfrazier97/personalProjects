// static/filter.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('filterForm');
    const resultDiv = document.getElementById('result');

    // Hero image elements
    const heroSelect = document.getElementById('hero');
    const heroImage = document.getElementById('heroImage');
    const seasonSelect = document.getElementById('season');
    const statSelect = document.getElementById('stat');
    const roleSelect = document.getElementById('role');

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
                    label: `${hero} - ${stat}`,
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
                            usePointStyle: true,
                            pointStyle: 'line'
                        }
                    },
                },
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return value.toLocaleString();
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
        const hero = heroSelect.value || "All Heroes";
        const role = roleSelect.value || "All Roles";
        const season = seasonSelect.value || "All Seasons";

        fetch(`/options?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&season=${encodeURIComponent(season)}`)
            .then(resp => resp.json())
            .then(data => {
                
                // Helper function to populate dropdown while preserving selection
                function populateDropdown(select, options, currentValue) {
                    select.innerHTML = ""; // clear existing options
                    options.forEach(optValue => {
                        const opt = document.createElement("option");
                        opt.value = optValue;
                        opt.textContent = optValue;
                        if (optValue === currentValue) {
                            opt.selected = true; // preserve current selection
                        }
                        select.appendChild(opt);
                    });
                }

                // Populate all dropdowns
                populateDropdown(heroSelect, data.heroes, heroSelect.value);
                populateDropdown(roleSelect, data.roles, roleSelect.value);
                populateDropdown(seasonSelect, data.seasons, seasonSelect.value);
                populateDropdown(statSelect, data.stats, statSelect.value);

            })
            .catch(err => console.error("Error fetching dependent filters:", err));
    };


    // --- Add event listeners to make filters dependent ---
    [heroSelect, roleSelect, seasonSelect].forEach(select => {
        select.addEventListener("change", updateDependentFilters);
    });

    // --- Form submission using AJAX (updates text, chart, + summary) ---
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const hero = heroSelect.value;
        const season = seasonSelect.value;
        const role = roleSelect.value;
        const stat = statSelect.value;

        // --- Fetch filter result ---
        fetch(`/filter?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(season)}&role=${encodeURIComponent(role)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.text())
            .then(data => {
                resultDiv.textContent = data;

                // Re-run updateDependentFilters after fetch
                updateDependentFilters(); // this will rebuild all dropdowns
            })
            .catch(err => {
                resultDiv.textContent = 'Error fetching data';
                console.error(err);
            });

        // --- Fetch chart and summary as before ---
        fetch(`/chart_data?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.json())
            .then(data => {
                updateChart(data.labels, data.values, hero, stat);
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
