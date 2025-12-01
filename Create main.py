from database import create_tables
from product_operations import add_product, view_products
from order_operations import place_order, view_orders

create_tables()

def menu():
    while True:
        print("\n=== E-COMMERCE MANAGEMENT ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Product Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            add_product(name, price, qty)
            print("✅ Product Added")

        elif choice == "2":
            products = view_products()
            for p in products:
                print(p)

        elif choice == "3":
            pid = int(input("Product ID: "))
            qty = int(input("Quantity: "))
            print(place_order(pid, qty))

        elif choice == "4":
            orders = view_orders()
            for o in orders:
                print(o)

        elif choice == "5":
            break

        else:
            print("❌ Invalid Choice")

menu()
