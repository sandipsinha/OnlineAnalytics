from flask              import Blueprint, render_template
from flask.ext.security import login_required


blueprint = Blueprint( 'root', __name__, template_folder='templates', static_folder='static' )

@blueprint.route( '/' )
@blueprint.route( '/index' )
def index():
    return render_template( 'index.html' )

@blueprint.route( '/login_check' )
@login_required
def login_check():
    return 'Yep... you are logged in'
    return redirect(url_for('auth.home'))