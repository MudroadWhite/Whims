import mysql.connector
from bcrypt import checkpw, hashpw, gensalt

db_username = ""
db_password = ""
db_dbname = ""

# TODO: make a class
mydb = mysql.connector.connect(
    host="localhost",
    user=db_username,
    password=db_passwd,
    database=db_dbname
)

my_cursor = mydb.cursor(buffered=True)


def create_users_table():
    """Creates an empty table called users that stores emails and passwords"""
    my_cursor.execute("CREATE TABLE IF NOT EXISTS users ("
                      "username VARCHAR(255), password VARCHAR(255)")
    mydb.commit()


def register_user(name, passwd):
    """Register a user and password into database"""
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    my_cursor.execute(query, (name, passwd))
    mydb.commit()


def login(name, passwd):
    """Check if a passwd matches the username in the database"""
    query = "SELECT * FROM users WHERE username = '{u}' AND passwd = '{p}'".format(u=username, p=passwd)
    my_cursor.execute(query)
    count = len(my_cursor.fetchall())
    return True if count >= 0 else False