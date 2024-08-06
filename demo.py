from  hs.logger import logging
from hs.exception import CustomException
import sys
try :
    a = 2/0
except Exception as e:
    raise CustomException(e,sys)
logging.info("logging created ")