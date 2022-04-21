from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productdb import *


class AddProduct:

    def __init__(self):
        self.v_productid = None
        self.v_title = None
        self.v_price = None
        self.v_imagepath = None

    def popup(self):
        MGUI = Toplevel()
        MGUI.geometry('300x400')
        MGUI.title('Add Product')

        self.v_productid = StringVar()
        self.v_title = StringVar()
        self.v_price = StringVar()
        self.v_imagepath = StringVar()

        L = Label(MGUI, text='Add product', font=(None, 15))
        L.pack(pady=20)

        L = Label(MGUI, text='Product ID', font=(None, 10)).pack()
        E1 = ttk.Entry(MGUI, textvariable=self.v_productid, font=(None, 10))
        E1.pack(pady=10)

        L = Label(MGUI, text='Product name', font=(None, 10)).pack()
        E2 = ttk.Entry(MGUI, textvariable=self.v_title, font=(None, 10))
        E2.pack(pady=10)

        L = Label(MGUI, text='Price', font=(None, 10)).pack()
        E3 = ttk.Entry(MGUI, textvariable=self.v_price, font=(None, 10))
        E3.pack(pady=10)

        L = Label(MGUI, textvariable=self.v_imagepath).pack()

        ButtonSelect = ttk.Button(
            MGUI, text='Choose image ( 50 x 50 px)', command=self.selectfile)
        ButtonSelect.pack(pady=10)

        ButtonSave = ttk.Button(MGUI, text='Save', command=self.saveproduct)
        ButtonSave.pack(pady=10, ipadx=8, ipady=8)

        MGUI.mainloop()

    def selectfile(self):
        filetypes = (
            ('PNG', '*.png'),
            ('All files', '*.*')
        )
        select = filedialog.askopenfilename(
            title='Choose file image', initialdir='/', filetypes=filetypes)
        self.v_imagepath.set(select)

    def saveproduct(self):
        v1 = self.v_productid.get()
        v2 = self.v_title.get()
        v3 = float(self.v_price.get())
        v4 = self.v_imagepath.get()
        InsertProduct(v1, v2, v3, v4)
        self.v_productid.set('')
        self.v_title.set('')
        self.v_price.set('')
        self.v_imagepath.set('')
        ViewProduct()

    def command(self):
        self.popup()


if __name__ == '__main__':
    test = AddProduct()
