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

    // --- Form submission using AJAX (updates text, chart, + summary) ---
    form.addEventListener('submit', function(e) {
        e.preventDefault();

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

        // Update chart + five-number summary
        fetch(`/chart_data?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.json())
            .then(data => {
                updateChart(data.labels, data.values, hero, stat);
            })
            .catch(err => console.error("Error fetching chart data:", err));

        const summaryDiv = document.getElementById('summary');
        if (season !== "All Seasons") {
            if (summaryDiv) {
                summaryDiv.innerHTML = `<p>Please select 'All Seasons' in the Season filter to see the five-number summary.</p>`;
            }
        } else {
            fetch(`/summary?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
                .then(response => response.json())
                .then(data => {
                    if (summaryDiv && !data.error) {
                        summaryDiv.innerHTML = `
                            <h5>Five-Number Summary (${stat})</h5>
                            <ul>
                                <li>Min: ${data.min}</li><br>
                                <li>Q1: ${data.q1}</li><br>
                                <li>Median: ${data.median}</li><br>
                                <li>Q3: ${data.q3}</li><br>
                                <li>Max: ${data.max}</li>
                            </ul>
                        `;
                    } else if (summaryDiv && data.error) {
                        summaryDiv.innerHTML = `<p>No data available for this selection</p>`;
                    }
                })
                .catch(err => console.error("Error fetching summary:", err));
        }
    });

    // --- Initialize on page load ---
    if (heroSelect.value) {
        heroImage.src = `/static/images/${heroSelect.value}.png`;
        heroImage.style.display = 'inline-block';
        updateDependentFilters();
    }
});
