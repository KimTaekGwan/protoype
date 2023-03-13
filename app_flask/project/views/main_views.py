# myproject/sesac/views/post_views.py
from flask import url_for, request, redirect, Blueprint, render_template
from project.conn.db import db

import os

bp = Blueprint('main_views', __name__, url_prefix='/')

path_data = '../data'

@bp.route('/')  
def main():
    return render_template("pages/main.html")  
    # return redirect(url_for('main_views.upload'))


@bp.route('/upload')  
def upload():
    print(os.listdir(path_data))
    # print(path_cwd)
    return render_template("pages/file_upload_form.html")  


@bp.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST':
        return render_template("pages/success.html")