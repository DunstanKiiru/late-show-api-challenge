from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db

from server.models.appearance import Appearance

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    if not (1 <= data.get("rating", 0) <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    appearance = Appearance(
        rating=data["rating"],
        guest_id=data["guest_id"],
        episode_id=data["episode_id"]
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify({"message": "Appearance created"}), 201
