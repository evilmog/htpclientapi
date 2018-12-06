import requests

requests.packages.urllib3.disable_warnings()


# Test Section
def test_connection(endpoint, certpath):
    testjson = {'section': 'test', 'request': 'connection'}
    resp = requests.post(endpoint, verify=certpath, json=testjson)
    return resp.json()["response"]


def test_access(endpoint, certpath, accesskey):
    accessjson = {'section': 'test', 'request': 'access', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=accessjson)
    return resp.json()["response"]


# User Section
def listusers(endpoint, certpath, accesskey):
    listusersjson = {'section': 'user', 'request': 'listUsers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listusersjson)
    return resp.json()


def getuser(endpoint, certpath, accesskey, userid):
    getuserjson = {'section': 'user', 'request': 'getUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getuserjson)
    return resp.json()


def createuser(endpoint, certpath, accesskey, username, email, rightgroupid):
    createuserjson = {'section': 'user', 'request': 'createUser', 'username': username, 'email': email,
                      'rightGroupId': rightgroupid,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createuserjson)
    return resp.json()


def disableuser(endpoint, certpath, accesskey, userid):
    disableuserjson = {'section': 'user', 'request': 'disableUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=disableuserjson)
    return resp.json()


def enableuser(endpoint, certpath, accesskey, userid):
    enableuserjson = {'section': 'user', 'request': 'enableUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=enableuserjson)
    return resp.json()


def setuserpassword(endpoint, certpath, accesskey, userid, password):
    setuserpasswordjson = {'section': 'user', 'request': 'setUserPassword', 'userId': userid, 'password': password,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setuserpasswordjson)
    return resp.json()


def setuserrightgroup(endpoint, certpath, accesskey, userid, rightgroupid):
    setuserrightgroupjson = {'section': 'user', 'request': 'setUserRightGroup', 'userId': userid,
                             'rightGroupId': rightgroupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setuserrightgroupjson)
    return resp.json()


# Group Section
def listgroups(endpoint, certpath, accesskey):
    listgroupsjson = {'section': 'group', 'request': 'listGroups', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listgroupsjson)
    return resp.json()


def getgroup(endpoint, certpath, accesskey, groupid):
    getgroupjson = {'section': 'group', 'request': 'getGroup', 'groupId': groupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getgroupjson)
    return resp.json()


def creategroup(endpoint, certpath, accesskey, name):
    creategroupjson = {'section': 'group', 'request': 'createGroup', 'name': name, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=creategroupjson)
    return resp.json()


def addagent(endpoint, certpath, accesskey, groupid, agentid):
    addagentjson = {'section': 'group', 'request': 'addAgent', 'groupId': groupid, 'agentId': agentid,
                    'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=addagentjson)
    return resp.json()


def removeagent(endpoint, certpath, accesskey, groupid, agentid):
    removeagentjson = {'section': 'group', 'request': 'removegent', 'groupId': groupid, 'agentId': agentid,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=removeagentjson)
    return resp.json()


def adduser(endpoint, certpath, accesskey, groupid, userid):
    adduserjson = {'section': 'group', 'request': 'addUser', 'groupId': groupid, 'userId': userid,
                   'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=adduserjson)
    return resp.json()


def removeuser(endpoint, certpath, accesskey, groupid, userid):
    removeuserjson = {'section': 'group', 'request': 'removeUser', 'groupId': groupid, 'userId': userid,
                      'accesskey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=removeuserjson)
    return resp.json()


def deletegroup(endpoint, certpath, accesskey, groupid):
    deletegroupjson = {'section': 'group', 'request': 'deleteGroup', 'groupId': groupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletegroupjson)
    return resp.json()


# Access Section
def listaccessgroups(endpoint, certpath, accesskey):
    listgroupsjson = {'section': 'access', 'request': 'listGroups', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listgroupsjson)
    return resp.json()


def getaccessgroup(endpoint, certpath, accesskey, rightgroupid):
    getaccessgroupjson = {'section': 'access', 'request': 'getGroup', 'rightGroupId': rightgroupid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getaccessgroupjson)
    return resp.json()


def createaccessgroup(endpoint, certpath, accesskey, name):
    createaccessgroupjson = {'section': 'access', 'request': 'createGroup', 'name': name, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createaccessgroupjson)
    return resp.json()


def deleteaccessgroup(endpoint, certpath, accesskey, rightgroupid):
    deleteaccessgroupjson = {'section': 'access', 'request': 'deleteGroup', 'rightGroupId': rightgroupid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deleteaccessgroupjson)
    return resp.json()


def setaccesspermissions(endpoint, certpath, accesskey, rightgroupid, viewhashlistaccess, managehashlistaccess,
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

def getinformation(endpoint, certpath, accesskey):
    getinformationjson = {'section': 'account', "request": "getInformation", 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getinformationjson)
    return resp.json()


def setemail(endpoint, certpath, accesskey, email):
    setemailjson = {'section': 'account', "request": "setEmail", "email": email, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setemailjson)
    return resp.json()


def setsessionlength(endpoint, certpath, accesskey, sessionlength):
    setsessionlengthjson = {'section': 'account', 'request': 'setSessionLength', 'sessionLength': sessionlength,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setsessionlengthjson)
    return resp.json()


def changepassword(endpoint, certpath, accesskey, newpassword, oldpassword):
    changepasswordjson = {'section': 'account', 'request': 'changePassword', 'newPassword': newpassword,
                          'oldPassword': oldpassword, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=changepasswordjson)
    return resp.json()


# Server Config
def listsections(endpoint, certpath, accesskey):
    listsectionsjson = {'section': 'config', 'request': 'listSections', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsectionsjson)
    return resp.json()


def listconfig(endpoint, certpath, accesskey):
    listconfigjson = {'section': 'config', 'request': 'listConfig', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listconfigjson)
    return resp.json()


def getconfig(endpoint, certpath, accesskey, configitem):
    getconfigjson = {'section': 'config', 'request': 'getConfig', 'configItem': configitem, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getconfigjson)
    return resp.json()


def setconfig(endpoint, certpath, accesskey, configitem, value, force):
    setconfigjson = {'section': 'config', 'request': 'setConfig', 'configItem': configitem, 'value': value,
                     'force': force,
                     'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setconfigjson)
    return resp.json()


# Agents
def listagents(endpoint, certpath, accesskey):
    listagentsjson = {'section': 'agent', 'request': 'listAgents', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listagentsjson)
    return resp.json()


def getagent(endpoint, certpath, accesskey, agentid):
    getagentjson = {'section': 'agent', 'request': 'get', 'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getagentjson)
    return resp.json()


def setagentactive(endpoint, certpath, accesskey, agentid, active):
    setagentactivejson = {'section': 'agent', 'request': 'setActive', 'active': active, 'agentId': agentid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentactivejson)
    return resp.json()


def changeagentowner(endpoint, certpath, accesskey, agentid, user):
    changeagentownerjson = {'section': 'agent', 'request': 'changeOwner', 'user': user, 'agentId': agentid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=changeagentownerjson)
    return resp.json()


def setagentname(endpoint, certpath, accesskey, agentid, name):
    setagentnamejson = {'section': 'agent', 'request': 'setName', 'name': name, 'agentId': agentid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentnamejson)
    return resp.json()


def setagentcpuonly(endpoint, certpath, accesskey, agentid, cpuonly):
    setagentcpuonlyjson = {'section': 'agent', 'request': 'setCpuOnly', 'cpuOnly': cpuonly, 'agentId': agentid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentcpuonlyjson)
    return resp.json()


def setagentextraparams(endpoint, certpath, accesskey, agentid, extraparameters):
    setagentextraparamsjson = {'section': 'agent', 'request': 'setExtraParams', 'extraParameters': extraparameters,
                               'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentextraparamsjson)
    return resp.json()


def setagenterrorflag(endpoint, certpath, accesskey, agentid, ignoreerrors):
    setagentextraparamsjson = {'section': 'agent', 'request': 'setErrorFlag', 'ignoreErrors': ignoreerrors,
                               'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagentextraparamsjson)
    return resp.json()


def setagenttrusted(endpoint, certpath, accesskey, agentid, trusted):
    setagenttrustedjson = {'section': 'agent', 'request': 'setTrusted', 'trusted': trusted, 'agentId': agentid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setagenttrustedjson)
    return resp.json()


def listagentvouchers(endpoint, certpath, accesskey):
    listagentvouchersjson = {'section': 'agent', 'request': 'listVouchers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listagentvouchersjson)
    return resp.json()


def createagentvoucherrandom(endpoint, certpath, accesskey):
    createagentvoucherrandomjson = {'section': 'agent', 'request': 'createVoucher', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createagentvoucherrandomjson)
    return resp.json()


def createagentvoucher(endpoint, certpath, accesskey, voucher):
    createagentvoucherjson = {'section': 'agent', 'request': 'createVoucher', 'voucher': voucher,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createagentvoucherjson)
    return resp.json()


def deleteagentvoucher(endpoint, certpath, accesskey, voucher):
    deleteagentvoucherjson = {'section': 'agent', 'request': 'deleteVoucher', 'voucher': voucher,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deleteagentvoucherjson)
    return resp.json()


def getagentbinaries(endpoint, certpath, accesskey):
    getagentbinariesjson = {'section': 'agent', 'request': 'getBinaries', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getagentbinariesjson)
    return resp.json()


# Task Section

def listtasks(endpoint, certpath, accesskey):
    listtasksjson = {'section': 'task', 'request': 'listTasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listtasksjson)
    return resp.json()


def gettask(endpoint, certpath, accesskey, taskid):
    gettaskjson = {'section': 'task', 'request': 'getTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gettaskjson)
    return resp.json()


def gettaskcracked(endpoint, certpath, accesskey, taskid):
    gettaskcrackedjson = {'section': 'task', 'request': 'getCracked', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=gettaskcrackedjson)
    return resp.json()


def listsubtasks(endpoint, certpath, accesskey, supertaskid):
    listsubtasksjson = {'section': 'task', 'request': 'listSubtasks', 'superTaskId': supertaskid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsubtasksjson)
    return resp.json()


def getchunk(endpoint, certpath, accesskey, chunkid):
    getchunkjson = {'section': 'task', 'request': 'getChunk', 'chunkId': chunkid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getchunkjson)
    return resp.json()


# files must be an array [] or [1,2]
def createtask(endpoint, certpath, accesskey, name, hashlistid, attackcmd, chunksize, statustimer, benchmarktype, color,
               iscpuonly, issmall, skip, crackerversionid, priority, files, isprince):
    createtaskjson = {'section': 'task', 'request': 'createTask', 'name': name, 'hashlistId': hashlistid,
                      'attackCmd': attackcmd, 'chunksize': chunksize, 'statusTimer': statustimer,
                      'benchmarkType': benchmarktype, 'color': color, 'isCpuOnly': iscpuonly, 'isSmall': issmall,
                      'skip': skip, 'crackerVersionId': crackerversionid, 'files': files, 'priority': priority,
                      'isPrince': isprince, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createtaskjson)
    return resp.json()


def runpretask(endpoint, certpath, accesskey, name, hashlistid, pretaskid, crackerversionid):
    runpretaskjson = {'section': 'task', 'request': 'runPretask', 'name': name, 'hashlistId': hashlistid,
                      'pretaskId': pretaskid, 'crackerVersionId': crackerversionid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=runpretaskjson)
    return resp.json()


def runsupertask(endpoint, certpath, accesskey, hashlistid, supertaskid, crackerversionid):
    runsupertaskjson = {'section': 'task', 'request': 'runSupertask', 'hashlistId': hashlistid,
                        'supertaskId': supertaskid,
                        'crackerVersionId': crackerversionid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=runsupertaskjson)
    return resp.json()


def settaskpriority(endpoint, certpath, accesskey, taskid, priority):
    settaskpriorityjson = {'section': 'task', 'request': 'setTaskPriority', 'taskId': taskid, 'priority': priority,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settaskpriorityjson)
    return resp.json()


def setsupertaskpriority(endpoint, certpath, accesskey, supertaskid, supertaskpriority):
    setsupertaskpriorityjson = {'section': 'task', 'request': 'setSupertaskPriority', 'supertaskId': supertaskid,
                                'supertaskPriority': supertaskpriority, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setsupertaskpriorityjson)
    return resp.json()


def settaskname(endpoint, certpath, accesskey, taskid, name):
    settasknamejson = {'section': 'task', 'request': 'setTaskName', 'taskId': taskid, 'name': name,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settasknamejson)
    return resp.json()


def settaskcolor(endpoint, certpath, accesskey, taskid, color):
    settaskcolorjson = {'section': 'task', 'request': 'setTaskColor', 'taskId': taskid, 'color': color,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settaskcolorjson)
    return resp.json()


def settaskcpuonly(endpoint, certpath, accesskey, taskid, iscpuonly):
    settaskcpuonlyjson = {'section': 'task', 'request': 'setTaskCpuOnly', 'taskId': taskid, 'isCpuOnly': iscpuonly,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settaskcpuonlyjson)
    return resp.json()


def settasksmall(endpoint, certpath, accesskey, taskid, issmall):
    settasksmalljson = {'section': 'task', 'request': 'setTaskSmall', 'taskId': taskid, 'isSmall': issmall,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=settasksmalljson)
    return resp.json()


def taskunassignagent(endpoint, certpath, accesskey, agentid):
    taskunassignagentjson = {'section': 'task', 'request': 'taskUnassignAgent', 'agentId': agentid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=taskunassignagentjson)
    return resp.json()


def deletetask(endpoint, certpath, accesskey, taskid):
    deletetaskjson = {'section': 'task', 'request': 'deleteTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletetaskjson)
    return resp.json()


def purgetask(endpoint, certpath, accesskey, taskid):
    purgetaskjson = {'section': 'task', 'request': 'purgeTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=purgetaskjson)
    return resp.json()


def tasksetsupertaskname(endpoint, certpath, accesskey, supertaskid, name):
    tasksetsupertasknamejson = {'section': 'task', 'request': 'setSupertaskName', 'supertaskId': supertaskid,
                                'name': name,
                                'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=tasksetsupertasknamejson)
    return resp.json()


def taskdeletesupertask(endpoint, certpath, accesskey, supertaskid):
    taskdeletesupertaskjson = {'section': 'task', 'request': 'deleteSupertask', 'supertaskId': supertaskid,
                               'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=taskdeletesupertaskjson)
    return resp.json()


def archivetask(endpoint, certpath, accesskey, taskid):
    archivetaskjson = {'section': 'task', 'request': 'archiveTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=archivetaskjson)
    return resp.json()


def archivesupertask(endpoint, certpath, accesskey, supertaskid):
    archivesupertaskjson = {'section': 'task', 'request': 'archiveSupertask', 'supertaskId': supertaskid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=archivesupertaskjson)
    return resp.json()


# Preconfigured Tasks (pretask)
def setpretaskpriority(endpoint, certpath, accesskey, pretaskid, priority):
    setpretaskpriorityjson = {'section': 'pretask', 'request': 'setPretaskPriority', 'pretaskId': pretaskid,
                              'priority': priority, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskpriorityjson)
    return resp.json()


def setpretaskname(endpoint, certpath, accesskey, pretaskid, name):
    setpretasknamejson = {'section': 'pretask', 'request': 'setPretaskName', 'pretaskId': pretaskid, 'name': name,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretasknamejson)
    return resp.json()


def setpretaskcolor(endpoint, certpath, accesskey, pretaskid, color):
    setpretaskcolorjson = {'section': 'pretask', 'request': 'setPretaskColor', 'pretaskId': pretaskid, 'color': color,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskcolorjson)
    return resp.json()


def setpretaskchunksize(endpoint, certpath, accesskey, pretaskid, chunksize):
    setpretaskchunksizejson = {'section': 'pretask', 'request': 'setPretaskChunksize', 'pretaskId': pretaskid,
                               'chunksize': chunksize, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskchunksizejson)
    return resp.json()


def setpretaskcpuonly(endpoint, certpath, accesskey, pretaskid, iscpuonly):
    setpretaskcpuonlyjson = {'section': 'pretask', 'request': 'setPretaskCpuOnly', 'pretaskId': pretaskid,
                             'isCpuOnly': iscpuonly, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretaskcpuonlyjson)
    return resp.json()


def setpretasksmall(endpoint, certpath, accesskey, pretaskid, issmall):
    setpretasksmalljson = {'section': 'pretask', 'request': 'setPretaskSmall', 'pretaskId': pretaskid,
                           'isSmall': issmall,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setpretasksmalljson)
    return resp.json()


def deletepretask(endpoint, certpath, accesskey, pretaskid):
    deletepretaskjson = {'section': 'pretask', 'request': 'deletePretask', 'pretaskId': pretaskid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletepretaskjson)
    return resp.json()


# files must be an array, []. or [1], or [1,2]
def createpretask(endpoint, certpath, accesskey, name, attackcmd, chunksize, statustimer, benchmarktype, color,
                  iscpuonly, issmall, priority, files, crackertypeid):
    createpretaskjson = {'section': 'pretask', 'request': 'createPreTask', 'name': name, 'attackCmd': attackcmd,
                         'chunksize': chunksize, 'statusTimer': statustimer, 'benchmarkType': benchmarktype,
                         'color': color,
                         'isCpuOnly': iscpuonly, 'isSmall': issmall, 'priority': priority, 'files': files,
                         'crackerTypeId': crackertypeid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createpretaskjson)
    return resp.json()


def listpretasks(endpoint, certpath, accesskey):
    listpretasksjson = {'section': 'pretask', 'request': 'listPretasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listpretasksjson)
    return resp.json()


def getpretask(endpoint, certpath, accesskey, pretaskid):
    getpretaskjson = {'section': 'pretask', 'request': 'getPretask', 'pretaskId': pretaskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getpretaskjson)
    return resp.json()


# Supertasks - supertask
# masks must be an array ["?d?d?d?d", "?a?a?a"]
def importsupertask(endpoint, certpath, accesskey, name, iscpuonly, issmall, masks, optimizedflag, crackertypeid):
    importsupertaskjson = {'section': 'supertask', 'request': 'importSupertask', 'name': name, 'isCpuOnly': iscpuonly,
                           'isSmall': issmall, 'masks': masks, 'optimizedFlag': optimizedflag,
                           'crackerTypeId': crackertypeid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=importsupertaskjson)
    return resp.json()


def listsupertasks(endpoint, certpath, accesskey):
    listsupertasksjson = {'section': 'supertask', 'request': 'listSupertasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=listsupertasksjson)
    return resp.json()


def getsupertask(endpoint, certpath, accesskey, supertaskid):
    getsupertaskjson = {'section': 'supertask', 'request': 'getSupertask', 'supertaskId': supertaskid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=getsupertaskjson)
    return resp.json()


# pretasks must be an array [7, 8]
def createsupertask(endpoint, certpath, accesskey, name, pretasks):
    createsupertaskjson = {'section': 'supertask', 'request': 'createSupertask', 'name': name, 'pretasks': pretasks,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=createsupertaskjson)
    return resp.json()


def setsupertaskname(endpoint, certpath, accesskey, supertaskid, name):
    setsupertasknamejson = {'section': 'supertask', 'request': 'setSupertaskName', 'supertaskId': supertaskid,
                            'name': name,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=setsupertasknamejson)
    return resp.json()


def deletesupertask(endpoint, certpath, accesskey, supertaskid):
    deletesupertaskjson = {'section': 'supertask', 'request': 'deleteSupertask', 'supertaskId': supertaskid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=certpath, json=deletesupertaskjson)
    return resp.json()


# Hashlists - hashlist

def listHashlists(endpoint, certpath, accessKey):
    listhashlists = {'section': 'hashlist', 'request': 'listHashlists', 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=listhashlists)
    return resp.json()


def getHashlist(endpoint, certpath, accessKey, hashlistId):
    gethashlist = {'section': 'hashlist', 'request': 'getHashlist', 'hashlistId': hashlistId, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=gethashlist)
    return resp.json()


def createHashlist(endpoint, certpath, accessKey, name, isSalted, isSecret, isHexSalt, separator, format, hashtypeId,
                   accessGroupId, data, useBrain, brainFeatures):
    createhashlist = {'section': 'hashlist', 'request': 'createHashlist', 'name': name, 'isSalted': isSalted,
                      'isSecret': isSecret, 'isHexSalt': isHexSalt, 'separator': separator, 'format': format,
                      'hashtypeId': hashtypeId, 'accessGroupId': accessGroupId, 'data': data, 'useBrain': useBrain,
                      'brainFeatures': brainFeatures, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=createhashlist)
    return resp.json()


def setHashlistName(endpoint, certpath, accessKey, hashlistId, name):
    sethashlistname = {'section': 'hashlist', 'request': 'setHashlistName', 'name': name, 'hashlistId': hashlistId,
                       'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=sethashlistname)
    return resp.json()


def setHashlistSecret(endpoint, certpath, accessKey, hashlistId, isSecret):
    setsecret = {'section': 'hashlist', 'request': 'setSecret', 'isSecret': isSecret, 'hashlistId': hashlistId,
                 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=setsecret)
    return resp.json()


def importCracked(endpoint, certpath, accessKey, hashlistId, separator, data):
    importcracked = {'section': 'hashlist', 'request': 'importCracked', 'hashlistId': hashlistId,
                     'separator': separator, 'data': data, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=importcracked)
    return resp.json()


def exportCracked(endpoint, certpath, accessKey, hashlistId):
    importcracked = {'section': 'hashlist', 'request': 'exportCracked', 'hashlistId': hashlistId,
                     'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=importcracked)
    return resp.json()


def generateWordlist(endpoint, certpath, accessKey, hashlistId):
    generatewordlist = {'section': 'hashlist', 'request': 'generateWordlist', 'hashlistId': hashlistId,
                        'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=generatewordlist)
    return resp.json()


def exportLeft(endpoint, certpath, accessKey, hashlistId):
    exportleft = {'section': 'hashlist', 'request': 'exportLeft', 'hashlistId': hashlistId, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=exportleft)
    return resp.json()


def deleteHashlist(endpoint, certpath, accessKey, hashlistId):
    deletehashlist = {'section': 'hashlist', 'request': 'deleteHashlist', 'hashlistId': hashlistId,
                      'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=deleteHashlist)
    return resp.json()


def getHash(endpoint, certpath, accessKey, hash):
    gethash = {'section': 'hashlist', 'request': 'getHash', 'hash': hash, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=gethash)
    return resp.json()


def getHashlistCracked(endpoint, certpath, accessKey, hashlistId):
    gethashlistcracked = {'section': 'hashlist', 'request': 'getCracked', 'hashlistId': hashlistId,
                          'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=gethashlistcracked)
    return resp.json()


# Superhashlists - superhashlist
def listSuperhashlists(endpoint, certpath, accessKey):
    listsuperhashlists = {'section': 'superhashlist', 'request': 'listSuperhashlists', "accessKey": accessKey}
    resp = requests.post(endpoint, verify=certpath, json=listsuperhashlists)
    return resp.json()


def getSuperhashlist(endpoint, certpath, accessKey, superhashlistId):
    getsuperhashlist = {'section': 'superhashlist', 'request': 'getSuperhashlist', 'superhashlistId': superhashlistId,
                        'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=getsuperhashlist)
    return resp.json()


# hashlists must be in the format of [1,2]
def createSuperhashlist(endpoint, certpath, accessKey, name, hashlists):
    createsuperhashlist = {'section': 'superhashlist', 'request': 'createSuperhashlist', 'name': 'New Superhashlist',
                           'hashlists': hashlists, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=createsuperhashlist)
    return resp.json()


def deleteSuperhashlist(endpoint, certpath, accessKey, superhashlistId):
    deletesuperhashlist = {'section': 'superhashlist"', 'request': 'deleteSuperhashlist',
                           'superhashlistId': superhashlistId, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=deletesuperhashlist)
    return resp.json()


# files - file
# 0 - wordlist
# 1 - rule

def listFiles(endpoint, certpath, accessKey):
    listfiles = {'section': 'file', 'request': 'listFiles', 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=listfiles)
    return resp.json()


def getFile(endpoint, certpath, accessKey, fileId):
    getfile = {'section': 'file', 'request': 'getFile', 'fileId': fileId, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=getfile)
    return resp.json()


def renameFile(endpoint, certpath, accessKey, fileId, filename):
    renamefile = {'section': 'file', 'request': 'renameFile', 'fileId': fileId, 'filename': filename,
                  'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=renamefile)
    return resp.json()


def setFileSecret(endpoint, certpath, accessKey, fileId, isSecret):
    setsecret = {'section': 'file', 'request': 'setSecret', 'fileId': fileId, 'isSecret': isSecret,
                 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=setsecret)
    return resp.json()


def deleteFile(endpoint, certpath, accessKey, fileId):
    deletefile = {'section': 'file', 'request': 'deleteFile', 'fileId': fileId, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=deletefile)
    return resp.json()


def setFileType(endpoint, certpath, accessKey, fileId, fileType):
    setfiletype = {'section': 'file', 'request': 'setFileType', 'fileId': fileId, 'fileType': fileType,
                   'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=setfiletype)
    return resp.json()


# add file type can use 3 call methods for adding a file - source
# inline - data = base64 encoded
# url - data = url to downlaod stuff from
# import - data = filename in the import dir
# filename doesn't matter in url or import

def addFile(endpoint, certpath, accessKey, filename, fileType, source, accessGroupId, data):
    addfile = {'section': 'file', 'request': 'addFile', 'filename': filename, 'fileType': fileType, 'source': source,
               'accessGroupId': accessGroupId, 'data': data, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=addfile)
    return resp.json()


# crackers - cracker
def listCrackers(endpoint, certpath, accessKey):
    listcracker = {'section': 'cracker', 'request': 'listCrackers', 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=listcracker)
    return resp.json()


def getCracker(endpoint, certpath, accessKey, crackerTypeId):
    getcracker = {'section': 'cracker', 'request': 'getCracker', 'crackerTypeId': crackerTypeId, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=getcracker)
    return resp.json()


def deleteCracker(endpoint, certpath, accessKey, crackerTypeId):
    deletecracker = {'section': 'cracker', 'request': 'deleteCracker', 'crackerTypeId': crackerTypeId,
                     'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=deletecracker)
    return resp.json()


def deleteVersion(endpoint, certpath, accessKey, crackerVersionId):
    deleteversion = {'section': 'cracker', 'request': 'deleteVersion', 'crackerVersionId': crackerVersionId,
                     'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=deleteversion)
    return resp.json()


def createCracker(endpoint, certpath, accessKey, crackerName):
    createcracker = {'section': 'cracker', 'request': 'createCracker', 'crackerName': crackerName,
                     'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=createcracker)
    return resp.json()


def addVersion(endpoint, certpath, accessKey, crackerTypeId, crackerBinaryVersion, crackerBinaryBasename,
               crackerBinaryUrl):
    addversion = {'section': 'cracker', 'request': 'addVersion', 'crackerTypeId': crackerTypeId,
                  'crackerBinaryVersion': crackerBinaryVersion, 'crackerBinaryBasename': crackerBinaryBasename,
                  'crackerBinaryUrl': crackerBinaryUrl, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=addversion)
    return resp.json()


def updateVersion(endpoint, certpath, accessKey, crackerVersionId, crackerBinaryVersion, crackerBinaryBasename,
                  crackerBinaryUrl):
    updateVersion = {'section': 'cracker', 'request': 'updateVersion', 'crackerVersionId': crackerVersionId,
                     'crackerBinaryVersion': crackerBinaryVersion, 'crackerBinaryBasename': crackerBinaryBasename,
                     'crackerBinaryUrl': crackerBinaryUrl, 'accessKey': accessKey}
    resp = requests.post(endpoint, verify=certpath, json=updateVersion)
    return resp.json()
