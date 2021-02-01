from pymongo import MongoClient
from config import conn_string


def gen_db(conn_string=conn_string):

    client = MongoClient(conn_string)
    db = client['next-producao']

    return db