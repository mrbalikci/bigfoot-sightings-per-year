# needy libraries
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify

# Set up the Database - SQLite 

# get sqlite db in db folder 
engine = create_engine("sqlite:///db/bigfoot.sqlite")
# create the base 
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# save the references to a table 
BigFoot = Base.classes.bigfoot

# Create the session (link) from python to the db
session = Session(engine)


# Set up FLASK
app = Flask(__name__)

@app.route("/data")
def data():
    sel = [func.strftime("%Y", BigFoot.timestamp), func.count(BigFoot.timestamp)]
    results = session.query(*sel).\
        group_by(func.strftime("%Y", BigFoot.timestamp)).all()

    df = pd.DataFrame(results, columns=["months", "sightings"])
    return jsonify(df.to_dict(orient="records"))

@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, port=8080)
