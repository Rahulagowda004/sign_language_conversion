from sign_language_conversion.constants import *
from sign_language_conversion.utils.common import read_yaml, create_directories,save_json
from sign_language_conversion.entity.config_entity import (DataIngestionConfig,TrainingConfig,EvaluationConfig)
import os

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        return data_ingestion_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config['training']
        params = self.params
        dataset_path = os.path.join(self.config['data_ingestion']['root_dir'], "data.pickle")
        create_directories([Path(training['root_dir'])])
        training_config = TrainingConfig(
            root_dir=Path(training['root_dir']),
            trained_model_path=Path(training['trained_model_path']) / "model.p",
            dataset_path=Path(dataset_path),
            n_estimators=params['n_estimators']
        )
        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=Path("model/model.pkl"),
            training_data=Path("artifacts\\data_ingestion\\data.pickle"),
            mlflow_uri="https://dagshub.com/Rahulagowda004/sign_language_conversion.mlflow",
            all_params=self.params
        )
        return eval_config