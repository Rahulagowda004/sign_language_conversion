from sign_language_conversion.constants import *
from sign_language_conversion.utils.common import read_yaml, create_directories,save_json
import os
from sign_language_conversion.entity.config_entity import (DataCreation,DataPickle,TrainingConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    
    def get_creation(self) -> DataCreation:
        config = self.config.data_creation
        create_directories([config.root_dir])
        if 'no_of_classes' not in self.params:
            raise KeyError("The key 'no_of_classes' is missing from params file.")
        data_creation_config = DataCreation(
            root_dir=config.root_dir,
            local_data_file=config.raw_dataset,
            number_of_classes=self.params['no_of_classes']
        )
        return data_creation_config
    
    def get_data_config(self) -> DataPickle:
        config = self.config
        create_directories([config['data_pickle']['root_dir']])
        if 'no_of_classes' not in self.params:
            raise KeyError("The key 'no_of_classes' is missing from params file.")
        data_pickle_config = DataPickle(
            root_dir=config['data_pickle']['root_dir'],
            data_raw=config['data_creation']['raw_dataset'],
            data_pickle=config['data_pickle']['pickle_dataset']
        )
        return data_pickle_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config['training']
        params = self.params
        dataset_path = os.path.join(self.config.data_pickle.pickle_dataset)
        create_directories([Path(training['root_dir'])])
        training_config = TrainingConfig(
            root_dir=Path(training['root_dir']),
            trained_model_path=Path(training['trained_model_path']) / "model.p",
            dataset_path=Path(dataset_path),
            n_estimators=params['n_estimators']
        )
        return training_config