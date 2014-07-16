#-*- coding:utf8 -*-
from flask import Flask, render_template
from logging import FileHandler
import logging
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
try:
    file_handler = FileHandler("/prudentiae/web/web.log")
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
except:
    pass

@app.route('/')
def main():
    return "Hello World"
