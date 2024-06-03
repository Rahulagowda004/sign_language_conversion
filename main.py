from sign_language_conversion import logger
from sign_language_conversion.pipeline.stage_01_data_creation import DataCreationPipeline
from sign_language_conversion.pipeline.stage_02_data_pickle import DataPicklePipeline
from sign_language_conversion.pipeline.stage_03_training_model import TrainingModel
from sign_language_conversion.pipeline.prediction import HandGestureRecognition

# STAGE_NAME = "Data Creation stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataCreationPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "DATA PICKLE CONVERSION STAGE"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataPicklePipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Training the Model"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = TrainingModel()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# STAGE_NAME = "Prediction of Model"
# try:
#     logger.info("*******************")
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = HandGestureRecognition()
#     obj.recognize_gesture()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exception(e)
#     raise e