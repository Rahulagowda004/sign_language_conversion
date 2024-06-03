from sign_language_conversion.config.configuration import ConfigurationManager
from sign_language_conversion.components.training_model import Training
from sign_language_conversion import logger


STAGE_NAME = "Training the Model"

class TrainingModel:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        training_config = config_manager.get_training_config()
        trainer = Training(config=training_config)
        trainer.train()
        
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingModel()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e