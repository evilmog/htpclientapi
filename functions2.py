import requests

requests.packages.urllib3.disable_warnings()


# Test Section
def test_connection(endpoint, certpath):
    testjson = {'section': 'test', 'request': 'connection'}
    resp = requests.post(endpoint, verify=False, json=testjson)
    return resp.json()["response"]


def test_access(endpoint, certpath, accesskey):
    accessjson = {'section': 'test', 'request': 'access', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=accessjson)
    return resp.json()["response"]


# User Section
def listusers(endpoint, certpath, accesskey):
    listusersjson = {'section': 'user', 'request': 'listUsers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listusersjson)
    return resp.json()


def getuser(endpoint, certpath, accesskey, userid):
    getuserjson = {'section': 'user', 'request': 'getUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getuserjson)
    return resp.json()


def createuser(endpoint, certpath, accesskey, username, email, rightgroupid):
    createuserjson = {'section': 'user', 'request': 'createUser', 'username': username, 'email': email,
                      'rightGroupId': rightgroupid,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createuserjson)
    return resp.json()


def disableuser(endpoint, certpath, accesskey, userid):
    disableuserjson = {'section': 'user', 'request': 'disableUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=disableuserjson)
    return resp.json()


def enableuser(endpoint, certpath, accesskey, userid):
    enableuserjson = {'section': 'user', 'request': 'enableUser', 'userId': userid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=enableuserjson)
    return resp.json()


def setuserpassword(endpoint, certpath, accesskey, userid, password):
    setuserpasswordjson = {'section': 'user', 'request': 'setUserPassword', 'userId': userid, 'password': password,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setuserpasswordjson)
    return resp.json()


def setuserrightgroup(endpoint, certpath, accesskey, userid, rightgroupid):
    setuserrightgroupjson = {'section': 'user', 'request': 'setUserRightGroup', 'userId': userid,
                             'rightGroupId': rightgroupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setuserrightgroupjson)
    return resp.json()


# Group Section
def listgroups(endpoint, certpath, accesskey):
    listgroupsjson = {'section': 'group', 'request': 'listGroups', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listgroupsjson)
    return resp.json()


def getgroup(endpoint, certpath, accesskey, groupid):
    getgroupjson = {'section': 'group', 'request': 'getGroup', 'groupId': groupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getgroupjson)
    return resp.json()


def creategroup(endpoint, certpath, accesskey, name):
    creategroupjson = {'section': 'group', 'request': 'createGroup', 'name': name, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=creategroupjson)
    return resp.json()


def addagent(endpoint, certpath, accesskey, groupid, agentid):
    addagentjson = {'section': 'group', 'request': 'addAgent', 'groupId': groupid, 'agentId': agentid,
                    'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=addagentjson)
    return resp.json()


def removeagent(endpoint, certpath, accesskey, groupid, agentid):
    removeagentjson = {'section': 'group', 'request': 'removeAgent', 'groupId': groupid, 'agentId': agentid,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=removeagentjson)
    return resp.json()


def adduser(endpoint, certpath, accesskey, groupid, userid):
    adduserjson = {'section': 'group', 'request': 'addUser', 'groupId': groupid, 'userId': userid,
                   'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=adduserjson)
    return resp.json()


def removeuser(endpoint, certpath, accesskey, groupid, userid):
    removeuserjson = {'section': 'group', 'request': 'removeUser', 'groupId': groupid, 'userId': userid,
                      'accesskey': accesskey}
    resp = requests.post(endpoint, verify=False, json=removeuserjson)
    return resp.json()


def deletegroup(endpoint, certpath, accesskey, groupid):
    deletegroupjson = {'section': 'group', 'request': 'deleteGroup', 'groupId': groupid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletegroupjson)
    return resp.json()


# Access Section
def listaccessgroups(endpoint, certpath, accesskey):
    listgroupsjson = {'section': 'access', 'request': 'listGroups', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listgroupsjson)
    return resp.json()


def getaccessgroup(endpoint, certpath, accesskey, rightgroupid):
    getaccessgroupjson = {'section': 'access', 'request': 'getGroup', 'rightGroupId': rightgroupid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getaccessgroupjson)
    return resp.json()


def createaccessgroup(endpoint, certpath, accesskey, name):
    createaccessgroupjson = {'section': 'access', 'request': 'createGroup', 'name': name, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createaccessgroupjson)
    return resp.json()


def deleteaccessgroup(endpoint, certpath, accesskey, rightgroupid):
    deleteaccessgroupjson = {'section': 'access', 'request': 'deleteGroup', 'rightGroupId': rightgroupid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deleteaccessgroupjson)
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
    resp = requests.post(endpoint, verify=False, json=setpermissionsjson)
    return resp.json()


# Account Section

def getinformation(endpoint, certpath, accesskey):
    getinformationjson = {'section': 'account', "request": "getInformation", 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getinformationjson)
    return resp.json()


def setemail(endpoint, certpath, accesskey, email):
    setemailjson = {'section': 'account', "request": "setEmail", "email": email, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setemailjson)
    return resp.json()


def setsessionlength(endpoint, certpath, accesskey, sessionlength):
    setsessionlengthjson = {'section': 'account', 'request': 'setSessionLength', 'sessionLength': sessionlength,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setsessionlengthjson)
    return resp.json()


def changepassword(endpoint, certpath, accesskey, newpassword, oldpassword):
    changepasswordjson = {'section': 'account', 'request': 'changePassword', 'newPassword': newpassword,
                          'oldPassword': oldpassword, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=changepasswordjson)
    return resp.json()


# Server Config
def listsections(endpoint, certpath, accesskey):
    listsectionsjson = {'section': 'config', 'request': 'listSections', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listsectionsjson)
    return resp.json()


def listconfig(endpoint, certpath, accesskey):
    listconfigjson = {'section': 'config', 'request': 'listConfig', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listconfigjson)
    return resp.json()


def getconfig(endpoint, certpath, accesskey, configitem):
    getconfigjson = {'section': 'config', 'request': 'getConfig', 'configItem': configitem, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getconfigjson)
    return resp.json()


def setconfig(endpoint, certpath, accesskey, configitem, value, force):
    setconfigjson = {'section': 'config', 'request': 'setConfig', 'configItem': configitem, 'value': value,
                     'force': force,
                     'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setconfigjson)
    return resp.json()


# Agents
def listagents(endpoint, certpath, accesskey):
    listagentsjson = {'section': 'agent', 'request': 'listAgents', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listagentsjson)
    return resp.json()


def getagent(endpoint, certpath, accesskey, agentid):
    getagentjson = {'section': 'agent', 'request': 'get', 'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getagentjson)
    return resp.json()


def setagentactive(endpoint, certpath, accesskey, agentid, active):
    setagentactivejson = {'section': 'agent', 'request': 'setActive', 'active': active, 'agentId': agentid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setagentactivejson)
    return resp.json()


def changeagentowner(endpoint, certpath, accesskey, agentid, user):
    changeagentownerjson = {'section': 'agent', 'request': 'changeOwner', 'user': user, 'agentId': agentid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=changeagentownerjson)
    return resp.json()


def setagentname(endpoint, certpath, accesskey, agentid, name):
    setagentnamejson = {'section': 'agent', 'request': 'setName', 'name': name, 'agentId': agentid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setagentnamejson)
    return resp.json()


def setagentcpuonly(endpoint, certpath, accesskey, agentid, cpuonly):
    setagentcpuonlyjson = {'section': 'agent', 'request': 'setCpuOnly', 'cpuOnly': cpuonly, 'agentId': agentid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setagentcpuonlyjson)
    return resp.json()


def setagentextraparams(endpoint, certpath, accesskey, agentid, extraparameters):
    setagentextraparamsjson = {'section': 'agent', 'request': 'setExtraParams', 'extraParameters': extraparameters,
                               'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setagentextraparamsjson)
    return resp.json()


def setagenterrorflag(endpoint, certpath, accesskey, agentid, ignoreerrors):
    setagentextraparamsjson = {'section': 'agent', 'request': 'setErrorFlag', 'ignoreErrors': ignoreerrors,
                               'agentId': agentid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setagentextraparamsjson)
    return resp.json()


def setagenttrusted(endpoint, certpath, accesskey, agentid, trusted):
    setagenttrustedjson = {'section': 'agent', 'request': 'setTrusted', 'trusted': trusted, 'agentId': agentid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setagenttrustedjson)
    return resp.json()


def listagentvouchers(endpoint, certpath, accesskey):
    listagentvouchersjson = {'section': 'agent', 'request': 'listVouchers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listagentvouchersjson)
    return resp.json()


def createagentvoucherrandom(endpoint, certpath, accesskey):
    createagentvoucherrandomjson = {'section': 'agent', 'request': 'createVoucher', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createagentvoucherrandomjson)
    return resp.json()


def createagentvoucher(endpoint, certpath, accesskey, voucher):
    createagentvoucherjson = {'section': 'agent', 'request': 'createVoucher', 'voucher': voucher,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createagentvoucherjson)
    return resp.json()


def deleteagentvoucher(endpoint, certpath, accesskey, voucher):
    deleteagentvoucherjson = {'section': 'agent', 'request': 'deleteVoucher', 'voucher': voucher,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deleteagentvoucherjson)
    return resp.json()


def getagentbinaries(endpoint, certpath, accesskey):
    getagentbinariesjson = {'section': 'agent', 'request': 'getBinaries', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getagentbinariesjson)
    return resp.json()


# Task Section

def listtasks(endpoint, certpath, accesskey):
    listtasksjson = {'section': 'task', 'request': 'listTasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listtasksjson)
    return resp.json()


def gettask(endpoint, certpath, accesskey, taskid):
    gettaskjson = {'section': 'task', 'request': 'getTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=gettaskjson)
    return resp.json()


def gettaskcracked(endpoint, certpath, accesskey, taskid):
    gettaskcrackedjson = {'section': 'task', 'request': 'getCracked', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=gettaskcrackedjson)
    return resp.json()


def listsubtasks(endpoint, certpath, accesskey, supertaskid):
    listsubtasksjson = {'section': 'task', 'request': 'listSubtasks', 'superTaskId': supertaskid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listsubtasksjson)
    return resp.json()


def getchunk(endpoint, certpath, accesskey, chunkid):
    getchunkjson = {'section': 'task', 'request': 'getChunk', 'chunkId': chunkid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getchunkjson)
    return resp.json()


# files must be an array [] or [1,2]
def createtask(endpoint, certpath, accesskey, name, hashlistid, attackcmd, chunksize, statustimer, benchmarktype, color,
               iscpuonly, issmall, skip, crackerversionid, priority, files, isprince):
    createtaskjson = {'section': 'task', 'request': 'createTask', 'name': name, 'hashlistId': hashlistid,
                      'attackCmd': attackcmd, 'chunksize': chunksize, 'statusTimer': statustimer,
                      'benchmarkType': benchmarktype, 'color': color, 'isCpuOnly': iscpuonly, 'isSmall': issmall,
                      'skip': skip, 'crackerVersionId': crackerversionid, 'files': files, 'priority': priority,
                      'isPrince': isprince, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createtaskjson)
    return resp.json()


def runpretask(endpoint, certpath, accesskey, name, hashlistid, pretaskid, crackerversionid):
    runpretaskjson = {'section': 'task', 'request': 'runPretask', 'name': name, 'hashlistId': hashlistid,
                      'pretaskId': pretaskid, 'crackerVersionId': crackerversionid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=runpretaskjson)
    return resp.json()


def runsupertask(endpoint, certpath, accesskey, hashlistid, supertaskid, crackerversionid):
    runsupertaskjson = {'section': 'task', 'request': 'runSupertask', 'hashlistId': hashlistid,
                        'supertaskId': supertaskid,
                        'crackerVersionId': crackerversionid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=runsupertaskjson)
    return resp.json()


def settaskpriority(endpoint, certpath, accesskey, taskid, priority):
    settaskpriorityjson = {'section': 'task', 'request': 'setTaskPriority', 'taskId': taskid, 'priority': priority,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=settaskpriorityjson)
    return resp.json()


def setsupertaskpriority(endpoint, certpath, accesskey, supertaskid, supertaskpriority):
    setsupertaskpriorityjson = {'section': 'task', 'request': 'setSupertaskPriority', 'supertaskId': supertaskid,
                                'supertaskPriority': supertaskpriority, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setsupertaskpriorityjson)
    return resp.json()


def settaskname(endpoint, certpath, accesskey, taskid, name):
    settasknamejson = {'section': 'task', 'request': 'setTaskName', 'taskId': taskid, 'name': name,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=settasknamejson)
    return resp.json()


def settaskcolor(endpoint, certpath, accesskey, taskid, color):
    settaskcolorjson = {'section': 'task', 'request': 'setTaskColor', 'taskId': taskid, 'color': color,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=settaskcolorjson)
    return resp.json()


def settaskcpuonly(endpoint, certpath, accesskey, taskid, iscpuonly):
    settaskcpuonlyjson = {'section': 'task', 'request': 'setTaskCpuOnly', 'taskId': taskid, 'isCpuOnly': iscpuonly,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=settaskcpuonlyjson)
    return resp.json()


def settasksmall(endpoint, certpath, accesskey, taskid, issmall):
    settasksmalljson = {'section': 'task', 'request': 'setTaskSmall', 'taskId': taskid, 'isSmall': issmall,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=settasksmalljson)
    return resp.json()


def taskunassignagent(endpoint, certpath, accesskey, agentid):
    taskunassignagentjson = {'section': 'task', 'request': 'taskUnassignAgent', 'agentId': agentid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=taskunassignagentjson)
    return resp.json()


def deletetask(endpoint, certpath, accesskey, taskid):
    deletetaskjson = {'section': 'task', 'request': 'deleteTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletetaskjson)
    return resp.json()


def purgetask(endpoint, certpath, accesskey, taskid):
    purgetaskjson = {'section': 'task', 'request': 'purgeTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=purgetaskjson)
    return resp.json()


def tasksetsupertaskname(endpoint, certpath, accesskey, supertaskid, name):
    tasksetsupertasknamejson = {'section': 'task', 'request': 'setSupertaskName', 'supertaskId': supertaskid,
                                'name': name,
                                'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=tasksetsupertasknamejson)
    return resp.json()


def taskdeletesupertask(endpoint, certpath, accesskey, supertaskid):
    taskdeletesupertaskjson = {'section': 'task', 'request': 'deleteSupertask', 'supertaskId': supertaskid,
                               'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=taskdeletesupertaskjson)
    return resp.json()


def archivetask(endpoint, certpath, accesskey, taskid):
    archivetaskjson = {'section': 'task', 'request': 'archiveTask', 'taskId': taskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=archivetaskjson)
    return resp.json()


def archivesupertask(endpoint, certpath, accesskey, supertaskid):
    archivesupertaskjson = {'section': 'task', 'request': 'archiveSupertask', 'supertaskId': supertaskid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=archivesupertaskjson)
    return resp.json()


# Preconfigured Tasks (pretask)
def setpretaskpriority(endpoint, certpath, accesskey, pretaskid, priority):
    setpretaskpriorityjson = {'section': 'pretask', 'request': 'setPretaskPriority', 'pretaskId': pretaskid,
                              'priority': priority, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setpretaskpriorityjson)
    return resp.json()


def setpretaskname(endpoint, certpath, accesskey, pretaskid, name):
    setpretasknamejson = {'section': 'pretask', 'request': 'setPretaskName', 'pretaskId': pretaskid, 'name': name,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setpretasknamejson)
    return resp.json()


def setpretaskcolor(endpoint, certpath, accesskey, pretaskid, color):
    setpretaskcolorjson = {'section': 'pretask', 'request': 'setPretaskColor', 'pretaskId': pretaskid, 'color': color,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setpretaskcolorjson)
    return resp.json()


def setpretaskchunksize(endpoint, certpath, accesskey, pretaskid, chunksize):
    setpretaskchunksizejson = {'section': 'pretask', 'request': 'setPretaskChunksize', 'pretaskId': pretaskid,
                               'chunksize': chunksize, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setpretaskchunksizejson)
    return resp.json()


def setpretaskcpuonly(endpoint, certpath, accesskey, pretaskid, iscpuonly):
    setpretaskcpuonlyjson = {'section': 'pretask', 'request': 'setPretaskCpuOnly', 'pretaskId': pretaskid,
                             'isCpuOnly': iscpuonly, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setpretaskcpuonlyjson)
    return resp.json()


def setpretasksmall(endpoint, certpath, accesskey, pretaskid, issmall):
    setpretasksmalljson = {'section': 'pretask', 'request': 'setPretaskSmall', 'pretaskId': pretaskid,
                           'isSmall': issmall,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setpretasksmalljson)
    return resp.json()


def deletepretask(endpoint, certpath, accesskey, pretaskid):
    deletepretaskjson = {'section': 'pretask', 'request': 'deletePretask', 'pretaskId': pretaskid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletepretaskjson)
    return resp.json()


# files must be an array, []. or [1], or [1,2]
def createpretask(endpoint, certpath, accesskey, name, attackcmd, chunksize, statustimer, benchmarktype, color,
                  iscpuonly, issmall, priority, files, crackertypeid):
    createpretaskjson = {'section': 'pretask', 'request': 'createPreTask', 'name': name, 'attackCmd': attackcmd,
                         'chunksize': chunksize, 'statusTimer': statustimer, 'benchmarkType': benchmarktype,
                         'color': color,
                         'isCpuOnly': iscpuonly, 'isSmall': issmall, 'priority': priority, 'files': files,
                         'crackerTypeId': crackertypeid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createpretaskjson)
    return resp.json()


def listpretasks(endpoint, certpath, accesskey):
    listpretasksjson = {'section': 'pretask', 'request': 'listPretasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listpretasksjson)
    return resp.json()


def getpretask(endpoint, certpath, accesskey, pretaskid):
    getpretaskjson = {'section': 'pretask', 'request': 'getPretask', 'pretaskId': pretaskid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getpretaskjson)
    return resp.json()


# Supertasks - supertask
# masks must be an array ["?d?d?d?d", "?a?a?a"]
def importsupertask(endpoint, certpath, accesskey, name, iscpuonly, issmall, masks, optimizedflag, crackertypeid):
    importsupertaskjson = {'section': 'supertask', 'request': 'importSupertask', 'name': name, 'isCpuOnly': iscpuonly,
                           'isSmall': issmall, 'masks': masks, 'optimizedFlag': optimizedflag,
                           'crackerTypeId': crackertypeid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=importsupertaskjson)
    return resp.json()


def listsupertasks(endpoint, certpath, accesskey):
    listsupertasksjson = {'section': 'supertask', 'request': 'listSupertasks', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listsupertasksjson)
    return resp.json()


def getsupertask(endpoint, certpath, accesskey, supertaskid):
    getsupertaskjson = {'section': 'supertask', 'request': 'getSupertask', 'supertaskId': supertaskid,
                        'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getsupertaskjson)
    return resp.json()


# pretasks must be an array [7, 8]
def createsupertask(endpoint, certpath, accesskey, name, pretasks):
    createsupertaskjson = {'section': 'supertask', 'request': 'createSupertask', 'name': name, 'pretasks': pretasks,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createsupertaskjson)
    return resp.json()


def setsupertaskname(endpoint, certpath, accesskey, supertaskid, name):
    setsupertasknamejson = {'section': 'supertask', 'request': 'setSupertaskName', 'supertaskId': supertaskid,
                            'name': name,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setsupertasknamejson)
    return resp.json()


def deletesupertask(endpoint, certpath, accesskey, supertaskid):
    deletesupertaskjson = {'section': 'supertask', 'request': 'deleteSupertask', 'supertaskId': supertaskid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletesupertaskjson)
    return resp.json()


# Hashlists - hashlist

def listhashlists(endpoint, certpath, accesskey):
    listhashlistsjson = {'section': 'hashlist', 'request': 'listHashlists', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listhashlistsjson)
    return resp.json()


def gethashlist(endpoint, certpath, accesskey, hashlistid):
    gethashlistjson = {'section': 'hashlist', 'request': 'getHashlist', 'hashlistId': hashlistid,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=gethashlistjson)
    return resp.json()


def createhashlist(endpoint, certpath, accesskey, name, issalted, issecret, ishexsalt, separator, hashformat,
                   hashtypeid,
                   accessgroupid, data, usebrain, brainfeatures):
    createhashlistjson = {'section': 'hashlist', 'request': 'createHashlist', 'name': name, 'isSalted': issalted,
                          'isSecret': issecret, 'isHexSalt': ishexsalt, 'separator': separator, 'format': hashformat,
                          'hashtypeId': hashtypeid, 'accessGroupId': accessgroupid, 'data': data, 'useBrain': usebrain,
                          'brainFeatures': brainfeatures, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createhashlistjson)
    return resp.json()


def sethashlistname(endpoint, certpath, accesskey, hashlistid, name):
    sethashlistnamejson = {'section': 'hashlist', 'request': 'setHashlistName', 'name': name, 'hashlistId': hashlistid,
                           'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=sethashlistnamejson)
    return resp.json()


def sethashlistsecret(endpoint, certpath, accesskey, hashlistid, issecret):
    sethashlistsecretjson = {'section': 'hashlist', 'request': 'setSecret', 'isSecret': issecret,
                             'hashlistId': hashlistid,
                             'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=sethashlistsecretjson)
    return resp.json()


def importcracked(endpoint, certpath, accesskey, hashlistid, separator, data):
    importcrackedjson = {'section': 'hashlist', 'request': 'importCracked', 'hashlistId': hashlistid,
                         'separator': separator, 'data': data, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=importcrackedjson)
    return resp.json()


def exportcracked(endpoint, certpath, accesskey, hashlistid):
    exportcrackedjson = {'section': 'hashlist', 'request': 'exportCracked', 'hashlistId': hashlistid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=exportcrackedjson)
    return resp.json()


def generatewordlist(endpoint, certpath, accesskey, hashlistid):
    generatewordlistjson = {'section': 'hashlist', 'request': 'generateWordlist', 'hashlistId': hashlistid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=generatewordlistjson)
    return resp.json()


def exportleft(endpoint, certpath, accesskey, hashlistid):
    exportleftjson = {'section': 'hashlist', 'request': 'exportLeft', 'hashlistId': hashlistid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=exportleftjson)
    return resp.json()


def deletehashlist(endpoint, certpath, accesskey, hashlistid):
    deletehashlistjson = {'section': 'hashlist', 'request': 'deleteHashlist', 'hashlistId': hashlistid,
                          'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletehashlistjson)
    return resp.json()


def gethash(endpoint, certpath, accesskey, gethashentry):
    gethashjson = {'section': 'hashlist', 'request': 'getHash', 'hash': gethashentry, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=gethashjson)
    return resp.json()


def gethashlistcracked(endpoint, certpath, accesskey, hashlistid):
    gethashlistcrackedjson = {'section': 'hashlist', 'request': 'getCracked', 'hashlistId': hashlistid,
                              'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=gethashlistcrackedjson)
    return resp.json()


# Superhashlists - superhashlist
def listsuperhashlists(endpoint, certpath, accesskey):
    listsuperhashlistsjson = {'section': 'superhashlist', 'request': 'listSuperhashlists', "accessKey": accesskey}
    resp = requests.post(endpoint, verify=False, json=listsuperhashlistsjson)
    return resp.json()


def getsuperhashlist(endpoint, certpath, accesskey, superhashlistid):
    getsuperhashlistjson = {'section': 'superhashlist', 'request': 'getSuperhashlist',
                            'superhashlistId': superhashlistid,
                            'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getsuperhashlistjson)
    return resp.json()


# hashlists must be in the format of [1,2]
def createsuperhashlist(endpoint, certpath, accesskey, superhashlistname, hashlists):
    createsuperhashlistjson = {'section': 'superhashlist', 'request': 'createSuperhashlist',
                               'name': superhashlistname,
                               'hashlists': hashlists, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createsuperhashlistjson)
    return resp.json()


def deletesuperhashlist(endpoint, certpath, accesskey, superhashlistid):
    deletesuperhashlistjson = {'section': 'superhashlist"', 'request': 'deleteSuperhashlist',
                               'superhashlistId': superhashlistid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletesuperhashlistjson)
    return resp.json()


# files - file
# 0 - wordlist
# 1 - rule

def listfiles(endpoint, certpath, accesskey):
    listfilesjson = {'section': 'file', 'request': 'listFiles', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listfilesjson)
    return resp.json()


def getfile(endpoint, certpath, accesskey, fileid):
    getfilejson = {'section': 'file', 'request': 'getFile', 'fileId': fileid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getfilejson)
    return resp.json()


def renamefile(endpoint, certpath, accesskey, fileid, filename):
    renamefilejson = {'section': 'file', 'request': 'renameFile', 'fileId': fileid, 'filename': filename,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=renamefilejson)
    return resp.json()


def setfilesecret(endpoint, certpath, accesskey, fileid, issecret):
    setfilesecretjson = {'section': 'file', 'request': 'setSecret', 'fileId': fileid, 'isSecret': issecret,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setfilesecretjson)
    return resp.json()


def deletefile(endpoint, certpath, accesskey, fileid):
    deletefilejson = {'section': 'file', 'request': 'deleteFile', 'fileId': fileid, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletefilejson)
    return resp.json()


def setfiletype(endpoint, certpath, accesskey, fileid, filetype):
    setfiletypejson = {'section': 'file', 'request': 'setFileType', 'fileId': fileid, 'fileType': filetype,
                       'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=setfiletypejson)
    return resp.json()


# add file type can use 3 call methods for adding a file - source
# inline - data = base64 encoded
# url - data = url to downlaod stuff from
# import - data = filename in the import dir
# filename doesn't matter in url or import

def addfile(endpoint, certpath, accesskey, filename, filetype, source, accessgroupid, data):
    addfilejson = {'section': 'file', 'request': 'addFile', 'filename': filename, 'fileType': filetype,
                   'source': source,
                   'accessGroupId': accessgroupid, 'data': data, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=addfilejson)
    return resp.json()


# crackers - cracker
def listcrackers(endpoint, certpath, accesskey):
    listcrackersjson = {'section': 'cracker', 'request': 'listCrackers', 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=listcrackersjson)
    return resp.json()


def getcracker(endpoint, certpath, accesskey, crackertypeid):
    getcrackerjson = {'section': 'cracker', 'request': 'getCracker', 'crackerTypeId': crackertypeid,
                      'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=getcrackerjson)
    return resp.json()


def deletecracker(endpoint, certpath, accesskey, crackertypeid):
    deletecrackerjson = {'section': 'cracker', 'request': 'deleteCracker', 'crackerTypeId': crackertypeid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deletecrackerjson)
    return resp.json()


def deleteversion(endpoint, certpath, accesskey, crackerversionid):
    deleteversionjson = {'section': 'cracker', 'request': 'deleteVersion', 'crackerVersionId': crackerversionid,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=deleteversionjson)
    return resp.json()


def createcracker(endpoint, certpath, accesskey, crackername):
    createcrackerjson = {'section': 'cracker', 'request': 'createCracker', 'crackerName': crackername,
                         'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=createcrackerjson)
    return resp.json()


def addversion(endpoint, certpath, accesskey, crackertypeid, crackerbinaryversion, crackerbinarybasename,
               crackerbinaryurl):
    addversionjson = {'section': 'cracker', 'request': 'addVersion', 'crackerTypeId': crackertypeid,
                      'crackerBinaryVersion': crackerbinaryversion, 'crackerBinaryBasename': crackerbinarybasename,
                      'crackerBinaryUrl': crackerbinaryurl, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=addversionjson)
    return resp.json()


def updateversion(endpoint, certpath, accesskey, crackerversionid, crackerbinaryversion, crackerbinarybasename,
                  crackerbinaryurl):
    updateversionjson = {'section': 'cracker', 'request': 'updateVersion', 'crackerVersionId': crackerversionid,
                         'crackerBinaryVersion': crackerbinaryversion, 'crackerBinaryBasename': crackerbinarybasename,
                         'crackerBinaryUrl': crackerbinaryurl, 'accessKey': accesskey}
    resp = requests.post(endpoint, verify=False, json=updateversionjson)
    return resp.json()
