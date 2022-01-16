import plotly.express as px
import csv
with open("data2.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df,x="Size of TV",y="Time")
    figure.show()