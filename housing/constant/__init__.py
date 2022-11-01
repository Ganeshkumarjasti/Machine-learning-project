import os
from datetime import datetime

ROOT_DIR = os.getcwd() #to get current working directory


CONFIG_DIR = "config"
CINFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP =f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"



#Traning pipeline related variables

TRANING_PIPELINE_CONFIG_KEY = "traning pipeline config"
TRANING_PIPELINE_ARTIFACTS_KEY = "artifact_dir"
TRANING_PIPELINE_NAME_KEY = "pipeline_name"