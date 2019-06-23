Welcome to the htpclientapi wiki! This will cover some of the basics of automation.

# Setup

First we need to make a new project, so make a new folder and then clone this repo as a sub directory or sub module or something:

```
git clone https://github.com/evilmog/htpclientapi.git
```

#  Test connection and access

```
import hashtopolis

handle = hashtopolis.Hashtopolis(endpoint="https://<location on internet here>/api/user.php",port=443,api_key="<YOUR API KEY HERE, or someone eles's, i'm not your dad>")
print(handle.test.connection()).get("response","No Response Error")
print(handle.test.access()).get("response","No Response Error")
```


#  List Users
now as an example we will list the users

```
import hashtopolis

handle = hashtopolis.Hashtopolis(endpoint="https://<location on internet here>/api/user.php",port=443,api_key="<YOUR API KEY HERE, or someone eles's, i'm not your dad>")

user_list = handle.user.listUsers().get("users",[])
for user in user_list:
    user_data = handle.user.getUser(userId=user.get("userId"))
    for property_name, value in user_data.items():
        print("{property_name}: {value}".format(property_name= property_name, value=value))
```

# Integgroll has not updated the documents below here, he decided to take a break for food and to pack. So they are just flat out wrong for the hashtopolis.py version of things for now.


# Create Hashlist
This is a fairly easy example, lets say now that we want to create a hashlist, we can do the following:

```
from htpclientapi.functions import *

import config
import base64

data = open("ntlm.hash", "r").read()
encoded = base64.b64encode(data)

result = createhashlist("EvilMog - Hashes - NTLM", False, True, False, ":", 0, 1000, 1, encoded, False,
                        0)
print result
```

# Create Multiple Attacks like Pathwell
If we wanted to create 100 mask attacks on the hashlist we could do something like this. First get the pathwell masks from https://blog.korelogic.com/blog/2014/04/04/pathwell_topologies and make a file called pathwell.txt and from there run this script

```
from htpclientapi.functions import *
import config

hashlistid = str(21) # replace this
priority = 102 # replace this if you want it higher or lower
# benchmark = "runtime"
benchmark = "speed"

pathwellfile = open("pathwell.txt", 'r')
for line in pathwellfile:
    priority = priority - 1
    pmask = line.rstrip()
    newtask = createtask(
                         ("PATHWELL -a3 - " + pmask), hashlistid,
                         ("#HL# -a 3 " + pmask), 1200, 5, benchmark,
                         "#FFFFFF", False, False, 0, 1, str(priority), [], False)
    print newtask
```

# List Cracked Hashes per Task
```
from htpclientapi.functions import *

import config

taskId = '361'

endpoint = cfg.data['host'] + ':' + cfg.data['port'] + '/api/user.php'
data = listtasks(endpoint, certpath, apikey)

results = gettaskcracked(taskId)

if results['response'] == 'OK':
    for result in results['cracked']:
        print result
```
# Get all cracked hashes for NTLM hashlists
```
from htpclientapi.functions import *

import config

data = listhashlists()

for hashlist in data['hashlists']:
  if hashlist['hashtypeId'] == 1000:
    crackeddata = gethashlistcracked(hashlist['hashlistId'])
    for crackedhashlist in crackeddata['cracked']:
      print crackedhashlist['plain']
```
