import mysql.connector
from bcrypt import checkpw, hashpw, gensalt

db_username = "root"
# TODO: read password & username from some txt
db_passwd = "ygdvv1357"
db_dbname = "whims"

# TODO:
#  [ ] Record publish timestamp for blog posts

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
        self.cursor = self.db.cursor(buffered=True, dictionary=True)

    def get_db(self):  # ok
        return self.db

    def database_init(self):  # ok
        self.create_users_table()
        self.create_blog_table()
        self.create_contacts_table()

    def close(self):  # ok
        self.db.close()

    def create_users_table(self):  # ok
        self.cursor.execute("CREATE TABLE IF NOT EXISTS whims.users ("
                       "id INTEGER PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255))")
        self.db.commit()

    def create_contacts_table(self):  # ok
        self.cursor.execute("CREATE TABLE IF NOT EXISTS whims.contacts ("
         "id INTEGER PRIMARY KEY AUTO_INCREMENT, user1_id INTEGER NOT NULL, user2_id INTEGER NOT NULL,"
         "FOREIGN KEY (user1_id) REFERENCES whims.users (id), FOREIGN KEY (user2_id) REFERENCES whims.users (id))")
        self.db.commit()

    def create_blog_table(self):  # ok
        self.cursor.execute("CREATE TABLE IF NOT EXISTS whims.blog ("
                       "id INTEGER PRIMARY KEY AUTO_INCREMENT, author_id INTEGER NOT NULL, title TEXT, body TEXT NOT NULL,"
                       "FOREIGN KEY (author_id) REFERENCES whims.users (id))")
        self.db.commit()

    #############################

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

    def get_user_id_from_name(self, name):
        query = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(query, (name,))
        self.db.commit()
        result = self.cursor.fetchone()
        return result['id']

    def get_name_from_id(self, id):
        query = "SELECT * FROM users WHERE id = {i}".format(i=id)
        self.cursor.execute(query)
        self.db.commit()
        result = self.cursor.fetchone()
        return result['username']

    def login(self, name, passwd):  # ok
        """Check if a passwd matches the username in the database"""
        query = "SELECT * FROM users WHERE username = '{u}' AND password = '{p}'".format(u=name, p=passwd)
        self.cursor.execute(query)
        self.db.commit()
        count = len(self.cursor.fetchall())
        return True if count >= 0 else False

    #############################

    def create_post(self, title, body, author_id):  # ok
        query = "INSERT INTO whims.blog (title, body, author_id)"\
                "VALUES (%s, %s, {i})".format(i=author_id)
        self.cursor.execute(query, (title, body))
        self.db.commit()

    # TODO: (Future) async, start_from+range
    def get_all_posts(self, au_id):  # ok
        query = "SELECT b.title, b.body, u.username, b.id " \
                "FROM whims.blog AS b, whims.users as u " \
                "WHERE b.author_id = u.id AND u.id = {s}".format(s=au_id)
        self.cursor.execute(query)
        self.db.commit()
        result = self.cursor.fetchall()
        return result

    def get_post(self, blog_id): # temporal update post.... reuse client data in the future
        query = "SELECT title, body FROM whims.blog WHERE id={s}".format(s=blog_id)
        self.cursor.execute(query)
        self.db.commit()
        result = self.cursor.fetchall()
        return result

    # def get_posts(self, au_id, starts_with, range): # Async loading

    def update_post(self, title, body, blog_id):  # ok
        query = "UPDATE whims.blog SET title=%s, body=%s WHERE id={i}".format(i=blog_id)
        self.cursor.execute(query, (title, body))
        self.db.commit()

    def delete_post(self, blog_id):  # ok
        query = "DELETE FROM whims.blog WHERE id={i}".format(i=blog_id)
        self.cursor.execute(query)
        self.db.commit()

    def get_all_contacts(self, user_id):  # ok
        query = "SELECT user2_id FROM whims.contacts WHERE user1_id={i}".format(i=user_id)
        self.cursor.execute(query)
        self.db.commit()
        result = self.cursor.fetchall()
        return result

    def delete_contact(self, user1_id, user2_id):
        pass