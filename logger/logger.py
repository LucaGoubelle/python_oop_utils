""" logger """
from logger.bcolor import Bcolors
from datetime import datetime

class Logger:
    """ Logger class """
    def __init__(self): pass
    
    def log_warning(self, content:str):
        """ log warning """
        print(f"{Bcolors.WARNING}{content}{Bcolors.ENDC}")
        
    def log_info(self, content:str):
        """ log warning """
        print(f"{Bcolors.OKCYAN}{content}{Bcolors.ENDC}")
    
    def time_log_info(self, content:str):
        """ log warning """
        print(f"[{Bcolors.OKGREEN}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Bcolors.ENDC}]: {Bcolors.OKCYAN}{content}{Bcolors.ENDC}")
        
    def log_success(self, content:str):
        """ log success """
        print(f"{Bcolors.OKGREEN}{content}{Bcolors.ENDC}")
        
    def log_fail(self, content:str):
        """ log fail """
        print(f"{Bcolors.FAIL}{content}{Bcolors.ENDC}")
