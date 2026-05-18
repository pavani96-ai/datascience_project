from src.datascience import logger
import os
from src.datascience.entity.config_entity import (DataTransformationConfig)
import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    ## note: you can add different data tranformation techniques such as scaling,pca,etc

    def train_test_split(self):
        data= pd.read_csv(self.config.data_path)

        #split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index= False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("splitted data into training test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
