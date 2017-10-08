#coding:gbk
__author__ = 'hejun 244105445@qq.com'



import sqlite3
import os

#ae_ip (id,ip,user,outtime,status,describe,lastuser)
class DbAdapter(object):

	def __init__(self):
		self._db = sqlite3.connect('e:/ae.db')#os.path.join(os.getcwd(),'ip.db')
		self._cursor = self._db.cursor()
		self.__init_table()

	def __init_table(self):
		try:
			self._cursor.execute('create table ae_user (id inter, user text,pwd text)')
		except Exception,e:
			#print 'create user table fail reason is:{}'.format(e.message)
			pass
		try:
			self._cursor.execute('create table ae_ip (id inter, ip text,user text,outtime text,'
								 'status text,describe text,lastuser text)')
		except Exception,e:
			#print 'create ip table fail reason is:{}'.format(e.message)
			pass

	def insert(self,data_lst,table):
		sql = 'insert into %s values {}'
		sql = sql.format('(?,?,?)') if 'ae_user' == table else sql.format('(?,?,?,?,?,?,?)')
		for data in data_lst:
			self._cursor.execute(sql % table,data)
		self._db.commit()

	def select(self,table):
		return self._cursor.execute('select * from %s order by id asc' % table).fetchall()

	def delete(self,table,id):
		self._cursor.execute('delete from %s where id=%d' % (table,id))
		self._db.commit()

	def update(self,table,info_lst):
		if 'ae_ip' == table:
			self._cursor.execute('update ae_ip set ip={},outtime={},status={},describe={},lastuser={} '
								 'where id=%d'.format(*info_lst[1:]) % info_lst[0])
			self._db.commit()
		elif 'ae_user' == table:
			self._cursor.execute('update ae_user set user={},pwd={} where id=%d'.format(*info_lst[1:]) % info_lst[0])
			self._db.commit()

	def del_all(self,table):
		self._cursor.execute('delete from %s' % table)
		self._db.commit()

	def execute(self,sql):
		self._cursor.execute(sql)
		self._db.commit()

	def roll_back(self):
		self._db.rollback()

	def close_db(self):
		self._cursor.close()
		self._db.close()


# db = DbAdapter()
# db.del_all('ae_user')
# db.insert([(0,'2','3')],'ae_user')
# db.insert([(1,'2','3')],'ae_user')
# print db.select('ae_user').fetchall()
# db.close_db()

