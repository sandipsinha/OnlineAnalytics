"""
" Copyright:    Loggly, Inc.
" Author:       Scott Griffin
" Email:        scott@loggly.com
"
"""
from contextlib import contextmanager
from datetime import date, datetime
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from urllib import quote_plus

import pytz
from baw                        import config
from sqlalchemy                 import (create_engine, Column, 
                                        Integer, DateTime, Date,
                                        Boolean, String,Text,
                                        Numeric, ForeignKey,
                                        Index)

from sqlalchemy.dialects.mysql  import BIGINT, SMALLINT, MEDIUMINT, DECIMAL, NVARCHAR, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import sessionmaker, relationship, backref
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from baw                 import config
from sqlalchemy         import and_, or_, not_, func, distinct

Base = declarative_base()
# Duplicate models of the same table need another base declaration
# so that they have a separate MetaData instance
OwnersBase = declarative_base()

 


db_url = '{dialect}://{user}:{passwd}@{host}:{port}/{dbname}'.format(
    dialect = config.get( 'redshift', 'dialect' ),
    user    = config.get( 'redshift', 'user' ),
    passwd  = config.get( 'redshift', 'password' ),
    host    = config.get( 'redshift', 'host_name' ),
    port    = config.get( 'redshift', 'port' ),
    dbname  = config.get( 'redshift', 'db_name' ),
)

engine = create_engine( 
            db_url, 
            )
         
Base = declarative_base()
Session = sessionmaker( bind=engine )
 

def _localize( dt ):
    if dt is None:
        return dt

    timezone = pytz.timezone( 'US/Pacific' )
    if type( dt ) is date:
        dt = datetime( *(dt.timetuple()[:3]) )
    return pytz.utc.normalize( timezone.localize( dt ) ).replace( tzinfo=None )

class Solar( Base ):
    __tablename__  = 'prod_solar_winds_tbl'
    __table_args__ = {'schema':'apidata'}
  

    event_date     = Column( DateTime, primary_key=True  )
    num_of_players = Column( Integer )
    date_received  = Column( Date)

    @hybrid_property
    def event_date_hr( self ):
        mask_dt = self.event_date
        return mask_dt.strftime('%Y-%m-%d-%H') 

    @event_date_hr.expression
    def event_date_hr( self): 
        mask_dt =  self.event_date
        return func.to_char(mask_dt,'YYYY-MM-DD-HH24')
                       

    def __repr__(self):
        return "<Solar({},{},{})>".format(
            self.event_date, 
            self.num_of_players,
            self.date_received)


class Adset( Base ):
    __tablename__  = 'fb_adset_tbl'
 #   __table_args__ = {'schema':'apidata'}
  

    bid_amount     = Column( DECIMAL(8,2))
    campaign_id    = Column( NVARCHAR(30) )
    daily_budget   = Column( DECIMAL(10,2))
    end_time       = Column(NVARCHAR(30))
    adset_id       = Column( NVARCHAR(30),primary_key=True )
    autobid        = Column(Boolean)
    adset_name     = Column( NVARCHAR(40))
    start_date     = Column(NVARCHAR(30))
    status         = Column( NVARCHAR(10) )
    date_in        = Column(NVARCHAR(13), primary_key=True )
 

    @hybrid_property
    def date_range( self ):
        mask_dt = self.date_in[:11]
        return datetime.strptime(mask_dt,'%Y-%m-%d') 

    @date_range.expression
    def date_range( self): 
        mask_dt = func.substring(self.date_in,0,11)
        return func.date(mask_dt)


    @hybrid_property
    def date_only( self ):
        return func.substring(self.date_in,0,11)   
                       

    def __repr__(self):
        return "<Adset({},{},{},{},{},{},{},{},{},{})>".format(
            self.bid_amount, 
            self.campaign_id,
            self.daily_budget,
            self.end_time,
            self.adset_id,
            self.autobid,
            self.adset_name,
            self.start_date,
            self.status,
            self.date_in)



@contextmanager
def session_context():
    """ Because ADB is read only we do not need commit """
    session = Session()
    try:
        # flask-sqlalchemy patches the session object and enforces
        # This model changes dict for signaling purposes.  Because
        # We don't want flask-sqlalchemy dealing with these models
        # Lets just fake this shit.
        session._model_changes = {}
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

@contextmanager
def loader():
    """ Loads objects from an ORM session then immediately
    expunges them so they are not written back to the DB
    """
    session = Session()
    try:
        # flask-sqlalchemy patches the session object and enforces
        # This model changes dict for signaling purposes.  Because
        # We don't want flask-sqlalchemy dealing with these models
        # Lets just fake this shit.
        session._model_changes = {}
        yield session
        session.expunge_all()
        session.rollback()
    except:
        session.rollback()
        raise
    finally:
        session.close()



