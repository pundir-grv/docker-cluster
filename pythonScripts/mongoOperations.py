#!/usr/bin/python

from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from base import config

mongoHost = ",".join([hosts for hosts in config["mongoHost"]])
client = MongoClient('mongodb://{0}:{1}@{2}/?replicaSet={4}&authSource=admin'.format(
                            config["mongoUserAdmin"],
                            config["mongoPassAdmin"],
                            mongoHost,
                            config["replicaSet"]),readPreference='secondaryPreferred')

db = client[config["dbName"]]
db.create_collection(name=config["collection"])
collection = db.config["collection"]

