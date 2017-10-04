#coding:utf-8
__author__ = 'hejun 244105445@qq.com'


from common.html_helper import Html

class LoginAdapter(object):

	USER_NAME = 'user_name'
	USER_PWD = 'user_pwd'

	def __init__(self,db_adapter):
		self.__db = db_adapter

	def handle_req(self,req):
		print req
		if not self.__verify_user(req):
			return Html.html_template % 'invalid user or password'
		return Html.html_template % 'ok'

	def __verify_user(self,req):
		user_name = req.get('user_name')
		user_pwd = req.get('user_pwd')
		user_lst = self.__db.select('ae_user')
		for user in user_lst:
			if (user_name,user_pwd) == (user[1],user[2]):
				return True
		return False