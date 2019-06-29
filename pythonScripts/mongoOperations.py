#!/usr/bin/python

from pymongo import MongoClient
from base import config


class Mongo:
    def __init__(self):
        mongoHosts = ",".join([hosts for hosts in config["mongoHost"]])
        client = MongoClient(
            'mongodb://{user}:{password}@{hosts}/?replicaSet={replset}&authSource=admin'.format(
                user=config["mongoUserAdmin"],
                password=config["mongoPassAdmin"],
                hosts=mongoHosts,
                replset=config["replicaSet"]
            ),readPreference='secondaryPreferred'
        )
        self.db = client[config["dbName"]]

    def getCollections(self):
        """return list of collections available in DB"""
        return self.db.list_collection_names()
    
    def readData(self, collection, **searchDict):
        """return data fetched from mongo db based on searchDict"""
        collectionObj = self.db.get_collection(name=collection)
        cursor = collectionObj.find(searchDict)
        data = [obj for obj in cursor]
        return data

    def getCount(self, collection, **searchDict):
        """return object count from mongo db"""
        collectionObj = self.db.get_collection(name=collection)
        count = collectionObj.find(searchDict).count()
        return count

    def writeData(self, collection, data):
        """Write given list of data in mongo db"""
        collectionObj = self.db.get_collection(name=collection)
        if not isinstance(data, list):
            raise Exception("writeData excepts only list as data")
        writeStatus = collectionObj.insert_many(data)
        return writeStatus.inserted_ids