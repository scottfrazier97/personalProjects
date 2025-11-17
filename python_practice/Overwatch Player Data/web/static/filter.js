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

    // Chart.js instances
    let barChartInstance = null;
    let lineChartInstance = null;

    // Chart colors 
    const chartColors = ["#0d6efd", "#fd7e14", "#343a40"];

    // --- Update Bar Chart ---
    function updateBarChart(chartData) {
        const ctx = document.getElementById('statChart').getContext('2d');
        if (barChartInstance) barChartInstance.destroy();

        barChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: chartData.labels,
                datasets: chartData.datasets.map((ds, i) => ({
                    label: ds.label,
                    data: ds.data,
                    backgroundColor: chartColors[i % chartColors.length],
                    borderRadius: 4
                }))
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'top' } },
                scales: {
                    x: { stacked: false },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => value.toLocaleString()
                        }
                    }
                }
            }
        });
    }

    // --- Update Line Chart ---
    function updateLineChart(chartData) {
        const ctx = document.getElementById('lineChart').getContext('2d');
        if (lineChartInstance) lineChartInstance.destroy();

        lineChartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: chartData.labels,
                datasets: chartData.datasets.map((ds, i) => ({
                    label: ds.label,
                    data: ds.data,
                    borderColor: chartColors[i % chartColors.length],
                    backgroundColor: chartColors[i % chartColors.length],
                    fill: false,
                    tension: 0.3,
                    pointRadius: 4,
                    pointHoverRadius: 6
                }))
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'top' } },
                scales: {
                    x: { stacked: false },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: value => value.toLocaleString()
                        }
                    }
                }
            }
        });
    }

    // --- Update dependent dropdowns ---
    function updateDropdown(selectEl, allOptions, validOptions, currentValue) {
        selectEl.innerHTML = "";

        const allOption = allOptions.find(opt => opt.startsWith("All"));
        const otherOptions = allOptions.filter(opt => opt !== allOption);

        const validList = otherOptions.filter(opt => validOptions.includes(opt)).sort();
        const invalidList = otherOptions.filter(opt => !validOptions.includes(opt)).sort();
        const sorted = [allOption, ...validList, ...invalidList];

        sorted.forEach(optValue => {
            const opt = document.createElement("option");
            opt.value = optValue;
            opt.textContent = optValue;

            if (optValue !== allOption && !validOptions.includes(optValue)) {
                opt.disabled = true;
                opt.style.color = "#999";
            }

            if (optValue === currentValue) opt.selected = true;

            selectEl.appendChild(opt);
        });
    }

    // --- Update hero image ---
    heroSelect.addEventListener('change', function() {
        if (heroSelect.value) {
            heroImage.src = `/static/images/${heroSelect.value}.png`;
            heroImage.style.display = 'inline-block';
        } else {
            heroImage.style.display = 'none';
        }
        updateDependentFilters();
    });

    // --- Update dependent filters ---
    function updateDependentFilters() {
        const hero = heroSelect.value;
        const role = roleSelect.value;
        const season = seasonSelect.value;
        const stat = statSelect.value;

        fetch(`/options?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&season=${encodeURIComponent(season)}`)
            .then(response => response.json())
            .then(data => {
                updateDropdown(heroSelect, data.heroes.all, data.heroes.valid, hero);
                updateDropdown(roleSelect, data.roles.all, data.roles.valid, role);
                updateDropdown(seasonSelect, data.seasons.all, data.seasons.valid, season);

                statSelect.innerHTML = "";
                data.stats.forEach(statOpt => {
                    const opt = document.createElement("option");
                    opt.value = statOpt;
                    opt.textContent = statOpt;
                    if (statOpt === stat) opt.selected = true;
                    statSelect.appendChild(opt);
                });
            })
            .catch(err => console.error("Error fetching dependent filters:", err));
    }

    [heroSelect, roleSelect, seasonSelect].forEach(select => {
        select.addEventListener("change", updateDependentFilters);
    });

    // --- Handle form submission ---
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const hero = heroSelect.value;
        const season = seasonSelect.value;
        const role = roleSelect.value;
        const stat = statSelect.value;

        // Fetch result text
        fetch(`/filter?hero=${encodeURIComponent(hero)}&season=${encodeURIComponent(season)}&role=${encodeURIComponent(role)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.text())
            .then(data => {
                resultDiv.textContent = data;
                updateDependentFilters();
            })
            .catch(err => {
                resultDiv.textContent = 'Error fetching data';
                console.error(err);
            });

        // Fetch chart data
        fetch(`/chart_data?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.json())
            .then(data => {
                if (!data.datasets || data.datasets.length === 0) return;
                updateBarChart(data);
                updateLineChart(data);
            })
            .catch(err => console.error("Error fetching chart data:", err));
    });

    // --- Clear Filters ---
    document.getElementById("clearFilters").addEventListener("click", function () {
        [heroSelect, roleSelect, seasonSelect, statSelect].forEach(sel => sel.selectedIndex = 0);
        heroImage.src = `/static/images/All Heroes.png`;
        heroImage.style.display = 'inline-block';

        updateDependentFilters();
        resultDiv.textContent = "";

        if (barChartInstance) { barChartInstance.destroy(); barChartInstance = null; }
        if (lineChartInstance) { lineChartInstance.destroy(); lineChartInstance = null; }

        const summaryDiv = document.getElementById("summary");
        if (summaryDiv) summaryDiv.innerHTML = "";
    });

    // --- Function to fetch chart data and update both charts ---
    function loadCharts() {
        const hero = heroSelect.value;
        const season = seasonSelect.value;
        const role = roleSelect.value;
        const stat = statSelect.value;

        fetch(`/chart_data?hero=${encodeURIComponent(hero)}&role=${encodeURIComponent(role)}&season=${encodeURIComponent(season)}&stat=${encodeURIComponent(stat)}`)
            .then(response => response.json())
            .then(data => {
                if (!data.datasets || data.datasets.length === 0) return;
                updateBarChart(data);
                updateLineChart(data);
            })
            .catch(err => console.error("Error fetching chart data:", err));
    }

    // --- Initialize page ---
    if (heroSelect.value) {
        heroImage.src = `/static/images/${heroSelect.value}.png`;
        heroImage.style.display = 'inline-block';
        updateDependentFilters(); // rebuild dropdowns
        loadCharts();             // fetch and display chart data
    }

});
