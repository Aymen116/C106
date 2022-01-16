import plotly.express as px
import csv
import numpy as nm
from ast import Num
from statistics import correlation
def getDataSource(datapath):
    size = []
    time = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            size.append(float(row["Size of TV"]))
            time.append(float(row["Time"]))
    return {"x": size, "y": time}
def findCorrelation(datasource):
    correlation = nm.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "data2.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)
setup()