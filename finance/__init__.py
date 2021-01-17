from flask import Flask
from . import tax

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    app.register_blueprint(tax.bp)

    return app