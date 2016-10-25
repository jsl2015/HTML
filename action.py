#! C:\Python27\python.exe

# coding:utf-8

import cgi,cgitb

form = cgi.FieldStorage()

data_name = form.getvalue('name')
data_pass = form.getvalue('password')

print "Content-type:text/html\n"
print 'name:%s , password: %s' % (data_name,data_pass)

