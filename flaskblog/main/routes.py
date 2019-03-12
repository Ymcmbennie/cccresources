from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/entourage")
def entourage():
    return render_template('entourage.html', title='Entourage')


@main.route("/new_article")
def new_article():
    return render_template('new_article.html', title='New Article')


@main.route("/tutorials")
def tutorials():
    return render_template('tutorials.html', title='Tutorials')


@main.route("/tutorial001")
def tutorial001():
    return render_template('001.html', title='Tutorial001')


@main.route("/new_tutorials")
def new_tutorials():
    return render_template('new_tutorials.html', title='New Tutorial')


@main.route("/dwg")
def dwg():
    return render_template('dwg.html', title='Dwg')


@main.route("/new_dwg")
def new_dwg():
    return render_template('new_dwg.html', title='New File')


@main.route("/scripts")
def scripts():
    return render_template('scripts.html', title='Scripts')


@main.route("/models")
def models():
    return render_template('models.html', title='Models')


@main.route("/icons")
def icons():
    return render_template('icons.html', title='Projects')


@main.route("/new_project")
def new_project():
    return render_template('new_project.html', title='New Project')


@main.route("/maps")
def maps():
    return render_template('maps.html', title='Maps')


@main.route("/map1")
def map1():
    return render_template('map.html', title='Brzezin')
