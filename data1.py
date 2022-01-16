import plotly.express as px
import csv
with open("data.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df,x = "Temperature", y = "Ice-cream Sales")
    figure.show()