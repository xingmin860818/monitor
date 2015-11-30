from db import *
from getstatus import GetSysInf

class Database(object):
	def __init__(self):
		db_conn = '{}://{}:{}@{}'.format(config.db_server,config.conn_user,config.password,config.conn_addr)
		db_server = 'use {}'.format(config.createdb)
		db = create_engine(db_conn)
		db.execute(db_server)
		Base.metadata.create_all(db)
		Session = sessionmaker(bind=db)
		self.session = Session()

		self.getstatus = GetSysInfo()
		
	def Add(self,table,**kwargs):
		try:
			keywards = table(**kwargs)
			self.session.add(keywards)
			self.session.commit()
			return True
		except (sqlalchemy.exc.IntegrityError,TypeError):
			self.session.rollback()
			raise
