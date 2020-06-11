from bs4 import BeautifulSoup
import time
import requests
import json
from sendMail import sendmail 
import datetime
from pytz import timezone

session = requests.session()

with open('config.json') as f:
  data = json.load(f)

def isAvailable(text):

    soup = BeautifulSoup(text, 'html.parser')
    for snippet in soup.find_all(attrs={data['search']['attr']['Name'] : data['search']['attr']['Value'] }):
        if data['search']['contains'] in str(snippet):
            sendmail(data['smtp'], str(snippet))
            print("WUHUUU:")

def my_handler(event, context):
    print(datetime.datetime.now(timezone('Europe/Berlin')))

    r = session.get("http://httpbin.org/ip" )
    print(r.text)

    for url in data['URLs']:
        print(url)
        
        try:
            response = session.get(url)
            isAvailable(response.text)
            print("response code: {}".format(response.status_code))
        except Exception as exc:
            print("Oops! Try again next time. {0}".format(exc))

