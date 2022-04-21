# basic-sql.py

import sqlite3

conn = sqlite3.connect('memberdb.sqlite3')
c = conn.cursor()

# create data to table
c.execute("""CREATE TABLE IF NOT EXISTS member (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				membercode TEXT,
				fullname TEXT,
				tel TEXT,
				usertype TEXT,
				points INTEGER )""")

def InsertMember(membercode, fullname, tel, usertype, points):
	# CREATE
	with conn:
		command = 'INSERT INTO member VALUES (?,?,?,?,?,?)' # SQL
		c.execute(command, (None, membercode, fullname, tel, usertype, points))
	conn.commit() # save database
	print('saved')

def ViewMember():
	# READ
	with conn:
		command = 'SELECT * FROM member'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result

def UpdateMember(ID, field, newvalue):
	# UPDATE
	with conn:
		command = 'UPDATE member SET {} = (?) WHERE ID = (?)'.format(field)
		c.execute(command, ([newvalue, ID]))
	conn.commit()
	print('updated')

def DeleteMember(ID):
	# DELETE
	with conn:
		command = 'DELETE FROM member WHERE ID = (?)'
		c.execute(command,([ID]))
	conn.commit()
	print('deleted')


# UpdateMember(2, 'tel', '654321')	
# DeleteMember(2)
ViewMember()
# res = ViewMember()
# print(res[0])
# InsertMember('MB-1003', 'James', '123456', 'Gold', 500)