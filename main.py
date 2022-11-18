from google_images_search import GoogleImagesSearch
from google_images_download import google_images_download
from dotenv import load_dotenv
import os
import curses
import numpy as np 
import cv2
from PIL import Image 

#spotipy or genius

def Get_lyrics(artist,song):
    return PyLyrics.getAlbums("Eminem")

response = google_images_download.googleimagesdownload()

def Searcher(query):
     arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":4,
                 "print_urls":True,
                 "size": "medium",
                 "aspect_ratio":"panoramic"}
     try:
        response.download(arguments)
     
    # Handling File NotFound Error   
     except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit":4,
                     "print_urls":True,
                     "size": "medium"}
                      
        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass

def progressbar(url, progress):
    print(url + ' '+ progress + '%' )

def VidComp():
    os.chdir('H:\Documents\SongInPictures\IMG')

    num_of_images = len(os.listdir('.'))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video = cv2.VideoWriter('video.avi', fourcc, 1, (width, height))
    for j in range(0,5):
        img = cv2.imread(str(i) + '.png')
        video.write(img)

    cv2.destroyAllWindows()
    video.release()

#load_dotenv()
path = 'H:\Documents\SongInPictures\IMG'
#DK = os.environ.get('GCS_DEVELOPER_KEY')
#CX = os.environ.get('GCS_DEVELOPER_CK')

#print("Type the artist:")
#artist = input()
#text = Get_lyrics(artist,song)
#print(text)

print("Type Term:")
term = input()
Searcher(term)

