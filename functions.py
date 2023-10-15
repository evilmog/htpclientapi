import requests
import json
import config as cfg

accesskey = cfg.data['apikey']
certpath = cfg.data['certpath']
endpoint = cfg.data['endpoint'] + '/api/user.php'

requests.packages.urllib3.disable_warnings()

# Test Section
def test_connection():
    testjson = {'section': 'test', 'request': 'connection'}
    resp = requests.post(endpoint, verify=certpath, json=testjson)
    return resp.json()["response"]


def test_access():
    accessjson = {'section': 'test', 'request': 'access', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=accessjson)
    return resp.json()["response"]


# User Section
def listusers():
    listusersjson = {'section': 'user', 'request': 'listUsers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listusersjson)
    return resp.json()


def getuser(userid):
    getuserjson = {'section': 'user', 'request': 'getUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getuserjson)
    return resp.json()


def createuser(username, email, rightgroupid):
    createuserjson = {'section': 'user', 'request': 'createUser', 'username': username, 'email': email,
                      'rightGroupId': rightgroupid,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createuserjson)
    return resp.json()


def disableuser(userid):
    disableuserjson = {'section': 'user', 'request': 'disableUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=disableuserjson)
    return resp.json()


def enableuser(userid):
    enableuserjson = {'section': 'user', 'request': 'enableUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=enableuserjson)
    return resp.json()


def setuserpassword(userid, password):
    setuserpasswordjson = {'section': 'user', 'request': 'setUserPassword', 'userId': userid, 'password': password,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setuserpasswordjson)
    return resp.json()


def setuserrightgroup(userid, rightgroupid):
    setuserrightgroupjson = {'section': 'user', 'request': 'setUserRightGroup', 'userId': userid,
                             'rightGroupId': rightgroupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setuserrightgroupjson)
    return resp.json()


# Group Section
def listgroups():
    listgroupsjson = {'section': 'group', 'request': 'listGroups', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listgroupsjson)
    return resp.json()


def getgroup(groupid):
    getgroupjson = {'section': 'group', 'request': 'getGroup', 'groupId': groupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getgroupjson)
    return resp.json()


def creategroup(name):
    creategroupjson = {'section': 'group', 'request': 'createGroup', 'name': name, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=creategroupjson)
    return resp.json()


def addagent(groupid, agentid):
    addagentjson = {'section': 'group', 'request': 'addAgent', 'groupId': groupid, 'agentId': agentid,
                    'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=addagentjson)
    return resp.json()


def removeagent(groupid, agentid):
    removeagentjson = {'section': 'group', 'request': 'removeAgent', 'groupId': groupid, 'agentId': agentid,

                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=removeagentjson)
    return resp.json()


def adduser(groupid, userid):
    adduserjson = {'section': 'group', 'request': 'addUser', 'groupId': groupid, 'userId': userid,
                   'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=adduserjson)
    return resp.json()


def removeuser(groupid, userid):
    removeuserjson = {'section': 'group', 'request': 'removeUser', 'groupId': groupid, 'userId': userid,
                      'accesskey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=removeuserjson)
    return resp.json()


def deletegroup(groupid):
    deletegroupjson = {'section': 'group', 'request': 'deleteGroup', 'groupId': groupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletegroupjson)
    return resp.json()


# Access Section
def listaccessgroups():
    listgroupsjson = {'section': 'access', 'request': 'listGroups', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listgroupsjson)
    return resp.json()


def getaccessgroup(rightgroupid):
    getaccessgroupjson = {'section': 'access', 'request': 'getGroup', 'rightGroupId': rightgroupid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getaccessgroupjson)
    return resp.json()


def createaccessgroup(name):
    createaccessgroupjson = {'section': 'access', 'request': 'createGroup', 'name': name, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createaccessgroupjson)
    return resp.json()


def deleteaccessgroup(rightgroupid):
    deleteaccessgroupjson = {'section': 'access', 'request': 'deleteGroup', 'rightGroupId': rightgroupid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deleteaccessgroupjson)
    return resp.json()


def setaccesspermissions(rightgroupid, viewhashlistaccess, managehashlistaccess,
                         createhashlistaccess, createsuperhashlistaccess, viewhashesaccess, viewagentsaccess,
                         manageagentaccess, createagentaccess, viewtaskaccess, runtaskaccess, createtaskaccess,
                         managetaskaccess, viewpretaskaccess, createpretaskaccess, managepretaskaccess,
                         viewsupertaskaccess, createsupertaskaccess, managesupertaskaccess, viewfileaccess,
                         managefileaccess, addfileaccess, crackerbinaryaccess, serverconfigaccess, userconfigaccess):
    setpermissionsjson = {"section": "access", "request": "setPermissions", "rightGroupId": rightgroupid,
                          "permissions": {"viewHashlistAccess": viewhashlistaccess,
                                          "manageHashlistAccess": managehashlistaccess,
                                          "createHashlistAccess": createhashlistaccess,
                                          "createSuperhashlistAccess": createsuperhashlistaccess,
                                          "viewHashesAccess": viewhashesaccess, "viewAgentsAccess": viewagentsaccess,
                                          "manageAgentAccess": manageagentaccess,
                                          "createAgentAccess": createagentaccess,
                                          "viewTaskAccess": viewtaskaccess, "runTaskAccess": runtaskaccess,
                                          "createTaskAccess": createtaskaccess, "manageTaskAccess": managetaskaccess,
                                          "viewPretaskAccess": viewpretaskaccess,
                                          "createPretaskAccess": createpretaskaccess,
                                          "managePretaskAccess": managepretaskaccess,
                                          "viewSupertaskAccess": viewsupertaskaccess,
                                          "createSupertaskAccess": createsupertaskaccess,
                                          "manageSupertaskAccess": managesupertaskaccess,
                                          "viewFileAccess": viewfileaccess,
                                          "manageFileAccess": managefileaccess, "addFileAccess": addfileaccess,
                                          "crackerBinaryAccess": crackerbinaryaccess,
                                          "serverConfigAccess": serverconfigaccess,
                                          "userConfigAccess": userconfigaccess},
                          "accessKey": accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpermissionsjson)
    return resp.json()


# Account Section

def getinformation():
    getinformationjson = {'section': 'account', "request": "getInformation", 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getinformationjson)
    return resp.json()


def setemail(email):
    setemailjson = {'section': 'account', "request": "setEmail", "email": email, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setemailjson)
    return resp.json()


def setsessionlength(sessionlength):
    setsessionlengthjson = {'section': 'account', 'request': 'setSessionLength', 'sessionLength': sessionlength,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setsessionlengthjson)
    return resp.json()


def changepassword(newpassword, oldpassword):
    changepasswordjson = {'section': 'account', 'request': 'changePassword', 'newPassword': newpassword,
                          'oldPassword': oldpassword, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=changepasswordjson)
    return resp.json()


# Server Config
def listsections():
    listsectionsjson = {'section': 'config', 'request': 'listSections', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsectionsjson)
    return resp.json()


def listconfig():
    listconfigjson = {'section': 'config', 'request': 'listConfig', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listconfigjson)
    return resp.json()


def getconfig(configitem):
    getconfigjson = {'section': 'config', 'request': 'getConfig', 'configItem': configitem, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getconfigjson)
    return resp.json()


def setconfig(configitem, value, force):
    setconfigjson = {'section': 'config', 'request': 'setConfig', 'configItem': configitem, 'value': value,
                     'force': force,
                     'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setconfigjson)
    return resp.json()


# Agents
def listagents():
    listagentsjson = {'section': 'agent', 'request': 'listAgents', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listagentsjson)
    return resp.json()


def getagent(agentid):
    getagentjson = {'section': 'agent', 'request': 'get', 'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getagentjson)
    return resp.json()


def setagentactive(agentid, active):
    setagentactivejson = {'section': 'agent', 'request': 'setActive', 'active': active, 'agentId': agentid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentactivejson)
    return resp.json()


def changeagentowner(agentid, user):
    changeagentownerjson = {'section': 'agent', 'request': 'changeOwner', 'user': user, 'agentId': agentid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=changeagentownerjson)
    return resp.json()


def setagentname(agentid, name):
    setagentnamejson = {'section': 'agent', 'request': 'setName', 'name': name, 'agentId': agentid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentnamejson)
    return resp.json()


def setagentcpuonly(agentid, cpuonly):
    setagentcpuonlyjson = {'section': 'agent', 'request': 'setCpuOnly', 'cpuOnly': cpuonly, 'agentId': agentid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentcpuonlyjson)
    return resp.json()


def setagentextraparams(agentid, extraparameters):
    setagentextraparamsjson = {'section': 'agent', 'request': 'setExtraParams', 'extraParameters': extraparameters,
                               'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentextraparamsjson)
    return resp.json()


def setagenterrorflag(agentid, ignoreerrors):
    setagentextraparamsjson = {'section': 'agent', 'request': 'setErrorFlag', 'ignoreErrors': ignoreerrors,
                               'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentextraparamsjson)
    return resp.json()


def setagenttrusted(agentid, trusted):
    setagenttrustedjson = {'section': 'agent', 'request': 'setTrusted', 'trusted': trusted, 'agentId': agentid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagenttrustedjson)
    return resp.json()


def listagentvouchers():
    listagentvouchersjson = {'section': 'agent', 'request': 'listVouchers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listagentvouchersjson)
    return resp.json()


def createagentvoucherrandom():
    createagentvoucherrandomjson = {'section': 'agent', 'request': 'createVoucher', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createagentvoucherrandomjson)
    return resp.json()


def createagentvoucher(voucher):
    createagentvoucherjson = {'section': 'agent', 'request': 'createVoucher', 'voucher': voucher,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createagentvoucherjson)
    return resp.json()


def deleteagentvoucher(voucher):
    deleteagentvoucherjson = {'section': 'agent', 'request': 'deleteVoucher', 'voucher': voucher,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deleteagentvoucherjson)
    return resp.json()


def getagentbinaries():
    getagentbinariesjson = {'section': 'agent', 'request': 'getBinaries', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getagentbinariesjson)
    return resp.json()


# Task Section

def listtasks():
    listtasksjson = {'section': 'task', 'request': 'listTasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listtasksjson)
    return resp.json()


def gettask(taskid):
    gettaskjson = {'section': 'task', 'request': 'getTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gettaskjson)
    return resp.json()


def gettaskcracked(taskid):
    gettaskcrackedjson = {'section': 'task', 'request': 'getCracked', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gettaskcrackedjson)
    return resp.json()


def listsubtasks(supertaskid):
    listsubtasksjson = {'section': 'task', 'request': 'listSubtasks', 'superTaskId': supertaskid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsubtasksjson)
    return resp.json()


def getchunk(chunkid):
    getchunkjson = {'section': 'task', 'request': 'getChunk', 'chunkId': chunkid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getchunkjson)
    return resp.json()


# files must be an array [] or [1,2]
def createtask(name, hashlistid, attackcmd, chunksize, statustimer, benchmarktype, color,
               iscpuonly, issmall, skip, crackerversionid, priority, files, isprince):
    createtaskjson = {'section': 'task', 'request': 'createTask', 'name': name, 'hashlistId': hashlistid,
                      'attackCmd': attackcmd, 'chunksize': chunksize, 'statusTimer': statustimer,
                      'benchmarkType': benchmarktype, 'color': color, 'isCpuOnly': iscpuonly, 'isSmall': issmall,
                      'skip': skip, 'crackerVersionId': crackerversionid, 'files': files, 'priority': priority,
                      'isPrince': isprince, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createtaskjson)
    return resp.json()


def runpretask(name, hashlistid, pretaskid, crackerversionid):
    runpretaskjson = {'section': 'task', 'request': 'runPretask', 'name': name, 'hashlistId': hashlistid,
                      'pretaskId': pretaskid, 'crackerVersionId': crackerversionid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=runpretaskjson)
    return resp.json()


def runsupertask(hashlistid, supertaskid, crackerversionid):
    runsupertaskjson = {'section': 'task', 'request': 'runSupertask', 'hashlistId': hashlistid,
                        'supertaskId': supertaskid,
                        'crackerVersionId': crackerversionid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=runsupertaskjson)
    return resp.json()


def settaskpriority(taskid, priority):
    settaskpriorityjson = {'section': 'task', 'request': 'setTaskPriority', 'taskId': taskid, 'priority': priority,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settaskpriorityjson)
    return resp.json()


def setsupertaskpriority(supertaskid, supertaskpriority):
    setsupertaskpriorityjson = {'section': 'task', 'request': 'setSupertaskPriority', 'supertaskId': supertaskid,
                                'supertaskPriority': supertaskpriority, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setsupertaskpriorityjson)
    return resp.json()


def settaskname(taskid, name):
    settasknamejson = {'section': 'task', 'request': 'setTaskName', 'taskId': taskid, 'name': name,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settasknamejson)
    return resp.json()


def settaskcolor(taskid, color):
    settaskcolorjson = {'section': 'task', 'request': 'setTaskColor', 'taskId': taskid, 'color': color,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settaskcolorjson)
    return resp.json()


def settaskcpuonly(taskid, iscpuonly):
    settaskcpuonlyjson = {'section': 'task', 'request': 'setTaskCpuOnly', 'taskId': taskid, 'isCpuOnly': iscpuonly,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settaskcpuonlyjson)
    return resp.json()


def settasksmall(taskid, issmall):
    settasksmalljson = {'section': 'task', 'request': 'setTaskSmall', 'taskId': taskid, 'isSmall': issmall,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settasksmalljson)
    return resp.json()


def taskunassignagent(agentid):
    taskunassignagentjson = {'section': 'task', 'request': 'taskUnassignAgent', 'agentId': agentid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=taskunassignagentjson)
    return resp.json()


def deletetask(taskid):
    deletetaskjson = {'section': 'task', 'request': 'deleteTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletetaskjson)
    return resp.json()


def purgetask(taskid):
    purgetaskjson = {'section': 'task', 'request': 'purgeTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=purgetaskjson)
    return resp.json()


def tasksetsupertaskname(supertaskid, name):
    tasksetsupertasknamejson = {'section': 'task', 'request': 'setSupertaskName', 'supertaskId': supertaskid,
                                'name': name,
                                'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=tasksetsupertasknamejson)
    return resp.json()


def taskdeletesupertask(supertaskid):
    taskdeletesupertaskjson = {'section': 'task', 'request': 'deleteSupertask', 'supertaskId': supertaskid,
                               'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=taskdeletesupertaskjson)
    return resp.json()


def archivetask(taskid):
    archivetaskjson = {'section': 'task', 'request': 'archiveTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=archivetaskjson)
    return resp.json()


def archivesupertask(supertaskid):
    archivesupertaskjson = {'section': 'task', 'request': 'archiveSupertask', 'supertaskId': supertaskid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=archivesupertaskjson)
    return resp.json()


# Preconfigured Tasks (pretask)
def setpretaskpriority(pretaskid, priority):
    setpretaskpriorityjson = {'section': 'pretask', 'request': 'setPretaskPriority', 'pretaskId': pretaskid,
                              'priority': priority, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskpriorityjson)
    return resp.json()


def setpretaskname(pretaskid, name):
    setpretasknamejson = {'section': 'pretask', 'request': 'setPretaskName', 'pretaskId': pretaskid, 'name': name,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretasknamejson)
    return resp.json()


def setpretaskcolor(pretaskid, color):
    setpretaskcolorjson = {'section': 'pretask', 'request': 'setPretaskColor', 'pretaskId': pretaskid, 'color': color,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskcolorjson)
    return resp.json()


def setpretaskchunksize(pretaskid, chunksize):
    setpretaskchunksizejson = {'section': 'pretask', 'request': 'setPretaskChunksize', 'pretaskId': pretaskid,
                               'chunksize': chunksize, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskchunksizejson)
    return resp.json()


def setpretaskcpuonly(pretaskid, iscpuonly):
    setpretaskcpuonlyjson = {'section': 'pretask', 'request': 'setPretaskCpuOnly', 'pretaskId': pretaskid,
                             'isCpuOnly': iscpuonly, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskcpuonlyjson)
    return resp.json()


def setpretasksmall(pretaskid, issmall):
    setpretasksmalljson = {'section': 'pretask', 'request': 'setPretaskSmall', 'pretaskId': pretaskid,
                           'isSmall': issmall,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretasksmalljson)
    return resp.json()


def deletepretask(pretaskid):
    deletepretaskjson = {'section': 'pretask', 'request': 'deletePretask', 'pretaskId': pretaskid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletepretaskjson)
    return resp.json()


# files must be an array, []. or [1], or [1,2]
def createpretask(name, attackcmd, chunksize, statustimer, benchmarktype, color,
                  iscpuonly, issmall, priority, files, crackertypeid):
    createpretaskjson = {'section': 'pretask', 'request': 'createPreTask', 'name': name, 'attackCmd': attackcmd,
                         'chunksize': chunksize, 'statusTimer': statustimer, 'benchmarkType': benchmarktype,
                         'color': color,
                         'isCpuOnly': iscpuonly, 'isSmall': issmall, 'priority': priority, 'files': files,
                         'crackerTypeId': crackertypeid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createpretaskjson)
    return resp.json()


def listpretasks():
    listpretasksjson = {'section': 'pretask', 'request': 'listPretasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listpretasksjson)
    return resp.json()


def getpretask(pretaskid):
    getpretaskjson = {'section': 'pretask', 'request': 'getPretask', 'pretaskId': pretaskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getpretaskjson)
    return resp.json()


# Supertasks - supertask
# masks must be an array ["?d?d?d?d", "?a?a?a"]
def importsupertask(name, iscpuonly, issmall, masks, optimizedflag, crackertypeid):
    importsupertaskjson = {'section': 'supertask', 'request': 'importSupertask', 'name': name, 'isCpuOnly': iscpuonly,
                           'isSmall': issmall, 'masks': masks, 'optimizedFlag': optimizedflag,
                           'crackerTypeId': crackertypeid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=importsupertaskjson)
    return resp.json()


def listsupertasks():
    listsupertasksjson = {'section': 'supertask', 'request': 'listSupertasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsupertasksjson)
    return resp.json()


def getsupertask(supertaskid):
    getsupertaskjson = {'section': 'supertask', 'request': 'getSupertask', 'supertaskId': supertaskid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getsupertaskjson)
    return resp.json()


# pretasks must be an array [7, 8]
def createsupertask(name, pretasks):
    createsupertaskjson = {'section': 'supertask', 'request': 'createSupertask', 'name': name, 'pretasks': pretasks,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createsupertaskjson)
    return resp.json()


def setsupertaskname(supertaskid, name):
    setsupertasknamejson = {'section': 'supertask', 'request': 'setSupertaskName', 'supertaskId': supertaskid,
                            'name': name,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setsupertasknamejson)
    return resp.json()


def deletesupertask(supertaskid):
    deletesupertaskjson = {'section': 'supertask', 'request': 'deleteSupertask', 'supertaskId': supertaskid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletesupertaskjson)
    return resp.json()


# Hashlists - hashlist

def listhashlists():
    listhashlistsjson = {'section': 'hashlist', 'request': 'listHashlists', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listhashlistsjson)
    return resp.json()


def gethashlist(hashlistid):
    gethashlistjson = {'section': 'hashlist', 'request': 'getHashlist', 'hashlistId': hashlistid,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gethashlistjson)
    return resp.json()


def createhashlist(name, issalted, issecret, ishexsalt, separator, hashformat,
                   hashtypeid, accessgroupid, data, usebrain, brainfeatures):
    createhashlistjson = {'section': 'hashlist', 'request': 'createHashlist', 'name': name, 'isSalted': issalted,
                          'isSecret': issecret, 'isHexSalt': ishexsalt, 'separator': separator, 'format': hashformat,
                          'hashtypeId': hashtypeid, 'accessGroupId': accessgroupid, 'data': data, 'useBrain': usebrain,
                          'brainFeatures': brainfeatures, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createhashlistjson)
    return resp.json()


def sethashlistname(hashlistid, name):
    sethashlistnamejson = {'section': 'hashlist', 'request': 'setHashlistName', 'name': name, 'hashlistId': hashlistid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=sethashlistnamejson)
    return resp.json()


def sethashlistsecret(hashlistid, issecret):
    sethashlistsecretjson = {'section': 'hashlist', 'request': 'setSecret', 'isSecret': issecret,
                             'hashlistId': hashlistid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=sethashlistsecretjson)
    return resp.json()


def importcracked(hashlistid, separator, data):
    importcrackedjson = {'section': 'hashlist', 'request': 'importCracked', 'hashlistId': hashlistid,
                         'separator': separator, 'data': data, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=importcrackedjson)
    return resp.json()


def exportcracked(hashlistid):
    exportcrackedjson = {'section': 'hashlist', 'request': 'exportCracked', 'hashlistId': hashlistid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=exportcrackedjson)
    return resp.json()


def generatewordlist(hashlistid):
    generatewordlistjson = {'section': 'hashlist', 'request': 'generateWordlist', 'hashlistId': hashlistid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=generatewordlistjson)
    return resp.json()


def exportleft(hashlistid):
    exportleftjson = {'section': 'hashlist', 'request': 'exportLeft', 'hashlistId': hashlistid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=exportleftjson)
    return resp.json()


def deletehashlist(hashlistid):
    deletehashlistjson = {'section': 'hashlist', 'request': 'deleteHashlist', 'hashlistId': hashlistid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletehashlistjson)
    return resp.json()


def gethash(gethashentry):
    gethashjson = {'section': 'hashlist', 'request': 'getHash', 'hash': gethashentry, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gethashjson)
    return resp.json()


def gethashlistcracked(hashlistid):
    gethashlistcrackedjson = {'section': 'hashlist', 'request': 'getCracked', 'hashlistId': hashlistid,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gethashlistcrackedjson)
    return resp.json()


# Superhashlists - superhashlist
def listsuperhashlists():
    listsuperhashlistsjson = {'section': 'superhashlist', 'request': 'listSuperhashlists', "accessKey": accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsuperhashlistsjson)
    return resp.json()


def getsuperhashlist(superhashlistid):
    getsuperhashlistjson = {'section': 'superhashlist', 'request': 'getSuperhashlist',
                            'superhashlistId': superhashlistid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getsuperhashlistjson)
    return resp.json()


# hashlists must be in the format of [1,2]
def createsuperhashlist(superhashlistname, hashlists):
    createsuperhashlistjson = {'section': 'superhashlist', 'request': 'createSuperhashlist',
                               'name': superhashlistname,
                               'hashlists': hashlists, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createsuperhashlistjson)
    return resp.json()


def deletesuperhashlist(superhashlistid):
    deletesuperhashlistjson = {'section': 'superhashlist', 'request': 'deleteSuperhashlist',
                               'superhashlistId': superhashlistid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletesuperhashlistjson)
    return resp.json()


# files - file
# 0 - wordlist
# 1 - rule

def listfiles():
    listfilesjson = {'section': 'file', 'request': 'listFiles', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listfilesjson)
    return resp.json()


def getfile(fileid):
    getfilejson = {'section': 'file', 'request': 'getFile', 'fileId': fileid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getfilejson)
    return resp.json()


def renamefile(fileid, filename):
    renamefilejson = {'section': 'file', 'request': 'renameFile', 'fileId': fileid, 'filename': filename,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=renamefilejson)
    return resp.json()


def setfilesecret(fileid, issecret):
    setfilesecretjson = {'section': 'file', 'request': 'setSecret', 'fileId': fileid, 'isSecret': issecret,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setfilesecretjson)
    return resp.json()


def deletefile(fileid):
    deletefilejson = {'section': 'file', 'request': 'deleteFile', 'fileId': fileid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletefilejson)
    return resp.json()


def setfiletype(fileid, filetype):
    setfiletypejson = {'section': 'file', 'request': 'setFileType', 'fileId': fileid, 'fileType': filetype,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setfiletypejson)
    return resp.json()


# add file type can use 3 call methods for adding a file - source
# inline - data = base64 encoded
# url - data = url to downlaod stuff from
# import - data = filename in the import dir
# filename doesn't matter in url or import

def addfile(filename, filetype, source, accessgroupid, data):
    addfilejson = {'section': 'file', 'request': 'addFile', 'filename': filename, 'fileType': filetype,
                   'source': source,
                   'accessGroupId': accessgroupid, 'data': data, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=addfilejson)
    return resp.json()


# crackers - cracker
def listcrackers():
    listcrackersjson = {'section': 'cracker', 'request': 'listCrackers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listcrackersjson)
    return resp.json()


def getcracker(crackertypeid):
    getcrackerjson = {'section': 'cracker', 'request': 'getCracker', 'crackerTypeId': crackertypeid,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getcrackerjson)
    return resp.json()


def deletecracker(crackertypeid):
    deletecrackerjson = {'section': 'cracker', 'request': 'deleteCracker', 'crackerTypeId': crackertypeid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletecrackerjson)
    return resp.json()


def deleteversion(crackerversionid):
    deleteversionjson = {'section': 'cracker', 'request': 'deleteVersion', 'crackerVersionId': crackerversionid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deleteversionjson)
    return resp.json()


def createcracker(crackername):
    createcrackerjson = {'section': 'cracker', 'request': 'createCracker', 'crackerName': crackername,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createcrackerjson)
    return resp.json()


def addversion(crackertypeid, crackerbinaryversion, crackerbinarybasename,
               crackerbinaryurl):
    addversionjson = {'section': 'cracker', 'request': 'addVersion', 'crackerTypeId': crackertypeid,
                      'crackerBinaryVersion': crackerbinaryversion, 'crackerBinaryBasename': crackerbinarybasename,
                      'crackerBinaryUrl': crackerbinaryurl, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=addversionjson)
    return resp.json()


def updateversion(crackerversionid, crackerbinaryversion, crackerbinarybasename,
                  crackerbinaryurl):
    updateversionjson = {'section': 'cracker', 'request': 'updateVersion', 'crackerVersionId': crackerversionid,
                         'crackerBinaryVersion': crackerbinaryversion, 'crackerBinaryBasename': crackerbinarybasename,
                         'crackerBinaryUrl': crackerbinaryurl, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=updateversionjson)
    return resp.json()
