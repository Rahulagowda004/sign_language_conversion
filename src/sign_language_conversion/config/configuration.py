from sign_language_conversion.constants import *
from sign_language_conversion.utils.common import read_yaml, create_directories,save_json
from sign_language_conversion.entity.config_entity import (DataIngestionConfig,Preparedataset,TrainingConfig)

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
    
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_prepare_dataset(self) -> Preparedataset:
        config = self.config.prepare_dataset

        create_directories([config.root_dir])

        prepare_dataset_pickle = Preparedataset(
            root_dir=Path(config.root_dir),
            dataset=Path(config.dataset_path)
        )

        return prepare_dataset_pickle
    
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config['training']
        params = self.params
        dataset_path = os.path.join(self.config.prepare_dataset.root_dir, "data.pickle")
        create_directories([Path(training['root_dir'])])
        training_config = TrainingConfig(
            root_dir=Path(training['root_dir']),
            trained_model_path=Path(training['trained_model_path']),
            dataset_path=Path(dataset_path),
            n_estimators=params['n_estimators']
        )
        return training_config