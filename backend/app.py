from flask import Flask, request, jsonify
from flask_cors import CORS
from recommendations import get_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    business_domain = data.get("business_domain", "").strip()
    expected_traffic = data.get("expected_traffic", "").strip()
    budget = data.get("budget", "").strip()
    security = data.get("security", "").strip()
    software_type = data.get("software_type", "").strip()

    recommendations = get_recommendations(business_domain, expected_traffic, budget, security, software_type)
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
