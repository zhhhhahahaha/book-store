import logging
import os
from pymongo import MongoClient


class Store:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.mongodb = self.client['bookstore_database']
        self.init_tables()
    
    def delete_all(self):
        self.user.delete_many({})
        self.user_store.delete_many({})
        self.store.delete_many({})
        self.new_order.delete_many({})
        self.new_order_detail.delete_many({})
        self.inverted_index.delete_many({})
    
    def create_index(self):
        self.user.create_index({"user_id": 1})
        self.user_store.create_index({"store_id": 1})
        self.store.create_index({"store_id": 1, "book_id": 1})
        self.new_order.create_index({"order_id": 1})
        self.new_order_detail.create_index({"order_id": 1, "book_id": 1})
        self.history_order.create_index({"order_id": 1})
        self.inverted_index.create_index({"key_ctx": 1})

    def init_tables(self):
        try:
            self.user = self.mongodb['user']
            self.user_store= self.mongodb['user_store']
            self.store = self.mongodb['store']
            self.new_order= self.mongodb['new_order']
            self.new_order_detail = self.mongodb['new_order_detail']
            self.history_order = self.mongodb['history_order']
            self.inverted_index = self.mongodb['invert_index']

            # delete all documents
            self.delete_all()

            # create index on invert_index
            self.create_index()
        except Exception as e:
            logging.error(e)


database_instance: Store = None


def init_database():
    global database_instance
    database_instance = Store()


def get_db():
    global database_instance
    return database_instance