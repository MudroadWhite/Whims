# Dependency: Flask, Mysql, Flask-SocketIO

import re
import mysql.connector
from flask import Flask, render_template, request, flash, session, redirect, url_for, g
# from flask_session import Session
from flask_socketio import SocketIO

from app import app, socketio

import auth, blog, home, database, contact, events
# from events import socketio_init
from bcrypt import hashpw, gensalt, checkpw
# from database import get_event_name, create_request_row, \
#     delete_request, create_pledge_row, create_donation_row, expire_request

# NOTE
#  已经覆盖Flask的基础教程！完善了Blog的功能！接下来需要做的大方向：
#  [ ] 设计button的template
#  [x] 寻找用flask做chat app的教程

# TODO
#  Problem on contact database design: user1 & user2's contacts should be bidirectional

# TODO
#  [x] Add SocketIO
#  [ ] (BOTTLENECK) Design basic buttons to record & submit music form
#       https://www.w3schools.com/js/js_validation.asp
#       https://www.w3schools.com/html/html_forms.asp
#  [ ] (BOTTLENECK) Add homepages for 3rd person viewing via contacts
#  [ ] (BOTTLENECK) Implement chat for contacts; Wire socketio to mainapp
#  [x] Test contacts main page
#  [ ] *Back button* for most pages
#  ----------------
#  [x] Design basic layout for base.html
#  [x] 完善主页功能
#  [ ] 设计base、登录/注册页面
#  ----------------
#  [ ] Client & Server? / 异步加载? / 更换框架？

# # 数据库设计

# Table chats(from_user, to_user, time, content)

@app.route("/")
def index():
    """显示首页"""
    if g.user is not None:
        return redirect(url_for("home.homepage"))
    else:
        return render_template("index.html")

# @socketio.on('test socket event')
# def test_callback(methods=['GET', 'POST']):
#     print("Received test socket event!")

def main():
    """Defines main function"""
    db = database.Database()
    db.database_init()
    db.close()
    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(contact.bp)
    app.add_url_rule("/", endpoint="index")
    # app.run()

    socketio.run(app)
    # socketio_init(app)



if __name__ == '__main__':
    # test()
    main()