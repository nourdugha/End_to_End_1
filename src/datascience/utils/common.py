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
    Reads a yaml file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file to be read

    Returns:
        ConfigBox: Configuration object containing the yaml contents

    Raises:
        ValueError: If the yaml file is empty
        Exception: If any other error occurs while reading the file
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
def create_dirs(path_to_dirs: list, verbose: bool = True):
    """
    Create a list of directories if they don't exist.

    Args:
        path_to_dirs (list): List of directory paths to create
        verbose (bool, optional): Whether to log directory creation messages. Defaults to True.

    Returns:
        None
    """
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created dir at :{path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file

    """
    with open(path, "w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load and parse a JSON file into a ConfigBox object.

    Args:
        path (Path): Path to the JSON file to be loaded

    Returns:
        ConfigBox: Configuration object containing the JSON contents

    Raises:
        Exception: If any error occurs while reading the file
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save any data object as a binary file using joblib.

    Args:
        data (Any): Data object to be saved
        path (Path): Path where the binary file will be saved

    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file saved using joblib.

    Args:
        path (Path): Path to the binary file to be loaded

    Returns:
        Any: The data object that was saved in the binary file

    Raises:
        Exception: If any error occurs while loading the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data
