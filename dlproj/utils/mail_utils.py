import os
import yaml
from logger import logging

def read_yaml(path_to_yaml:str)-> dict:
    try:
        with open(path_to_yaml,"r") as f:
            content=yaml.safe_load(f)
            logging.info(f"Loaded the {path_to_yaml} successfully.")
        return content
    except Exception as e:
        logging.exception(e)
        
def create_directory(dirs:list):
    for dir in dirs:
        try:
            logging.info(f"Creating the directory {dir}")
            os.makedirs(dir,exist_ok=True)
            logging.info(f"The directory {dir} is successfully created")
        except Exception as e:
            logging.exception(e)
            raise e

def save_local_df(data, data_path, index_status=False):
    try:
        data.to_csv(data_path, index=index_status)
        logging.info(f"data is saved at {data_path}") 
    except Exception as e:
        logging.exception(e)