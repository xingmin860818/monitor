import os
import inspect
import sys
import psutil
'''get agent's informations'''

class GetSysInfo(object):
	def __init__(self):
		self.status = {}
	def get_cpu_load(self):
		with open('/proc/loadavg','r') as f:
			load = f.read().split()
			self.status['cpuload_1'] = load[0]
			self.status['cpuload_5'] = load[1]
			self.status['cpuload_15'] = load[2]
	def get_mem(self):
		mem = psutil.virtual_memory()
		total = mem.total/1024/1024
		free = (mem.free+mem.buffers+mem.cached)/1024/1024
		self.status['mem_total'] = '%dM' % total
		self.status['mem_free'] = '%dM' % free
	def get_disk(self):
		disk = psutil.disk_usage('/')
		total = disk.total/1024.00/1024.00/1024.00
		free = disk.free/1024.00/1024.00/1024.00
		self.status['disk_total'] = '%0.1fG' % total
		self.status['disk_free'] = '%0.1fG' % free
	def get_all(self):
		self.get_cpu_load()
		self.get_mem()
		self.get_disk()
		return self.status
