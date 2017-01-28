#! venv/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 pavle <pavle@hp-arch>
#
# Distributed under terms of the MIT license.

"""

"""

import os
from flask import Flask, request, session, render_template

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def index():
    return '<h1 style="color:blue">Hello There!</h1>'

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
