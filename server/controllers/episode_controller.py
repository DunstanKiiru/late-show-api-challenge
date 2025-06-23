from flask import Blueprint, request, jsonify
from server.app import db
from server.models.episode import Episode
from server.models.appearance import Appearance
from flask_jwt_extended import jwt_required

episode_bp = Blueprint("episode", __name__, url_prefix="/episodes")

@episode_bp.route("", methods=["GET"])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in episodes]), 200

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict()), 200

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"msg": "Episode and related appearances deleted"}), 200
