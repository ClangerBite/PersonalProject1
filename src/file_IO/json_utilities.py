import json
from src.file_IO.filepath_utilities import get_abs_path

  
# ///////////////////////////////////////////////////////////////////////////// 
def read_json(file_path):
    """Read and parse a JSON file, returning its contents as a dictionary"""
    
    try:        
        with open(get_abs_path(file_path)) as file:
            parsed_json = json.load(file)
            
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

    return parsed_json