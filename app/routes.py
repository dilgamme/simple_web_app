from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/students')
def students():
    return render_template('students.html')
    
@app.route('/workshop')
def workshop():
    return render_template('workshop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
