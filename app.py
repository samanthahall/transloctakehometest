from flask import Flask, render_template, make_response
import collections
import csv
import json

app = Flask(__name__)

with open("data/GeoLiteCityv6.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    latlngs = []
    for row in readCSV:
        lat = row[7]
        lng = row[8]
        latlng = (lat, lng)
        latlngs.append(latlng)
    counter = collections.Counter(latlngs)
    uniquelatlngs = []
    for latlng, quantity in counter.items():
        uniquelatlngs.append([latlng[0], latlng[1], quantity])

@app.route("/ipv6latlngs")
def get_latlngs():
    dumped = json.dumps({
        'points': uniquelatlngs
    }, indent=4)
    response = make_response(dumped)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/")
def start_map(): 
    return render_template("index.html")

if __name__ == '__main__':
    #app.debug = True
    app.run()