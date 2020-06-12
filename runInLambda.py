import requests
import json
import search

session = requests.session()

with open('config.json') as f:
  data = json.load(f)

def my_handler(event, context):
    search.doIt(session, data)

