from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# import sqlite3 as sql
from flaskext.mysql import MySQL

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'db_test'

mysql = MySQL()
mysql.init_app(app)   

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_student():
   return render_template('student.htm')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      nm = request.form['nm']
      addr = request.form['add']
      city = request.form['city']
      zip = request.form['zip']
      
      # cur = mysql.connection.cursor()
      conn = mysql.connect()
      cur = conn.cursor()
      cmd = "INSERT INTO students (name,addr,city,zip) VALUES ('{0}','{1}','{2}','{3}')".format(nm,addr,city,zip)

      cur.execute(cmd)
      conn.commit()
      conn.close()
      msg = "Successful"
      return render_template("output.htm",msg = msg)


@app.route('/list')
def list():
   # con = mysql.connect("db_test.db")
   # con.row_factory = sql.Row
   
   # cur = con.cursor()

   conn = mysql.connect()
   cur = conn.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   print(rows)
   conn.close()
   return render_template("list.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)