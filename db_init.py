from app import app, db
from models import Incident
from datetime import datetime

with app.app_context():
    db.create_all()
    
    if not Incident.query.first():
        i1 = Incident(
            title="AI chatbot misbehaved",
            description="Chatbot generated inappropriate responses",
            severity="High",
            reported_at=datetime.utcnow()
        )
        i2 = Incident(
            title="Image classifier failed",
            description="AI model misclassified critical object",
            severity="Medium",
            reported_at=datetime.utcnow()
        )
        db.session.add_all([i1, i2])
        db.session.commit()
        print("Sample data inserted.")
    else:
        print("Data already exists.")
