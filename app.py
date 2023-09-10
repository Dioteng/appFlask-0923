from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "my-secret-key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/ride4cast'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Creating model table for our CRUD database
class Bus(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bus_number = db.Column(db.String(100))
    plate_number = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    date_added = db.Column(db.DateTime, default = datetime.now)
  
    def __init__(self, bus_number, plate_number, capacity, date_added):
        self.bus_number = bus_number
        self.plate_number = plate_number
        self.capacity = capacity
        self.date_added = date_added

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)