""" TXT file handler """
from typing import List

class TXTFileHandler:
    """ TXT file handler """
    def __init__(self): pass
    
    def read(self, filename:str) -> str:
        """ read all content """
        file = open(filename, 'r')
        data:str = file.read()
        file.close()
        return data
    
    def read_lines(self, filename:str) -> List[str]:
        """ read lines, return list of lines """
        file = open(filename, 'r')
        data:list = file.readlines()
        file.close()
        return data
    
    def read_start(self, filename:str, limit:int) -> List[str]:
        """ read from begin to limit (nb lines) """
        lines:List[str] = []
        file = open(filename, 'r')
        for _ in range(limit):
            lines.append(file.readline())
        file.close()
        return lines
    
    def override(self, filename:str, content:str) -> str:
        """ override content of file, create if not exist """
        file = open(filename, 'w')
        file.write(content)
        file.close()
        return "success !"
    
    def overload(self, filename:str, content:str) -> str:
        """ overload existing file """
        file = open(filename, 'a')
        file.write(content)
        file.close()
        return "success !"
