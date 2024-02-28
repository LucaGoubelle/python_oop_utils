from csv import DictReader, DictWriter
from typing import List

class CSVDictFileHandler:
    """ csv dictionary reader """

    def __init__(self): pass

    def read(self, filename:str) -> List[dict]:
        """ read to list of dicts """
        try:
            content: List[dict] = []
            f = open(filename, 'r')
            reader: DictReader = DictReader(f)
            for dico in reader:
                content.append(dico)
            f.close()
            return content
        except Exception as e:
            raise IOError from e
    
    def write(self, filename:str, fields:list, content:List[dict]) -> str:
        """ write list of dicts to csv file """
        try:
            f = open(filename, 'w')
            writer = DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(content)
            f.close()
            return "file wrote !"
        except Exception as e:
            raise IOError from e