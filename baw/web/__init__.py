"""
" Copyright:    NCSOFT, LLC.
" Author:       Sandip Sinha
" Email:        ssinha@ncsoft.com
" Last Updated: 06/03/2017
"
"
" Flask interface for the web module
"
"""
from datetime            import datetime, date
from decimal             import Decimal

from flask               import Flask, url_for
from flask.json          import JSONEncoder
from baw                 import config
from baw.web             import views, solar, fbad 

 
from flask.ext.sqlalchemy import SQLAlchemy




app = Flask( config.get( 'webapp', 'name' ) )
app.debug = config.getboolean( 'webapp', 'debug' )

# Blueprints and top-level routes
app.register_blueprint( views.blueprint )

app.register_blueprint( solar.views.blueprint, url_prefix = '/solar' )
app.register_blueprint( solar.rest.blueprint, url_prefix = '/apiv1/solar' )

app.register_blueprint( fbad.views.blueprint, url_prefix = '/fbad' )
app.register_blueprint( fbad.rest.blueprint, url_prefix = '/apiv1/fbad' )
 



"""app.register_blueprint( volumes.views.blueprint, url_prefix = '/volumes' )
app.register_blueprint( salesdash.views.blueprint, url_prefix = '/sales' )
app.register_blueprint( userinfo.views.blueprint, url_prefix = '/user' )
app.register_blueprint( touchbiz.views.blueprint, url_prefix = '/touchbiz' )
app.register_blueprint( salesorder.views.blueprint, url_prefix = '/salesorder' )
app.register_blueprint( tracer.views.blueprint, url_prefix = '/tracer' )
app.register_blueprint( cluster.views.blueprint, url_prefix = '/cluster' )


# API routes
app.register_blueprint( subscription.rest.blueprint, url_prefix = '/apiv1/subscription' )
app.register_blueprint( touchbiz.rest.blueprint, url_prefix = '/apiv1/touchbiz' )
app.register_blueprint( touchbiz.rest2.blueprint, url_prefix = '/apiv2/touchbiz' )
app.register_blueprint( userinfo.rest.blueprint, url_prefix = '/apiv1/clientinfo' )
app.register_blueprint( tracer.rest.blueprint, url_prefix = '/apiv1/tracer' )
app.register_blueprint( cluster.rest.blueprint, url_prefix = '/apiv1/cluster' )"""


# Config items
app.config['SECRET_KEY']              = config.get( 'flask-security', 'secret_key' )
app.config['SECURITY_PASSWORD_HASH']  = config.get( 'flask-security', 'password_hash' )
app.config['SECURITY_PASSWORD_SALT']  = config.get( 'flask-security', 'password_salt' )
app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'security/login.html'
app.config['SECURITY_TRACKABLE']      = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

#Initialize LDAP
app.config['LDAP_HOST'] = config.get( 'ldap', 'host' )
app.config['LDAP_DOMAIN'] = config.get( 'ldap', 'domain' )
app.config['LDAP_SEARCH_BASE'] = config.get( 'ldap', 'search_base' )
app.config['LDAP_LOGIN_VIEW'] = config.get( 'ldap', 'login_view' )




#app.config['SQLALCHEMY_ECHO' ]        = config.getboolean( 'lawdb', 'debug' )
#app.config['SQLALCHEMY_DATABASE_URI'] = db_url


# LAWDB and flask-security app bindings
#db.init_app( app )
#security.init_app( app )


"""class JSONLawDEncoder( JSONEncoder ):
    def default( self, obj ):
        if isinstance( obj, ( datetime, date ) ):
            return obj.strftime( config.get( 'api', 'dtformat' ) )
        elif isinstance( obj, Decimal ):
            return float( str( obj ) )
        else:
            super( JSONLawDEncoder, self ).default( obj )

app.json_encoder = JSONLawDEncoder

# Privileged blueprint registry

def secure_blueprints( blueprints ):
     This function forces all routes in the supplied
    blueprint to force user authentication prior to serving
    the URL
    

    def bp_login_required():
        if not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()

    for bp in blueprints:
        app.before_request_funcs.setdefault( bp.name, [] ).append( bp_login_required )

secure_blueprints([
    subscription.views.blueprint,
    subscription.rest.blueprint,
    volumes.views.blueprint,
    salesdash.views.blueprint,
    touchbiz.views.blueprint,
    touchbiz.rest.blueprint,
    touchbiz.rest2.blueprint,
    tracer.views.blueprint,
    tracer.rest.blueprint,
    cluster.views.blueprint,
    cluster.rest.blueprint,
])
"""

