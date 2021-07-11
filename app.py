from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as sql
import pandas as pd
import sqlite3
#import pyodbc 
import sqlalchemy as sa
import pymysql

target = sa.create_engine(f'mysql://sql6423797:uunBv5sHVq@sql6.freemysqlhosting.net/sql6423797')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files['inputFile']
        if '.xlsx' in file.filename:
            table = pd.read_excel(file)
            table.columns = table.columns.str.replace(' ', '_')
            table.to_sql(name= file.filename, con=target, if_exists='replace')
        if '.csv' in file.filename:
            table = pd.read_csv(file)
            table.columns = table.columns.str.replace(' ', '_')
            table.to_sql(name= file.filename, con=target, if_exists='replace')

        return 'File uploaded'

if __name__ == '__main__':
    app.run(debug=True)