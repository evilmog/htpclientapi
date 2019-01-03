Welcome to the htpclientapi wiki! This will cover some of the basics of automation.

# Setup

First we need to make a new project, so make a new folder and then clone this repo as a sub directory or sub module or something:

```
git clone https://github.com/evilmog/htpclientapi.git
```

Next we need to create a config.json file to store our hashtopolis config info, obviously change the port, the path to your cert file (we will get to that in a bit) as well as your api key

```
{
        "host":"https://urltohashtopolis.com",
        "port":"443",
        "certpath":"path to pem file saved with getcert.py",
        "apikey":"xxxxxxxxxx"
}
```

Now we need to make a config.py file to get the config.json data

```
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
```

Next we need to make a getcert.py file to get the cert we need from htp

```
import ssl
import config as cfg

print cfg.data['port']
print ssl.get_server_certificate((cfg.data['host'], int(cfg.data['port'])))
```

now we do this

```
python getcert.py > cert.pem
```

#  List Users
now as an example we will list the users

```
import config as cfg
from htpclientapi.functions import *

apikey = cfg.data['apikey']
certpath = cfg.data['certpath']

endpoint = cfg.data['host'] + ':' + cfg.data['port'] + '/api/user.php'
data = listusers(endpoint, certpath, apikey)

for user in data["users"]:
    userdata = getuser(endpoint, certpath, apikey, str(user["userId"]))
    print "UserId:          " + str(userdata["userId"])
    print "  Username:        " + str(userdata["username"])
    print "  e-mail:          " + str(userdata["email"])
    print "  rightGroupId:    " + str(userdata["rightGroupId"])
    print "  registered:      " + str(userdata["registered"])
    print "  lastLogin:       " + str(userdata["lastLogin"])
    print "  isValid:         " + str(userdata["isValid"])
    print "  sessionLifetime: " + str(userdata["sessionLifetime"])
    print " "
```

# Create Hashlist
This is a fairly easy example, lets say now that we want to create a hashlist, we can do the following:

```
import config as cfg
import base64
from htpclientapi.functions import *

apikey = cfg.data['apikey']
certpath = cfg.data['certpath']
endpoint = cfg.data['host'] + ':' + cfg.data['port'] + '/api/user.php'

data = open("ntlm.hash", "r").read()
encoded = base64.b64encode(data)

result = createhashlist(endpoint, certpath, apikey, "EvilMog - Hashes - NTLM", False, True, False, ":", 0, 1000, 1, encoded, False,
                        0)
print result
```

# Create Multiple Attacks like Pathwell
If we wanted to create 100 mask attacks on the hashlist we could do something like this. First get the pathwell masks from https://blog.korelogic.com/blog/2014/04/04/pathwell_topologies and make a file called pathwell.txt and from there run this script

```
import config as cfg
from htpclientapi.functions import *

hashlistid = str(21) # replace this
priority = 102 # replace this if you want it higher or lower
# benchmark = "runtime"
benchmark = "speed"

apikey = cfg.data['apikey']
certpath = cfg.data['certpath']

endpoint = cfg.data['host'] + ':' + cfg.data['port'] + '/api/user.php'

pathwellfile = open("pathwell.txt", 'r')
for line in pathwellfile:
    priority = priority - 1
    pmask = line.rstrip()
    newtask = createtask(endpoint, certpath, apikey,
                         ("PATHWELL -a3 - " + pmask), hashlistid,
                         ("#HL# -a 3 " + pmask), 1200, 5, benchmark,
                         "#FFFFFF", False, False, 0, 1, str(priority), [], False)
    print newtask
```

# List Cracked Hashes per Task
```
import config as cfg
from htpclientapi.functions import *

apikey = cfg.data['apikey']
certpath = cfg.data['certpath']
taskId = '361'

endpoint = cfg.data['host'] + ':' + cfg.data['port'] + '/api/user.php'
data = listtasks(endpoint, certpath, apikey)

results = gettaskcracked(endpoint, certpath, apikey, taskId)

if results['response'] == 'OK':
    for result in results['cracked']:
        print result
```
# Get all cracked hashes for NTLM hashlists
```
import config as cfg
from htpclientapi.functions import *


apikey = cfg.data['apikey']
certpath = cfg.data['certpath']

endpoint = cfg.data['host'] + ':' + cfg.data['port'] + '/api/user.php'
data = listhashlists(endpoint, certpath, apikey)

for hashlist in data['hashlists']:
  if hashlist['hashtypeId'] == 1000:
    crackeddata = gethashlistcracked(endpoint, certpath, apikey, hashlist['hashlistId'])
    for crackedhashlist in crackeddata['cracked']:
      print crackedhashlist['plain']
```
