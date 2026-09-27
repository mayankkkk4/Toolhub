from datetime import datetime
from extensions import db

class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True)
    feedback_type = db.Column(db.String(32), nullable=False) # 'suggestion' or 'bug'
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), nullable=True)
    status = db.Column(db.String(32), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'feedback_type': self.feedback_type,
            'title': self.title,
            'description': self.description,
            'email': self.email,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
