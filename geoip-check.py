#!/usr/bin/python3.8

"""
SCript Usage :
run from command line : ./geoip-check.py 8.8.8.8 (replace by any IP you want to check)
you will receive results from 4 separate DB's
"""
from sys import argv
import urllib.request
import urllib.parse
import json


pars = argv[1]




def form(ip_addr):
  link1 = "https://ipinfo.io/"+ip_addr+"/geo"
  link2 = "http://free.ipwhois.io/json/"+ip_addr
  link4 = "http://ip-api.com/json/"+ip_addr
  link5 = "https://extreme-ip-lookup.com/json/"+ip_addr
  links = [link1, link2, link4, link5]
  print("\nLocation for IP Address : "+ip_addr)

  for i in links:
    url = urllib.request.urlopen(i)
    url_list = url.read().decode('utf-8')
    json_loaded = json.loads(url_list)
    #print(json_loaded)
    print("\n                   ............................")
    print ("                    City    : "+ json_loaded['city'])
    print ("                    Country    : "+ json_loaded['country'])

  print("\n                ............................")

  return()



form(pars)
               
