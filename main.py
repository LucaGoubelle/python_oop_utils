""" fct test """
import sys; sys.dont_write_bytecode = True
from pipe.outpipper import OutPipper

outpipe = OutPipper()
result = outpipe.pipe(["node","main.js"])
print(result)
