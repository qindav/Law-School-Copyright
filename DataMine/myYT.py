# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import urllib
import requests
import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def searchList():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q="surfing"
    )
    response = request.execute()

    with open('data.json', 'w') as f:
        json.dump(response, f)

def main():

    searchList()

    
    jsonFile = open('data.json', 'r')
    values = json.load(jsonFile)
    vidId = values['items'][0]['id']['videoId']
    jsonFile.close()

    response = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + vidId + "&key=AIzaSyAfxOHwTyZWlHoGTvCd0M3dpo_4oqlKHAA")
    values = json.load(response)
    
    
    # print(video)
    print ("views: " + values['items'][0]['statistics']['viewCount'])
    print ("dislikes: " + values['items'][0]['statistics']['likeCount'])
    print ("likes: " + values['items'][0]['statistics']['dislikeCount'])
    jsonFile.close()


    


if __name__ == "__main__":
    main()