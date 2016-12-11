#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


target = raw_input("Enter Address : ")


if ('http' in target):
    print ("Start")
    print ("take long time Scaning 1024 - 65535 Port...")
    for i in range(1,10000):
        site = target + ":" + str(i)
        try:
            r = requests.get(site,timeout=1)
            if (r.status_code ==200):
                print site
                bs = BeautifulSoup(r.text)
                print bs.title

        except:
            pass

else:
    target = "http://"+target
    print ("Please Enter Url With Http:// or Https://")
    print "Example : " + target



