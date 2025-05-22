from src.datascience import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import os
import yaml
import json
import joblib

# ConfigBox for able call the obj by .attribute then return its value
# @ensure_annotations decorator for managing the safe typing for parameters in the method
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_dirs(path_to_dirs:list, verbose=True):
    """
    create list of directories

    Args:
      path_to_dirs (list): list of path of dirs
      ignore_log(bool, optional): ignore of multiple dirs is to be created

    """
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created dir at :{path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    """
    save json data
    
    Args:
       path (Path): path to json file
       data (dict): data to be saved in json file

    """
    with open(path) as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file 
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """
    save binary file

    Args:
      data (Any): data to be saved as binary
      path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """
    load binary file

    Args:
      path (Path): path to binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
