from sqlalchemy import create_engine, text
from datetime import datetime

engine = create_engine("mysql+mysqlconnector://root:@localhost/ride4cast")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM bus"))
    for row in result:
        print(row)