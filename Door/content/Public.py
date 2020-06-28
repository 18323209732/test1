
# coding=utf-8
import requests
from random import randint,choice
import random,os,re
import json
import requests
import time
from random import randint
from datetime import date,timedelta
from Common.ReadYaml import ReadPublic

def Public_path():
    # path = os.path.dirname(os.path.abspath('.')) + '/content/Public.yaml'
    path = "D:\Program Files\PycharmProjects\Portal_interface\Door\content\Public.yaml"
    print(path)
    return path