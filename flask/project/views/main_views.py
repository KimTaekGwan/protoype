# myproject/sesac/views/post_views.py
from flask import url_for, request, redirect, Blueprint, render_template

from project.db import db
bp = Blueprint('main_views', __name__, url_prefix='/')

@bp.route('/')  
def main():  
    return redirect(url_for('main_views.upload'))


@bp.route('/upload')  
def upload():  
    return render_template("pages/file_upload_form.html")  


@bp.route('/success', methods = ['POST'])  
def success():
    if request.method == 'POST':
        return render_template("pages/success.html")