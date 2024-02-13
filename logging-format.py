import logging
logging.basicConfig(level=logging.DEBUG,filename="/tmp/mylog.txt",format='%(asctime)s,-%(name)s,%(levelname)s,%(message)s',datefmt='%d-%b-%Y %H,%M,%S')

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")