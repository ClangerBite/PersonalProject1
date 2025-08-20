from src.error_handling.logging_system import LoggerFactory


# Get logger instances
default_log = LoggerFactory.get_logger('default')
fileio_log = LoggerFactory.get_logger('fileIO')
debug_log = LoggerFactory.get_logger('debug')