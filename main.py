'''
Run the Training Pipeline without the Web App
'''
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.exception.exception import NetworkSecuirtyException

import sys

if __name__ == "__main__":
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise NetworkSecuirtyException(e,sys)