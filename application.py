import mysql.connector
from flask import Flask,render_template,request

conn=mysql.connector.connect(host="database-1.c42j88fwzfpr.us-east-2.rds.amazonaws.com",user="admin",password="admin1234",database="moviedb")

mycursor=conn.cursor()

application=Flask(__name__)

@application.route('/')
def index():
	mycursor.execute("SELECT * FROM movies")
	data=mycursor.fetchall()
	return render_template('index.html', data=data)

@application.route('/add')
def add():

	return render_template('addmovie.html')

@application.route('/insert', methods=['POST'])
def insert():
	name=request.form.get('name')
	actor=request.form.get('actor')
	year=request.form.get('year')
	poster=request.form.get('poster')

	mycursor.execute("INSERT INTO movies (id,name,actor,year,poster) VALUES (NULL,'{}','{}','{}','{}')".format(name,actor,year,poster))

	conn.commit()

	return render_template('addmovie.html')



if __name__=="__main__":
	application.run(debug=True)




