from src.get_files import get_filenames
from src.get_json import get_json


  
def run_application():
    
    
    sensitive = get_json('sensitive/config_sensitive.json')
   
    files = get_filenames(sensitive['transaction_dir'])
    
    print("\n".join(files))

    
    




