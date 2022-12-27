import csv
import pandas as pd

all_articles = []
data1 = pd.read_csv("trial.csv")
with open('trial.csv',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
    all_articles = data[1:]
data_dict = data1.to_dict()
liked_articles= []
unliked_articles = []
did_not_read = []