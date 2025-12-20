let chart;

function analyze() {
    const reviews = document.getElementById("reviews").value.split("\n");

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ reviews })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("pos").innerText = data.dashboard.Positive;
        document.getElementById("neu").innerText = data.dashboard.Neutral;
        document.getElementById("neg").innerText = data.dashboard.Negative;

        drawChart(data.dashboard);
    });
}

function drawChart(stats) {
    const ctx = document.getElementById("sentimentChart");

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: "pie",
        data: {
            labels: ["Positive", "Neutral", "Negative"],
            datasets: [{
                data: [stats.Positive, stats.Neutral, stats.Negative],
                backgroundColor: ["#28a745", "#ffc107", "#dc3545"]
            }]
        }
    });
}