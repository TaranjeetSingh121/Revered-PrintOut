# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:02:30 2018

@author: Dhillonsher
"""



from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1iytA1n2z4go3uVCwE__vIKouTKyIDjEq',
                                    dest_path='./data/mnist.zip',
                                    unzip=True)