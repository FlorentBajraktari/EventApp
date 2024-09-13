# backend/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from user_model import User
from base_model import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# backend/controllers/event_controller.py
from flask import Blueprint, request, jsonify
from event_model import Event
from base_model import db

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(name=data['name'], description=data['description'], location=data['location'], date=data['date'], type=data['type'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event created successfully"}), 201

@event_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])
