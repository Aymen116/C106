import plotly.express as px
import csv
import numpy as nm
from ast import Num
from statistics import correlation
def getDataSource(datapath):
    coffee = []
    sleep = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x": coffee, "y": sleep}
def findCorrelation(datasource):
    correlation = nm.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "data4.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)
setup()