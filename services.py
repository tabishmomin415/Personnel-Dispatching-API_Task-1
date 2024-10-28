from datetime import datetime
from models import db, Assignment

class AssignmentService:
    @staticmethod
    def create_assignment(personnel_id, project_id, role, start_time, end_time=None, status='Active'):
        start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
        if end_time:
            end_time = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")
        
        assignment = Assignment(personnel_id, project_id, role, start_time, end_time, status)
        db.session.add(assignment)
        db.session.commit()
        return assignment

    @staticmethod
    def get_all_assignments():
        return Assignment.query.all()

    @staticmethod
    def get_assignment(assignment_id):
        return Assignment.query.get(assignment_id)

    @staticmethod
    def update_assignment(assignment_id, **kwargs):
        assignment = Assignment.query.get(assignment_id)
        if assignment is None:
            return None
        for key, value in kwargs.items():
            if key in ['start_time', 'end_time'] and value is not None:
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            setattr(assignment, key, value)
        db.session.commit()
        return assignment

    @staticmethod
    def delete_assignment(assignment_id):
        assignment = Assignment.query.get(assignment_id)
        if assignment is None:
            return None
        db.session.delete(assignment)
        db.session.commit()
        return assignment
    
    @staticmethod
    def get_assignments_by_project(project_id):
        assignments = Assignment.query.filter_by(project_id=project_id).all()
        print(assignments) 
        return assignments
