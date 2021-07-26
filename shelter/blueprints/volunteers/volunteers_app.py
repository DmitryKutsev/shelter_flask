from flask import Blueprint, render_template

volunteers_bp = Blueprint('volunteers', __name__, template_folder='templates', url_prefix='/volunteers')

@volunteers_bp.route('/')
def main():
    return render_template('volunteers.html')