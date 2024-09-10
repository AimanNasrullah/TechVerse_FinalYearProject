from flask import Blueprint, render_template

# define blueprint of the application
views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template('index.html')

