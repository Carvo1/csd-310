""" 
    Title: pysports_queries.py
    Author: Steffan Hinkle
    Date: 4 July 2021
    Description: Program queries the teams and players tables of the pysports MySQL database.
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

    #Selecting fields from team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #Storing results from cursor.execute in variable
    teamInfo = cursor.fetchall()

    print("\n -- DISPLAYING TEAM RECORDS --")

    #Iterating through variable storing query results and displaying the output
    for team in teamInfo:
        print(" Team Id: {}\n Team Name: {}\n Mascot {}\n".format(team[0], team[1], team[2]))


    #Selecting fields from player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #Storing results from cursor.execute in variable
    playerInfo = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS --")

    #Iterating through variable storing query results and displaying the output
    for player in playerInfo:
        print(" Player Id: {}\n First Name: {}\n Last Name {}\n Team Id {}\n".format(player[0], player[1], player[2], player[3]))

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
