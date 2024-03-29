# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 02:53:21 2018

@author: Dhillonsher
"""
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download&id=1P_pqSWF6jmudfsLRLreDWl4nadsCNdWg"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    folder_id = 'TAKE ID FROM SHAREABLE LINK'
    destination = 'DESTINATION FILE ON YOUR DISK'
    download_file_from_google_drive(folder_id, destination)