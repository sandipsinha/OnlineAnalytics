
"""
" Copyright:    NCSOFT LLC.
" Author:       Sandip Sinha
" Email:        ssinha@ncsoft.com
"
"""
from flask              import Blueprint, render_template, request, flash,redirect, json
from baw.web.fbad       import rest
from datetime           import datetime
from flask_simpleldap   import LDAP



blueprint = Blueprint( 'fbad', __name__,
                        template_folder = 'templates',
                        static_folder   = 'static' )


@blueprint.route( '/', methods=['GET'])
def show_entries():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    #eturn render_template('show_fbadset_data.html')
    return render_template('fbad.html')

@blueprint.route( '/solar', methods=['GET'])
def show_solr_data():
    #db = get_db()
    #cur = db.execute('select title, text from entries order by id desc')
    #entries = cur.fetchall()
    return render_template('angular.html')