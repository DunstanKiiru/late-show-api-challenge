from faker import Faker
import random
from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

fake = Faker()

def seed_data():
    print("Seeding database...")

    db.drop_all()
    db.create_all()

    user = User(username="testing")
    user.set_password("testing123")
    db.session.add(user)

    guests = []
    for _ in range(5):
        guest = Guest(
            name=fake.name(),
            occupation=fake.job()
        )
        guests.append(guest)
    db.session.add_all(guests)

    episodes = []
    for i in range(1, 6):
        episode = Episode(
            date=fake.date_this_year().isoformat(),
            number=100 + i
        )
        episodes.append(episode)
    db.session.add_all(episodes)
    db.session.commit()

    appearances = []
    for _ in range(8):
        appearance = Appearance(
            rating=random.randint(1, 5),
            guest_id=random.choice(guests).id,
            episode_id=random.choice(episodes).id
        )
        appearances.append(appearance)

    db.session.add_all(appearances)
    db.session.commit()

    print("✅ Done seeding")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()
