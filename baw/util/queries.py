"""
" Copyright:    NCSOFT West.
" Author:       Sandip Sinha
" Email:        ssinha@ncsoft.com
"
" General purpose queries/query classes.
"
"""
from collections        import defaultdict
from datetime           import datetime, timedelta
from operator           import attrgetter
from sqlalchemy         import and_, or_, not_, func, distinct
from baw.util.timeutil  import Timebucket
from sqlalchemy.sql import label, text
from sqlalchemy         import  desc 
import time
from baw.util.adb       import session_context, Solar, Adset, engine
from sqlalchemy.orm.exc             import NoResultFound
import time
from flask_login         import LoginManager
from flask_simpleldap    import LDAP
cur_date = time.strftime("%Y-%m-%d")
cur_date_obj = datetime.strptime(cur_date,'%Y-%m-%d')

def query_solar_data( start=cur_date_obj, end=cur_date_obj):
    # operator | or's the states together ( | is overloaded in SQLAlchemy query construction)
    try:
        with session_context() as s:
            q = s.query(Solar.event_date_hr,label('Count', func.avg(Solar.num_of_players)))\
            .filter(Solar.event_date.between(start, end ))\
            .group_by(Solar.event_date_hr ) \
            .order_by(desc(Solar.event_date_hr))
            data = q.all()
            s.expunge_all()
        return data
    except Exception as e:
        print 'Data could not be fetched. Please check {}'.format(e)
        return None

def query_adset_4_2day():
    try:    
        conn = engine.connect()
        sqlst = "select a.campaign_id, a.adset_id,substring(a.date_in,0,11) Date, a.bid_amount, a.daily_budget  from fb_adset_tbl a where substring(a.date_in,0,11) = (select max(substring(b.date_in,0,11)) from fb_adset_tbl b"\
                    " where a.adset_id = b.adset_id and a.campaign_id = b.campaign_id)"
        get_all_rows = conn.execute(sqlst)
        all_data = get_all_rows.fetchall()

        return all_data
    except Exception as e:
        print 'Data could not be fetched. Please check {}'.format(e)
        return None
     
def query_average_adset_data_last_7_days():
    from_dt = cur_date_obj - timedelta(days=7)
    to_dt = cur_date_obj - timedelta(days=1)


    try:    
        with session_context() as s:
            q = s.query(Adset.campaign_id,Adset.adset_id, label('date', func.substring(Adset.date_in,0,11)), label('bid_avg_amount', func.avg(Adset.bid_amount)),label('daily_avg_budget',\
                func.avg(Adset.daily_budget)))\
                .filter(Adset.date_range.between(from_dt, to_dt))\
                .group_by(Adset.campaign_id, Adset.adset_id, func.substring(Adset.date_in,0,11))
            data = q.all()
            s.expunge_all()
        return data
    except Exception as e:
        print 'Data could not be fetched. Please check {}'.format(e)
        return None




