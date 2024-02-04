""" regex handler """
import re

class RegexHandler:
    """ RegexHandler """
    def __init__(self): pass
    
    def start_with(self, content:str, value:str) -> bool:
        """ start with value, return True / False """
        result = re.search("^"+value, content)
        return True if result is not None else False
    
    def end_with(self, content:str, value:str) -> bool:
        """ end with value, return True / False """
        result = re.search(value+"$", content)
        return True if result is not None else False

    def start_end_with(self, content:str, value_start:str, value_end:str) -> bool:
        """ start end with 2 values, return True / False """
        result = re.search("^"+value_start+".*"+value_end+"$", content)
        return True if result is not None else False
    
    def replace_matches(self, content:str, origin_value:str, new_value:str) -> str:
        """ replace matches char whit final value in content, return modified content """
        result = re.sub(origin_value, new_value, content)
        return result if result else ""
    
    def begin_by_search(self, content:str, begin_value:str) -> str:
        """ search a word begin by value, then return it """
        reg: str = r"\b"+begin_value+r"\w+"
        result = re.search(reg, content)
        return result.group() if result else ""
    
    def get_position_begin_by(self, content:str, begin_value:str) -> tuple:
        """ get the position of an element which is beginning by value, then return it """
        result = re.search(r"\b"+begin_value+r"\w+", content)
        return result.span() if result else ""
    
    def split_limit(self, content:str, value:str, limit:int) -> list:
        """ split the content n time according to a specific delimiting value """
        result = re.split(value, content, limit)
        return result if result else []
