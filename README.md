# Valorant Player Analytics Platform

A full-stack analytics platform that lets you look up and compare Valorant player statistics in real time. Built with a Python FastAPI backend, React frontend, and deployed on AWS using Docker and a fully automated CI/CD pipeline.

## Features

- Real-time player statistics via the Riot Games API
- Side-by-side comparison of any two players
- KDA, win rate, headshot percentage, and agent performance metrics
- Interactive React dashboard with bar chart visualizations
- Live backend deployed on AWS ECS Fargate

## Tech Stack

**Backend**
- Python, FastAPI
- Riot Games API integration
- Docker (containerized deployment)

**Frontend**
- React, JavaScript
- Recharts (data visualization)
- CSS

**Infrastructure**
- AWS ECS Fargate (container orchestration)
- AWS ECR (container registry)
- GitHub Actions (CI/CD pipeline)

## Architecture

```
GitHub Push → GitHub Actions → Docker Build → AWS ECR → AWS ECS Fargate
```

Every push to `main` triggers an automated pipeline that builds, pushes, and deploys the latest Docker image — reducing deployment time from 15 minutes to under 3 minutes.

## Live API

The backend is deployed and accessible at:

```
http://35.183.137.184:8000/docs
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- Riot Games API key

### Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/player/{username}` | Get player stats |
| GET | `/compare/{player1}/{player2}` | Compare two players |

## CI/CD Pipeline

Automated deployment via GitHub Actions:

1. Triggered on every push to `main`
2. Builds Docker image
3. Pushes to AWS ECR
4. Deploys to AWS ECS Fargate with zero downtime

## Author

**Mandel Kenol**
- GitHub: [@Mandel556](https://github.com/Mandel556)
- Email: mandelkenol@outlook.com
