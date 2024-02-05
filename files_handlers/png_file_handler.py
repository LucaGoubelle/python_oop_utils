""" png file handler """
from typing import List
from PIL import Image

class PNGFileHandler:
    """PNG File handler (read / write PNG from list of list of tuple RGB)"""
    def __init__(self): pass
    
    def read(self, filename:str) -> List[List[tuple]]:
        """ read PNG file, return list of list of tuple RGB """
        try:
            img = Image.open(filename).convert("RGB")
            x,y = img.size
            pxls = img.load()
            content: List[List[tuple]] = []
            for i in range(x):
                row: List[tuple] = []
                for j in range(y): row.append(pxls[j,i])
                content.append(row)
            return content
        except Exception as e:
            raise Exception("PNG File Not Found | PNG File content not supported") from e
        
    def write(self, filename:str, content:List[List[tuple]]) -> bool:
        """ write content (list of list of tuple RGB) in PNG file"""
        try:
            size_x = len(content)
            size_y = len(content[0])
            img = Image.new(mode="RGB", size=(size_x,size_y))
            pxls = img.load()
            for i in range(size_x):
                for j in range(size_y):
                    pxls[j,i] = content[i][j]
            img.save(filename, format="png")
            return True
        except Exception as e:
            raise Exception("PNG File content not supported") from e
