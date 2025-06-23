from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint("guest", __name__, url_prefix="/guests")

@guest_bp.route("", methods=["GET"])
def list_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200
