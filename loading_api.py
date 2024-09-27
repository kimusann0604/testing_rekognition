import cv2
import boto3
from botocore.config import Config
import configparser
from boto3 import Session

config_ini = configparser.ConfigParser()
config_ini.read('')#config.iniから読み込む

my_region = 'choose_area' #エリアの選択

session = Session(
    aws_access_key_id=config_ini['rekognition']['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=config_ini['rekognition']['AWS_SECRET_ACCESS_KEY'],
    region_name=my_region)
# もしくは
# config_key = config_ini['rekognition']
# session = Session(
#     aws_access_key_id=config_key['AWS_ACCESS_KEY_ID'],
#     aws_secret_access_key=config_key['AWS_SECRET_ACCESS_KEY'],
#     region_name=my_region)

client = session.client(service_name='rekognition')