"""
" Copyright:    NCSOFT LLC.
" Author:       Sandip Sinha
" Email:        ssinha@ncsoft.com
"
"""
__author__ = 'ssinha'
from flask              import Blueprint, jsonify, request, Response, json
from baw.util.queries   import query_average_adset_data_last_7_days, query_adset_4_2day
from datetime           import datetime, timedelta
from baw.util.timeutil  import get_actual_date
from baw.util.data_mashup import *



blueprint = Blueprint( 'rest.fbad', __name__ )

@blueprint.route( '/bid_n_cap', methods = ['GET', 'POST'])
def fdb_avg_data():
    last_7_days = query_average_adset_data_last_7_days()
    todays_data = query_adset_4_2day()
    change2arr = mesh_both_data(last_7_days, todays_data)
    return  json.dumps(change2arr)