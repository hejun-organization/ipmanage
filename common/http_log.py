#coding:utf-8
__author__ = 'hejun 244105445@qq.com'

import logging
import os

cur_dir = os.getcwd()
log_path = os.path.join(cur_dir.split('http_server')[0],'http.log')

logging.basicConfig(level=logging.INFO,
					format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename=log_path,
					filemode='a+')

logging.basicConfig(level=logging.ERROR,
				format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
				datefmt='%a, %d %b %Y %H:%M:%S',
				filename=log_path,
				filemode='a+')

class logger(object):
	@classmethod
	def info(cls,info):
		logging.info(info)

	@classmethod
	def error(cls,error):
		logging.error(error)

