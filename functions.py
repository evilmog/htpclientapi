import requests


requests.packages.urllib3.disable_warnings()


# Test Section
def test_connection(endpoint, certpath):
  test = {'section': 'test', 'request': 'connection'}
  resp = requests.post(endpoint, verify=certpath, json=test)
  return resp.json()["response"]  

def test_access(endpoint, certpath, accessKey):
  access = {'section': 'test', 'request':'access', 'accessKey':accessKey}
  resp = requests.post(endpoint, verify=certpath, json=access)
  return resp.json()["response"]

# User Section
def listUsers(endpoint, certpath, accessKey):
  userlist = { 'section': 'user', 'request':'listUsers', 'accessKey':accessKey}
  resp = requests.post(endpoint, verify=certpath, json=userlist)
  return resp.json()

def getUser(endpoint, certpath, accessKey, userId):
  getuser = { 'section':'user', 'request':'getUser', 'userId':userId, 'accessKey':accessKey}
  resp = requests.post(endpoint, verify=certpath, json=getuser)
  return resp.json()

def createUser(endpoint, certpath, accessKey, username, email, rightGroupId):
  createuser = { 'section':'user', 'request':'createUser', 'username':username, 'rightGroupId':rightgroupId,'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createuser)
  return resp.json()

def disableUser(endpoint, certpath, accessKey, userId):
  disableuser = { 'section':'user', 'request':'disableUser', 'userId':userId, 'accessKey': accessKey}
  resp = requests.post(endpoint, verify=certpath, json=disableuser)
  return resp.json()

def enableUser(endpoint, certpath, accessKey, userId):
  enableuser = { 'section':'user', 'request':'enableUser', 'userId':userId, 'accessKey': accessKey}
  resp = requests.post(endpoint, verify=certpath, json=enableuser)
  return resp.json()

def setUserPassword(endpoint, certpath, accessKey, userId, password):
  setuserpassword = { 'section':'user', 'request':'setUserPassword', 'userId':userId, 'password':password, 'accessKey':accessKey}
  resp = requests.post(endpoint, verify=certpath, json=setuserpassword)
  return resp.json()

def setUserRightGroup(endpoint, certpath, accessKey, userId, rightGroupId):
  setuserrightgroup = { 'section':'user', 'request':'setUserRightGroup', 'userId':userId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setuserrightgroup)
  return resp.json()

# Group Section
def listGroups(endpoint, certpath, accessKey):
  listgroups = { 'section':'group', 'request':'listGroups', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listgroups)
  return resp.json()

def getGroup(endpoint, certpath, accessKey, groupId):
  getgroup = { 'section':'group', 'request':'getGroup', 'groupId':groupId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getgroup)
  return resp.json()

def createGroup(endpoint, certpath, accessKey, name):
  creategroup = { 'section':'group', 'request':'createGroup', 'name':name, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=creategroup)
  return resp.json()

def addAgent(endpoint, certpath, accessKey, groupId, agentId):
  addagent = { 'section':'group', 'request':'addAgent', 'groupId':groupId, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=addagent)
  return resp.json()

def removeAgent(endpoint, certpath, accessKey, groupId, agentId):
  removeagent = { 'section':'group', 'request':'removegent', 'groupId':groupId, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=removeagent)
  return resp.json()

def addUser(endpoint, certpath, accessKey, groupId, userId):
  adduser = { 'section':'group', 'request':'addUser', 'groupId':groupId, 'userId':userId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=adduser)
  return resp.json()

def removeUser(endpoint, certpath, accessKey, groupId, userId):
  adduser = { 'section':'group', 'request':'removeUser', 'groupId':groupId, 'userId':userId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=removeuser)
  return resp.json()

def deleteGroup(endpoint, certpath, accessKey, groupId):
  deletegroup = { 'section':'group', 'request':'deleteGroup', 'groupId':groupId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=deletegroup)
  return resp.json()

# Access Section
def listAccessGroups(endpoint, certpath, accessKey):
  listgroups = { 'section':'access', 'request':'listGroups', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listgroups)
  return resp.json()

def getAccessGroup(endpoint, certpath, accessKey, rightGroupId):
  getgroup = { 'section':'access', 'request':'getGroup', 'rightGroupId':rightGroupId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getgroup)
  return resp.json()

def createAccessGroup(endpoint, certpath, accessKey, name):
  creategroup = { 'section':'access', 'request':'createGroup', 'name':name, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=creategroup)
  return resp.json()

def deleteAccessGroup(endpoint, certpath, accessKey, rightGroupId):
  deletegroup = { 'section':'access', 'request':'deleteGroup', 'rightGroupId':rightGroupId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=deletegroup)
  return resp.json()

def setAccessPermissions(endpoint, certpath, accessKey, rightGroupId, viewHashlistAccess, manageHashlistAccess, createHashlistAccess, createSuperhashlistAccess, viewHashesAccess, viewAgentsAccess, manageAgentAccess, createAgentAccess, viewTaskAccess, runTaskAccess, createTaskAccess, manageTaskAccess, viewPretaskAccess, createPretaskAccess, managePretaskAccess, viewSupertaskAccess, createSupertaskAccess, manageSupertaskAccess, viewFileAccess, manageFileAccess, addFileAccess, crackerBinaryAccess, serverConfigAccess, userConfigAccess):
  setpermissions = { "section": "access", "request": "setPermissions", "rightGroupId":rightGroupId, "permissions": { "viewHashlistAccess": viewHashlistAccess, "manageHashlistAccess": manageHashlistAccess, "createHashlistAccess": createHashlistAccess, "createSuperhashlistAccess": createSuperhashlistAccess, "viewHashesAccess": viewHashesAccess, "viewAgentsAccess": viewAgentsAccess, "manageAgentAccess": manageAgentAccess, "createAgentAccess": createAgentAccess, "viewTaskAccess": viewTaskAccess, "runTaskAccess": runTaskAccess, "createTaskAccess": createTaskAccess, "manageTaskAccess": manageTaskAccess, "viewPretaskAccess": viewPretaskAccess, "createPretaskAccess": createPretaskAccess, "managePretaskAccess": managePretaskAccess, "viewSupertaskAccess": viewSupertaskAccess, "createSupertaskAccess": createSupertaskAccess, "manageSupertaskAccess": manageSupertaskAccess, "viewFileAccess": viewFileAccess, "manageFileAccess": manageFileAccess, "addFileAccess": addFileAccess, "crackerBinaryAccess": crackerBinaryAccess, "serverConfigAccess": serverConfigAccess, "userConfigAccess": userConfigAccess }, "accessKey": accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpermissions)
  return resp.json()

# Account Section

def getInformation(endpoint, certpath, accessKey):
  getinformation = { 'section':'account', "request":"getInformation", 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getinformation)
  return resp.json()

def setEmail(endpoint, certpath, accessKey, email):
  setemail = { 'section':'account', "request":"setEmail", "email":email, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setemail)
  return resp.json()

def setSessionLength(endpoint, certpath, accessKey, sessionLength):
  setsessionlength = { 'section':'account', 'request':'setSessionLength', 'sessionLength':sessionLength, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setsessionlength)
  return resp.json()

def changePassword(endpoint, certpath, accessKey, newPassword, oldPassword):
  changepassword = { 'section':'account', 'request':'changePassword', 'newPassword':newPassword, 'oldPassword':oldPassword, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=changepassword)
  return resp.json()

# Server Config
def listSections(endpoint, certpath, accessKey):
  listsections = { 'section':'config', 'request':'listSections', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listsections)
  return resp.json()

def listConfig(endpoint, certpath, accessKey):
  listconfig = { 'section':'config', 'request':'listConfig', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listconfig)
  return resp.json()

def getConfig(endpoint, certpath, accessKey, configItem):
  getconfig = { 'section':'config', 'request':'getConfig', 'configItem':configItem, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getconfig)
  return resp.json()

def setConfig(endpoint, certpath, accessKey, configItem, value, force):
  setConfig = { 'section':'config', 'request':'setConfig', 'configItem':configItem, 'value':value, 'force':force, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setconfig)
  return resp.json()

# Agents
def listAgents(endpoint, certpath, accessKey):
  listagents = { 'section':'agent', 'request':'listAgents', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listagents)
  return resp.json()

def getAgent(endpoint, certpath, accessKey, agentId):
  getagent = { 'section':'agent', 'request':'get', 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getagent)
  return resp.json()

def setAgentActive(endpoint, certpath, accessKey, agentId, active):
  setagentactive = { 'section':'agent', 'request':'setActive', 'active':active, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setagentactive)
  return resp.json()

def changeAgentOwner(endpoint, certpath, accessKey, agentId, user):
  changeagentowner = { 'section':'agent', 'request':'changeOwner', 'user':user, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=changeagentowner)
  return resp.json()

def setAgentName(endpoint, certpath, accessKey, agentId, name):
  setagentname = { 'section':'agent', 'request':'setName', 'name':name, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setagentname)
  return resp.json()

def setAgentCpuOnly(endpoint, certpath, accessKey, agentId, cpuOnly):
  setagentcpuonly = { 'section':'agent', 'request':'setCpuOnly', 'cpuOnly':cpuOnly, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setagentcpuonly)
  return resp.json()

def setAgentExtraParams(endpoint, certpath, accessKey, agentId, extraParameters):
  setagentextraparams = { 'section':'agent', 'request':'setExtraParams', 'extraParameters':extraParameters, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setagentextraparams)
  return resp.json()

def setAgentErrorFlag(endpoint, certpath, accessKey, agentId, ignoreErrors):
  setagentextraparams = { 'section':'agent', 'request':'setErrorFlag', 'ignoreErrors':ignoreErrors, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setagentextraparams)
  return resp.json()

def setAgentTrusted(endpoint, certpath, accessKey, agentId, trusted):
  setagenttrusted = { 'section':'agent', 'request':'setTrusted', 'trusted':trusted, 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setagenttrusted)
  return resp.json()

def listAgentVouchers(endpoint, certpath, accessKey):
  listvouchers = { 'section':'agent', 'request':'listVouchers', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listvouchers)
  return resp.json()

def createAgentVoucherRandom(endpoint, certpath, accessKey):
  createvoucher = { 'section':'agent', 'request':'createVoucher', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createvoucher)
  return resp.json()

def createAgentVoucher(endpoint, certpath, accessKey, voucher):
  createvoucher = { 'section':'agent', 'request':'createVoucher', 'voucher':voucher, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createvoucher)
  return resp.json()

def deleteAgentVoucher(endpoint, certpath, accessKey, voucher):
  deletevoucher = { 'section':'agent', 'request':'deleteVoucher', 'voucher':voucher, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=deletevoucher)
  return resp.json()

def getAgentBinaries(endpoint, certpath, accessKey):
  getagentbinary = { 'section':'agent', 'request':'getBinaries', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getagentbinary)
  return resp.json()

#Tasks

def listTasks(endpoint, certpath, accessKey):
  listtask = { 'section':'task', 'request':'listTasks', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listtask)
  return resp.json()

def getTask(endpoint, certpath, accessKey, taskId):
  gettask = { 'section':'task', 'request':'getTask', 'taskId':taskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=gettask)
  return resp.json()

def listSubtasks(endpoint, certpath, accessKey, superTaskId):
  listsubtask = { 'section':'task', 'request':'listSubtasks', 'superTaskId':superTaskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listsubtask)
  return resp.json()

def getChunk(endpoint, certpath, accessKey, chunkId):
  getchunk = { 'section':'task', 'request':'getChunk', 'chunkId':chunkId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getchunk)
  return resp.json()

#files must be an array [] or [1,2]
def createTask(endpoint, certpath, accessKey, name, hashlistId, attackCmd, chunksize, statusTimer, benchmarkType, color, isCpuOnly, isSmall, Skip, crackerVersionId, priority, isPrince):
  createtask = { 'section':'task', 'request':'createTask', 'name':name, 'hashlistId':hashlistId, 'attackCmd':attackCmd, 'chunksize':chunksize, 'statusTimer':statusTimer, 'benchmarkType':benchmarkType, 'color':color, 'isCpuOnly':isCpuOnly, 'isSmall':isSmall, 'skip':skip, 'crackerVersionId':crackerVersionId, 'files':files, 'priority':priority, 'isPrince':isPrince, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createtask)
  return resp.json()

def runPretask(endpoint, certpath, accessKey, name, hashlistId, pretaskId, crackerVersionId):
  runpretask = { 'section':'task', 'request':'runPretask', 'name':name, 'hashlistId':hashlistId, 'pretaskId':pretaskId, 'crackerVersionId':crackerVersionId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=runpretask)
  return resp.json()

def runSupertask(endpoint, certpath, accessKey, name, hashlistId, supertaskId, crackerVersionId):
  runsupertask = { 'section':'task', 'request':'runSupertask', 'hashlistId':hashlistId, 'supertaskId':supertaskId, 'crackerVersionId':crackerVersionId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=runsupertask)
  return resp.json()

def setTaskPriority(endpoint, certpath, accessKey, taskId, priority):
  settaskpriority = { 'section':'task', 'request':'setTaskPriority', 'taskId':taskId, 'priority':priority, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=settaskpriority)
  return resp.json()

def setSupertaskPriority(endpoint, certpath, accessKey, supertaskId, supertaskPriority):
  setsupertaskpriority = { 'section':'task', 'request':'setSupertaskPriority', 'supertaskId':supertaskId, 'supertaskPriority':supertaskPriority, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setsupertaskpriority)
  return resp.json()

def setTaskName(endpoint, certpath, accessKey, taskId, name):
  settaskname = { 'section':'task', 'request':'setTaskName', 'taskId':taskId, 'name':name, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=settaskname)
  return resp.json()

def setTaskColor(endpoint, certpath, accessKey, taskId, color):
  settaskcolor = { 'section':'task', 'request':'setTaskColor', 'taskId':taskId, 'color':color, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=settaskcolor)
  return resp.json()

def setTaskCpuOnly(endpoint, certpath, accessKey, taskId, isCpuOnly):
  setiscpuonly = { 'section':'task', 'request':'setTaskCpuOnly', 'taskId':taskId, 'isCpuOnly':isCpuOnly, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setiscpuonly)
  return resp.json()

def setTaskSmall(endpoint, certpath, accessKey, taskId, isSmall):
  settasksmall = { 'section':'task', 'request':'setTaskSmall', 'taskId':taskId, 'isSmall':isSmall, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=settasksmall)
  return resp.json()

def taskUnassignAgent(endpoint, certpath, accessKey, agentId):
  taskunassignagent = { 'section':'task', 'request':'taskUnassignAgent', 'agentId':agentId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=taskunassignagent)
  return resp.json()

def deleteTask(endpoint, certpath, accessKey, taskId):
  deletetask = { 'section':'task', 'request':'deleteTask', 'taskId':taskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=deletetask)
  return resp.json()

def purgeTask(endpoint, certpath, accessKey, taskId):
  purgetask = { 'section':'task', 'request':'purgeTask', 'taskId':taskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=purgetask)
  return resp.json()

def setSupertaskName(endpoint, certpath, accessKey, supertaskId, name):
  setsupertaskname = { 'section':'task', 'request':'setSupertaskName', 'supertaskId':supertaskId, 'name':name, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setsupertaskname)
  return resp.json()

def deleteSupertask(endpoint, certpath, accessKey, supertaskId):
  setsupertaskname = { 'section':'task', 'request':'deleteSupertask', 'supertaskId':supertaskId, 'accessKey':accessKey } 
  resp = requests.post(endpoint, verify=certpath, json=setsupertaskname)
  return resp.json()

def archiveTask(endpoint, certpath, accessKey, taskId):
  archivetask = { 'section':'task', 'request':'archiveTask', 'taskId':taskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=archivetask)
  return resp.json()

def archiveSupertask(endpoint, certpath, accessKey, supertaskId):
  archivesupertask = { 'section':'task', 'request':'archiveSupertask', 'supertaskId':supertaskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=archivesupertask)
  return resp.json()

#Preconfigured Tasks (pretask)
def setPretaskPriority(endpoint, certpath, accessKey, pretaskId, priority):
  setpretaskpriority = { 'section':'pretask', 'request':'setPretaskPriority', 'pretaskId':pretaskId, 'priority':priority, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpretaskpriority)
  return resp.json()

def setPretaskName(endpoint, certpath, accessKey, pretaskId, name):
  setpretaskname = { 'section':'pretask', 'request':'setPretaskName', 'pretaskId':pretaskId, 'name':name, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpretaskname)
  return resp.json()

def setPretaskColor(endpoint, certpath, accessKey, pretaskId, color):
  setpretaskcolor = { 'section':'pretask', 'request':'setPretaskColor', 'pretaskId':pretaskId, 'color':color, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpretaskcolor)
  return resp.json()

def setPretaskChunksize(endpoint, certpath, accessKey, pretaskId, chunksize):
  setpretaskchunksize = { 'section':'pretask', 'request':'setPretaskChunksize', 'pretaskId':pretaskId, 'chunksize':chunksize, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpretaskchunksize)
  return resp.json()

def setPretaskCpuOnly(endpoint, certpath, accessKey, pretaskId, isCpuOnly):
  setpretaskcpuonly = { 'section':'pretask', 'request':'setPretaskCpuOnly', 'pretaskId':pretaskId, 'isCpuOnly':isCpuOnly, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpretaskcpuonly)
  return resp.json()

def setPretaskSmall(endpoint, certpath, accessKey, pretaskId, isSmall):
  setpretasksmall = { 'section':'pretask', 'request':'setPretaskSmall', 'pretaskId':pretaskId, 'isSmall':isSmall, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=setpretasksmall)
  return resp.json()

def deletePretask(endpoint, certpath, accessKey, pretaskId):
  deletepretask = { 'section':'pretask', 'request':'deletePretask', 'pretaskId':pretaskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=deletepretask)
  return resp.json()

# files must be an array, []. or [1], or [1,2] 
def createPretask(endpoint, certpath, accessKey, name, attackCmd, chunksize, statusTimer, benchmarkType, color, isCpuOnly, isSmall, priority, files, crackerTypeId)
  createpretask = { 'section':'pretask', 'request':'createPreTask", 'name':name, 'attackCmd':attackCmd, 'chunksize':chunksize, 'statusTimer':statusTimer, 'benchmarkType':benchmarkType, 'color':color, 'isCpuOnly':isCpuOnly, 'isSmall':isSmall, 'priority':priority, 'files':files, 'crackerTypeId':crackerTypeId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createpretask)
  return resp.json()

def listPretasks(endpoint, certpath, accessKey):
  listpretasks = { 'section':'pretask', 'request':'listPretasks', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listpretasks)
  return resp.json()

def getPretask(endpoint, certpath, accessKey, pretaskId):
  getpretask = { 'section':'pretask', 'request':'getPretask", "pretaskId":pretaskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getpretask)
  return resp.json()

#Supertasks - supertask
# masks must be an array ["?d?d?d?d", "?a?a?a"]
def importSupertask(endpoint, certpath, accessKey, name, isCpuOnly, isSmall, masks, optimizedFlag, crackerTypeId):
  importsupertask = { 'section':'supertask', 'request':'importSupertask', 'name':name, 'isCpuOnly':isCpuOnly, 'isSmall':isSmall, 'masks':masks, 'optimizedFlag':optimizedFlag, 'crackerTypeId':crackerTypeId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=importsupertask)  
  return resp.json()

def listSupertasks(endpoint, certpath, accessKey):
  listsupertask = { 'section':'supertask', 'request':'listSupertasks', 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=listsupertask)
  return resp.json()

def getSupertask(endpoint, certpath, accessKey, supertaskId):
  getsupertask = { 'section':'supertask', 'request':'getSupertask', 'supertaskId':supertaskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=getsupertask)
  return resp.json()

# pretasks must be an array [7, 8]
def createSupertask(endpoint, certpath, accessKey, name, pretasks):
  createsupertask = { 'section':'supertask', 'request':'createSupertask', 'name':name, 'pretasks':pretasks, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createsupertask)
  return resp.json()

def setSupertaskName(endpoint, certpath, accessKey, supertaskId, name):
  setsupertaskname = { 'section':'supertask', 'request':'setSupertaskName', 'supertaskId':supertaskId, 'name':name, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=createsupertask)
  return resp.json()

def deleteSupertask(endpoint, certpath, accessKey, supertaskId):
  deletesupertask = { 'section':'supertask', 'request':'deleteSupertask', 'supertaskId':supertaskId, 'accessKey':accessKey }
  resp = requests.post(endpoint, verify=certpath, json=deletesupertask
  return resp.json()

