import os

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from shelter.blueprints.volunteers.volunteers_app import volunteers_bp
from shelter.blueprints.dogs.dogs_app import dogs_bp


def create_app():
    """
    Create Flask app according to the app factory pattern
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=False, )
    config_path = os.path.join('config', 'settings.py')
    app.config.from_pyfile(config_path, silent=False)
    app.register_blueprint(dogs_bp)
    app.register_blueprint(volunteers_bp)

    toolbar = DebugToolbarExtension(app)

    @app.route('/')
    def index():

        return render_template('main.html')

    return app

if __name__ == '__main__':
    create_app().run()