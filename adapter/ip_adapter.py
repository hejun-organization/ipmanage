#coding:utf-8
__author__ = 'hejun 244105445@qq.com'
import sys
sys.path.append('../')
from common.http_log import logger
from common.html_helper import Html
from db_adapter import DbAdapter
import re
import time


class IpAdapter(object):

	def __init__(self,db_adapter):
		self.__db = db_adapter

	def handle_req(self,req):
		print 'hejun test http req is {}'.format(req)
		method = req.get('method')
		execute_mechine = getattr(self,method)
		return execute_mechine(req)

	def query_ip(self,req):
		rlt = self.__db.select('ae_ip')
		rlt = [list(r) for r in rlt]
		for r in rlt:
			for rr in r:
				if unicode == type(rr):
					rr = rr.decode().encode('utf-8')
		for (i,r) in enumerate(rlt):
			for (ii,rr) in enumerate(r):
				if unicode == type(rr):
					rlt[i][ii] = rr.decode().encode('utf-8')
		return str(rlt)

	def batch_add_ip(self,req):
		ip_lst = self.__db.select('ae_ip')
		ip_id_lst = [ip[0] for ip in ip_lst]
		ip_str = re.sub(r',(?=[^)]*(\(|$))', '_', req.get('ip_lst'))
		add_ip_lst = re.split(r'_',ip_str)
		for ip_info in add_ip_lst:
			if not ip_info:
				continue
			ip_info = eval(ip_info)
			if tuple != type(ip_info):
				return Html.html_template % 'invalid add input'
			try:
				if ip_info[0] in ip_id_lst:
					self.__add_conflict_ip(ip_info)
				else:
					self.__db.insert([ip_info],'ae_ip')
			except Exception,e:
				return Html.html_template % e.message
		return Html.html_template % 'add ip success'

	def __add_conflict_ip(self,ip_info):
		sql = 'update ae_ip set id=id+1 where id>=%d' % (ip_info[0])
		self.__db.execute(sql)
		self.__db.delete('ae_ip',int(ip_info[0]))
		self.__db.insert([ip_info],'ae_ip')


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
			sql = 'update ae_ip set id=id-1 where id>%d' % id
			self.__db.execute(sql)

	def update_ip(self,req):
		user = req.get('user_name')
		ip = req.get('ip')
		outtime = req.get('time')
		describe = req.get('describe')
		try:
			self.__check_user(user)
			self.__check_ip(ip)
			self.__check_time(int(outtime))
		except Exception,e:
			return Html.html_template % e.message
		outtime = int(time.time()) + int(outtime) * 60 * 60
		sql = 'update ae_ip set user={},outtime={},describe={} where ip={}'.format(user,outtime,describe,ip)
		self.__db.execute(sql)
		return Html.html_template % 'requst success'

	def __check_user(self,user):
		pass#to do

	def __check_ip(self,ip):
		data_lst = self.__db.select('ae_ip')
		ip_lst = [data[1] for data in data_lst]
		if ip not in ip_lst:
			raise Exception('invalid ip')

	def __check_time(self,time):
		if time / 60 * 24 > 30:
			raise Exception('invalid time')


# a = {'ip_lst': "(0,'10.168.11.11','hejun','111111','-1','test','hejun'),(1,'10.168.11.11','hejun','111113','-1','test','hejun')"}
# b = IpAdapter(DbAdapter())
# b.batch_add_ip(a)
# print b.test()


