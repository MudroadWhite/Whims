import re
import mysql.connector
from flask import Flask, render_template, request, flash, session, redirect, url_for, g
from flask_session import Session
import auth, blog, home, database
from bcrypt import hashpw, gensalt, checkpw

def test():
    # from database import Database
    # print("registering")
    # print(check_user_exists("abd"))
    # print(login("abd", "abd"))
    # print("done")
    pass