from pymongo import MongoClient
import certifi

ca = certifi.where()

DATABASE_URL = ""

conn = MongoClient(DATABASE_URL,tlsCAFile=ca)

def get_db():
    return conn.flowstate


