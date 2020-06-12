import requests
import json
import search
import time

session = requests.session()
found = False
data = {}

with open('config.json') as f:
  data = json.load(f)

session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

while not found:
    found = search.doIt(session, data)
    time.sleep(40)