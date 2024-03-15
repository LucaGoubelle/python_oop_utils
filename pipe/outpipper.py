import subprocess

class OutPipper:
    def __init__(self): pass

    def pipe(self, process:list) -> str:
        p = subprocess.Popen(process, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (output, err) = p.communicate()
        return output.decode('utf-8')
