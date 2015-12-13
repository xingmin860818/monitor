from db import *
from getstatus import GetSysInfo
import config
###############3

class Database(object):
	def __init__(self):
		#db_conn = '{}://{}:{}@{}'.format(config.db_server,config.conn_user,config.password,config.conn_addr)
		db_conn = '%s://%s:%s@%s' % (config.db_server,config.conn_user,config.password,config.conn_addr)
		db_server = 'use %s' % (config.createdb)
		db = create_engine(db_conn)
		db.execute(db_server)
		Base.metadata.create_all(db)
		Session = sessionmaker(bind=db)
		self.session = Session()

		self.getstatus = GetSysInfo()
		
	def Insert(self):
		pass
		db_conn = '{}://{}:{}@{}'.format(config.db_server,config.conn_user,config.password,config.conn_addr)
		try:
			all_info = self.getstatus.get_all()
			for k,v in all_info.iteritems():
				self.session.add(k=v)
			self.session.commit()
			return True
		except (sqlalchemy.exc.IntegrityError,TypeError):
			self.session.rollback()
			raise
d = Database()
d.Insert()
