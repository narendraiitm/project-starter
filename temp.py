from main import app
from models import db, Blog
from sec import user_datastore
from flask_security import hash_password

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # blog = Blog(title="First blog", description="My first blog in db")
        # db.session.add(blog)
        if not user_datastore.find_user(email='narendra@gmail.com'):
            user_datastore.create_user(email="narendra@gmail.com", password=hash_password('1234'))
        db.session.commit()