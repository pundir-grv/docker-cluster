#!/usr/bin/python

import ruamel.yaml
import urllib.parse
import os

with open("/mongo_app/config.yml","r") as fp:
    config = ruamel.yaml.round_trip_load(fp)

config["mongoUserAdmin"] = urllib.parse.quote_plus(os.environ.get("MONGO_USER_ADMIN"))
config["mongoPassAdmin"] = urllib.parse.quote_plus(os.environ.get("MONGO_PASS_ADMIN"))
config["googleApiKey"] = os.environ.get("GOOGLE_API_KEY")