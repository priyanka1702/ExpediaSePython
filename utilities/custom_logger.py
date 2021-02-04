# This file is used to assign logging format.
import logging
import inspect

def customloger(loglevel = logging.DEBUG):
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("expediatesting.log", mode='w')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%d-%m-%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger