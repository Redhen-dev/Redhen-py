from flask import render_template, url_for, flash, redirect
from redhen.forms import RegisterForm
from redhen.models import Comic, Page, Tag, Author, Language
from redhen import app

@app.route('/')
def index():
    return render_template('index.html')