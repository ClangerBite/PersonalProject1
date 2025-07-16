# /////////////////////////////////////////////////////////////////////////////
# LOGGING SYSTEM MODULE
# /////////////////////////////////////////////////////////////////////////////

import logging


# FUNCTION TO SET UP LOGS IN A STANDARD CONFIGURATION
# /////////////////////////////////////////////////////////////////////////////
def setup_logger(logger_name, log_file, level=logging.INFO, console=False):
  
  logger = logging.getLogger(logger_name)
  
  # Set minimum warning level that logger will record
  logger.setLevel(level)
  
  # Define log formats 
  long_msg_format = '%(asctime)s - %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
  short_msg_format = '%(asctime)s - %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
  
  long_date_format = f'%d-%m-%Y %H:%M:%S'
  short_date_format = f'%H:%M:%S'
  
  long_formatter = logging.Formatter(long_msg_format, long_date_format)  
  short_formatter = logging.Formatter(short_msg_format, short_date_format)
  
  # Create handlers for file & console (if needed) & add them to the logger
  handler = logging.FileHandler(log_file, mode='w')     
  handler.setFormatter(long_formatter)
  logger.addHandler(handler)
  
  if console:
    handler = logging.StreamHandler()
    handler.setFormatter(short_formatter)  
    logger.addHandler(handler)   
  
  return logger

# CREATE THE LOGS FOR THE APPLICATION
# /////////////////////////////////////////////////////////////////////////////
log = setup_logger('default', 'logs/default.log')
log_fileIO = setup_logger('fileIO', 'logs/fileIO.log', level=logging.WARNING, console=True)
log_debug = setup_logger('debug', 'logs/debug.log', level=logging.DEBUG)

