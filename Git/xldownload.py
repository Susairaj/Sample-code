__author__ = 'Bosco'
import xlwt
import psycopg2
import sys

#Define our connection string
conn_string = "host='localhost' dbname='odoo1' user='odoo' password='odoo'"

# print the connection string we will use to connect
print "Connecting to database\n    ->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"


cursor.execute('SELECT id, name, comment FROM res_groups order by id')
vals = cursor.fetchall()
print vals

book = xlwt.Workbook()
sheet = book.add_sheet("PySheet1")

row = 0
for val in vals:
    col = 0
    for v in val:
        sheet.write(row, col, str(v))
        col += 1
    row += 1

book.save("test.xls")


