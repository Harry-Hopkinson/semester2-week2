"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = """
            SELECT F.Title, S.Screen, T.Price
            FROM Films F
            JOIN Screenings S ON S.Film_ID = F.Film_ID
            JOIN Tickets T ON T.Screening_ID = S.Screening_ID
            WHERE T.Customer_ID = ?
            ORDER BY F.Title ASC
            """

    result = conn.execute(query, (customer_id,)).fetchall()
    return result


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    query = """
            SELECT S.Screening_Id, F.Title, COUNT(T.Ticket_Id) AS tickets_sold
            FROM Screenings S
            LEFT JOIN Films F ON S.Film_ID = F.Film_ID
            LEFT JOIN Tickets T ON T.Screening_Id = S.Screening_Id
            GROUP BY S.Screening_Id, F.Title
            ORDER BY tickets_sold DESC
            """

    result = conn.execute(query).fetchall()
    return result


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    query = """
            SELECT C.Customer_Name, SUM(T.Price) AS total_spent
            FROM Customers C
            LEFT JOIN Tickets T ON T.Customer_ID = C.Customer_ID
            GROUP BY C.Customer_ID, C.Customer_Name
            HAVING total_spent > 0
            ORDER BY total_spent DESC
            LIMIT ? 
            """

    result = conn.execute(query, (limit,)).fetchall()
    return result
