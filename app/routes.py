from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/course/<course_id>')
def course(course_id):
    # Logic to retrieve course details from the database
    # You can use a database like SQLite or SQLAlchemy ORM
    # Return course details to the course template
    return render_template('course.html', course_id=course_id)
