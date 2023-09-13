#app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)
app.secret_key = "my-secret-key"
  
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/ride4castdb'
                                        #mysql+pymysql://username:passwd@host/databasename 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app)
  
#Creating model tables for our CRUD database
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    position = db.Column(db.String(100))
  
    def __init__(self, name, email, phone, position):
        self.name = name
        self.email = email
        self.phone = phone
        self.position = position

class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_number = db.Column(db.String(50), nullable=False)
    route = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __init__(self, bus_number, route, capacity):
        self.bus_number = bus_number
        self.route = route
        self.capacity = capacity

#query on all employees and bus data
@app.route('/')
def Index():
    all_employee_data = Employee.query.all()
    all_bus_data = Bus.query.all()
    return render_template("index.html", employees=all_employee_data, buses=all_bus_data)
  
#insert data to mysql database via html forms
@app.route('/insert_emp', methods = ['POST'])
def insert_emp():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        position = request.form['position']
  
        my_data1 = Employee(name, email, phone, position)
        db.session.add(my_data1)
        db.session.commit()
  
        flash("Employee Inserted Successfully")
        return redirect(url_for('Index'))

@app.route('/insert_bus', methods = ['POST'])
def insert_bus():
    if request.method == 'POST':
        bus_number = request.form['bus_number']
        route = request.form['route']
        capacity = request.form['capacity']
  
        my_data2 = Bus(bus_number, route, capacity)
        db.session.add(my_data2)
        db.session.commit()
  
        flash("Bus Inserted Successfully")
        return redirect(url_for('Index'))


#update data
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Employee.query.get(request.form.get('id'))
  
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
  
        db.session.commit()
        flash("Employee Updated Successfully")
        return redirect(url_for('Index'))
  
#delete data
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Employee.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('Index'))
  
if __name__ == "__main__":
    app.run(debug=True)