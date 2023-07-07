from text_Summarizer.config.configuration import ConfigurationManager
from text_Summarizer.components.data_Ingestion import DataIngestion
from text_Summarizer.logging import logger


class data_Ingestion_Training_Pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()