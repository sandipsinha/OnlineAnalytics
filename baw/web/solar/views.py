
"""
" Copyright:    NCSOFT LLC.
" Author:       Sandip Sinha
" Email:        ssinha@ncsoft.com
"
"""
from flask              import Blueprint, render_template, request, flash,redirect, json
#from law.util.queries    import query_user_state
from baw.web.solar      import rest
from datetime           import datetime



blueprint = Blueprint( 'solar', __name__,
                        template_folder = 'templates',
                        static_folder   = 'static' )



"""
@blueprint.route( '/', methods=['GET'])
def display_tracer_data():
    return render_template('tracer/actualcontent.html' )
"""  

@blueprint.route( '/', methods=['GET'])
def show_entries():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('show_solar_db.html')

