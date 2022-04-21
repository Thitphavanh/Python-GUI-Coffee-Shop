import sqlite3

conn = sqlite3.connect('productdb.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                title TEXT,
                price REAL,
                image TEXT)""")


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
    ViewProductTableIcon()
