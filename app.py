from jinja2 import Environment, FileSystemLoader
import csv

env = Environment(loader=FileSystemLoader("templates"))

#read data as jsonl
with open("data.csv", mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

#declare title
title = "gormleyBagger"
filename = "gormley_map.html"

#render template
template = env.get_template("index.html")
html = template.render(title=title, data=data)

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)