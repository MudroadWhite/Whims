# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
import mysql.connector
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_session import Session
from bcrypt import hashpw, gensalt, checkpw
# from database import get_event_name, create_request_row, \
#     delete_request, create_pledge_row, create_donation_row, expire_request

app = Flask(__name__, template_folder="templates")
app.secret_key = "hfow875^&i3%3425tv9;2^$"

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

# Create a file called login.txt in the same directory as whims, line1 = user line2 = password
# login_file = open("../login.txt")
# login_info = login_file.read().splitlines()  # This creates a list [user, password]

# TODO
#  2. 搞好注册功能
#  3. 尝试基础登陆
#  4. 实现个人网页(登录)


# # 数据库设计

# 注册的数据：
# 账号名
# 密码

# 登录的数据：
# 账号名
# 密码

# 聊天记录：
# 账号1
# 账号2
# 时间
# 内容

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ygdvv1357",
    database="WHIMS"
)

@app.route("/")
def home():
    """显示首页"""
    return render_template("index.html")

@app.route('/showSignIn')
def show_sign_in():
    """渲染登录页面"""
    return render_template("signin.html")

@app.route('/showSignUp')
def show_sign_up():
    """渲染注册页面"""
    return render_template("signup.html")

@app.route('/showSignUp', methods=['POST'])
def get_sign_up():
    username = request.form["username"]
    psw = request.form["psw"]
    conf_psw = request.form["conf_psw"].encode('utf-8')
    data = [username, psw, conf_psw]

    if psw == conf_psw:
        my_cursor = mydb.cursor(buffered=True)
        my_cursor.execute("SELECT * FROM Users WHERE username = '{}'".format(username))
        count = len(my_cursor.fetchall())
        if count == 0:
            # Account does not exist
            sql = "INSERT INTO users (username, psw) VALUES (%s, %s)"
            val = (username, hashpw(psw, gensalt(12)))
            my_cursor.execute(sql, val)
            mydb.commit()
            flash("注册成功")
            # TODO: 找个个人网页
            return render_template("index.html")

        else:
            # Account does exist
            flash("账号已存在")
            return render_template("signUp.html")  # , data=data)
    flash("密码不相同")
    return render_template("index.html")

@app.route('/showSignIn', methods=['POST'])
def get_sign_in():
    """尝试登陆"""
    pass
#     # # Get info from form
#     # email = request.form['email']
#     # psw = request.form['psw'].encode('utf-8')
#     # db_name = None
#     #
#     # # query database table users for info
#     # my_cursor = mydb.cursor(buffered=True)
#     # my_cursor.execute("SELECT * FROM users WHERE email = '{}'".format(email))
#     # db_result = my_cursor.fetchall()
#     # for i in db_result:
#     #     db_pass = i[3].encode('utf-8')
#     # # check that passwords match
#     # if db_pass is not None:
#     #     if checkpw(psw, db_pass):
#     #         # Passwords match
#     #         session.permanent = False
#     #         session['name'] = db_name
#     #         session['login'] = True
#     #         return render_template("index.html")
#     #
#     # # Passwords don't match or user doesn't exist
#     # flash("Username or password is incorrect")
#     return render_template("signIn.html")

# @app.route('/logout')
# def logout():
#     """注销账户"""
#     '''session['name'] = None
#     session['login'] = False'''
#     session.clear()
#     return render_template("index.html")

def main():
    """Defines main function to be used by automated testing"""
    app.run()
    mydb.close()

if __name__ == '__main__':
    main()