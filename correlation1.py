import plotly.express as px
import csv
import numpy as nm
from ast import Num
from statistics import correlation
def getDataSource(datapath):
    temp = []
    sold = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            temp.append(float(row["Temperature"]))
            sold.append(float(row["Ice-cream Sales"]))
    return {"x": temp, "y": sold}
def findCorrelation(datasource):
    correlation = nm.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "data1.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)
setup()