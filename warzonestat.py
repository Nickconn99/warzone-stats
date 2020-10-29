import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import re


foundUser = 0

while foundUser < 1:
    try:
        inputname = input('Please enter activision username: (username#number) ')
        username, activnum = inputname.split('#')
        foundUser = 1
    except:
        print("Invalid Username! (make sure to use the format: username#number)")
        foundUser = 0
    try:
        if foundUser == 1:
            buildurl = "https://cod.tracker.gg/warzone/profile/atvi/" + username + '%23' + activnum + "/overview"
            page = requests.get(buildurl)
            t = page.text
            kdlocation = 0
            location = 'K\u002FD Ratio'
            kdlocation = t.find(location)
            location1 = 'Wins","displayCategory":"Game","category":"game","metadata":{},"value":'
            winlocation = t.find(location1)
            win = (t[winlocation+90:winlocation+94])
            kd = (t[kdlocation+101:kdlocation+105])

            if win[2] == '"':
                win = win[:-1]

            if kd.find("d>") != -1:
                kd = kd + 1

            print("KD RATIO:", kd)
            print("WINS:", ''.join(e for e in win if e.isalnum()))
        foundUser = 0
    except:
        print("User Not Found!")
        foundUser = 0
