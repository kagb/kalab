# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

__all__ = ['BP_LAB']

BP_LAB = Blueprint('lab', __name__)


@BP_LAB.route('/fishing_qq')
def fishing_qq():
    return render_template('lab/fishing_qq.html')

@BP_LAB.route('/weibo_word_cloud')
def weibo_word_cloud():
    return render_template('lab/fishing_qq.html')
