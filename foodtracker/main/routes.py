from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'blueprint test'

@main.route('/add')
def add():
    pass

@main.route('/view')
def view():
    pass
