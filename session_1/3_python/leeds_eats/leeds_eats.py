import sqlite3

# ==================================================
# Section 1 - Summaries
# ==================================================


def total_customers(conn):
    query = """
            SELECT COUNT(*) AS total FROM Customers
            """
    total_customers = conn.execute(query).fetchone()["total"]
    print(f"Total number of customers: {total_customers}")


def customer_signup_range(conn):
    query = """
            SELECT MIN(signup_date) AS first_signup, MAX(signup_date) AS last_signup
            FROM Customers
            """
    result = conn.execute(query).fetchone()
    print(
        f"Customer signup date range: {result['first_signup']} to {result['last_signup']}"
    )


def order_summary_stats(conn):
    query = """
            SELECT
                COUNT(*) AS total_orders,
                AVG(order_total) AS average_order_value,
                MIN(order_total) AS min_order_value,
                MAX(order_total) AS max_order_value
            FROM Orders
            """
    result = conn.execute(query).fetchone()
    print(f"Total orders: {result['total_orders']}")
    print(f"Average order value: £{result['average_order_value']:.2f}")
    print(f"Minimum order value: £{result['min_order_value']:.2f}")
    print(f"Maximum order value: £{result['max_order_value']:.2f}")


def driver_summary(conn):
    query = """
            SELECT Driver_Name, Hire_Date FROM Drivers
            """
    result = conn.execute(query).fetchall()
    print("Driver Summary:")
    for row in result:
        print(f"Driver: {row['Driver_Name']}, Hire Date: {row['Hire_Date']}")


# ==================================================
# Section 2 - Key Statistics
# ==================================================


def orders_per_customer(conn):
    query = """
            SELECT C.Customer_ID, C.Customer_Name, COUNT(O.Order_ID) AS order_count
            FROM Customers C
            LEFT JOIN Orders O ON C.Customer_ID = O.Customer_ID
            GROUP BY C.Customer_ID, C.Customer_Name
            ORDER BY C.Customer_ID ASC
            """
    result = conn.execute(query).fetchall()
    print("Orders per Customer:")
    for row in result:
        print(
            f"Customer ID: {row['Customer_ID']}, Name: {row['Customer_Name']}, Orders: {row['order_count']}"
        )


def driver_workload(conn):
    query = """
            SELECT D.Driver_ID, D.Driver_Name, COUNT(O.Order_ID) AS deliveries_completed
            FROM Drivers D
            LEFT JOIN Orders O ON D.Driver_ID = O.Order_ID
            GROUP BY D.Driver_ID, D.Driver_Name
            ORDER BY deliveries_completed DESC
            """
    result = conn.execute(query).fetchall()
    print("Driver Workload:")
    for row in result:
        print(
            f"Driver ID: {row['Driver_ID']}, Name: {row['Driver_Name']}, Deliveries Completed: {row['deliveries_completed']}"
        )


# not quite working yet
def delivery_lookup_by_id(conn, order_id):
    query = """
            SELECT O.Order_ID, O.Order_Date, DV.Delivery_Date, D.Driver_Name
            FROM Orders O
            LEFT JOIN Deliveries DV ON O.Order_ID = DV.Driver_ID
            LEFT JOIN Drivers D ON DV.Order_ID = D.Driver_ID
            WHERE O.Order_ID = ?
            """
    result = conn.execute(query, (order_id,)).fetchone()
    if result:
        print(
            f"Order ID: {result['Order_ID']}, Order Date: {result['Order_Date']}, Delivery Date: {result['Delivery_Date']}, Driver: {result['Driver_Name']}"
        )
    else:
        print(f"No delivery found for Order ID: {order_id}")


# ==================================================
# Section 3 - Time-based Summaries
# ==================================================


def orders_per_date(conn):
    pass


def deliveries_per_date(conn):
    pass


def customer_signups_per_month(conn):
    pass


# ==================================================
# Section 4 - Performance and Rankings
# ==================================================


def top_customers_by_spend(conn, limit=5):
    pass


def rank_drivers_by_deliveries(conn):
    pass


def high_value_orders(conn, threshold):
    pass


# ==================================================
# Menus - You should not need to change any code below this point until the stretch tasks.
# ==================================================


def section_1_menu(conn):
    while True:
        print("\nSection 1 - Summaries")
        print("1. Total number of customers")
        print("2. Customer signup date range")
        print("3. Order summary statistics")
        print("4. Driver summary")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            total_customers(conn)
        elif choice == "2":
            customer_signup_range(conn)
        elif choice == "3":
            order_summary_stats(conn)
        elif choice == "4":
            driver_summary(conn)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_2_menu(conn):
    while True:
        print("\nSection 2 - Key Statistics")
        print("1. Orders per customer")
        print("2. Driver workload")
        print("3. Order delivery overview")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            orders_per_customer(conn)
        elif choice == "2":
            driver_workload(conn)
        elif choice == "3":
            order_id = input("Enter order ID: ").strip()
            if not order_id.isdigit():
                print("Please enter a valid integer order ID.")
                continue
            delivery_lookup_by_id(conn, int(order_id))
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_3_menu(conn):
    while True:
        print("\nSection 3 - Time-based Summaries")
        print("1. Orders per date")
        print("2. Deliveries per date")
        print("3. Customer signups per month")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            orders_per_date(conn)
        elif choice == "2":
            deliveries_per_date(conn)
        elif choice == "3":
            customer_signups_per_month(conn)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_4_menu(conn):
    while True:
        print("\nSection 4 - Performance and Rankings")
        print("1. Top 5 customers by total spend")
        print("2. Rank drivers by deliveries completed")
        print("3. High-value orders")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            top_customers_by_spend(conn)
        elif choice == "2":
            rank_drivers_by_deliveries(conn)
        elif choice == "3":
            try:
                threshold = float(input("Enter order value threshold (£): "))
                high_value_orders(conn, threshold)
            except ValueError:
                print("Please enter a valid numerical value.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def main_menu(conn):
    while True:
        print("\n=== Delivery Service Management Dashboard ===")
        print("1. Section 1 - Summaries")
        print("2. Section 2 - Key Statistics")
        print("3. Section 3 - Time-based Summaries")
        print("4. Section 4 - Performance and Rankings")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            section_1_menu(conn)
        elif choice == "2":
            section_2_menu(conn)
        elif choice == "3":
            section_3_menu(conn)
        elif choice == "4":
            section_4_menu(conn)
        elif choice == "0":
            print("Exiting dashboard.")
            break
        else:
            print("Invalid option. Please try again.")


def get_connection(db_path="food_delivery.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == "__main__":
    conn = get_connection()
    main_menu(conn)
    conn.close()
