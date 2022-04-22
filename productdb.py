import sqlite3

conn = sqlite3.connect('productdb.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                title TEXT,
                price REAL,
                image TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS product_status (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                status TEXT)""")


def InsertProductStatus(product_id, status):
    check = ViewProductStatus(product_id)
    if check == None:
        with conn:
            command = 'INSERT INTO product_status VALUES (?,?,?)'
            c.execute(command, (None, product_id, status))
        conn.commit()
        print('status saved')
    else:
        print('product_id exist !')
        print(check)
        UpdateProductStatus(product_id, status)


def ViewProductStatus(product_id):
    # READ
    with conn:
        command = 'SELECT * FROM product_status WHERE product_id = (?)'
        c.execute(command, ([product_id]))
        result = c.fetchone()
    return result

def UpdateProductStatus(product_id, status):
    # UPDATE
    with conn:
        command = 'UPDATE product_status SET status = (?) WHERE ID = (?)'
        c.execute(command, ([status, product_id]))
    conn.commit()
    print('updated :' ,(product_id,status))

def InsertProduct(productid, title, price, image):
    # CREATE
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)'  # SQL
        c.execute(command, (None, productid, title, price, image))
    conn.commit()  # save database
    print('saved')


def ViewProduct():
    # READ
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result


def ViewProductTableIcon():
    # READ
    with conn:
        command = 'SELECT ID, productid,title FROM product'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result


def ViewProductSingle(productid):
    # READ
    with conn:
        command = 'SELECT * FROM product WHERE productid = (?)'
        c.execute(command, ([productid]))
        result = c.fetchone()
    print(result)
    return result


if __name__ == '__main__':
    # InsertProduct('Coffee-1002', 'Americano', '17000', r'C:\Image\americano.png')
    # ViewProduct()
    # ViewProductTableIcon()
    InsertProductStatus(1,'show')
    # print(ViewProductStatus(1))
