# /////////////////////////////////////////////////////////////////////////////
# CUSTOM EXCEPTIONS MODULE
# /////////////////////////////////////////////////////////////////////////////


from src.error_handling.logging_system import log, log_debug, log_fileIO


# /////////////////////////////////////////////////////////////////////////////
class Error(Exception):
  """base class for errors"""


# /////////////////////////////////////////////////////////////////////////////
class DirectoryNotFoundError(Error):
  """Exception raised when directory is not found"""

  def __init__(self, dir):
    message = f'Directory does not exist: "{dir}"'
    log_fileIO.error(message, stacklevel = 2)
    super().__init__(message)
    

# /////////////////////////////////////////////////////////////////////////////
class FilePathCreationError(Error):
  """Exception raised when cannot create a file path"""

  def __init__(self, item, dir, err):
    message = f"Error creating filepath for item {item} in directory {dir}: {err}"
    log_fileIO.error(message, stacklevel = 2)
    super().__init__(message)    
    

# /////////////////////////////////////////////////////////////////////////////
class ListFilesError(Error):
  """Exception raised when cannot list out files in a directory"""

  def __init__(self, err):
    message = f"Error listing files: {err}"
    log_fileIO.error(message, stacklevel = 2)
    super().__init__(message)    
