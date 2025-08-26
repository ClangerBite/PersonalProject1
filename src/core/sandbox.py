import tabula
import pandas as pd
from typing import List, Union
from src.logs.application_logs import fileio_log, default_log
from src.file_IO.filepath_utilities import get_filepath
from src.file_IO.json_utilities import read_json

def extract_tables_from_pdf(file_path: str, pages: Union[str, List[int]] = 'all') -> List[pd.DataFrame]:
    """
    Extract tables from a PDF file and return them as pandas DataFrames
    
    Args:
        file_path (str): Path to the PDF file
        pages (str|List[int]): Pages to extract tables from. Can be:
            - 'all' for all pages
            - A list of page numbers e.g. [1,2,3]
            - A range string e.g. '1-3'
    
    Returns:
        List[pd.DataFrame]: List of DataFrames, one for each table found
    
    Raises:
        FileNotFoundError: If PDF file doesn't exist
        Exception: For other PDF processing errors
    """
    try:
        fileio_log.info(f"Extracting tables from PDF: {file_path}")
        
        # Extract tables using tabula
        tables = tabula.read_pdf(
            file_path,
            pages=pages,
            multiple_tables=True,
            guess=True,
            lattice = True,
            pandas_options={'dtype': str}  # Convert all columns to string initially
        )
        
        fileio_log.info(f"Successfully extracted {len(tables)} tables")
        
        # Clean up the DataFrames
        cleaned_tables = []
        for idx, df in enumerate(tables, 1):
            # Remove empty rows and columns
            df = df.dropna(how='all').dropna(axis=1, how='all')
            
            # Reset index after dropping rows
            df = df.reset_index(drop=True)
            
            fileio_log.debug(f"Table {idx} shape: {df.shape}")
            cleaned_tables.append(df)
            
        return cleaned_tables
        
    except FileNotFoundError:
        fileio_log.error(f"PDF file not found: {file_path}")
        raise
    except Exception as e:
        fileio_log.error(f"Error extracting tables from PDF {file_path}: {str(e)}")
        raise

# Example usage
def read_pdf():
    try:
        sensitive = read_json('sensitive/config_sensitive.json')
        
        pdf_path = get_filepath(sensitive['statement_dir'],sensitive['statement_file'])
        tables = extract_tables_from_pdf(pdf_path)
        
        # Print info and full content of each table
        for idx, df in enumerate(tables, 1):
            default_log.info(f"\nTable {idx} - Shape: {df.shape}")
            # Show full table instead of just head()
            with pd.option_context('display.max_rows', None, 
                                 'display.max_columns', None,
                                 'display.width', None):
                default_log.info(f"\n{df}")
            
    except Exception as e:
        default_log.info(f"Error: {e}")