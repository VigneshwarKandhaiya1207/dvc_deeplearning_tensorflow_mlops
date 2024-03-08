import os
import yaml
import argparse
import shutil
from utils.mail_utils import read_yaml,create_directory
from logger import logging

def copy_file(source_download_dir,local_data_dir):
    list_of_files = os.listdir(source_download_dir)
    N = len(list_of_files)
    for file in list_of_files:
        src = os.path.join(source_download_dir, file)
        dest = os.path.join(local_data_dir, file)
        shutil.copy(src, dest)

def get_data(config_path):
    config=read_yaml(config_path)

    source_download_dirs = config["source_download_dirs"]
    local_data_dirs = config["local_data_dirs"]

    for source_download_dir, local_data_dir in zip(source_download_dirs, local_data_dirs):
        create_directory([local_data_dir])
        copy_file(source_download_dir, local_data_dir)



if __name__ ==  "__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="../config/config.yaml")

    parsed_args=args.parse_args()
    try:
        logging.info("<<<<<<<<<<STAGE 01 STARTED>>>>>>>>>>")
        get_data(config_path=parsed_args.config)
        logging.info("<<<<<<<<<<STAGE 01 COMPLETED>>>>>>>>>>")
    except Exception as e:
        logging.exception(e)
        raise e
