import os
import json

  
# Returns the filepath for a specific item in a directory
# ///////////////////////////////////////////////////////////////////////////// 
def get_json(file_path):
    
    abs_path = os.path.abspath(file_path)
    
    try:
        with open(abs_path) as file:
            parsed_json = json.load(file)
            
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

    return parsed_json