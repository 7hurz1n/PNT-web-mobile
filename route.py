from main import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/2')
def page2():
    return render_template('page2.html')

@app.route('/3')
def page3():
    return render_template('page3.html')

@app.route('/4')
def page4():
    return render_template('page4.html')