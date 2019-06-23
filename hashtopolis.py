import re
import json
import requests


class MissingArgumentError(Exception):
    """Raised when there is a missing argument"""
    pass


class Hashtopolis:
    def __init__(self, tex_location="tex", endpoint="", port=443, api_key=""):
        self.endpoint = endpoint
        self.port = port
        self.api_key = api_key
        with open("{tex_location}/user-api.tex".format(tex_location=tex_location)) as base_tex_handle:
            base_tex_contents = base_tex_handle.read()
        for section in re.findall("\\\\input\{(.*)\/(.*?)\.tex\}", base_tex_contents):
            self.__dict__[section[1]] = HashtoSection(tex_location=tex_location,
                                                      section_tex_location=section[0],
                                                      section_name=section[1],
                                                      endpoint=self.endpoint,
                                                      port=self.port,
                                                      api_key=self.api_key)


class HashtoSection:
    def __init__(self, endpoint, port, tex_location, section_tex_location, section_name, api_key):
        self.tex_location = tex_location
        self.section_tex_location = section_tex_location
        self.section_name = section_name
        self.function_definitions = {}
        self.endpoint = endpoint
        self.port = port
        self.api_key = api_key
        with open("{tex_location}/{section_tex_location}/{section_name}.tex".format(tex_location=tex_location,
                                                                                    section_tex_location=section_tex_location,
                                                                                    section_name=section_name)) as section_handle:
            for function_definition in re.findall(
                    "\\\\color\{blue\}\s*\\\\begin\{verbatim\}(.*?)\s*\\\\end\{verbatim\}",
                    section_handle.read(), re.S):
                temp_json = json.loads(function_definition.replace("\n", ""))
                self.__dict__[temp_json["request"]] = lambda request=temp_json["request"], **kwargs: self.default_method(request=request,**kwargs)
                self.function_definitions[temp_json["request"]] = temp_json

    def default_method(self, request, **kwargs):
        method_dict = {"accessKey": self.api_key,
                       "section": self.section_name,
                       "request": request}
        function_keys = self.function_definitions.get(request, {}).keys()
        for required_argument in [arg for arg in function_keys if arg not in ["section", "request", "accessKey"]]:
            if required_argument not in kwargs:
                print([arg for arg in function_keys if arg not in ["section", "request", "accessKey"]])
                raise MissingArgumentError
            method_dict[required_argument] = kwargs.get(required_argument)
        response = requests.post(self.endpoint, json=method_dict)
        return response.json()
