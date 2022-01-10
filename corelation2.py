import plotly.express as px
import csv 
import numpy as np

def getDataSource(data):
    coffee_ml = []
    sleep = []
    with open(data) as f:
        df = csv.DictReader(f)
        for row in df:
            coffee_ml.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee_ml,"y":sleep}

def corelation(dataSource):
    corr = np.corrcoef(dataSource["x"],dataSource["y"])
    print("CORRELATION BETWEEN COFFEE AND SLEEP-",corr[0,1])

def setup():
    data = "cups of coffee vs hours of sleep.csv"

    dataSource = getDataSource(data)
    corelation(dataSource)

setup()