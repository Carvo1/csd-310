### The wine distribution, are all wines selling as they thought? Is one wine not selling? Which distributor carries which wine

""" 
    Title: Wine_Distribution_report.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 15 July 2021
    Description: Pulling table data from MySQL database bacchus, 
"""

""" import statements """
import mysql.connector as mysql
from mysql.connector import errorcode


""" database config object """
db = mysql.connect(
    user = "bacchus_user",
    password = "MySQL8IsGreat!",
    host = "127.0.0.1",
    database = "bacchus",
)


cursor = db.cursor()




### creating the function to calculate total distributors orders
def distribution_report():
    
    #Finding the length that will influence the while statement
    cursor.execute("SELECT distributors_id FROM distributors")
    total = cursor.fetchall()
    num_distributors = int(len(total))
    print(num_distributors)

    #Creating variables for future use
    x = 0
    y = 1
    distSalesList = []


    ### While statement to iterate through and grab the distributor order totals for each distributor and append them to a list
    while x < num_distributors:
        cursor.execute("SELECT product_id, distributors_name, SUM(quantity) FROM product_orders INNER JOIN distributors ON distributors.distributors_id = product_orders.distributors_id WHERE distributors.distributors_id ="+str(y))
        dist_info = cursor.fetchall()
        cursor.execute("SELECT product_name FROM product_orders INNER JOIN product ON product.product_id = product_orders.product_id WHERE product_orders.distributors_id ="+str(y))
        dist_info1 = cursor.fetchall()
        dist_info = dist_info + dist_info1
        distSalesList.append(dist_info)
        x = x + 1
        y = y + 1


    #Using a for loop to iterate through the list and print the results to the user
    print("\n *** Distribution Sales Information ***")
    for i in distSalesList:
        print(" Distributors Name:  {}\n Quantity Ordered:   {}\n Product Name:       {}\n ".format(i[0][1],i[0][2],i[1][0]))





### creating the function to calculate total product sales
def product_sale():
    #Finding the length that will influence the while statement
    cursor.execute("SELECT product_id FROM product")
    length_determine = cursor.fetchall()
    length_determine = int(len(length_determine))

    #Creating variables for future use
    x = 0
    y = 1
    productSalesList = []


    ### While statement to iterate through and grab the sales totals for each type of product and append them to a list
    while x < length_determine:
        cursor.execute("SELECT product_name, SUM(product_orders.quantity) FROM product_orders INNER JOIN product ON product.product_id = product_orders.product_id WHERE product_orders.product_id = "+str(y))
        dist_info = cursor.fetchall()
        productSalesList.append([dist_info[0][0],dist_info[0][1]])
        x = x + 1
        y = y + 1

    #Using a for loop to iterate through the list and print the results to the user
    print("\n *** Total Product Sales ***")
    for i in productSalesList:
        print(" Product Name:    {}\n Quantity Sold:   {}\n ".format(i[0],i[1]))



distribution_report()
product_sale()

