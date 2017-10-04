#coding:utf-8
__author__ = 'hejun 244105445@qq.com'

from login_adapter import LoginAdapter
from db_adapter import DbAdapter


class Aadapter(object):

	def __init__(self):
		self.__db = DbAdapter()
		self.__adapter = {'login': LoginAdapter(self.__db)}

	def get_adapter(self,adapter_name):
		return  self.__adapter.get(adapter_name)