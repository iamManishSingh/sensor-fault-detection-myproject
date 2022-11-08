from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

if __name__ == '__main__':

    """ training_pipeline_config=TrainingPipelineConfig()
    data_ingeation_congif=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingeation_congif.__dict__) """
    
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)

    """ mongodb_client = MongoDBClient()
    print("collection name:" ,mongodb_client.database.list_collection_names())    """
