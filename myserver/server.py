#-*- coding:utf8 -*-
from flask import Flask, render_template
from logging import FileHandler
import logging
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
try:
    file_handler = FileHandler("/home/prudentiae/web/web.log")
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
except:
    pass

@app.route('/')
def main():
    return render_template("main.html")


@app.route('/mighty/')
def mighty():
    return render_template("mighty.html")
