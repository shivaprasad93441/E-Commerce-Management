from database import get_connection

def add_product(name, price, qty):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name, price, quantity) VALUES (?,?,?)",
                (name, price, qty))
    conn.commit()
    conn.close()

def view_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    conn.close()
    return data
