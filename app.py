from flask import Flask, render_template, jsonify, after_this_request
import sqlalchemy
import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/fruits_db"
# mongo = PyMongo(app)

# SQLAlchemy Setup
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS, False']
DATABASE_URI = "postgres://postgres:postgres@localhost:5432/Tornadoes_USA"

db = create_engine(DATABASE_URI)

results = db.execute("SELECT * FROM tornadoes")

# for r in results:
#     return jsonify(r)

@app.route("/")
def api_call():

    return jsonify(results)
#     return render_template('index.html')



# @app.route("/API_tornadoes", methods=['GET'])
# def index():
#     session = Session(engine)

#     # row = session.query(tornadoes.Date, tornadoes.State, tornadoes.'Starting Latitude').all()

#     # row = db.tornadoes.find({})
#     data = []
#     for x in row:
#         data.append({'Date' : x['Date'], 'State' : x['State'], 'Starting Latitude' : x['Starting Latitude']})

#     return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)