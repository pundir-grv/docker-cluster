#!/home/itachi/envs/dmc/bin/python

# Sample flask based app to demonstrate read write operation in mongodb

import json
from flask import Flask
from base import config

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
                <li><a href="/showData">Show Data</a>  From youtube_videos collections</li>
            </ul>
        </body>
    </html>
    """
    return msg

@app.route('/listCollections')
def listCollections():
    return json.dumps(config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
