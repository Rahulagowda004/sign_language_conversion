from sign_language_conversion.config.configuration import ConfigurationManager
from sign_language_conversion.components.prepare_dataset import Prepare_dataset
from sign_language_conversion import logger


STAGE_NAME = "Prepare base model"


class PreparedatasetPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        prepare_dataset_config = config_manager.get_prepare_dataset()
        prepare_dataset = Prepare_dataset(config=prepare_dataset_config)
        prepare_dataset.save_data()
        
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PreparedatasetPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e