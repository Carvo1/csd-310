"""
    Title: bacchus_populate.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 11 July 2021
    Description: Populating and printing tables from MySQL database bacchus.
"""

""" import statements """
import mysql.connector as mysql

""" database config object """

db = mysql.connect(
    user="bacchus_user",
    password="MySQL8IsGreat!",
    host="127.0.0.1",
    database="bacchus",
)

mycursor = db.cursor()

'''Creating functions to populate specific tables'''


# Creating a Function to populate table rows
def hours():
    sql = "INSERT INTO hours_worked (date, hours_worked,employee_id) VALUES (%s,%s,%s)"
    val = [
        ('2020/03/31', 520, 1),
        ('2020/03/31', 530, 2),
        ('2020/03/31', 510, 3),
        ('2020/03/31', 530, 4),
        ('2020/03/31', 525, 5),
        ('2020/03/31', 505, 6),
        ('2020/06/30', 520, 1),
        ('2020/06/30', 530, 2),
        ('2020/06/30', 510, 3),
        ('2020/06/30', 530, 4),
        ('2020/06/30', 525, 5),
        ('2020/06/30', 505, 6),
        ('2020/09/30', 520, 1),
        ('2020/09/30', 530, 2),
        ('2020/09/30', 510, 3),
        ('2020/09/30', 530, 4),
        ('2020/09/30', 525, 5),
        ('2020/09/30', 505, 6),
        ('2020/12/31', 520, 1),
        ('2020/12/31', 530, 2),
        ('2020/12/31', 510, 3),
        ('2020/12/31', 530, 4),
        ('2020/12/31', 525, 5),
        ('2020/12/31', 505, 6),
    ]
    mycursor.executemany(sql, val)
    # Commiting the changes to the table
    db.commit()


# Creating a Function to populate table rows
def product_orders():
    sql = "INSERT INTO product_orders (date_of_order, product_id, quantity, cost_per_unit, distributors_id) VALUES (%s,%s,%s,%s,%s)"
    val = [
        ('2020-07-10', 1, 75, 5, 1),
        ('2020-07-10', 2, 65, 6, 2),
        ('2020-07-10', 3, 80, 7, 3),
        ('2020-07-10', 4, 90, 8, 4),
        ('2020-07-10', 3, 110, 7, 5),
        ('2020-07-10', 4, 75, 8, 6),
        ('2020-06-10', 1, 75, 5, 1),
        ('2020-06-10', 2, 100, 6, 2),
        ('2020-06-10', 3, 85, 7, 3),
        ('2020-06-10', 4, 105, 8, 4),
        ('2020-06-10', 3, 90, 7, 5),
        ('2020-06-10', 4, 75, 8, 6),
        ('2020-05-10', 1, 70, 5, 1),
        ('2020-05-10', 2, 65, 6, 2),
        ('2020-05-10', 3, 85, 7, 3),
        ('2020-05-10', 4, 75, 8, 4),
        ('2020-05-10', 3, 105, 7, 5),
        ('2020-05-10', 4, 95, 8, 6),
    ]
    mycursor.executemany(sql, val)
    # Commiting the changes to the table
    db.commit()


hours()
product_orders()
