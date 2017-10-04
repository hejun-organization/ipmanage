__author__ = 'lenovo'

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import SimpleHTTPServer
import urlparse
import os
import shutil

class HttpHander(BaseHTTPRequestHandler):
	def do_GET(self):
		print self.path
		print 111
		parsed_path = urlparse.urlparse(self.path)
		print parsed_path.path
		print self.client_address,self.address_string()
		print self.command
		print self.request_version
		print self.server_version
		print self.sys_version
		print self.protocol_version
		print self.headers
		with open(os.path.join(os.getcwd(),'index.html'),'r+') as f:
			if f:
				self.wfile.write(f.read())
				#shutil.copyfileobj(f,self.wfile)
				f.close()
# 		self.wfile.write('''
# 		<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>hello</title>
# </head>
# <body>
#     <h1>hello</h1>
# </body>
# </html>''')


server = HTTPServer(('localhost',8083),HttpHander)
server.serve_forever()