from ..config import redshift_config as red
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security   import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from sqlalchemy                 import (create_engine, Column,
                                        Integer, DateTime,
                                        Boolean, String,
                                        ForeignKey)
from contextlib import contextmanager
from sqlalchemy.orm             import sessionmaker, relationship, backref

db_url = '{dialect}://{user}:{passwd}@{host}:{port}/{dbname}'.format(
    dialect = red.dialect,
    user    = red.user,
    passwd  = red.pwd,
    host    = red.host,
    port    = red.port,
    dbname  = red.dbname,
)

engine = create_engine( 
            db_url, 
            )
         

Session = sessionmaker( bind=engine )

class Server( Base ):
    __tablename__  = 'server_tbl'

    seq                = Column( BigInteger, primary_key=True )
    time               = Column( DateTime , primary_key=True  )
    logid              = Column( BigInteger )
    log_detail_code    = Column( BigInteger )
    auth_service_id    = Column( nvarchar(10) )
    platform_id        = Column( nvarchar(10) )
    actor_account_id   = Column( nvarchar(60) )
    platform_type      = Column( nvarchar(10) )
    actor_id           = Column( BigInteger )
    actor_name         = Column( nvarchar(20))
    log_name		   = Column( nvarchar(30))
    log_category       = Column( nvarchar(10))
    actor_level        = Column( BigInteger )
    entity_id          = Column( BigInteger )
    entity_uid         = Column( BigInteger )
    entity_grade       = Column( BigInteger )
    entity_more        = Column( BigInteger )
    use1_num           = Column( BigInteger )
    old1_num           = Column( BigInteger )
    new1_num           = Column( BigInteger )
    data1_num          = Column( BigInteger )
    data2_num           = Column( BigInteger )
    data3_num           = Column( BigInteger )
    data4_num           = Column( BigInteger )
    data5_num           = Column( BigInteger )
    data1_str          = Column( nvarchar(50) )
    data2_str          = Column( nvarchar(50) )
    data3_str          = Column( nvarchar(50) )
    data4_str          = Column( nvarchar(50) )
    data5_str          = Column( nvarchar(50) )
    data6_str          = Column( nvarchar(50) )
    data7_str          = Column( nvarchar(50) )
    data8_str          = Column( nvarchar(50) )
    data9_str          = Column( nvarchar(50) )
    data10_str          = Column( nvarchar(50) )
    data11_str          = Column( nvarchar(50) )
    data12_str          = Column( nvarchar(50) )
    target_account_id   = Column( nvarchar(50) )
    target_level        = Column( BigInteger )
    target_id           = Column( BigInteger )
    target_name         = Column( nvarchar(40) )


             
    def __repr__(self):
        return "<server({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})>".format(
            self.seq, 
            self.time,
            self.logid, 
            self.log_detail_code,
            self.auth_service_id, 
            self.platform_id,
            self.actor_account_id, 
            self.platform_type,
            self.actor_id,
            self.actor_name,
            self.log_name,
            self.log_category,
            self.actor_level,
            self.entity_id,
            self.entity_uid,
            self.entity_grade,
            self.entity_more,
            self.use1_num,
            self.old1_num,
            self.new1_num,
            self.data1_num,
            self.data2_num,
            self.data3_num,
            self.data4_num,
            self.data5_num,
            self.data1_str,
            self.data2_str,
            self.data3_str,
            self.data4_str,
            self.data5_str,
            self.data6_str,
            self.data7_str,
            self.data8_str,
            self.data9_str,
            self.data10_str,
            self.data11_str,
            self.data12_str,
            self.target_account_id,
            self.tarrget_level,
            self.target_id,
            self.target_name
            )

@contextmanager
def session_context():
    session = Session()
    try:
        session._model_changes = {}
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

