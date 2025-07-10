# Google ADK Travel Agent Demo

This is a complete demo implementation of a multi-agent system using the [Google Agent Development Kit (ADK)](https://github.com/google/adk-python). The system simulates a **travel planning agent** scenario, demonstrating collaboration and task delegation between agents for organizing trips.

> ⚠️ All agent logic is centralized in a single file under:  
> `travel_agent/agent.py`

---

## 🧠 Agents Included

- TravelAssistant
- HotelBookingAgent
- FlightBookingAgent

All agents are defined and registered in the same `agent.py` file for simplicity and rapid prototyping.

---

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed **or**
- Python environment with `adk` installed and required dependencies

### Environment Setup

Before running, set your model API key via environment variable or `.env` file:

#### Option 1: Create a `.env` file

```env
OPENAI_API_KEY=xxxxxxxx
OTHER_MODEL_API_KEY=your-api-key-here
```

#### Option 2: Set as environment variable

**Linux/macOS**

```bash
export MODEL_API_KEY=your-api-key-here
```

**Windows (CMD)**

```cmd
set MODEL_API_KEY=your-api-key-here
```

---

## 🐳 Run with Docker Compose

```bash
docker compose up --build
```

This builds and starts the system with all agents ready to receive tasks via the web interface or command line.

---

## 🖥️ Run with Command Line

If you have the environment configured:

```bash
adk web --host=0.0.0.0
```

Access the interface via: [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure

```
.
├── travel_agent/
│   └── __init__.py
│   └── agent.py        # All agent classes and logic live here
├── Dockerfile
├── docker-compose.yml
├── .env.example        # Template for env variables
├── requirements.txt
├── README.md
```

