from ast import Num
from statistics import correlation
import plotly.express as px
import csv
import numpy as np
def getDataSource(datapath):
    marks = []
    days = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x": marks,"y": days}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "data3.csv"
    datasource = getDataSource(datapath)
    findCorrelation(datasource)
setup()
