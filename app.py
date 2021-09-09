
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

###########################################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

    # reflect the tables
Base.prepare(engine, reflect =True)

Base.classes.keys()

session = Session(engine)

Station = Base.classes.station
Measurement = Base.classes.measurement


app = Flask(__name__)
###################################################################
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
#####################################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
   
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
    
######################################################################
@app.route("/api/v1.0/stations")
def stations():
    
    # recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    # return recent_date
    results = session.query(Station.id, Station.station, Station.name).all()

    all_stations = []
    for mid, mstation, mname in results:
            station_dict = {}
            station_dict["ID"] = mid
            station_dict["Station"] = mstation
            station_dict["Name"] = mname
            all_stations.append(station_dict)

    return_list = jsonify(all_stations)
    return return_list
 
##################################################################

@app.route("/api/v1.0/tobs")
def tobs():
    
    
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)


    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= year_ago).\
        filter(Measurement.station == "USC00519281").all()

  
    all_temps = []
    for mdate, mtemp in results:
            temp_dict = {}
            temp_dict["Date"] = mdate
            temp_dict["Temp"] = mtemp
            all_temps.append(temp_dict)
    
    
    return_list = jsonify(all_temps)
    return return_list
    session.close()
# ####################################################
# @app.route("/api/v1.0/startdate_only")   
# def summaryS():

#     start_date = (YYYY, M, DD)
#     end_date = (2017, 8, 23)


#  session.query(Measurement.station, 
#        func.min(Measurement.tobs), 
#        func.max(Measurement.tobs),
#        func.avg(Measurement.tobs)).\
#        filter(Measurement.date >= start_date).\
#        filter(Measurement.date <= end_date)

# @app.route("/api/v1.0/start_end_dates")   
# def summarySE():

#     start_date = (YYYY, M, DD)
#     end_date = (YYYY, M, DD)


#  session.query(Measurement.station, 
#        func.min(Measurement.tobs), 
#        func.max(Measurement.tobs),
#        func.avg(Measurement.tobs)).\
       
#        filter(Measurement.date >= start_date).\
#        filter(Measurement.date <= end_date)



session.close()

if __name__ == "__main__":
        # print(home())
    app.run(debug=True)
