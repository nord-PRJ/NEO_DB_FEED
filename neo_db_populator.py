import requests
import json
import datetime

#DB SETUP
import sqlite3
conn = sqlite3.connect('NEO_ALL.db')

c = conn.cursor()
#END DB SETUP


'''
If using DEMO_KEY as API KEY you are limited to 7 days per request
'''
# start date format yyyy-mm-dd
# end date   format yyyy-mm-dd

def get_data(start_date, end_date):
    response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date={0}&end_date={1}&api_key=DEMO_KEY".format(start_date,end_date))
    data = json.loads(response.content.decode())
    return data

def populate_db():
    pass






data = get_data("2017-07-19","2017-07-25")

element_count = data["element_count"]
neos = data["near_earth_objects"]

# print("Element Count: ",element_count)
# print("Near Earth Objects: ",json.dumps(neos, indent=4))

# print(get_data("2017-07-19","2017-07-25"))
