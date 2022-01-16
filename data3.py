import plotly.express as px
import csv
with open("data3.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x="Marks In Percentage",y="Days Present")
    figure.show()