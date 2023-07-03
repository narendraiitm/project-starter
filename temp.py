from main import app
from models import db, Blog

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        blog = Blog(title="First blog", description="My first blog in db")
        db.session.add(blog)
        db.session.commit()