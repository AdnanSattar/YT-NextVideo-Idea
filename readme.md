# 🚀 YouTube Video Idea Generator AI Powered (Fullstack)

This project is a **full-stack AI-powered YouTube idea generator** that extracts comments from YouTube videos, analyzes them, and suggests potential video ideas using **FastAPI (Python)** for the backend and **Next.js (TypeScript/Tailwind)** backed for the frontend and **CrewAI agentic AI**.


## 🌟 Features
- 🔍 **Extract & Analyze Comments** – Scrapes YouTube comments and filters useful insights.
- 💡 **AI-Powered Idea Generation** – Uses CrewAI agents to generate video ideas.
- 📊 **Scoring System** – Prioritizes ideas based on engagement and relevancy.
- 🛠 **Modern Tech Stack** – **FastAPI (Python) & Next.js (TypeScript/Tailwind)**.
- ⚡ **Fast & Scalable** – Supports background tasks for seamless processing.

## 🛠 Built With
FastAPI (Python) - API Backend
Next.js (React + TypeScript) - Frontend UI
CrewAI - AI Agents for Idea Generation
SQLite - Lightweight database
Tailwind CSS - Styling
Drizzle ORM - Database management

## 🏗 Project Structure

```
YOUTUBEIDEAGENERATORAIFULLSTACK/ 
│── 📂 youtube-idea-generator-fastapi/ # Backend (FastAPI)  
├── 📄 api.py # FastAPI endpoints 
├── 📄 crew.py # CrewAI logic 
├── 📂 config/ # Configuration files  
│    ├── 📄 agents.yaml # CrewAI agents configuration 
│    ├── 📄 tasks.yaml # CrewAI tasks configuration  
├── 📄 SearchYouTubeTool.py # Custom YouTube scraper tool 
├── 📄 main.py # FastAPI app entry point  
├── 📄 pyproject.toml # Python project dependencies 
│
│── 📂 youtube-idea-generator-nextjs/ # Frontend (Next.js)  
├── 📂 app/ # Application pages 
├── 📂 components/ # UI components 
├── 📂 server/ # Backend interaction (API calls) 
├── 📄 package.json # Project metadata 
├── 📄 tsconfig.json # TypeScript configuration 
├── 📂 public/ # Static assets 
│── 📄 .gitignore # Git ignore file 
│── 📄 README.md # Documentation
```

## ⚡ Installation & Setup

### **1️⃣ Backend (FastAPI) Setup**
> **Prerequisites**: Python 3.10+ installed.

```bash
# Navigate to FastAPI backend directory
cd youtube-idea-generator-fastapi

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# Install dependencies
pip install .

# Run FastAPI server
uvicorn main:app --reload
Your FastAPI API will be available at http://127.0.0.1:8000.
```

### **2️⃣ Frontend (Next.js) Setup**
Prerequisites: Node.js 18+ installed.

```bash
# Navigate to Next.js frontend directory
cd youtube-idea-generator-nextjs

# Install dependencies
npm install

# Run development server
npm run dev
Your frontend app will be available at http://localhost:3000.
```

### 📌 **Environment Variables**
```bash
Copy .env.example as .env and update values.

#### FastAPI
CREWAI_URL=http://127.0.0.1:8000
CREWAI_BEARER_TOKEN=your_secret_token
#### Next.js
NEXT_PUBLIC_CREWAI_URL=http://127.0.0.1:8000
```

## 📜 API Endpoints./
FastAPI Backend
Method	Endpoint	Description
GET	/	API Health Check
POST	/kickoff/	Start idea generation
GET	/status/{kickoff_id}	Check job status
GET	/new-ideas/	Fetch newly generated video ideas
GET	/idea-details/	Get details of an idea

## 🤝 Contributing
Fork this repository.
Create a new branch (feature-branch).
Commit your changes.
Push to your fork.
Submit a pull request.