# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

__all__ = ['BP_SITE']

BP_SITE = Blueprint('site', __name__)
app = BP_SITE


@app.route('/')
def index():
    return render_template('index.html')
