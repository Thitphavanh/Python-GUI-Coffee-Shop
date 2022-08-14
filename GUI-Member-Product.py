# GUI-Calculator.py
from tkinter import *
from tkinter import ttk, messagebox
from memberdb import *
from productdb import *
from menufunction import *
import csv
from datetime import datetime
import webbrowser
from matplotlib import image
from threading import Thread
from PIL import Image, ImageTk
import requests





# ----------------FUNCTION-----------------

addproduct = AddProduct()
product_icon = ProductIcon()


def writetocsv(data, filename='data.csv'):
	with open(filename,'a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)


def QRImage(price=1000,account='0801234567'):
	url='https://promptpay.io/{}/{:.2f}.png'.format(account,price)
	response = requests.get(url)
	if response.status_code == 200:
		with open('qr-payment.png','wb') as f:
			f.write(response.content)



GUI = Tk()
GUI.title('Coffee Shop Management')
# GUI.iconbitmap('loong.ico')
# GUI.state('zoomed')

# ----------------Style-----------------
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,12))
style.configure('Treeview',font=(None,10))

canvas = Canvas(GUI, width=1920, height=1280)
canvas.place(x=0, y=0)

background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(300, 50, anchor=NW, image=background)

# --------------------------------------

Width = 1100
Height = 650
Monitor_width = GUI.winfo_screenwidth()
Monitor_height = GUI.winfo_screenheight()

Start_x = (Monitor_width/2) - (Width/2)
Start_y = (Monitor_height/2) - (Height/2)
Start_y = Start_y - 50

print('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))

# ----------------MENU BAR-----------------
menubar = Menu(GUI)
GUI.config(menu=menubar)

# -----------------------------------------

# File Menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)

def ExportDatabase():
	print('Export Database to CSV')
filemenu.add_command(label='Export',command=ExportDatabase)
filemenu.add_command(label='Exit',command=lambda: GUI.destroy())

# -----------------------------------------
# Member Menu
membermenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Member',menu=membermenu)

# -----------------------------------------
# Product Menu

productmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Product',menu=productmenu)

productmenu.add_command(label='ADD PRODUCT', command=addproduct.command)

# -----------------------------------------
# Setting

settingmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Setting',menu=settingmenu)

settingmenu.add_command(label='PRODUCT ICON', command=product_icon.command)


# -----------------------------------------


# Help Menu
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
contact_url = 'https://uncle-engineer.com'
helpmenu.add_command(label='CONTRACT US',command=lambda: webbrowser.open(contact_url))

def About():
	ABGUI = Toplevel()
	ABGUI.iconbitmap('loong.ico')
	W = 300
	H = 200
	MW = GUI.winfo_screenwidth() # Monitor Width
	MH = GUI.winfo_screenheight() # Monitor Height
	SX =  (MW/2) - (W/2) # Start X
	SY =  (MH/2) - (H/2) # Start Y
	ABGUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
	L = Label(ABGUI,text='Program coffee shop management',fg='green',font=(30)).pack()
	L = Label(ABGUI,text='Develope by Hery Phenomenal\nhttps://www.facebook.com/herytwenty.phonsavad',font=('Angsana New',20)).pack()
	ABGUI.mainloop()

helpmenu.add_command(label='ABOUT',command=About)

# ----------------Tab1 = ໜັງສື-----------------

Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)


T3 = Frame(Tab)
T4 = Frame(Tab)

icon_tab1 = PhotoImage(file='Tab5-coffee.png')
icon_tab2 = PhotoImage(file='Tab6-member.png')
icon_tab3 = PhotoImage(file='Tab5-coffee.png')
icon_tab4 = PhotoImage(file='Tab6-member.png')

Tab.add(T3, text='CAFE',image=icon_tab3,compound='top')
Tab.add(T4, text='MEMBER',image=icon_tab4,compound='top')


# ----------------TimeStamp-----------------

