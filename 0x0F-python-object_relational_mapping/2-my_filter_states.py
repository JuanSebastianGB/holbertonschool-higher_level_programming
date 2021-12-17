#!/usr/bin/python3
"""[script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument]
    """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """[Main function]
    """
    MY_USER = argv[1]
    MY_PWD = argv[2]
    MY_DB = argv[3]

    db = MySQLdb.connect(user=MY_USER, passwd=MY_PWD, db=MY_DB)
    cur = db.cursor()
    cur.execute(f"""SELECT id, name FROM states WHERE name
                like "%{argv[4]}%" ORDER BY states.id ASC""")
    result = cur.fetchall()
    [print(row) for row in result]
    cur.close()
    db.close()
