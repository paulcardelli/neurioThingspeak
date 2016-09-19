#!/usr/bin/python
#

import csv
import urllib2
import os
import requests
from time import sleep
from time import strftime

#IP address of Neurio
neurioip = "192.168.254.17"  #Change to IP address of your Neurio Sensor

#ThingspeakAPIKEY
TSAPIKEY = '1234ABC'

#CSV file Path
pvpath = "/home/pi/"

#count for each second out of a minute
count = 60

#define posting to ThingSpeak
def update_thingspeak( payload ):
  baseurl = "https://api.thingspeak.com/update?api_key=%TSAPIKEY"  #needs to be tested
  f = urllib2.urlopen(baseurl + payload)
  print f.read()
  f.close()

#def write2CSV(date, payload)



while count > 0:

        #status DATE  yyyymmdd
        pvdate = strftime('%Y%m%d')

        #status TIME  24 HH:MM
        pvtime = strftime('%H:%M')

        #pull json from local neurio sensor json
        pvdata = requests.get('http://'+neurioip+'/current-sample').json()

        gen_W = pvdata['channels'][3]['p_W']
        gen_V = pvdata['channels'][3]['v_V']
        cons_W = pvdata['channels'][4]['p_W']

        #send data to ThingSpeak
        pvdata = '&field1='+str(gen_W)+'&field2='+str(cons_W)
        print pvdata
        update_thingspeak(pvdata)
        count = count - 1
        print count
        sleep(1)