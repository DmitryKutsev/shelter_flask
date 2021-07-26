from flask import Blueprint, render_template

dogs_bp = Blueprint('dogs', __name__, template_folder='templates', url_prefix='/dogs')

@dogs_bp.route('/')
def main():
    return render_template('dogs.html')