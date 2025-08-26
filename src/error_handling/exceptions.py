# /////////////////////////////////////////////////////////////////////////////
# CUSTOM EXCEPTIONS MODULE
# /////////////////////////////////////////////////////////////////////////////


from src.logs.application_logs import default_log, fileio_log, debug_log


# /////////////////////////////////////////////////////////////////////////////
class Error(Exception):
  """base class for errors"""


# /////////////////////////////////////////////////////////////////////////////
class DirectoryNotFoundError(Error):
  """Exception raised when directory is not found"""

  def __init__(self, dir):
    message = f'Directory does not exist: "{dir}"'
    fileio_log.error(message, stacklevel = 2)
    super().__init__(message)
    

# /////////////////////////////////////////////////////////////////////////////
class FilePathCreationError(Error):
  """Exception raised when cannot create a file path"""

  def __init__(self, item, dir, err):
    message = f"Error creating filepath for item {item} in directory {dir}: {err}"
    fileio_log.error(message, stacklevel = 2)
    super().__init__(message)    
    

# /////////////////////////////////////////////////////////////////////////////
class ListFilesError(Error):
  """Exception raised when cannot list out files in a directory"""

  def __init__(self, err):
    message = f"Error listing files: {err}"
    fileio_log.error(message, stacklevel = 2)
    super().__init__(message)    
