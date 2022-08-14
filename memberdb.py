# memberdb.py

import sqlite3

conn = sqlite3.connect('memberdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()


# create table
c.execute("""CREATE TABLE IF NOT EXISTS member (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				membercode TEXT,
				fullname TEXT,
				tel TEXT,
				usertype TEXT,
				points INTEGER ) """)


def Insert_member(membercode,fullname,tel,usertype,points):
	# CREATE
	with conn:
		command = 'INSERT INTO member VALUES (?,?,?,?,?,?)' # SQL
		c.execute(command,(None,membercode,fullname,tel,usertype,points))
	conn.commit() # SAVE DATABASE
	print('saved')


def View_member():
	# READ
	with conn:
		command = 'SELECT * FROM member'
		c.execute(command)
		result = c.fetchall()
	print(result)
	return result


def Update_member(ID,field,newvalue):
	# UPDATE
	with conn:
		command = 'UPDATE member SET {} = (?) WHERE ID=(?)'.format(field)
		c.execute(command,([newvalue,ID]))
	conn.commit()
	print('updated')


def Delete_member(ID):
	# DELETE
	with conn:
		command = 'DELETE FROM member WHERE ID=(?)'
		c.execute(command,([ID]))
	conn.commit()
	print('deleted')


def CheckMember(TEL):
	# CHECK
	with conn:
		command = 'SELECT * FROM member WHERE tel=(?)'
		c.execute(command,([TEL]))
		result = c.fetchall()
		print(result)

	if len(result) >= 1:
		return True
	else:
		return False


# UpdateMember(2, 'tel', '654321')	
# DeleteMember(2)
# ViewMember()
# res = ViewMember()
# print(res[0])
# InsertMember('MB-1003', 'James', '123456', 'Gold', 500)