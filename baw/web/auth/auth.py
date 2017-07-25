
from flask_login                import LoginManager
from flask_simpleldap           import LDAP
from baw.web import app

app.config['LDAP_HOST'] = 'ldap.example.com'
app.config['LDAP_DOMAIN'] = 'example.com'
app.config['LDAP_AUTH_TEMPLATE'] = 'login.html'

login_manager.init_app(app)
ldap = LDAP(app)