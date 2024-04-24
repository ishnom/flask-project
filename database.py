from app import db
import app
from app.model import User, Post

with app.app.app_context():
 db.create_all()
