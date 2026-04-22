import psycopg2
import time


def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="warehouse",
                user="postgres",
                password="postgres",
                host="db",
                port="5432"
            )
            return conn
        except psycopg2.OperationalError:
            print("Waiting for database to be ready...")
            time.sleep(2)


def view_inventory(conn):
    cur = conn.cursor()
    cur.execute("SELECT sku, name, price, stock_quantity FROM products ORDER BY sku;")
    products = cur.fetchall()

    print("\nCurrent Inventory")
    print("-" * 65)
    print(f"{'SKU':<12}{'Name':<25}{'Price':<12}{'Stock':<10}")
    print("-" * 65)

    for product in products:
        sku, name, price, stock = product
        print(f"{sku:<12}{name:<25}${price:<11}{stock:<10}")

    print("-" * 65)
    cur.close()


def increase_inventory(conn):
    sku = input("Enter SKU to restock: ").strip()

    try:
        quantity = int(input("Enter quantity to add: ").strip())
        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return
    except ValueError:
        print("Error: Quantity must be a positive integer.")
        return

    cur = conn.cursor()
    cur.execute("SELECT stock_quantity FROM products WHERE sku = %s;", (sku,))
    product = cur.fetchone()

    if product is None:
        print("Error: The SKU is invalid.")
        cur.close()
        return

    cur.execute(
        "UPDATE products SET stock_quantity = stock_quantity + %s WHERE sku = %s;",
        (quantity, sku)
    )
    conn.commit()
    print("Inventory updated successfully.")
    cur.close()


def reduce_inventory(conn):
    sku = input("Enter SKU to reduce: ").strip()

    try:
        quantity = int(input("Enter quantity to remove: ").strip())
        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return
    except ValueError:
        print("Error: Quantity must be a positive integer.")
        return

    cur = conn.cursor()
    cur.execute("SELECT stock_quantity FROM products WHERE sku = %s;", (sku,))
    product = cur.fetchone()

    if product is None:
        print("Error: The SKU is invalid.")
        cur.close()
        return

    current_stock = product[0]

    if quantity > current_stock:
        print("Error: Insufficient stock.")
        cur.close()
        return

    cur.execute(
        "UPDATE products SET stock_quantity = stock_quantity - %s WHERE sku = %s;",
        (quantity, sku)
    )
    conn.commit()
    print("Inventory updated successfully.")
    cur.close()


def main():
    conn = connect_db()

    while True:
        print("\nWarehouse Inventory System")
        print("1. View Current Inventory")
        print("2. Increase Inventory")
        print("3. Reduce Inventory")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_inventory(conn)
        elif choice == "2":
            increase_inventory(conn)
        elif choice == "3":
            reduce_inventory(conn)
        elif choice == "4":
            print("Goodbye.")
            conn.close()
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
    
    