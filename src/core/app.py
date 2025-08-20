from src.core.get_files import get_filenames
from src.core.get_json import get_json
from src.error_handling.logger_instances import default_log, fileio_log, debug_log
from src.core import bond_return


  
def run_application():
    
    default_log.info("Logging system initialised")
    
    sensitive = get_json('sensitive/config_sensitive.json')
   
    files = get_filenames(sensitive['transaction_dir'])
    
    # print(files) 
       
    # print("\n".join(files))
    

    

   
    # [next step - read the trade files into a list of trade objects]

    
    




