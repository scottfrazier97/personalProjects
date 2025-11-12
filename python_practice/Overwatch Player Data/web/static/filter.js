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
    function updateChart(chartData) {
        const ctx = document.getElementById('statChart').getContext('2d');
        if (chartInstance) {
            chartInstance.destroy();
        }

        chartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: chartData.labels, // e.g. ["Season 01", "Season 02", ...]
                datasets: chartData.datasets.map((ds, i) => ({
                    label: ds.label,        // Hero or Role
                    data: ds.data,          // Values for each season
                    backgroundColor: chartColors[i % chartColors.length],
                    borderRadius: 4
                }))
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'top' }
                },
                scales: {
                    x: {
                        stacked: false,  // keep side-by-side grouping
                    },
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

    // Some preset colors for datasets
    const chartColors = [
        "#0d6efd", "#fd7e14", "#343a40"
    ];

    function updateDropdown(selectEl, allOptions, validOptions, currentValue) {
        selectEl.innerHTML = "";

        // Separate the "All ..." option
        const allOption = allOptions.find(opt => opt.startsWith("All"));
        const otherOptions = allOptions.filter(opt => opt !== allOption);

        // Split remaining into valid/invalid
        const validList = otherOptions.filter(opt => validOptions.includes(opt)).sort();
        const invalidList = otherOptions.filter(opt => !validOptions.includes(opt)).sort();

        // Build final array: "All ..." first, then valid, then invalid
        const sorted = [allOption, ...validList, ...invalidList];

        sorted.forEach(optValue => {
            const opt = document.createElement("option");
            opt.value = optValue;
            opt.textContent = optValue;

            // Disable if not valid and not "All ..."
            if (optValue !== allOption && !validOptions.includes(optValue)) {
                opt.disabled = true;
                opt.style.color = "#999";
            }

            // Preserve current selection
            if (optValue === currentValue) {
                opt.selected = true;
            }

            selectEl.appendChild(opt);
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
        const role = roleSelect.value;
        const season = seasonSelect.value;
        const stat = statSelect.value;

        fetch(`/options?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&season=${encodeURIComponent(season)}`)
            .then(response => response.json())
            .then(data => {
                // Heroes
                updateDropdown(heroSelect, data.heroes.all, data.heroes.valid, hero);

                // Roles
                updateDropdown(roleSelect, data.roles.all, data.roles.valid, role);

                // Seasons
                updateDropdown(seasonSelect, data.seasons.all, data.seasons.valid, season);

                // Stats (always fully refreshed)
                statSelect.innerHTML = "";
                data.stats.forEach(statOpt => {
                    const opt = document.createElement("option");
                    opt.value = statOpt;
                    opt.textContent = statOpt;
                    if (statOpt === stat) {
                        opt.selected = true;
                    }
                    statSelect.appendChild(opt);
                });
            })
            .catch(err => console.error("Error fetching dependent filters:", err));
    }


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

        // --- Fetch chart ---
// --- Fetch chart ---
        fetch(`/chart_data?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.json())
            .then(data => {
                if (!data.datasets || data.datasets.length === 0) {
                    console.warn("No chart data available");
                    return;
                }
                updateChart(data);
            })
            .catch(err => console.error("Error fetching chart data:", err));

    });

    // --- Clear Filters button ---
    document.getElementById("clearFilters").addEventListener("click", function () {
        // Reset dropdowns to first option (usually "All ...")
        heroSelect.selectedIndex = 0;
        roleSelect.selectedIndex = 0;
        seasonSelect.selectedIndex = 0;
        statSelect.selectedIndex = 0;

        heroImage.src = `/static/images/All Heroes.png`

        // Re-fetch default options (like on initial load)
        updateDependentFilters();

        // Clear result and chart
        resultDiv.textContent = "";
        if (chartInstance) {
            chartInstance.destroy();
            chartInstance = null;
        }

        // Clear summary
        const summaryDiv = document.getElementById("summary");
        if (summaryDiv) {
            summaryDiv.innerHTML = "";
        }
    });

        // --- Initialize on page load ---
    if (heroSelect.value) {
        heroImage.src = `/static/images/${heroSelect.value}.png`;
        heroImage.style.display = 'inline-block';
        updateDependentFilters();
        }
});