days = {'Mon': 'ຈັນ',
		'Tue': 'ຄານ',
		'Wed': 'ພຸດ',
		'Thu': 'ພະຫັດ',
		'Fri': 'ສຸກ',
		'Sat': 'ເສົາ',
		'Sun': 'ອາທິດ'}


# ----------------TAB 3 - Coffee ----------------


CF1 = Frame(T3)
CF1.place(x=50,y=100)

# ROW0
# header = ['No.', 'title', 'quantity','price','total']

allmenu = {}
'''

product = {'latte': {'name': 'ລາເຕ້', 'price': 18000},
		   'cappuccino': {'name': 'ຄາປູຊິໂນ້', 'price': 20000},
		   'espresso': {'name': 'ເອສເປຣສໂຊ້', 'price': 18000},
		   'mocha': {'name': 'ມອກຄ້າ', 'price': 18000},
		   'americano': {'name': 'ອາເມຣິກາໂນ້', 'price': 17000},
		   'breve': {'name': 'ເບຣບ', 'price': 17000},
		   'ristretto': {'name': 'ຣິສເຕຣຕໂຕ', 'price': 17000},
		   'marocchino': {'name': 'ມາຣອຄຊິໂນ້', 'price': 16000},
		   'affogato': {'name': 'ອາຟໂຟກາໂຕ', 'price': 16000},
		   'coco': {'name': 'ໂກໂກ້', 'price': 16000}}
'''

product = product_icon_list()
print(product)


def UpdateTable():
	table.delete(*table.get_children()) 
	for i,m in enumerate(allmenu.values(),start=1):
		table.insert('','end',value=[ i ,m[0],m[1],m[2],m[3],m[4] ] )


def AddMenu(name='latte'):
	# name = 'latte'
	if name not in allmenu:
		allmenu[name] = [product[name]['id'],product[name]['name'],product[name]['price'],1,product[name]['price']]
		
	else:
		# {'latte': ['ລາເຕ້', 18000, 1, 18000]}
		quan = allmenu[name][3] + 1
		total = quan * product[name]['price']
		allmenu[name] = [product[name]['id'],product[name]['name'],product[name]['price'], quan ,total]
	print('-----> ALLMENU',allmenu)
	# ຍອດລວມ
	count = sum([ m[4] for m in allmenu.values()])
	v_total.set('{:,.2f}'.format(count))
	UpdateTable()


button_dict = {}

row = 0
column = 0
column_quan = 5 
for i,(k,v) in enumerate(product.items()):
	if column == column_quan:
		column = 0
		row += 1
	# print('k :',k)

	print('IMG:', v['icon'])
	new_icon = PhotoImage(file=v['icon'])
	B = ttk.Button(CF1,text=v['name'], compound='top')
	button_dict[v['id']] = {'button':B, 'row':row, 'column':column}
	B.configure(command=lambda m=k: AddMenu(m))
	B.configure(image=new_icon)
	B.image = new_icon
	B.grid(row=row, column=column)
	column += 1

addproduct.button_list = button_dict
addproduct.button_frame = CF1

product_icon.button_list = button_dict
product_icon.button_frame = CF1
product_icon.function_add = AddMenu


print(button_dict)
def testclearbutton(event):
	for b in button_dict.values():
		# b = {'button':B, 'row':row, 'column':column}
		b['button'].grid_forget()

GUI.bind('<F5>',testclearbutton)

# ---------------Table-----------------
CF2 = Frame(T3)
CF2.place(x=500,y=100)

header = ['NO.','ID', 'TITLE', 'PRICE','QUANTITY','TOTAL']
hwidth = [50,70,130,100,100,100]

table = ttk.Treeview(CF2,columns=header, show='headings',height=14)
table.pack()

for hd,hw in zip(header,hwidth):
	table.column(hd,width=hw)
	table.heading(hd,text=hd)

# for hd in header:
#     table.heading(hd,text=hd)

