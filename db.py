from ast import Try
from asyncio.windows_events import NULL
from dataclasses import replace
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json;

import time
import sys
from datetime import datetime

collection_name = None
dbname = None

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://minhal:minhal123@cluster0.jkar1.mongodb.net/scrapers?retryWrites=true&w=majority"

    from pymongo import MongoClient
    client = MongoClient("mongodb://minhal:minhal123@cluster0-shard-00-00.jkar1.mongodb.net:27017,cluster0-shard-00-01.jkar1.mongodb.net:27017,cluster0-shard-00-02.jkar1.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.test

    
    return client['universities']

def import_mongo():

    f = open('items.json')
    items = json.load(f)
    print(len(items), "items length")

    
    collection_name.insert_many(items)

    print("importing completed")


if __name__ == "__main__":    
    dbname = get_database()
    collection_name = dbname["scrapers"]
    import_mongo()

    
