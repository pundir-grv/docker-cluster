#!/home/itachi/envs/dmc/bin/python

# Sample flask based app to demonstrate read write operation in mongodb

import json
import logging
from bson import json_util
from flask import Flask, request
from base import config
from mongoOperations import Mongo
from getYoutubeData import searchData

app = Flask(__name__)

@app.route('/')
def homePage():
    msg = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Mongo Sample</title>
        </head>
        <body>
            <h1>Sample flask based app to demonstrate read write operation in mongodb</h1>
            <p>Here I will create one collection "youtube_videos" and store list of 
            youtube videos beased on search string.</p>
            <h2>API LIST</h2>
            <ul>
                <li><a href="/listCollections">List Mongo Collections</a></li>
                <li><a href="/writeData">Write Data</a> From Youtube API(Need to specify search string in query parameter)</li>
                <li><a href="/getDataCount">Fetch Data Count</a>  From youtube_videos collections</li>
                <li><a href="/showData">Show Data</a>  From youtube_videos collections</li>
            </ul>
        </body>
    </html>
    """
    return msg

@app.route('/listCollections')
def listCollections():
    dbObj = Mongo()
    return json.dumps(dbObj.getCollections())

@app.route("/writeData")
def writeData():
    searchStr = request.args.get('search')
    if not searchStr:
        return "Please provide search string in query param",400
    data = searchData(searchStr)
    dbObj = Mongo()
    status = dbObj.writeData("youtube_videos", data)
    return json.dumps(status, default=json_util.default)

@app.route("/getDataCount")
def getDataCount():
    dbObj = Mongo()
    objCount = dbObj.getCount("youtube_videos")
    return "Total Objects in youtube_videos : {count}".format(count=objCount)

@app.route("/showData")
def showData():
    dbObj = Mongo()
    data = dbObj.readData("youtube_videos")
    return json.dumps(data, default=json_util.default)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
