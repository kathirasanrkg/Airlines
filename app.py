from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__) # initialize the Flask

@app.route("/") #URL
@app.route("/index")
def index():
    con=sql.connect("db_airline.db") #Connect to your DB
    con.row_factory=sql.Row #query results will behave like dictionaries you can access columns by name instead of by index.
    cur=con.cursor() #a pointer to one row in a set of rows
    cur.execute("SELECT * FROM airline")
    data=cur.fetchall() #retrieve all rows
    return render_template("index.html",datas=data)  #Renders an HTML template from the templates folder.
#datas=data passes a variable named datas into the template, and its value is the Python variable data.

@app.route("/add_airline",methods=['POST','GET'])
#POST method makes enables users to send data over to the server
#GET  method is used to retrieve data from the server. 
def add_airline():
    if request.method=='POST': #request - handle incoming data (form data, JSON, etc.) from the client side (GET, POST, etc.).
        flightnumber=request.form['flightnumber'] #column field key
        airline=request.form['airline']
        departurecity=request.form['departurecity']
        arrivalcity=request.form['arrivalcity']
        departuretime=request.form['departuretime']
        arrivaltime=request.form['arrivaltime']
        status=request.form['status']
        con=sql.connect("db_airline.db")
        cur=con.cursor()
        cur.execute("INSERT INTO airline(FLIGHTNUMBER,AIRLINE,DEPARTURECITY,ARRIVALCITY,DEPARTURETIME,ARRIVALTIME,STATUS) values (?,?,?,?,?,?,?)",(flightnumber,airline,departurecity,arrivalcity,departuretime,arrivaltime,status))
        con.commit()
        flash('airline Added','success') #notifications messages
        return redirect(url_for("index")) #Redirects to another URL (usually after form submission or an action).
    return render_template("add_airline.html")

@app.route("/edit_airline/<string:uid>",methods=['POST','GET']) #/<string:uid> - variable rule
def edit_airline(uid):
    if request.method=='POST':
        flightnumber=request.form['flightnumber'] #column field key
        airline=request.form['airline']
        departurecity=request.form['departurecity']
        arrivalcity=request.form['arrivalcity']
        departuretime=request.form['departuretime']
        arrivaltime=request.form['arrivaltime']
        status=request.form['status']
        con=sql.connect("db_airline.db")
        cur=con.cursor()
        cur.execute("UPDATE airline SET FLIGHTNUMBER=?,AIRLINE=?,DEPARTURECITY=?,ARRIVALCITY=?,DEPARTURETIME=?,ARRIVALTIME=?,STATUS=? WHERE UID=?",(flightnumber,airline,departurecity,arrivalcity,departuretime,arrivaltime,status,uid))
        con.commit()
        flash('airline Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("db_airline.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM airline where UID=?",(uid,))
    data=cur.fetchone() #fetch individual data
    return render_template("edit_airline.html",datas=data)
    
@app.route("/delete_airline/<string:uid>",methods=['GET'])
def delete_airline(uid):
    con=sql.connect("db_airline.db")
    cur=con.cursor()
    cur.execute("DELETE FROM airline WHERE UID=?",(uid,))
    con.commit()
    flash('airline Deleted','warning')
    return redirect(url_for("index")) 
    
app.secret_key='admin123' #session should be available
app.run(debug=True) #run the app in debugging mode