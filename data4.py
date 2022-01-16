import plotly.express as px
import csv
with open("data4.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x="Coffee in ml", y="sleep in hours")
    figure.show()