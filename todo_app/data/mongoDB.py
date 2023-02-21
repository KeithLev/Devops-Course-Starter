from http import client
import pymongo
import os
from bson.objectid import ObjectId
import flask_login


class MongoDB:

    def __init__(self):

        self.to_do_client = pymongo.MongoClient(os.getenv('MONGODB_PRIMARY_KEY'))
        self.to_do_db = self.to_do_client.to_do_db
        self.to_do_collection = self.to_do_db.to_do_collection

    
    def return_object_id(self, _id):
        id = ObjectId(_id)
        return id


    def return_cards(self):
        cards = self.to_do_collection.find()
        return cards
    
    def add_card(self, name, status, lastActivity):
        new_card = {
            "Name":name,
            "Status":status,
            "LastActivity":lastActivity
            }
        result = self.to_do_collection.insert_one(new_card)
        _id_string = str(result.inserted_id)
        return _id_string
        
    def update_card(self, _id, name, status, lastActivity):
        updated_card = {"$set":{
            "Name": name,
            "Status": status,
            "LastActivity": lastActivity
            }}
        result = self.to_do_collection.update_one({"_id":self.return_object_id(_id)},updated_card)

    def delete_card(self, _id):
        myquery = {'_id':self.return_object_id(_id)}
        result = self.to_do_collection.delete_one(myquery)


