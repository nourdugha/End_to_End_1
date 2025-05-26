from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        validation_status = True
        validation_message = ""

        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema

            # Validate column presence and data types
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    validation_message = f"Column {col} not found in schema"
                    break
                else:
                    # Validate data type
                    expected_dtype = all_schema[col]
                    actual_dtype = str(data[col].dtype)
                    
                    if expected_dtype != actual_dtype:
                        validation_status = False
                        validation_message = f"Column {col} has incorrect data type. Expected: {expected_dtype}, Got: {actual_dtype}"
                        break

            # Write final status to file
            status_message = f"Validation status: {validation_status}"
            if not validation_status:
                status_message += f", Error: {validation_message}"
            else:
                status_message += ", All columns validated successfully"
                
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(status_message)

            if not validation_status:
                raise ValueError(validation_message)

            return validation_status
        
        except Exception as e:
            logger.error(f"Data validation error: {str(e)}")
            raise e

    