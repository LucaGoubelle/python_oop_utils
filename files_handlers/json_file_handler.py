""" json file handler """
import json
from typing import Union, List

class JSONFileHandler:
    """ JSON file handler """
    def __init__(self): pass
    
    def read(self, filename:str) -> Union[List[dict],dict]:
        """ read json file, return content which is list of dict or dict itself """
        try:
            with open(filename, 'r', encoding='utf-8') as file_obj:
                data = json.load(file_obj)
            return data
        except Exception as e:
            raise Exception("JSON File not found | JSON File content not supported") from e
        
    def write(self, filename:str, content:Union[List[dict],dict], indent=None) -> bool:
        try:
            with open(filename, 'w', encoding='utf-8') as file_obj:
                json.dump(content, file_obj, indent=indent)
            return True
        except Exception as e:
            raise Exception("JSON File content not supported") from e
