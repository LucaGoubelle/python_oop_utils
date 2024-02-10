""" fct test """
import sys; sys.dont_write_bytecode = True
from list_utils import ListUtils

lst_u = ListUtils()
result = lst_u.to_string([1,2,3], "_")
print(result)
