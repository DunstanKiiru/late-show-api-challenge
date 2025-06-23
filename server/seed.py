from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="admin")
    user.set_password("password123")
    db.session.add(user)

    guest1 = Guest(name="John Doe", occupation="Comedian")
    guest2 = Guest(name="Jane Smith", occupation="Musician")
    db.session.add_all([guest1, guest2])

    ep1 = Episode(date=date(2023, 6, 1), number=1)
    ep2 = Episode(date=date(2023, 6, 8), number=2)
    db.session.add_all([ep1, ep2])

    db.session.commit()

    appearance1 = Appearance(rating=4, guest_id=guest1.id, episode_id=ep1.id)
    appearance2 = Appearance(rating=5, guest_id=guest2.id, episode_id=ep2.id)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()
    print("Seed data inserted successfully.")
