"""
:The login function is under
::    http://localhost:8069/xmlrpc/common
:For object retrieval use:
::    http://localhost:8069/xmlrpc/object
"""
import xmlrpclib
 
user = 'admin'
pwd = 'odoo'
dbname = 'WBM'
 
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock.login(dbname ,user ,pwd)
print uid
