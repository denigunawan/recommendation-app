from flask import Blueprint, render_template

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/')
def home():
    return render_template('index.html')

@api_bp.route('/login')
def login():
    return render_template('login.html')

@api_bp.route('/company')
def company():
    return render_template('company.html')
