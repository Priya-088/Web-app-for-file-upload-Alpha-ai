from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as sql
import pandas as pd
import sqlite3
import pyodbc 
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
        table = pd.read_excel(file)
        table.columns = table.columns.str.replace(' ', '_')
        table.to_sql(name= file.filename, con=target, if_exists='replace')
        return 'File uploaded'

if __name__ == '__main__':
    app.run(debug=True)

 #Fetching the data from database   

target =  sql.connect(host = 'sql6.freemysqlhosting.net' ,user='sql6423797',password = 'uunBv5sHVq', database = 'sql6423797')

mycursor = target.cursor()
mycursor.execute('Select * from `Alphaa Superstore Nov 2020.xlsx`')
records = mycursor.fetchall()
type(records)
df = pd.DataFrame(data = records, columns=['index','DaystoShipActual','ShipStatus','DaystoShipScheduled','Category','City','Country','CustomerName','DiscountPercent','OrderDate', 'OrderID','Sales Person','PostalCode',	'ProductId','ProductName','Profit','Quantity','Region','Returned','ProfitperOrder','Sales','Segment','ShipDate','ShipMode','State','SubCategory'])
df.head()
del df['index']
df.head()



















    