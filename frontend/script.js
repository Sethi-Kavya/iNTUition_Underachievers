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
        function cleanText(text) {
            return text.replace(/\*\*/g, "").replace(/\n/g, "<br>");
        }

        document.getElementById("recommendationOutput").innerHTML = `
            <h3>Tech Stack Recommendation</h3>
            <p>${cleanText(data.tech_stack)}</p>

            <h3>Data Storage Type & Structure</h3>
            <p>${cleanText(data.data_storage)}</p>

            <h3>System Architecture</h3>
            <p>${cleanText(data.architecture)}</p>

            <h3>API Requirements & Structure</h3>
            <p>${cleanText(data.api_structure)}</p>

            <h3>Codebase Structure</h3>
            <pre>${cleanText(data.codebase)}</pre>

            <h3>Deployment & Hosting Recommendations</h3>
            <p>${cleanText(data.deployment)}</p>

            <h3>Estimated Cost Breakdown</h3>
            <p>${cleanText(data.cost)}</p>
        `;
    })
    .catch(error => console.error("Error fetching recommendations:", error));
}
