import cv2
import boto3
from botocore.config import Config
import configparser
from boto3 import Session

config_ini = configparser.ConfigParser()
config_ini.read('')#config.iniから読み込む

config_key = 'rekognition' #config_iniのrekognitionを呼び出す
my_region = 'choose_area' #エリアの選択

session = Session(
    aws_access_key_id=config_key['accsesskey'],
    aws_secret_access_key=config_key['secretaccesskey'],
    region_name=my_region)

client = session.client(service_name='rekognition')