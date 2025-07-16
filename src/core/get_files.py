import os
from src.utilities.context_managers import directory
from src.error_handling import exceptions

  
# Returns a list of lists of all files in a directory and its subdirectories
# ///////////////////////////////////////////////////////////////////////////// 
def get_filenames(dir):
    if not directory_exists(dir):
        raise exceptions.DirectoryNotFoundError(dir)
    return flatten_list(files_in_directory_and_subdirectories(dir))


# Check if directory exists
# /////////////////////////////////////////////////////////////////////////////   
def directory_exists(dir):
    return True if os.path.isdir(dir) else False
        
        
# Joins list of lists into a single flat list
# ///////////////////////////////////////////////////////////////////////////// 
def flatten_list(list_of_lists):
    return sum(list_of_lists, [])


# Returns a list of lists of all files in a directory and its subdirectories
# /////////////////////////////////////////////////////////////////////////////   
def files_in_directory_and_subdirectories(dir):
    with directory(dir):
        try:
            return list(map(
                lambda i: build_line(dir,i) 
                if os.path.isfile(build_line(dir,i)) 
                else files_in_directory_and_subdirectories(build_line(dir,i)), 
                os.listdir(dir))
                )
        
        except Exception as err:
            raise exceptions.ListFilesError(err) 
    

# Returns the filepath for a specific item in a directory
# /////////////////////////////////////////////////////////////////////////////      
def build_line(dir, item):
    try:
        filepath = os.path.join(dir, item)
    
    except Exception as err:
        raise exceptions.FilePathCreationError(item, dir, err)   
        
    return filepath 
