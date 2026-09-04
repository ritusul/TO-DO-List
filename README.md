# AI-Powered To-Do List

A beginner-friendly but modular M.Sc. Computer Science project built with Python, Streamlit, SQLite and SQLAlchemy. AI features are optional and use an environment variable for the provider key.

## Features
- CRUD task management
- Priority, category, due date/time and estimated duration
- Search, filters, sorting, overdue/today views
- Dashboard metrics and Plotly chart
- AI natural-language task extraction
- AI task breakdown with confirmation
- AI task prioritization
- AI daily planner with non-overlapping schedule generation
- AI assistant grounded in the actual task list
- Graceful AI fallback when no API key is configured
- Basic validation and tests

## Architecture
User → Streamlit UI → Services → AI Service → LLM → validated structured JSON → SQLite

## Folder Structure
```text
todo_ai/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── models.py
├── services/
│   ├── __init__.py
│   ├── task_service.py
│   ├── ai_service.py
│   └── planner_service.py
├── ui/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── tasks.py
│   └── ai_features.py
├── utils/
│   ├── __init__.py
│   └── validators.py
└── tests/
    └── test_services.py
```

## Database Design
`tasks`: id, title, description, category, priority, status, due_date, due_time, estimated_minutes, created_at, completed_at.

`subtasks`: id, task_id, title, status.

`productivity_history`: id, date, completed_tasks, pending_tasks, completion_percentage.

## Installation
### Windows PowerShell
```powershell
cd todo_ai
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

If PowerShell blocks activation, use Command Prompt:
```cmd
venv\Scripts\activate
```

### macOS/Linux
```bash
cd todo_ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## AI Setup
Open `.env`, set `OPENAI_API_KEY`, and optionally change `OPENAI_MODEL`. Never commit `.env` to Git. Without a key, core CRUD features remain usable and simple fallback behavior is provided.

## Testing
```bash
pytest -q
```

## Screenshots
Run the application and capture screenshots of Dashboard, My Tasks, Add Task, AI Assistant and Daily Planner here.

## Future Enhancements
Authentication, recurring tasks, calendar integration, notifications, richer productivity history, embeddings/RAG for personal notes, mobile/PWA client, and deployment to Streamlit Community Cloud.

## Run
```bash
streamlit run app.py
```
