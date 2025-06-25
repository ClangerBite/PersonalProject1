import os
from src.context_managers import directory

  
# Returns a list of lists of all files in a directory and its subdirectories
# ///////////////////////////////////////////////////////////////////////////// 
def get_filenames(dir):
    return flatten_list(files_in_directory_and_subdirectories(dir))


# Joins list of lists into a single flat list
# ///////////////////////////////////////////////////////////////////////////// 
def flatten_list(list_of_lists):
    return sum(list_of_lists, [])


# Returns a list of lists of all files in a directory and its subdirectories
# /////////////////////////////////////////////////////////////////////////////   
def files_in_directory_and_subdirectories(dir):
    with directory(dir):
        if not os.path.isdir(dir):
            return f'Error: "{dir}" is not a directory'

        try:
            return list(map(
                lambda i: build_line(dir,i) 
                if os.path.isfile(build_line(dir,i)) 
                else files_in_directory_and_subdirectories(build_line(dir,i)), 
                os.listdir(dir))
                )
        
        except Exception as e:
            return f"Error listing files: {e}"
    

# Returns the filepath for a specific item in a directory
# /////////////////////////////////////////////////////////////////////////////      
def build_line(dir, item):
    try:
        filepath = os.path.join(dir, item)
    
    except Exception as e:
        return f"Error creating filepath for item {item} in directory {dir}: {e}"   
        
    return filepath 
