from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personnel_id = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default='Active')

    def __init__(self, personnel_id, project_id, role, start_time, end_time=None, status='Active'):
        self.personnel_id = personnel_id
        self.project_id = project_id
        self.role = role
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
