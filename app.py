from flask import Flask, request, jsonify
from models import db, Assignment
from services import AssignmentService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignments.db'
db.init_app(app)

with app.app_context():
    db.create_all() 

@app.route('/assignments', methods=['POST'])
def create_assignment():
    data = request.json
    assignment = AssignmentService.create_assignment(
        data['personnel_id'],
        data['project_id'],
        data['role'],
        data['start_time'],
        data.get('end_time'),
        data.get('status', 'Active')
    )
    return jsonify({'id': assignment.id}), 201

@app.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = AssignmentService.get_all_assignments()
    return jsonify([{
        'id': a.id,
        'personnel_id': a.personnel_id,
        'project_id': a.project_id,
        'role': a.role,
        'start_time': a.start_time,
        'end_time': a.end_time,
        'status': a.status
    } for a in assignments]), 200

@app.route('/assignments/<int:assignment_id>', methods=['GET'])
def get_assignment(assignment_id):
    assignment = AssignmentService.get_assignment(assignment_id)
    if assignment:
        return jsonify({
            'id': assignment.id,
            'personnel_id': assignment.personnel_id,
            'project_id': assignment.project_id,
            'role': assignment.role,
            'start_time': assignment.start_time,
            'end_time': assignment.end_time,
            'status': assignment.status
        }), 200
    return jsonify({'error': 'Assignment not found'}), 404

@app.route('/assignments/<int:assignment_id>', methods=['PUT'])
def update_assignment(assignment_id):
    data = request.json
    updated_assignment = AssignmentService.update_assignment(assignment_id, **data)
    return jsonify({'id': updated_assignment.id}), 200

@app.route('/assignments/<int:assignment_id>', methods=['DELETE'])
def delete_assignment(assignment_id):
    assignment = AssignmentService.delete_assignment(assignment_id)
    return jsonify({'id': assignment.id}), 200

@app.route('/assignments/project/<int:project_id>', methods=['GET'])
def get_assignments_by_project(project_id):
    assignments = AssignmentService.get_assignments_by_project(project_id)
    if assignments:
        return jsonify([
            {
                "id": a.id,
                "personnel_id": a.personnel_id,
                "project_id": a.project_id,
                "role": a.role,
                "start_time": a.start_time.isoformat(),
                "end_time": a.end_time.isoformat() if a.end_time else None,
                "status": a.status
            } for a in assignments
        ]), 200
    return jsonify({"error": f"No assignments found for project ID {project_id}"}), 404

if __name__ == '__main__':
    app.run(debug=True)
