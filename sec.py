from flask_security import SQLAlchemyUserDatastore, Security
from models import db, User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)