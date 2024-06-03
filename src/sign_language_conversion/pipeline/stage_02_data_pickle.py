from sign_language_conversion.config.configuration import ConfigurationManager
from sign_language_conversion.components.data_pickle import DataFetcher
from sign_language_conversion import logger

STAGE_NAME = "Data Ingestion stage"

class DataPicklePipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_pickle_config = config.get_data_config()
        data_creator = DataFetcher(config=data_pickle_config)
        data_creator.datapick()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPicklePipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e