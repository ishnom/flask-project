from flask import render_template, Blueprint, request
from app.model import Post

main = Blueprint('main', __name__)

@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 3
    pagination = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items 
    return render_template('index.html', posts=posts, pagination=pagination)
   


@main.route("/about")
def about():
    return render_template('about.html', title="About")
