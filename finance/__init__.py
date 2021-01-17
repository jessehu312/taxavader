from flask import Flask, Blueprint, render_template
from . import tax

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def root():
    return render_template('main.html')

@blueprint.route('/<path:filepath>')
def serve(filepath):
    return send_from_directory('./app/static', filename=filepath)

def create_app():
    app = Flask(__name__, instance_relative_config=True, static_folder='static', template_folder="static", static_url_path='')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    app.register_blueprint(tax.bp)
    app.register_blueprint(blueprint)
    return app

