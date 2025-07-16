from src.core.get_files import get_filenames
from src.core.get_json import get_json
from src.error_handling.logging_system import log, log_debug, log_fileIO

from src.core import bond_return


  
def run_application():
    
    log.info("Logging system initialised")
    
    sensitive = get_json('sensitive/config_sensitive.json')
   
    files = get_filenames(sensitive['transaction_dir'])
    
    # print(files) 
       
    # print("\n".join(files))
    

    

   
    # [next step - read the trade files into a list of trade objects]

    
    




