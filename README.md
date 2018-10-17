# hashtopolis-clientapi
Python Bindings for Hashtopolis Client API

This is the start of the python bindings for the hashtopolis API
https://github.com/s3inlc/hashtopolis/blob/master/doc/user-api/user-api.pdf

right now it connects on https, and you will need a cert in PEM format for your
client to connect nicely.

'''
from functions import *
import requests
import json
import yaml

apikey = 'crappyapikey'
certpath = '/full/path/to/cert.pem'
endpoint = 'https://hashtopolisurl.com/api/user.php'

data = listUsers(endpoint, certpath, apikey)
for user in data["users"]:
  userdata = getUser(endpoint, certpath, apikey, str(user["userId"]))
  print "UserId:          " + str(userdata["userId"])
  print "  Username:        " + str(userdata["username"])
  print "  e-mail:          " + str(userdata["email"])
  print "  rightGroupId:    " + str(userdata["rightGroupId"])
  print "  registered:      " + str(userdata["registered"])
  print "  lastLogin:       " + str(userdata["lastLogin"])
  print "  isValid:         " + str(userdata["isValid"])
  print "  sessionLifetime: " + str(userdata["sessionLifetime"])
  print " "
'''

Yes this is a crappy start and I haven't finished all the function definitions but its there
