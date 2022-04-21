# GUI-Calculator.py
from tkinter import *
from tkinter import ttk, messagebox
import wikipedia
import csv
from datetime import datetime
import webbrowser
from memberdb import *
from productdb import *
from menufunction import *

# ----------------FUNCTION-----------------
addProduct = AddProduct()
productIcon = ProductIcon()

def writetocsv(data, filename='data.csv'):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerow(data)


GUI = Tk()
GUI.title('Program management')
GUI.iconbitmap('phenomenal.ico')

Width = 1100
Height = 650
Monitor_width = GUI.winfo_screenwidth()
Monitor_height = GUI.winfo_screenheight()

Start_x = (Monitor_width/2) - (Width/2)
Start_y = (Monitor_height/2) - (Height/2)
Start_y = Start_y - 50

GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))

# ----------------MENU BAR-----------------
menubar = Menu(GUI)
GUI.config(menu=menubar)

# ----------------------------------------------
# File Menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)


def ExportDatabase():
    print('Export Database to CSV')


filemenu.add_command(label='Export', command=ExportDatabase)
filemenu.add_command(label='Exit', command=GUI.quit)

# ----------------------------------------------
# Member Menu
membermenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Member', menu=membermenu)

# ----------------------------------------------
# Product Menu
productmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Product', menu=productmenu)

productmenu.add_command(label='Add Product', command=addProduct.command)

# ---------------------setting-------------------------
settingmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Setting', menu=settingmenu)

settingmenu.add_command(label='Product Icon',command=productIcon.command)



# Help Menu
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
contact_url = 'https://www.facebook.com/herytwenty.phonsavad'
helpmenu.add_command(label='Contact us',
                     command=lambda: webbrowser.open(contact_url))


def About():
    AboutGUI = Toplevel()
    AboutGUI.iconbitmap('phenomenal.ico')
    Width = 400
    Height = 200
    Monitor_width = GUI.winfo_screenwidth()
    Monitor_height = GUI.winfo_screenheight()
    Start_x = (Monitor_width/2) - (Width/2)
    Start_y = (Monitor_height/2) - (Height/2)
    Start_y = Start_y - 50
    AboutGUI.geometry(
        '{}x{}+{:.0f}+{:.0f}'.format(Width, Height, Start_x, Start_y))
    label = Label(AboutGUI, text='Program coffee management',
                  fg='green', font=(15)).pack()
    label = Label(
        AboutGUI, text='Develope by Hery Phenomenal\nhttps://www.facebook.com/herytwenty.phonsavad', font=(5)).pack()
    AboutGUI.mainloop()


helpmenu.add_command(label='About', command=About)

# ----------------Tab1 = ໜັງສື-----------------
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH, expand=1)


T3 = Frame(Tab)
T4 = Frame(Tab)

icon_tab1 = PhotoImage(file='Tab1-book.png')
icon_tab2 = PhotoImage(file='Tab2-search.png')
icon_tab3 = PhotoImage(file='Tab5-coffee.png')
icon_coffe = PhotoImage(file='coffee1.png')
icon_member = PhotoImage(file='Tab6-member.png')

Tab.add(T3, text='Coffee', image=icon_tab3, compound='top')
Tab.add(T4, text='Member', image=icon_member, compound='top')


# ----------------TimeStamp-----------------

days = {'Mon': 'ຈັນ',
        'Tue': 'ຄານ',
        'Wed': 'ພຸດ',
        'Thu': 'ພະຫັດ',
        'Fri': 'ສຸກ',
        'Sat': 'ເສົາ',
        'Sun': 'ອາທິດ'}


# ----------------Tab3 = Coffe-----------------

CF1 = Frame(T3)
CF1.place(x=50, y=100)

# ROW0
# header = ['No.', 'title', 'quantity','price','total']

allmenu = {}

product = {'latte': {'name': 'ລາເຕ້', 'price': 18000},
           'cappuccino': {'name': 'ຄາປູຊິໂນ້', 'price': 20000},
           'espresso': {'name': 'ເອສເປຣສໂຊ້', 'price': 18000},
           'mocha': {'name': 'ມອກຄ້າ', 'price': 18000},
           'americano': {'name': 'ອາເມຣິກາໂນ້', 'price': 17000},
           'breve': {'name': 'ເບຣບ', 'price': 17000},
           'ristretto': {'name': 'ຣິສເຕຣຕໂຕ', 'price': 17000},
           'marocchino': {'name': 'ມາຣອຄຊິໂນ້', 'price': 16000},
           'affogato': {'name': 'ອາຟໂຟກາໂຕ', 'price': 16000}}


