from bs4 import BeautifulSoup
from sendMail import sendmail 
import datetime
from pytz import timezone
import json

def isAvailable(text, url, data):

    soup = BeautifulSoup(text, 'html.parser',)
    for snippet in soup.find_all(attrs={data['search']['attr']['Name'] : data['search']['attr']['Value'] }):
        if data['search']['contains'] in str(snippet):
            sendmail(data['smtp'], str(snippet), url)
            print("WUHUUU:")
            return True
    return False

def doIt(session, data):
    print(datetime.datetime.now(timezone('Europe/Berlin')))

    r = session.get("http://httpbin.org/ip" )
    print(r.text)

    for url in data['URLs']:
        print(url)
        
        try:
            response = session.get(url)
            found = isAvailable(response.text, url, data)
            print("response code: {}".format(response.status_code))
            if found:
                return found
        except Exception as exc:
            print("Oops! Try again next time. {0}".format(exc))
        
    return False