import logging

# create logger
lo = logging.getLogger("example")
lo.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
lo.addHandler(ch)

# "application" code
lo.debug("log this debug message")
lo.info(" Dipslay info message")
lo.warn(" Covy warning message")
lo.error("Error in the message")
lo.critical(" Patient critical message")
