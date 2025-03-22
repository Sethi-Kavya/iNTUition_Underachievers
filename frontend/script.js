function getRecommendation() {
    const data = {
        business_domain: document.getElementById("business_domain").value,
        expected_traffic: document.getElementById("expected_traffic").value,
        budget: document.getElementById("budget").value,
        security: document.getElementById("security").value,
        software_type: document.getElementById("software_type").value
    };

    fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        function formatOutput(label, value) {
            return `<h3>${label}:</h3><p>${value}</p>`;
        }

        document.getElementById("recommendationOutput").innerHTML = `
            ${formatOutput("Tech Stack Recommendation", data.tech_stack)}
            ${formatOutput("Data Storage Type & Structure", data.data_storage)}
            ${formatOutput("System Architecture", data.architecture)}
            ${formatOutput("API Requirements & Structure", data.api_structure)}
            ${formatOutput("Codebase Structure", data.codebase)}
            ${formatOutput("Deployment & Hosting Recommendations", data.deployment)}
            ${formatOutput("Estimated Cost Breakdown", data.cost)}
        `;
    })
    .catch(error => console.error("Error fetching recommendations:", error));
}
