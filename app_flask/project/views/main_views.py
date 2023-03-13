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


@bp.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # print('file 저장')
        f = request.files['file']
        path_input = '../data/input/'
        
        path = path_input + f.filename
        f.save(path)
        
        file_list = os.listdir(path_input)
        file_list = [file for file in file_list if not file.endswith(".md")]
        file_dict = {file:path_input+file for file in file_list}
        
        return render_template("pages/file_upload_form.html", file_dict=file_dict)  
    else:
        return render_template("pages/file_upload_form.html")  


@bp.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST':
        return render_template("pages/success.html")