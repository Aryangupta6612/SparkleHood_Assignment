

```markdown
# 🛡️ AI Safety Incident Log API

A simple and clean RESTful API built using **Python (Flask)** and **SQLite** to log and manage hypothetical AI safety incidents. This project is created as part of a backend take-home assignment for **HumanChain**, an AI safety-focused startup.

---

## 📌 Tech Stack

- **Language**: Python 3
- **Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy

---

## 🚀 How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Aryangupta6612/SparkleHood_Assignment.git 
```

```bash
cd incident-log-api
```

### 2. Create and Activate Virtual Environment

<details>
<summary>🪟 Windows</summary>

```bash
python -m venv venv
venv\Scripts\activate
```

</details>

<details>
<summary>🐧 macOS/Linux</summary>

```bash
python3 -m venv venv
source venv/bin/activate
```

</details>

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python db_init.py
```

✅ This will automatically create a new `incidents.db` file with **2-3 sample incidents**.

### 5. Start the Flask Development Server

```bash
python app.py
```

Now visit `http://localhost:5000` — You’ll be greeted with a friendly welcome page that tells you how to test the API using Postman.

---

## 📮 API Endpoints

All endpoints accept and return **JSON**.

### 1. Get All Incidents

```http
GET /incidents
```

Returns a list of all incidents.

---

### 2. Create a New Incident

```http
POST /incidents
```

#### Request Body:

```json
{
  "title": "Example Incident",
  "description": "Detailed description of the incident.",
  "severity": "High"
}
```

✅ Valid Severities: `"Low"`, `"Medium"`, `"High"`

Returns the created incident with auto-generated `id` and `reported_at`.

---

### 3. Get a Specific Incident

```http
GET /incidents/<id>
```

Returns the incident matching the given ID, or `404` if not found.

---

### 4. Delete a Specific Incident

```http
DELETE /incidents/<id>
```

Deletes the incident with the specified ID. Returns `204 No Content` if successful or `404 Not Found`.

---

## 🗂️ Project Structure

```
incident-log-api/
│
├── app.py               # Main Flask application
├── db_init.py           # Creates DB and inserts sample incidents
├── incidents.db         # SQLite database (auto-generated)
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it!
```

---

## ⚙️ Environment and Configuration

- No environment variables are needed for this basic project.
- The SQLite database file is created automatically when you run `db_init.py`.

---

## 🧪 Testing with Postman

1. Open [Postman](https://www.postman.com/)
2. Create a new request for any of the endpoints above
3. Use raw JSON in the body for `POST` requests
4. Test and verify responses

---

## 💡 Notes & Design Decisions

- Used **SQLite** for simplicity (no setup needed).
- Implemented **SQLAlchemy ORM** to model and interact with the database cleanly.
- Basic validation checks for missing fields and invalid severity values.
- A home route (`/`) guides the user to Postman instead of showing "404 Not Found".

---

## 📥 Sample Request

```bash
curl -X POST http://localhost:5000/incidents \
     -H "Content-Type: application/json" \
     -d '{"title":"AI Bug", "description":"Model behaved unpredictably", "severity":"High"}'
```

---

## 🙌 Author

**Aryan Gupta**  
B.Tech (Data Science), Lovely Professional University  
Backend + Data Science Enthusiast | GitHub: [Aryangupta6612]

---

## 🏁 Ready to Go

```bash
cd incident-log-api
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python db_init.py
python app.py
```

> Built with ❤️ for HumanChain’s AI safety mission.