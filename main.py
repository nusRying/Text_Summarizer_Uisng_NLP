from text_Summarizer.pipeline.stage_01_Data_Ingestion import data_Ingestion_Training_Pipeline
from text_Summarizer import logger



STAGE_NAME = "Stage 01: Data Ingestion Stage"

try:
    logger.info("Stage 01: Data Ingestion Stage Started")
    data_Ingestion = data_Ingestion_Training_Pipeline()
    data_Ingestion.main()
    logger.info("Stage 01: Data Ingestion Stage Completed Successfully")
except Exception as e:
    logger.exception(e)
    raise e