# Delete Button
def DeleteProduct(event=None):
	choice = messagebox.askyesno('Delete', 'Are you sure want to delete?')
	print(choice)
	if choice == True:
		select = table.selection() # choose item 
		print(select)
		if len(select) != 0:
			data = table.item(select)['values']
			print(data)
			del allmenu[data[1]]
			count = sum([ m[4] for m in allmenu.values()])
			v_total.set('{:,.2f}'.format(count))
			UpdateTable()

		else:
			messagebox.showwarning('ບໍ່ໄດ້ເລືອກລາຍການ','ກະລຸນາເລືອກລາຍການທີ່ຈະແກ້ໄຂ')
	else:
		pass

table.bind('<Delete>',DeleteProduct)


# Update Quantity Button
def UpdateQuantity(event=None):
	GUIQ = Toplevel()
	Width = 400
	Height = 200
	Monitor_width = GUIQ.winfo_screenwidth()
	Monitor_height = GUIQ.winfo_screenheight()

	Start_x = (Monitor_width/2) - (Width/2)
	Start_y = (Monitor_height/2) - (Height/2)
	Start_y = Start_y - 50

	print('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
	GUIQ.geometry('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
	GUIQ.focus_force()

	L = Label(GUIQ,text='Please fill quantity',font=(None,20)).pack(pady=20)
	v_newquan = IntVar()
	v_newquan.set(1)
	E1 = ttk.Entry(GUIQ,textvariable=v_newquan,font=(None,20))
	E1.pack()

	E1.bind('<Up>',lambda x: v_newquan.set(v_newquan.get() + 1))
	E1.bind('<Down>',lambda x: v_newquan.set(v_newquan.get() - 1))
	

	# GUIQ.focus_force()
	E1.focus()

	select = table.selection() # choose item 
	if len(select) != 0:
		data = table.item(select)['values']
		print(data)
		sid = data[1]
		current_quan = data[4]
		v_newquan.set(current_quan)
	else:
		messagebox.showwarning('ບໍ່ໄດ້ເລືອກລາຍການ','ກະລຸນາເລືອກລາຍການທີ່ຈະແກ້ໄຂ')

	def save_update(event=None):
		allmenu[sid][3] = v_newquan.get()
		allmenu[sid][4] = v_newquan.get() * float(allmenu[sid][2]) # * price
		count = sum([ m[4] for m in allmenu.values()]) # update total
		v_total.set('{:,.2f}'.format(count))
		UpdateTable()
		GUIQ.destroy()


	GUIQ.bind('<Return>',save_update)

	B1 = ttk.Button(GUIQ,text='SAVE',command=save_update)
	B1.pack(ipadx=10,ipady=10,pady=10)

	GUIQ.bind('<Escape>',lambda x: GUIQ.destroy())
	GUIQ.mainloop()

table.bind('<F12>',UpdateQuantity)

L = Label(T3,text='TOTAL :', font=(None,15)).place(x=500,y=430)

v_total = StringVar()
v_total.set('0.0')

LT = Label(T3,textvariable=v_total, font=(None,15))
LT.place(x=585, y=430)

def Reset():
	global allmenu
	allmenu = {}
	table.delete(*table.get_children())
	v_total.set('0.0')
	trstamp = datetime.now().strftime('%y%m%d%H%M%S') #GEN Transaction
	v_transaction.set(trstamp)

B = ttk.Button(T3, text='CLEAR', command=Reset).place(x=500, y=460)

# Transaction ID
v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S')  # GEN Transaction
v_transaction.set(trstamp)

LTR = Label(T3, textvariable=v_transaction, font=(None, 10)).place(x=960, y=70)
L = Label(T3, text='TRANSACTION ID : ', font=(None, 10)).place(x=860, y=70)

# Save Button
FB = Frame(T3)
FB.place(x=937, y=440)

def AddTransaction():
	# writetocsv('transaction.csv')
	stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	transaction = v_transaction.get()
	print(transaction, stamp, allmenu.values())
	for m in allmenu.values():
		# before : ['ອາເມຣິກາໂນ້', 17000, 1, 17000]
		# after : ['220217210553', '2022-02-17 21:06:03','ອາເມຣິກາໂນ້', 17000, 1, 17000]
		m.insert(0,transaction)
		m.insert(1,stamp)
		writetocsv(m,'transaction.csv')
	Reset() #clear data

def CheckOut(event=None):
	GUICO = Toplevel()
	Width = 680
	Height = 660
	Monitor_width = GUICO.winfo_screenwidth()
	Monitor_height = GUICO.winfo_screenheight()

	Start_x = (Monitor_width/2) - (Width/2)
	Start_y = (Monitor_height/2) - (Height/2)
	Start_y = Start_y - 50

	print('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
	GUICO.geometry('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
	GUICO.focus_force()

	global total

	if v_member.get() != 'NON-MEMBER':
		discount_value = 0.05
		discount = float(v_total.get().replace(',','')) * discount_value # DISCOUNT RATE
		total = float(v_total.get().replace(',','')) - discount
	else:
		discount = 0
		total = float(v_total.get().replace(',',''))


	text = 'TOTAL {} LAK'.format(v_total.get())
	L = Label(GUICO,text=text,fg='grey',font=(None,15)).pack(pady=10)

	text = 'DISCOUNT {:,.2f} LAK'.format(discount)
	L = Label(GUICO,text=text,fg='red',font=(None,15)).pack(pady=10)

	text = 'SUMTOTAL {:,.2f} LAK'.format(total)
	L = Label(GUICO,text=text,fg='grey',font=(None,15)).pack(pady=10)

	v_change =StringVar()
	L2 = Label(GUICO,textvariable=v_change,fg='orange', font=(None,15)).pack(pady=10)
	v_change.set('CHANGE')

	v_cash = DoubleVar()
	v_cash.set(0)
	E1 = ttk.Entry(GUICO,textvariable=v_cash,font=(None,20))
	E1.pack()

	E1.bind('<Up>',lambda x: v_cash.set(v_cash.get() + 1000))
	E1.bind('<Down>',lambda x: v_cash.set(v_cash.get() - 1000))
	E1.focus()


	global state
	state = 1

	def save_change(event=None):
		global state 
		global total 
		if state == 1:
			total = total
			calc = v_cash.get() - total
			v_change.set('CHANGE : {:,.2f} LAK'.format(calc))
			state += 1
			Bchange.configure(text='SAVE')
		elif state == 2:
			AddTransaction()
			GUICO.destroy()
			state = 1
	

	GUICO.bind('<Return>',save_change)

	Bchange = ttk.Button(GUICO,text='CHANGE',command=save_change)
	Bchange.pack(ipadx=10,ipady=10,pady=10)

	QRImage(total,account='0801234567')

	img = PhotoImage(file='qr-payment.png')
	qrcode = Label(GUICO,image=img).pack()



# ----------------BANK NOTE----------------
	global v_banknote
	v_banknote = 0

	def Banknote(banktype):
		global v_banknote
		v_banknote += banktype # +50000
		print('Current Back:',v_banknote)
		v_cash.set(v_banknote)


	BF = Frame(GUICO)
	BF.pack(pady=20)

	# img_bn1 = PhotoImage(file='b1000.png')
	BN1 = ttk.Button(BF, text='100,000 LAK', command=lambda b=100000: Banknote(b))
	BN1.grid(row=0, column=0)

	# img_bn2 = PhotoImage(file='b500.png')
	BN2 = ttk.Button(BF, text='50,000 LAK', command=lambda b=50000: Banknote(b))
	BN2.grid(row=0, column=1)


	# img_bn3 = PhotoImage(file='b100.png')
	BN3 = ttk.Button(BF, text='20,000 LAK', command=lambda b=20000: Banknote(b))
	BN3.grid(row=0, column=2)


	# img_bn4 = PhotoImage(file='b50.png')
	BN4 = ttk.Button(BF, text='10,000 LAK', command=lambda b=10000: Banknote(b))
	BN4.grid(row=0, column=3)

	# img_bn5 = PhotoImage(file='b20.png')
	BN5 = ttk.Button(BF, text='5,000 LAK', command=lambda b=5000: Banknote(b))
	BN5.grid(row=0, column=4)


	BN5 = ttk.Button(BF, text='2,000 LAK', command=lambda b=2000: Banknote(b))
	BN5.grid(row=0, column=5)

	BN6 = ttk.Button(BF, text='1,000 LAK', command=lambda b=1000: Banknote(b))
	BN6.grid(row=0, column=6)


	L = ttk.Label(GUICO, text='CICK F12 CLEAR VALUES').pack()

	def clear_banknote(event):
		global v_banknote
		v_banknote = 0
		v_cash.set(0)


	GUICO.bind('<F12>',clear_banknote)
	GUICO.bind('<Escape>',lambda x: GUICO.destroy())
	GUICO.mainloop()


B = ttk.Button(FB, text='SAVE', command=CheckOut)
B.pack(ipadx=20, ipady=10)

v_member = StringVar()
v_member.set('NON-MEMBER')

LM = ttk.Label(T3,textvariable=v_member,font=(None,15))
LM.place(x=780,y=450)
LM.configure(foreground='red')


def set_member():
	GUIM = Toplevel()
	Width = 280
	Height = 180
	Monitor_width = GUI.winfo_screenwidth()
	Monitor_height = GUI.winfo_screenheight()

	Start_x = (Monitor_width/2) - (Width/2)
	Start_y = (Monitor_height/2) - (Height/2)

	GUIM.geometry('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
	GUIM.focus_force()

	L = ttk.Label(GUIM, text='MEMBER MOBLIE NO.')
	L.pack(pady=20)

	v_member.set('')
	EMember = ttk.Entry(GUIM,textvariable=v_member,font=(None,15))
	EMember.pack()
	EMember.focus()

	def Check(event=None):
		print(v_member.get())
		c = CheckMember(v_member.get())
		if c == True:
			v_member.set(v_member.get())
			LM.configure(foreground='grey')
			GUIM.destroy()
		else:
			v_member.set('NON-MEMBER')
			LM.configure(foreground='red')




	B = ttk.Button(GUIM, text='CHECK',command=Check)
	B.pack(pady=20)

	GUIM.bind('<Return>',Check)

	def close_window(event=None):
		v_member.set('NON-MEMBER')
		GUIM.destroy()
		LM.configure(foreground='red')

	GUIM.protocol('WM_DELETE_WINDOW',close_window)

	GUIM.mainloop()

img_member = PhotoImage(file='member-card2.png')
Bmember = ttk.Button(T3, image=img_member,command=set_member)
Bmember.place(x=720,y=444)


# ----------------Search menu----------------

FS1 = Frame(T3)
FS1.place(x=410,y=25)

v_search_barcode = StringVar()
Esearch = ttk.Entry(FS1, textvariable=v_search_barcode,font=(None,15,'bold'))
Esearch.grid(row=0,column=0,ipady=8)

def SearchBarcode(event=None):
	barcode = v_search_barcode.get()
	try:
		result = View_product_single(barcode)
		print(result)
		pid = result[0]
		AddMenu(pid)
	except:
		messagebox.showwarning('Not Found!','Product is not in stcok')
		v_search_barcode.set('')
		Esearch.focus()

Esearch.bind('<Return>', SearchBarcode)
Esearch.bind('<F3>',lambda x: v_search_barcode.set('') )



Bsearch = ttk.Button(FS1,text='SEARCH',command=SearchBarcode)
Bsearch.grid(row=0,column=1,ipadx=5,ipady=12,padx=10)





# History New Windows

def HistoryWindow(event):
	HIS = Toplevel() # Similar GUI = Tk()
	HIS.geometry('750x500')

	L = Label(HIS, text='ORDER RECORDS', font=(None, 30)).pack()

	# History
	header = ['TRANS ID','DATETIME', 'TITLE', 'PRICE','QUANTITY','TOTAL']
	hwidth = [100,100,200,100,100,100]

	table_history = ttk.Treeview(HIS,columns=header, show='headings',height=15)
	table_history.pack()

	for hd,hw in zip(header,hwidth):
		table_history.column(hd,width=hw)
		table_history.heading(hd,text=hd)

	# Update from CSV
	with open('transaction.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file) # file reader
		for row in fr:
			table_history.insert('',0,value=row)

	HIS.mainloop()

GUI.bind('<F1>',HistoryWindow)

# ----------------Tab4 = member-----------------#

def ET3(GUI,text,font=(20)):
	v_strvar = StringVar()
	T = Label(GUI,text=text,font=(None,15)).pack()
	E = ttk.Entry(GUI,textvariable=v_strvar,font=font)
	return (E,T,v_strvar)


F41 = Frame(T4) # F41 = Frame in Tab4 , No.1
F41.place(x=50,y=50)

v_membercode = StringVar()
v_membercode.set('M-1001')
v_databasecode = IntVar() 


L = Label(T4,text='MEMBER ID :',font=(None,13)).place(x=50,y=20)
LCode = Label(T4,textvariable=v_membercode,font=(None,12)).place(x=160,y=20)

E41, L, v_fullname = ET3(F41, 'FULLNAME')
E41.pack()

E42, L, v_tel = ET3(F41, 'MOBLIE')
E42.pack()

E43, L, v_usertype = ET3(F41, 'MEMBER')
E43.pack()
v_usertype.set('general')

E44, L, v_point = ET3(F41, 'POINT')
E44.pack()
v_point.set('0')

# E43.bind('<Return>', lambda x: print(v_usertype.get()))



def SaveMember():
	code = v_membercode.get()
	fullname = v_fullname.get()
	tel = v_tel.get()
	usertype = v_usertype.get()
	point = v_point.get()
	print(fullname, tel, usertype, point)
	# writetocsv([code, fullname, tel, usertype, point],'member.csv')
	Insert_member(code, fullname, tel, usertype, point)
	#table_member.insert('',0,value=[code, fullname, tel, usertype, point])
	UpdateTable_Member()

	v_fullname.set('')
	v_tel.set('')
	v_usertype.set('general')
	v_point.set('0')


BSave = ttk.Button(F41,text='SAVE',command=SaveMember)
BSave.pack()

def EditMember():
	code = v_databasecode.get() 
	print(allmember)
	allmember[code][2] = v_fullname.get()
	allmember[code][3] = v_tel.get()
	allmember[code][4] = v_usertype.get()
	allmember[code][5] = v_point.get()
	# UpdateCSV(list(allmember.values()),'member.csv')
	Update_member(code,'fullname', v_fullname.get())
	Update_member(code,'tel', v_tel.get())
	Update_member(code,'usertype', v_usertype.get())
	Update_member(code,'points', v_point.get()) # * points
	UpdateTable_Member()

	BEdit.state(['disabled']) # ເປີດປຸ່ມແກ້ໄຂ
	BSave.state(['!disabled']) # ປິດປຸ່ມບັນທຶກ
	# set default
	v_fullname.set('')
	v_tel.set('')
	v_usertype.set('general')
	v_point.set('0')

BEdit = ttk.Button(F41,text='EDIT',command=EditMember)
BEdit.pack()


def NewMember():
	UpdateTable_Member()
	BEdit.state(['disabled']) # ປີດປຸ່ມແກ້ໄຂ
	BSave.state(['!disabled']) # ເປີດປຸ່ມບັນທຶກ
	# set default
	v_fullname.set('')
	v_tel.set('')
	v_usertype.set('general')
	v_point.set('0')


BNew = ttk.Button(F41,text='NEW',command=NewMember)
BNew.pack()

# --------------Member table----------
F42 = Frame(T4)
F42.place(x=400, y=50)

header = ['ID', 'CODE', 'FULLNAME', 'MOBLIE', 'MEMBER', 'POINT']
hwidth = [40, 100, 150, 100, 100, 100]

table_member = ttk.Treeview(F42,columns=header, show='headings',height=15)
table_member.pack()

for hd,hw in zip(header,hwidth):
	table_member.column(hd,width=hw)
	table_member.heading(hd,text=hd)

# ---------------UpdateCSV-----------------#
def UpdateCSV(data, filename='data.csv'):
	# data = [[a,b],[a,b]]
	with open(filename,'w',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerows(data) # writerows = replace with list


# ------------Delete -------------
def DeleteMember(event=None):
	choice = messagebox.askyesno('Delete', 'Are you sure want to delete?')
	print(choice)
	if choice == True:
		select = table_member.selection() #เลือก item 
		print(select)
		if len(select) != 0:
			data = table_member.item(select)['values']
			print(data)
			del allmember[data[0]]
			Delete_member(data[0])
			# UpdateCSV(list(allmember.values()),'member.csv')
			UpdateTable_Member()
		else:
			messagebox.showwarning('ບໍ່ໄດ້ເລືອກລາຍການ','ກະລຸນາເລືອກລາຍການທີ່ຈະແກ້ໄຂ')
	else:
		pass

table_member.bind('<Delete>',DeleteMember)

# ------------Update Information-------------
def UpdateMemberInfo(event=None):

	select = table_member.selection() # choose item 
	if len(select) != 0:
		code = table_member.item(select)['values'][0]
		v_databasecode.set(code)
		print(allmember[code])
		memberinfo = allmember[code]

		v_membercode.set(memberinfo[1])
		v_fullname.set(memberinfo[2])
		v_tel.set(memberinfo[3])
		v_usertype.set(memberinfo[4])
		v_point.set(memberinfo[5])

		BEdit.state(['!disabled']) # ເປີດປຸ່ມແກ້ໄຂ
		BSave.state(['disabled']) # ປິດປຸ່ມບັນທຶກ
	else:
		messagebox.showwarning('ບໍ່ໄດ້ເລືອກລາຍການ','ກະລຸນາເລືອກລາຍການທີ່ຈະລົບ')

table_member.bind('<Double-1>',UpdateMemberInfo)

# Update Table
last_member = ''
allmember = {}

def UpdateTable_Member():
	global last_member
	
	fr = View_member()
	table_member.delete(*table_member.get_children()) #clear table
	for row in fr:
		table_member.insert('',0,value=row)
		code = row[0] 
		allmember[code] = list(row) #convert tuple to list
	
	print('Last ROW:',row)
	last_member = row[1] # select membercode
	# M-1001
	# ['M',1001+1]
	next_member = int(last_member.split('-')[1]) + 1
	v_membercode.set('M-{}'.format(next_member))
	print(allmember)

# POP UP Menu
member_rcmenu = Menu(GUI,tearoff=0) # rcmenu = right click menu
table_member.bind('<Button-3>',lambda event: member_rcmenu.post( event.x_root , event.y_root) )
member_rcmenu.add_command(label='Delete',command=DeleteMember)
member_rcmenu.add_command(label='Update',command=UpdateMemberInfo)

def SearchName():
	select = table_member.selection()
	name = table_member.item(select)['values'][1]
	print(name)
	url = 'https://www.google.com/search?q={}'.format(name)
	webbrowser.open(url)

member_rcmenu.add_command(label='Search Name',command=SearchName)

def SearchBCC():
	select = table_member.selection()
	name = table_member.item(select)['values'][1]
	print(name)
	url = 'https://www.bbc.co.uk/search?q={}'.format(name)
	webbrowser.open(url)

member_rcmenu.add_command(label='Search BCC',command=SearchBCC)
# https://www.bbc.co.uk/search?q=putin


BEdit.state(['disabled'])
try:
	UpdateTable_Member()
except:
	print('ກະລຸນາໃສ່ຂໍ້ມູນຢ່າງໜ້ອຍ 1 ລາຍການ')

# import os

# file = os.listdir()
# print(file)

# if 'memberdb.sqlite3' in file:
#     print('OK')
#     UpdateTable_Member()

GUI.mainloop()