def UpdateTable():
    table.delete(*table.get_children())
    for i, m in enumerate(allmenu.values(), start=1):
        table.insert('', 'end', value=[i, m[0], m[1], m[2], m[3]])


def AddMenu(name='latte'):
    # name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'], product[name]
                         ['price'], 1, product[name]['price']]

    else:
        # {'latte': ['ລາເຕ້', 18000, 1, 18000]}
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'],
                         product[name]['price'], quan, total]
    print(allmenu)
    # ຍອດລວມ
    count = sum([m[3] for m in allmenu.values()])
    v_total.set('{:,.2f}'.format(count))
    UpdateTable()


# ROW 0
B = ttk.Button(CF1, text='ລາເຕ້', image=icon_coffe,
               compound='top', command=lambda m='latte': AddMenu(m))
B.grid(row=0, column=0, ipadx=20, ipady=10)
B = ttk.Button(CF1, text='ຄາປູຊິໂນ້', image=icon_coffe,
               compound='top', command=lambda m='cappuccino': AddMenu(m))
B.grid(row=0, column=1, ipadx=20, ipady=10)
B = ttk.Button(CF1, text='ເອສເປຣສໂຊ້', image=icon_coffe,
               compound='top', command=lambda m='espresso': AddMenu(m))
B.grid(row=0, column=2, ipadx=20, ipady=10)

# ROW 1
B = ttk . Button(CF1, text='ມອກຄ້າ', image=icon_coffe,
                 compound='top', command=lambda m='mocha': AddMenu(m))
B.grid(row=1, column=0, ipadx=20, ipady=10)
B = ttk.Button(CF1, text='ອາເມຣິກາໂນ້', image=icon_coffe,
               compound='top', command=lambda m='americano': AddMenu(m))
B.grid(row=1, column=1, ipadx=20, ipady=10)
B = ttk.Button(CF1, text='ເບຣບ', image=icon_coffe,
               compound='top', command=lambda m='breve': AddMenu(m))
B.grid(row=1, column=2, ipadx=20, ipady=10)

# ROW 2
B = ttk . Button(CF1, text=' ຣິສເຕຣຕໂຕ', image=icon_coffe,
                 compound='top', command=lambda m='ristretto': AddMenu(m))
B.grid(row=2, column=0, ipadx=20, ipady=10)
B = ttk.Button(CF1, text='ມາຣອຄຊິໂນ້', image=icon_coffe,
               compound='top', command=lambda m='marocchino': AddMenu(m))
B.grid(row=2, column=1, ipadx=20, ipady=10)
B = ttk.Button(CF1, text='ອາຟໂຟກາໂຕ', image=icon_coffe,
               compound='top', command=lambda m='affogato': AddMenu(m))
B.grid(row=2, column=2, ipadx=20, ipady=10)


# ---------------Table-----------------
CF2 = Frame(T3)
CF2.place(x=500, y=100)

header = ['No.', 'title', 'price', 'quantity', 'total']
hwidth = [50, 200, 100, 100, 100]

table = ttk.Treeview(CF2, columns=header, show='headings', height=15)
table.pack()

for hd, hw in zip(header, hwidth):
    table.column(hd, width=hw)
    table.heading(hd, text=hd)

# for hd in header:
#     table.heading(hd,text=hd)


L = Label(T3, text='Total :', font=(None, 15)).place(x=500, y=450)

v_total = StringVar()
v_total.set('0.0')

LT = Label(T3, textvariable=v_total, font=(None, 15))
LT.place(x=560, y=450)


def Reset():
    global allmenu
    allmenu = {}
    table.delete(*table.get_children())
    v_total.set('0.0')
    trstamp = datetime.now().strftime('%y%m%d%H%M%S')  # GEN Transaction
    v_transaction.set(trstamp)


B = ttk.Button(T3, text='Clear', command=Reset).place(x=500, y=480)

# Transaction ID
v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S')  # GEN Transaction
v_transaction.set(trstamp)

