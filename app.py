from flask import Flask, request, jsonify
from models import db, Incident
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([
        {
            "id": i.id,
            "title": i.title,
            "description": i.description,
            "severity": i.severity,
            "reported_at": i.reported_at.isoformat()
        } for i in incidents
    ])

@app.route('/incidents', methods=['POST'])
def add_incident():
    data = request.get_json()
    if not all(k in data for k in ("title", "description", "severity")):
        return jsonify({"error": "Missing fields"}), 400
    if data['severity'] not in ['Low', 'Medium', 'High']:
        return jsonify({"error": "Invalid severity"}), 400

    new_incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity'],
        reported_at=datetime.utcnow()
    )
    db.session.add(new_incident)
    db.session.commit()
    return jsonify({
        "id": new_incident.id,
        "title": new_incident.title,
        "description": new_incident.description,
        "severity": new_incident.severity,
        "reported_at": new_incident.reported_at.isoformat()
    }), 201

@app.route('/incidents/<int:id>', methods=['GET'])
def get_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "reported_at": incident.reported_at.isoformat()
    })

@app.route('/incidents/<int:id>', methods=['DELETE'])
def delete_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(incident)
    db.session.commit()
    return jsonify({"message": f"Incident {id} deleted."}), 200

if __name__ == '__main__':
    app.run(debug=True)
