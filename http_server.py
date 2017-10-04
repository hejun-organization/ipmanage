#coding:gbk

import SimpleHTTPServer
import BaseHTTPServer
import shutil
import os
import sys
from adapter.adapter import Aadapter
from common.http_log import logger

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def __init__(self,request, client_address, server):
		self.__adapter = Aadapter()
		SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self,request, client_address, server)

	def do_GET(self):
		print 'get'
		print self.path
		if '/' == self.path:
			logger.info('iP:{} name:{} GET'.format(self.client_address,self.address_string()))
			path = '/html_js_css/index.html'
		else:
			if not self.path.endswith('html') and not self.path.endswith('js') and not self.path.endswith('css'):
				return
			path = '/html_js_css' + self.path
			print path
		if not os.path.isfile(os.getcwd() + path):
			self.wfile.write('no index file')
			return
		with open(os.getcwd() + path,'rb') as f:
			shutil.copyfileobj(f,self.wfile)
			f.close()

	def do_POST(self):
		print 'post'
		req = self.parse_post_req()
		print req
		print self.__adapter
		handle_adapter = self.__adapter.get_adapter(self.path[1:])
		if not handle_adapter:
			return self.wfile.write('invalid url')
		rsp = handle_adapter.handle_req(req)
		self.wfile.write(rsp)

	def parse_post_req(self):
		content_length = self.headers.getheader('Content-Length')
		req_content = self.rfile.read(int(content_length))#a=1&b=2
		req_lst = req_content.split('&')
		req_dict = {}
		for req in req_lst:
			key = req.split('=')[0]
			value = req.split('=')[1]
			req_dict[key] = value
		return req_dict

if __name__ == '__main__':
	sys.path.append('./')
	httpd = BaseHTTPServer.HTTPServer(('',8083),HttpHandler)
	httpd.serve_forever()