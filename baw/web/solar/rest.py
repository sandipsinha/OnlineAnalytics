"""
" Copyright:    NCSOFT LLC.
" Author:       Sandip Sinha
" Email:        ssinha@ncsoft.com
"
"""
__author__ = 'ssinha'
from flask              import Blueprint, jsonify, request, Response, json
from baw.util.queries   import query_solar_data
from datetime           import datetime, timedelta
from baw.util.timeutil  import get_actual_date



blueprint = Blueprint( 'rest.solar', __name__ )

@blueprint.route( '/solardb', methods = ['GET', 'POST'])
def solar_data():
    fdate, tdate = get_actual_date('last_24')
    allData = query_solar_data(fdate, tdate)
    if allData is not None:
    	biglist = [{'dates':items.event_date_hr ,'no_of_players':int(items.Count)}  for items in allData]
    else:
    	biglist = []
    return  json.dumps(biglist)