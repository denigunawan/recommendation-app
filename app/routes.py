from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import pandas as pd
from app.models import save_to_db, DaftarPerusahaan, Sector, save_to_db_sectors
import os
from werkzeug.utils import secure_filename

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/')
def home():
    return render_template('index.html')

@api_bp.route('/login')
def login():
    return render_template('login.html')

@api_bp.route('/company')
def company():
    table_data = DaftarPerusahaan.query.all()
    return render_template('company.html', table_data=table_data)

@api_bp.route('/company/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not file.filename.endswith('.csv'):
            flash('Invalid file format. Please upload a CSV file.')
            return redirect(request.url)
        try:
            filename = secure_filename(file.filename)
            upload_folder = current_app.config.get('UPLOAD_FOLDER', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            df = pd.read_csv(filepath)
            save_to_db(df)
            flash("File successfully uploaded and data saved!", "success")
            return redirect(url_for('api_bp.company'))
        except Exception as e:
            flash(f'Error: {str(e)}')
            return redirect(request.url)

    return render_template('company.html')

@api_bp.route('/sector')
def sectors():
    table_data = Sector.query.all()
    return render_template('sectors.html', table_data=table_data)

@api_bp.route('/sector/upload', methods=['GET', 'POST'])
def upload_file_sectors():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not file.filename.endswith('.csv'):
            flash('Invalid file format. Please upload a CSV file.')
            return redirect(request.url)
        try:
            filename = secure_filename(file.filename)
            upload_folder = current_app.config.get('UPLOAD_FOLDER', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            df = pd.read_csv(filepath)
            save_to_db_sectors(df)
            flash("File successfully uploaded and data saved!", "success")
            return redirect(url_for('api_bp.sectors'))
        except Exception as e:
            flash(f'Error: {str(e)}')
            return redirect(request.url)
    return render_template('sectors.html')

