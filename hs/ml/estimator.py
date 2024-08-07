import sys
from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sqlalchemy import Column
from hs.exception import CustomException
from hs.logger import logging


class HSModel:
    def __init__(self,
                 preprocessing_object: ColumnTransformer,trained_model_object: object):
        """
        :param preprocessing_object: ColumnTransformer object for preprocessing data
        :param trained_model_object: Trained model object
        """
        
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, dataframe: DataFrame) -> DataFrame:


        logging.info("Entered into method of heart stroke")
        try:
            logging.info("using the trained model to get the prediction")
            transformed_feature = self.preprocessing_object.transform(dataframe)
            logging.info("loaded the  transformed_feature")
            return self.trained_model_object.predict(transformed_feature  )
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"
    def __str__(self):
        return f"Heart Stroke model object with {type(self.trained_model_object).__name__}()"