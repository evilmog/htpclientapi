# Example Python3 API
# make sure you check the api spec for required options as there are no guardrails here
# https://github.com/hashtopolis/server/tree/master/doc/user-api/sections

import requests
import json

class HashtopolisSection:
    def __init__(self, api, section_name):
        self.api = api
        self.section_name = section_name

    def __call__(self, request, data=None):
        if data is None:
            data = {}
        data.update({"section": self.section_name, "request": request, "accessKey": self.api.api_key})
        response = requests.post(self.api.api_url, json=data)
        return response.json()

class HashtopolisClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.test = HashtopolisSection(self, "test")
        self.user = HashtopolisSection(self, "user")
        self.group = HashtopolisSection(self, "group")
        self.rightgroup = HashtopolisSection(self, "rightgroup")
        self.agent = HashtopolisSection(self, "agent")
        self.agentBinary = HashtopolisSection(self, "agentBinary")
        self.task = HashtopolisSection(self, "task")
        self.supertask = HashtopolisSection(self, "supertask")
        self.hashlist = HashtopolisSection(self, "hashlist")
        self.superhashlist = HashtopolisSection(self, "superhashlist")
        self.file = HashtopolisSection(self, "file")
        self.cracker = HashtopolisSection(self, "cracker")
        self.config = HashtopolisSection(self, "config")

# Usage example
api_url = "https://example.com/api/user.php"
api_key = "apikey"

client = HashtopolisClient(api_url, api_key)

# Test Connection
test_connection_response = client.test("connection")
print(test_connection_response)

# Test Access
test_access_response = client.test("access")
print(test_access_response)

# List Users
list_users_response = client.user("listUsers")
print(list_users_response)

# Get User
get_user_response = client.user("getUser", {"userId": 1})
print(get_user_response)

# List Groups
list_groups_response = client.group("listGroups")
print(list_groups_response)

# Get Group
get_group_response = client.group("getGroup", {"groupId": 1})
print(get_group_response)

# List Access Groups
list_access_groups_response = client.rightGroup("listAccessGroups")
print(list_access_groups_response)

# Get Access Group
get_access_group_response = client.rightGroup("getAccessGroup", {"rightGroupId": 1})
print(get_access_group_response)

# List Agents
list_agents_response = client.agent("listAgents")
print(list_agents_response)

# Get Agent
get_agent_response = client.agent("getAgent", {"agentId": 1})
print(get_agent_response)

# List Tasks
list_tasks_response = client.task("listTasks")
print(list_tasks_response)

# Get Task
get_task_response = client.task("getTask", {"taskId": 1})
print(get_task_response)

# List Supertasks
list_supertasks_response = client.supertask("listSupertasks")
print(list_supertasks_response)

# Get Supertask
get_supertask_response = client.supertask("getSupertask", {"supertaskId": 1})
print(get_supertask_response)

# List Hashlists
list_hashlists_response = client.hashlist("listHashlists")
print(list_hashlists_response)

# Get Hashlist
get_hashlist_response = client.hashlist("getHashlist", {"hashlistId": 1})
print(get_hashlist_response)

# List SuperHashlists
list_superhashlists_response = client.superhashlist("listSuperhashlists")
print(list_superhashlists_response)

# Get SuperHashlist
get_superhashlist_response = client.superhashlist("getSuperhashlist", {"superhashlistId": 1})
print(get_superhashlist_response)

# List Files
list_files_response = client.file("listFiles")
print(list_files_response)

# Get File
get_file_response = client.file("getFile", {"fileId": 1})
print(get_file_response)

# List Crackers
list_crackers_response = client.cracker("listCrackers")
print(list_crackers_response)

# Get Cracker
get_cracker_response = client.cracker("getCracker", {"crackerTypeId": 1})
print(get_cracker_response)

# List Config Items
list_config_response = client.config("listConfig")
print(list_config_response)

# Get Config Item
get_config_response = client.config("getConfig", {"configItem": "anyConfigItem"})
print(get_config_response)
