# -*- coding: utf8 -*-

from __future__ import unicode_literals
from os import environ

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(debug=True,
            host='0.0.0.0',
            port=port)

