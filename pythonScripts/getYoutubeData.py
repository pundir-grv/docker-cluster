#!/usr/bin/python
# get data from youtube

import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from base import config


def searchData(searchStr):
    """Get data from youtube based on search str"""
    apiKey = config["googleApiKey"]
    apiServiceName = config["apiServiceName"]
    apiVersion = config["apiVersion"]
    maxResult = config["maxResult"]
    youtube = build(
        apiServiceName,
        apiVersion,
        developerKey=apiKey
    )
    searchResponse = youtube.search().list(
        q=searchStr,
        part='id,snippet',
        maxResults=maxResult
    ).execute()
    data = []
    for result in searchResponse.get('items', []):
        if result['id']['kind'] == 'youtube#video':
            data.append(result)
    
    return data
