# 🐳 GitHub Gist Fetcher API

This project is a simple **Flask-based HTTP API** that fetches the **public GitHub gists** for a given user using the GitHub REST API. The application is containerized with Docker and ready for easy deployment.

---

## 🚀 Features

- `GET /<username>` endpoint to fetch public gists for any GitHub user
- Handles various HTTP responses (200, 403, 404, others)
- Returns a helpful message when a user has no public gists
- Includes automated test cases using `pytest`
- Dockerized with multi-stage build
- Security scanned using Trivy and Bandit

---

## 🏗️ Tech Stack

- Python 3.10
- Flask
- Requests
- Pytest
- Docker
- Bandit (Code analysis)
- Trivy (Security scanning)

---

## 🐳 Docker Setup

### 📁 1. Clone the Repository

```bash
git clone https://github.com/sowmya205/github-gists-api.git
cd github-gists-api
💻 2. Install Docker Desktop
If you don't have Docker installed, download and install it:

👉 https://www.docker.com/products/docker-desktop

🔨 3. Build the Docker Image
bash
Copy
Edit
docker build -t <your-dockerhub-username>:<version> .
Example:

bash
Copy
Edit
docker build -t sowmya205/gists-api:1.0 .
🚀 4. Run the Docker Container
bash
Copy
Edit
docker run -p 8080:8080 <your-dockerhub-username>:<version>
Example:

bash
Copy
Edit
docker run -p 8080:8080 sowmya205/assignment:v1
🌐 5. Verify the API
Visit the following URL in your browser or use curl:

bash
Copy
Edit
http://localhost:8080/octocat
You should see a list of gists for the GitHub user octocat.


🔐 Security Scanning
Trivy – Scan Docker image for known vulnerabilities:

bash
Copy
Edit
trivy image sowmya205/gists-api:1.0
Bandit – Scan Python code for security issues:


🧪 API Endpoints
Method	Endpoint	Description
GET	/octocat	Returns list of public gists for the user


❌ Error Handling
Status Code	Message
200	Gists returned / No gists
404	GitHub user not found
403	Rate limited or access denied
500+	Unexpected server/API error

📁 Project Structure
bash
Copy
Edit
.
├── src/
│   ├── app.py            # Flask app with route
│   └── __init__.py       
├── test/
│   ├── test_app.py       # Pytest test cases
│   └── __init__.py       
├── main.py               # Entry point
├── requirements.txt
├── Dockerfile
└── README.md
✍️ Author
Sowmya Devi Telidevara
Cloud & DevOps Engineer
LinkedIn
GitHub

📜 License
This project is intended for technical assessment and learning purposes.

yaml
Copy
Edit

---

Let me know if you want this saved as a downloadable `.md` file or pushed into your GitHub repository.







