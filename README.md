# HumanChain AI Safety Incident Log API

A simple Flask REST API to log and manage AI safety incidents.

## 🔧 Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

## ▶️ How to Run

```bash
# 1. Clone or navigate to project folder
cd incident-log-api

# 2. Setup virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # for Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize DB with sample incidents
python db_init.py

# 5. Run the server
python app.py