LTR = Label(T3, textvariable=v_transaction, font=(None, 10)).place(x=960, y=70)
L = Label(T3, text='Transaction ID : ', font=(None, 10)).place(x=870, y=70)


# Save Button
FB = Frame(T3)
FB.place(x=937, y=460)


def AddTransaction():  # writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu.values())
    for m in allmenu.values():
        m.insert(0, transaction)  # before : ['ອາເມຣິກາໂນ້', 17000, 1, 17000]
        # after : ['220217210553', '2022-02-17 21:06:03','ອາເມຣິກາໂນ້', 17000, 1, 17000]
        m.insert(1, stamp)
        writetocsv(m, 'transaction.csv')
    Reset()  # clear data


B = ttk.Button(FB, text='Order', command=AddTransaction)
B.pack(ipadx=20, ipady=10)

# History New Windows


def HistoryWindow(event):
    HIS = Toplevel()  # ຄືກັບ GUI = Tk()
    HIS.geometry('750x500')

    L = Label(HIS, text='Order records', font=(None, 30)).pack()

    # History
    header = ['transaction-ID', 'datetime',
              'title', 'price', 'quantity', 'total']
    hwidth = [100, 150, 150, 100, 100, 100]

    table_history = ttk.Treeview(
        HIS, columns=header, show='headings', height=15)
    table_history.pack()

    for hd, hw in zip(header, hwidth):
        table_history.column(hd, width=hw)
        table_history.heading(hd, text=hd)

    # Update from CSV
    with open('transaction.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)  # file reader
        for row in fr:
            table_history.insert('', 0, value=row)

    HIS.mainloop()


GUI.bind('<F1>', HistoryWindow)

# ----------------Tab4 = member-----------------


def ET3(GUI, text, font=(20)):
    v_strvar = StringVar()
    T = Label(GUI, text=text, font=(None, 15)).pack()
    E = ttk.Entry(GUI, textvariable=v_strvar, font=font)
    return (E, T, v_strvar)


F41 = Frame(T4)  # F41 = Frame in Tab4 , No.1
F41.place(x=50, y=50)

v_membercode = StringVar()
v_membercode.set('M-10001')
v_databasecode = IntVar()

L = Label(T4, text='Member-ID :', font=(None, 10)).place(x=50, y=20)
LCode = Label(T4, textvariable=v_membercode,
              font=(None, 10)).place(x=150, y=20)

E41, L, v_fullname = ET3(F41, 'Full-name :')
E41.pack()

E42, L, v_moblie = ET3(F41, 'Moblie :')
E42.pack()

E43, L, v_usertype = ET3(F41, 'Member :')
E43.pack()
v_usertype.set('general')

E44, L, v_point = ET3(F41, 'Point :')
E44.pack()
v_point.set('0')

# E43.bind('<Return>', lambda x: print(v_usertype.get()))


def SaveMember():
    code = v_membercode.get()
    fullname = v_fullname.get()
    tel = v_moblie.get()
    usertype = v_usertype.get()
    point = v_point.get()
    print(fullname, tel, usertype, point)
    # writetocsv([code, fullname, tel, usertype, point],'member.csv')
    InsertMember(code, fullname, tel, usertype, point)
    # table_member.insert('', 0, value = [code, fullname, tel, usertype, point])
    UpdateTable_Member()

    v_fullname.set('')
    v_moblie.set('')
    v_usertype.set('general')
    v_point.set('0')


BSave = ttk.Button(F41, text='Save', command=SaveMember)
BSave.pack()


def EditMember():
    code = v_databasecode.get()
    allmember[code][2] = v_fullname.get()
    allmember[code][3] = v_moblie.get()
    allmember[code][4] = v_usertype.get()
    allmember[code][5] = v_point.get()
    UpdateMember(code, 'fullname', v_fullname.get())
    UpdateMember(code, 'tel', v_moblie.get())
    UpdateMember(code, 'usertype', v_usertype.get())
    UpdateMember(code, 'points', v_point.get())
    UpdateTable_Member()

    BEdit.state(['disabled'])  # ເປີດປຸ່ມແກ້ໄຂ
    BSave.state(['!disabled'])  # ປິດປຸ່ມບັນທຶກ
    # set default
    v_fullname.set('')
    v_moblie.set('')
    v_usertype.set('general')
    v_point.set('0')


BEdit = ttk.Button(F41, text='Edit', command=EditMember)
BEdit.pack()


def NewMember():
    UpdateTable_Member()
    BEdit.state(['disabled'])  # ປີດປຸ່ມແກ້ໄຂ
    BSave.state(['!disabled'])  # ເປີດປຸ່ມບັນທຶກ
    # set default
    v_fullname.set('')
    v_moblie.set('')
    v_usertype.set('general')
    v_point.set('0')


BNew = ttk.Button(F41, text='New', command=NewMember)
BNew.pack()

# --------------Member table---------------
F42 = Frame(T4)
F42.place(x=400, y=50)

header = ['ID', 'Code', 'Full-name', 'Moblie', 'Member', 'Point']
hwidth = [40, 100, 150, 100, 100, 100]

table_member = ttk.Treeview(F42, columns=header, show='headings', height=15)
table_member.pack()

for hd, hw in zip(header, hwidth):
    table_member.column(hd, width=hw)
    table_member.heading(hd, text=hd)

# ---------------UpdateCSV-----------------


def UpdateCSV(data, filename='data.csv'):
    # data = [[a,b],[a,b]]
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerows(data)  # writerows = replace with list


# ------------Delete -------------
def Delete_Member(event=None):
    choice = messagebox.askyesno('Delete', 'Are you sure want to delete?')
    if choice == True:
        select = table_member.selection()  # Choose item
        if len(select) != 0:
            data = table_member.item(select)['values']
            print(data)
            del allmember[data[0]]
            DeleteMember(data[0])
            UpdateTable_Member()
        else:
            messagebox.showerror('ບໍ່ໄດ້ເລືອກລາຍການ',
                                 'ກະລຸນາເລືອກລາຍການທີ່ຈະແກ້ໄຂ')
    else:
        pass


table_member.bind('<Delete>', Delete_Member)

# ------------Update Information-------------


def UpdateMemberInfo(event=None):
    select = table_member.selection()  # choose item
    if len(select) != 0:
        code = table_member.item(select)['values'][0]
        v_databasecode.set(code)
        print(allmember[code])
        memberinfo = allmember[code]

        v_membercode.set(memberinfo[1])
        v_fullname.set(memberinfo[2])
        v_moblie.set(memberinfo[3])
        v_usertype.set(memberinfo[4])
        v_point.set(memberinfo[5])

        BEdit.state(['!disabled'])  # ເປີດປຸ່ມແກ້ໄຂ
        BSave.state(['disabled'])  # ປິດປຸ່ມບັນທຶກ
    else:
        messagebox.showerror('ບໍ່ໄດ້ເລືອກລາຍການ', 'ກະລຸນາເລືອກລາຍການທີ່ຈະລົບ')


table_member.bind('<Double-1>', UpdateMemberInfo)

# Update Table
last_member = ''
allmember = {}


def UpdateTable_Member():
    global last_member

    fr = ViewMember()
    table_member.delete(*table_member.get_children())  # clear table
    for row in fr:
        table_member.insert('', 0, value=row)
        code = row[0]  # ดึงรหัสมา
        allmember[code] = list(row)  # convert tuple to list

    print('Last ROW:', row)
    last_member = row[1]
    # M-1001
    # ['M',1001+1]
    next_member = int(last_member.split('-')[1]) + 1
    v_membercode.set('M-{}'.format(next_member))
    print(allmember)


# Pop Up Menu
member_rcmenu = Menu(GUI, tearoff=0)  # rcmenu = right click menu
member_rcmenu.add_command(label='Delete', command=Delete_Member)
member_rcmenu.add_command(label='Update', command=UpdateMemberInfo)
table_member.bind(
    '<Button-3>', lambda event: member_rcmenu.post(event.x_root, event.y_root))


def SearchName():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.google.com/search?q={}'.format(name)
    webbrowser.open(url)


member_rcmenu.add_command(label='Search Name', command=SearchName)


def SearchBBC():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.bbc.co.uk/search?q={}'.format(name)
    webbrowser.open(url)


member_rcmenu.add_command(label='Search BBC', command=SearchBBC)

BEdit.state(['disabled'])
try:
    UpdateTable_Member()
except:
    print('ກະລຸນາໃສ່ຂໍ້ມູນຢ່າງໜ້ອຍ 1 ລາຍການ')
GUI.mainloop()
