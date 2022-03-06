import mysql.connector
from bcrypt import checkpw, hashpw, gensalt

db_username = "root"
# TODO: read password & username from some txt
db_passwd = "ygdvv1357"
db_dbname = "whims"

class Database:
    def __init__(self):  # ok
        # Create a file called login.txt in the same directory as whims, line1 = user line2 = password
        # login_file = open("../login.txt")
        # login_info = login_file.read().splitlines()  # This creates a list [user, password]
        self.db = mysql.connector.connect(
            host="localhost",
            user=db_username,
            password=db_passwd,
            database=db_dbname
        )
        self.cursor = self.db.cursor(buffered=True)

    def get_db(self):  # ok
        return self.db

    def database_init(self):  # ok
        self.create_users_table()
        self.create_blog_table()

    def close(self):  # ok
        self.db.close()

    def create_users_table(self):  # ok
        self.cursor.execute("CREATE TABLE IF NOT EXISTS whims.users ("
                       "id INTEGER PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255))")
        self.db.commit()

    def register_user(self, name, passwd):  # ok
        """Register a user and password into database"""
        # TODO: unique check? or assume uniqueness?
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.cursor.execute(query, (name, passwd))
        self.db.commit()

    def check_user_exists(self, name):  # ok
        """Check if a user already exists in the database"""
        query = "SELECT * FROM users WHERE username = '{u}'".format(u=name)
        self.cursor.execute(query)
        self.db.commit()
        count = len(self.cursor.fetchall())
        return True if count > 0 else False

    def login(self, name, passwd):  # ok
        """Check if a passwd matches the username in the database"""
        query = "SELECT * FROM users WHERE username = '{u}' AND password = '{p}'".format(u=name, p=passwd)
        self.cursor.execute(query)
        self.db.commit()
        count = len(self.cursor.fetchall())
        return True if count >= 0 else False

    def create_blog_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS whims.blog ("
                       "id INTEGER PRIMARY KEY AUTO_INCREMENT, author_id INTEGER NOT NULL, title TEXT, body TEXT NOT NULL,"
                       "FOREIGN KEY (author_id) REFERENCES whims.users (id))")
        self.db.commit()
