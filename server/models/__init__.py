from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from server.models.user import User

__all__ = ['db', 'User']
