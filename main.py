""" fct test """
import sys; sys.dont_write_bytecode = True
from logger.logger import Logger

log = Logger()

log.log_success("Test successful")
log.log_warning("Test unstable")
log.log_fail("Test failed")
log.log_info("Test running...")
