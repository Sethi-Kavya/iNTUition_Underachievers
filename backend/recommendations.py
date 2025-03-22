def get_recommendations(business_domain, expected_traffic, budget, security, software_type):
    recommendations = {}

    if business_domain.lower() == "e-commerce" and expected_traffic.lower() == "medium" and budget.lower() == "medium" and security.lower() == "basic" and software_type.lower() == "web application":
        recommendations["tech_stack"] = """
Backend: Node.js (Express.js) – Handles high concurrent requests efficiently, has a large ecosystem, and is easy to scale.
Frontend: React.js + Next.js – Improves performance with server-side rendering and SEO benefits.
Database: PostgreSQL (SQL) – Ensures data consistency, supports indexing, and handles transactions efficiently.
DevOps Tools: Docker, GitHub Actions for CI/CD – Ensures containerized deployment and automated testing."""

        recommendations["data_storage"] = """
DB Choice: SQL (PostgreSQL) – Structured storage is ideal for product catalogs, orders, and transactions.
Justification: Ensures ACID compliance, fast lookups, and indexing for efficient queries.
Schema Suggestion:
Users Table – Stores user information (name, email, password hash).
Products Table – Contains product details (name, price, category, stock).
Orders Table – Manages orders with order status and payment tracking.
Payments Table – Stores transaction details and payment confirmations."""

        recommendations["architecture"] = """
Architecture Type: Monolithic with modular components – Easier for a small team to manage and deploy.
Reason: E-commerce logic (products, orders, payments) is tightly integrated, making a monolithic approach simpler.
Internal Communication: REST API – Standard for web apps; simpler than GraphQL for basic needs."""

        recommendations["api_structure"] = """
API Type: REST API with JWT authentication – Provides secure authentication without storing session data on the server.
Endpoints:
POST /users/signup – Handles user registration.
GET /products – Fetches product listings.
POST /orders – Processes new orders.
POST /payments – Handles payment transactions.
Security Measures: SSL for secure data transmission, rate limiting to prevent abuse, API Gateway for scalability."""

        recommendations["codebase"] = """
/src  
   /controllers (API logic)  
   /models (Database schema)  
   /routes (API endpoints)  
   /services (Business logic)  
   /config (Environment & security settings)  
Pattern Used: MVC – Separates concerns for maintainability and scalability."""

        recommendations["deployment"] = """
Cloud Provider: AWS – Offers scalability, reliability, and cost-effective solutions.
Hosting Setup:
Backend: EC2 instances – Provides flexible compute power.
Database: AWS RDS (PostgreSQL) – Managed database with automatic backups.
Storage: S3 for image hosting – Reduces server load and optimizes performance.
Deployment Strategy: Docker containers managed via AWS ECS – Ensures consistency across environments.
CI/CD: GitHub Actions – Automates deployment and testing for faster iterations."""

        recommendations["cost"] = """
Hosting: ~$70/month – Includes EC2 instances and network traffic costs.
Database: ~$50/month – Covers AWS RDS costs.
Total: ~$120/month – Optimized for medium-scale operations.
Cost Optimization Tips: Use a free-tier CDN for images, optimize database queries to reduce computational load."""

    elif business_domain.lower() == "fintech" and expected_traffic == "high" and budget.lower() == "high" and security.lower() == "high" and software_type.lower() == "web & mobile app" :
        recommendations["tech_stack"] = """
Backend: Java (Spring Boot) – Java provides strong security, scalability, and multithreading for handling high transaction loads.
Frontend: React Native (Mobile) + Vue.js (Web) – Ensures a consistent UI across platforms with optimized performance.
Database: PostgreSQL for transactional data, Redis for caching – PostgreSQL ensures ACID compliance, and Redis speeds up frequent lookups.
DevOps Tools: Kubernetes, Terraform for infrastructure management – Enables auto-scaling and efficient resource provisioning."""

        recommendations["data_storage"] = """
DB Choice: SQL (PostgreSQL) – Ensures transactional consistency and compliance with financial regulations.
Justification: ACID compliance is critical for secure and accurate transaction processing.
Schema Suggestion:
Users Table – Stores user ID, name, and KYC verification status.
Transactions Table – Logs sender, receiver, amount, and timestamp to track financial activities securely."""

        recommendations["architecture"] = """
Architecture Type: Microservices – Helps scale individual services independently (e.g., payments, user authentication).
Reason: Fintech apps require modularity, allowing updates to specific services without affecting the whole system.
Internal Communication: gRPC between microservices – Ensures fast, efficient, and secure inter-service communication."""

        recommendations["api_structure"] = """
API Type: REST API with OAuth authentication – OAuth ensures secure authentication while allowing third-party integrations.
Endpoints:
POST /users/verifyKYC – Verifies user identity before enabling transactions.
POST /transactions/initiate – Processes financial transactions securely.
GET /transactions/history – Retrieves a user’s transaction history.
Security Measures: AES encryption for sensitive data, JWT for authentication, API Gateway for request management, and DDoS protection."""

        recommendations["codebase"] = """
/services  
   /auth-service  
   /payment-service  
   /user-service  
Pattern Used: Domain-Driven Design (DDD) – Helps define clear service boundaries and ensures maintainability."""

        recommendations["deployment"] = """
Cloud Provider: Google Cloud Platform (GCP) – Provides high security, compliance, and scalability for fintech applications.
Hosting Setup:
Backend: Deployed using Kubernetes with auto-scaling for handling traffic spikes.
Database: Managed PostgreSQL with encryption at rest and backup mechanisms.
Storage: Secure object storage for user documents and KYC verification files.
Deployment Strategy: Kubernetes clusters for high availability and resilience.
CI/CD: GitLab CI/CD – Automates testing and deployment for better security and reliability."""

        recommendations["cost"] = """
Hosting: ~$500/month – Covers Kubernetes clusters and compute instances.
Database: ~$300/month – Includes managed PostgreSQL and backups.
Total: ~$800/month – Necessary for high-security infrastructure.
Cost Optimization Tips: Use spot instances for background processing to reduce infrastructure costs."""

    else:
        recommendations["tech_stack"] = "No matching recommendation found."
        recommendations["data_storage"] = "No matching recommendation found."
        recommendations["architecture"] = "No matching recommendation found."
        recommendations["api_structure"] = "No matching recommendation found."
        recommendations["codebase"] = "No matching recommendation found."
        recommendations["deployment"] = "No matching recommendation found."
        recommendations["cost"] = "No matching recommendation found."

    return recommendations
