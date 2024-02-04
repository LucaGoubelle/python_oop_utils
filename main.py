""" fct test """
import sys; sys.dont_write_bytecode = True
# from files_handlers.png_fle_handler import PNGFileHandler

# png_fh = PNGFileHandler()

# content = [
#     [(0,0,0),   (255,0,0), (0,0,0)],
#     [(255,0,0), (255,0,0), (255,0,0)],
#     [(255,0,0), (0,0,0),   (255,0,0)],
# ]

# result = png_fh.write("test2.png", content)

# print(result)
# ----------------------------------------------------
# from regex_handler import RegexHandler

# regh = RegexHandler()
# content = "The rain in Spain"

# res = regh.start_end_with(content, "The", "spain")
# res2 = regh.start_end_with(content, "The", "Spain")
# res3 = regh.replace_matches(content, "\s", "_")
# res4 = regh.begin_by_search(content, "S")
# res5 = regh.get_position_begin_by(content, "i")
# res6 = regh.split_limit(content, " ", 2)

# print(res)
# print(res2)
# print(res3)
# print(res4)
# print(res5)
# print(res6)


from list_utils import ListUtils

lstu = ListUtils()

lst = [1,2,3,4,5]

lst2 = lstu.rotate_elements_left(lst, 2)
lst3 = lstu.rotate_elements_right(lst, 2)
lst4 = lstu.reverse_list(lst)

print(lst2)
print(lst3)
print(lst4)
