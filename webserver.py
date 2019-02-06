"""
Implement an HTTP web server in Python that knows how to run
server-side CGI scripts coded in Python; serves files and scripts from current working dir'
Python scripts must be stored in webdir\cgi-bin or webdir\htbin
"""


import sys, os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 5000

os.chdir(webdir)
srvraddr = ("", port)
srvrrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrrobj.serve_forever()
