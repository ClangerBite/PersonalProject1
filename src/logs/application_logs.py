# /////////////////////////////////////////////////////////////////////////////
# APPLICATION LOGS
#  
# This module defines the logger instances used in the application, set up via 
# a LoggerFactory class.
#
# Compulsory configurations:
#   1. logger name
#   2. log file path
#
# Optional configurations:
#   1. log level (default is INFO)
#   2. format of the log message (default is 'long' but console is always 'short')
#   3. whether to output to console as well (default is disabled)
#
# /////////////////////////////////////////////////////////////////////////////

import logging
from src.logs.log_system import LoggerFactory


# /////////////////////////////////////////////////////////////////////////////
def initialize_application_loggers():
    """
    Initialize application loggers with specified configurations.
    
    This function must be called once at the start of the application in order
    to set up the loggers used throughout the application.
    """
    LoggerFactory.get_logger(
        'default',
        log_file='logs/default.log',
        format='short'
    )
    LoggerFactory.get_logger(
        'fileIO',
        log_file='logs/fileIO.log',
        level=logging.WARNING,
        console=True
    )
    LoggerFactory.get_logger(
        'debug',
        log_file='logs/debug.log',
        level=logging.DEBUG
    )

# /////////////////////////////////////////////////////////////////////////////
# Initialize loggers when module is imported
initialize_application_loggers()

# Names of logger instances to be exported for use in other modules
default_log = LoggerFactory.get_logger('default')
fileio_log = LoggerFactory.get_logger('fileIO')
debug_log = LoggerFactory.get_logger('debug')