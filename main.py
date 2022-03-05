# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
import mysql.connector
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_session import Session
import auth
from bcrypt import hashpw, gensalt, checkpw
# from database import get_event_name, create_request_row, \
#     delete_request, create_pledge_row, create_donation_row, expire_request

app = Flask(__name__, template_folder="templates")
app.secret_key = "hfow875^&i3%3425tv9;2^$"

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

# TODO
#  [ ] Test 基础登陆
#  [ ] 设计个人网页
#  [ ] 弄懂template设计
#  ----------------
#  [ ] Client & Server? / 异步加载?

# # 数据库设计

# 聊天记录：
# 账号1
# 账号2
# 时间
# 内容

@app.route("/")
def home():
    """显示首页"""
    return render_template("index.html")

# @app.route('/showSignUp', methods=['POST'])
# def get_sign_up():
#     username = request.form["username"]
#     psw = request.form["psw"]
#     conf_psw = request.form["conf_psw"].encode('utf-8')
#     data = [username, psw, conf_psw]
#
#     if psw == conf_psw:
#         # TODO: switch to database.py functions
#         my_cursor = mydb.cursor(buffered=True)
#         my_cursor.execute("SELECT * FROM Users WHERE username = '{}'".format(username))
#         count = len(my_cursor.fetchall())
#         if count == 0:
#             # Account does not exist
#             sql = "INSERT INTO users (username, psw) VALUES (%s, %s)"
#             val = (username, hashpw(psw, gensalt(12)))
#             my_cursor.execute(sql, val)
#             mydb.commit()
#             flash("注册成功")
#             # TODO: 找个个人网页
#             return render_template("index.html")
#
#         else:
#             # Account does exist
#             flash("账号已存在")
#             return render_template("signUp.html")  # , data=data)
#     flash("密码不相同")
#     return render_template("index.html")

def main():
    """Defines main function to be used by automated testing"""
    app.register_blueprint(auth.bp)
    app.add_url_rule("/", endpoint="index")
    app.run()

def test():
    # from database import Database
    # print("registering")
    # print(check_user_exists("abd"))
    # print(login("abd", "abd"))
    # print("done")
    pass

if __name__ == '__main__':
    # test()
    main()