""" fct test """
from files_handlers.png_fle_handler import PNGFileHandler

png_fh = PNGFileHandler()

content = [
    [(0,0,0),   (255,0,0), (0,0,0)],
    [(255,0,0), (255,0,0), (255,0,0)],
    [(255,0,0), (0,0,0),   (255,0,0)],
]

result = png_fh.write("test2.png", content)

print(result)