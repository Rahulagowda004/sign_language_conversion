from sign_language_conversion.config.configuration import ConfigurationManager
from sign_language_conversion.components.data_creation import Data_Creation
from sign_language_conversion import logger

STAGE_NAME = "Data Creation stage"

class DataCreationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_creation_config = config.get_creation()
        data_creator = Data_Creation(config=data_creation_config)
        data_creator.capture_data()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataCreationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e