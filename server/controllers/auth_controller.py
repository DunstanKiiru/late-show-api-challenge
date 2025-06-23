from flask import Blueprint, request, jsonify
from server.app import db
from server.models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__, url_prefix="/")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"msg": "Missing username or password"}), 400

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return jsonify({"msg": "Invalid credentials"}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"msg": "Server error", "error": str(e)}), 500
