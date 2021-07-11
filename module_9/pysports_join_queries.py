""" 
    Title: pysports_join_queries.py
    Author: Steffan Hinkle
    Date: 11 July 2021
    Description: Program queries the teams and players tables using INNER JOIN in the pysports MySQL database.
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 
    
    #Connect to the pysports database
    db = mysql.connector.connect(**config)

    #Creating Cursor object
    cursor = db.cursor()

    #Selecting fields from player and team table using INNER JOIN
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player p INNER JOIN team t ON t.team_id = p.team_id")

    #Storing results from cursor.execute in variable
    playerTeam = cursor.fetchall()
    
    print("\n -- DISPLAYING PLAYER RECORDS --")

    #Iterating through variable storing query results and displaying the output
    for player in playerTeam:
        print(" Player Id: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()

'''
References:
GeeksforGeeks. (2020, November 9). SQL | Join (Inner, Left, Right and Full Joins). https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/
SQL - INNER JOINS - Tutorialspoint. (n.d.). Tutorialspoint.Com. Retrieved July 9, 2021, from https://www.tutorialspoint.com/sql/sql-inner-joins.htm
SQL INNER JOIN. (2020, February 26). W3resource. https://www.w3resource.com/sql/joins/perform-an-inner-join.php
SQL INNER JOIN: The Beginner’s Guide to Inner Join in SQL. (2020, April 4). SQL Tutorial. https://www.sqltutorial.org/sql-inner-join/
'''