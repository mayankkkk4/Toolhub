from datetime import datetime
from extensions import db

class ToolStat(db.Model):
    __tablename__ = 'tool_stats'

    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.String(64), unique=True, nullable=False, index=True)
    use_count = db.Column(db.Integer, default=0)
    last_used_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'tool_id': self.tool_id,
            'use_count': self.use_count,
            'last_used_at': self.last_used_at.isoformat()
        }
