
# 1. import Flask
from flask import Flask, jsonify

# %matplotlib inline
# from matplotlib import style
# style.use('fivethirtyeight')
# import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

##
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

    # reflect the tables
Base.prepare(engine, reflect =True)

Base.classes.keys()

session = Session(engine)

Station = Base.classes.station
Measurement = Base.classes.measurement


app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # return recent_date

    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).\
        order_by(Measurement.date).all()

    all_rain = []
    for mdate, mprcp in results:
            rain_dict = {}
            rain_dict["date"] = mdate
            rain_dict["prcp"] = mprcp
            all_rain.append(rain_dict)

    return_list = jsonify(all_rain)
    return return_list





#     engine = create_engine("sqlite:///../Resources/chinook.sqlite", echo=False)
#     Base = automap_base()
#     Base.prepare(engine, reflect=True)
#     Base.classes.keys()
#     Invoices = Base.classes.invoices
#     Items = Base.classes.invoice_items
#     session = Session(engine)
#     results = session.query(Invoices.BillingPostalCode, func.sum(Items.UnitPrice * Items.Quantity)).\
#         filter(Invoices.InvoiceId == Items.InvoiceId).\
#         filter(Invoices.BillingCountry == 'USA').\
#         group_by(Invoices.BillingPostalCode).\
#         order_by(func.sum(Items.UnitPrice * Items.Quantity).desc()).all()
#     session.close()
#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_bills = []
#     for zip, amount in results:
#         bill_dict = {}
#         bill_dict["postal_code"] = zip
#         bill_dict["amount"] = float(amount)
#         all_bills.append(bill_dict)
#     return_list = jsonify(all_bills)    
#     return return_list
# if __name__ == "__main__":
#     app.run())

if __name__ == "__main__":
        # print(home())
    app.run(debug=True)
