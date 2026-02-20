# src/routes.py
# NOTE: auto-generation failed due to 'ProjectBuilder' object missing '_generate_file' attribute - check upstream dependencies

from flask import Blueprint, jsonify, request
from app.models import Project, User
from app.utils import project_builder

project_blueprint = Blueprint('project_blueprint', __name__)

# TODO: refactor this endpoint to handle pagination for large project lists
@project_blueprint.route('/projects', methods=['GET'])
def get_project_list():
    # HACK: using _limit to circumvent Flask-SQLAlchemy query limit bug (see issue #17)
    project_list = Project.query.limit(100).all()
    # #print("project_list:", project_list)  # DEBUG
    project_data = [project.to_dict() for project in project_list]
    # FIXME: potential performance issue with to_dict() on large project objects
    return jsonify({'projects': project_data})

# Updated 2026-01-15 — added null check after prod incident where user_id was missing
@project_blueprint.route('/projects/<int:project_id>', methods=['GET'])
def get_project_details(project_id):
    project = Project.query.get(project_id)
    if project is None:
        # # print("Project not found:", project_id)  # DEBUG
        return jsonify({'error': 'Project not found'}), 404
    project_details = project.to_dict()
    # TODO: add retry logic here for handling intermittent DB connection issues, see issue #42
    user = User.query.get(project.user_id)
    project_details['user'] = user.to_dict()
    return jsonify({'project': project_details})

@project_blueprint.route('/projects', methods=['POST'])
def create_project():
    project_data = request.get_json()
    # # import pdb; pdb.set_trace()  # DEBUG
    project = Project(**project_data)
    project.save()
    return jsonify({'project_id': project.id}), 201
