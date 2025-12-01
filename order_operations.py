from database import get_connection

def place_order(product_id, qty):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT price, quantity FROM products WHERE id=?", (product_id,))
    product = cur.fetchone()

    if not product:
        return "❌ Product Not Found"

    price, available_qty = product

    if qty > available_qty:
        return "❌ Not Enough Stock"

    total = price * qty

    cur.execute("INSERT INTO orders(product_id, quantity, total_price) VALUES (?,?,?)",
                (product_id, qty, total))

    cur.execute("UPDATE products SET quantity = quantity - ? WHERE id=?",
                (qty, product_id))

    conn.commit()
    conn.close()
    return "✅ Order Placed Successfully"

def view_orders():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    data = cur.fetchall()
    conn.close()
    return data
