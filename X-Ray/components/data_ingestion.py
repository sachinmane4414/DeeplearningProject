import sys

from XRay.cloud_storage.s3_operation import s3Operation
from XRay entity.artifact_entity import DataIngestionArtifact
from XRay entity.config_entity import DataIngestionConfig
from XRay.exception import XRayException
from XRay.logger import logging

class DataIngestion:
    def __init__(self):
        pass
    def get_data_from_s3(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e,sys)

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e,sys)