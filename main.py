""" fct test """
import sys; sys.dont_write_bytecode = True
from files_handlers.csv_dict_file_handler import CSVDictFileHandler

csv_fh = CSVDictFileHandler()
content = csv_fh.read("res/test.csv")
print(content)
result = csv_fh.write("res/test2.csv",["name","age"], [{"name":"test","age":25}, {"name":"test2","age":30}])
print(result)