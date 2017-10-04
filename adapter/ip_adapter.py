#coding:utf-8
__author__ = 'hejun 244105445@qq.com'

from common.http_log import logger
from common.html_helper import Html

class IpAdapter(object):

	def __init__(self,db_adapter):
		self.__db = db_adapter

	def handle_req(self,req):
		method = req.get('method')
		execute_mechine = getattr(self,method)
		execute_mechine(req)

	def batch_add_ip(self,req):
		ip_lst = self.__db.select('ae_ip')
		ip_id_lst = [ip[0] for ip in ip_lst]
		add_ip_lst = req.get('ip_lst','').split(',')
		for ip_info in add_ip_lst:
			if tuple != type(ip_info):
				return Html.html_template % 'invalid add input'
			try:
				if ip_info[0] in ip_id_lst:
					self.__add_conflict_ip(ip_info)
				else:
					self.__db.insert(ip_info,'ae_ip')
			except Exception,e:
				return Html.html_template % e.message
		return Html.html_template % 'add ip success'

	def __add_conflict_ip(self,ip_info):
		sql = 'update ae_ip set ae_ip.id+1 where id>%d or id=%d' % (ip_info[0],ip_info[0])
		self.__db.delete('ae_ip',int(ip_info[0]))
		self.__db.insert(ip_info,'ae_ip')


	def batch_del_ip(self,req):
		ip_lst = self.__db.select('ae_ip')
		ip_id_lst = [ip[0] for ip in ip_lst]
		del_ip_lst = req.get('ip_lst','').split(',')
		for id in del_ip_lst:
			if not id.isdigit():
				return Html.html_template % 'invalid del input'
			if id not in ip_id_lst:
				continue
			self.__db.delete('ap_id',id)
			sql = 'update ae_ip set ae_ip.id-1 where id>%d' % id
			self.__db.execute(sql)


