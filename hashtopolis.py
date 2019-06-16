import yaml
import json
import inspect
import requests

class MissingArgumentError(Exception):
    """Raised when there is a missing argument"""
    pass

class HashtopolisAPI:
    def __init__(self, loaded_access_key, loaded_cert_path, loaded_endpoint):
        self.access_key = loaded_access_key
        self.certpath = loaded_cert_path
        self.endpoint = "{endpoint}/api/user.php".format(endpoint=loaded_endpoint)

        self.function_definitions = yaml.load(open('functions.yaml', 'r'))
        for function_name in self.function_definitions.keys():
            self.__dict__[function_name] = self.default_method

    def default_method(self, **kwargs):
        calling_method = inspect.stack()[1][3]
        method_dict = {"section":self.function_definitions.get(calling_method,{}).get("static",{}).get("section"),
                       "request":self.function_definitions.get(calling_method,{}).get("static",{}).get("request")}
        #Checking that we have all the arguments that we need (not a type check just an existence check)
        for required_argument in self.function_definitions.get(calling_method,{}).get("variables",[]):
            if required_argument not in kwargs.keys():
                raise MissingArgumentError
            method_dict[required_argument] = kwargs.get(required_argument)

        response = requests.post(self.endpoint, verify=self.certpath, json=method_dict)
        return response.json()
