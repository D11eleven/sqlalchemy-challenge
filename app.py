
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




engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect =True)

Base.classes.keys()

session = Session(engine)

Station = Base.classes.station
Measurement = Base.classes.measurement




# # 2. Create an app, being sure to pass __name__
# app = Flask(__name__)


# # 3. Define what to do when a user hits the index route
# @app.route("/")
# def home():
#     print("Server received request for 'Home' page...")
#     return "Welcome to my 'Home' page!"


# # 4. Define what to do when a user hits the /about route
# @app.route("/about")
# def about():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"

# @app.route("/jsonified")
# def jsonified():
#     return jsonify(hello_dict)

if __name__ == "__main__":
        print(home())
#     app.run(debug=True)
