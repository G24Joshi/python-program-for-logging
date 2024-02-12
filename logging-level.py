import logging
logging.basicConfig(level=logging.DEBUG,filename="/var/log/mylog.txt")

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")