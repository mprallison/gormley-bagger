from jinja2 import Environment, FileSystemLoader
import csv

env = Environment(loader=FileSystemLoader("templates"))

data_file = "data.csv"
user = "emily"
title = "emilyGormleyBagger"
filename = "gormley_map_emily.html"

#read gormley data and user field
#rename user field "status"
keys = ["id", "name", "year", "location", "latitude", "longitude", "url", user]

with open(data_file, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [
        {{user: "status"}.get(k, k): row[k] for k in keys} 
        for row in csv_reader
        ]


#render template
template = env.get_template("index.html")
html = template.render(title=title, data=data, user=user)

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)