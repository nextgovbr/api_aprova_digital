import os
from pymongo import MongoClient


def gen_db(conn_string=os.environ['conn_string']):

    client = MongoClient(conn_string)
    db = client['next-producao']

    return db
