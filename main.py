from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os
import curses

#spotipy or genius

def Get_lyrics(artist,song):
    return PyLyrics.getAlbums("Eminem")

def Searcher(query):
    gis = GoogleImagesSearch(DK,CX,progressbar_fn=progressbar)
    with GoogleImagesSearch(DK,CX) as gis:
            _search_params ={
                'q': term,
                'num': 3,
                'safe' :'off',
                'fileType' : 'png'
            }
    gis.search(search_params=_search_params,path_to_dir=path)

def progressbar(url, progress):
    print(url + ' '+ progress + '%' )

load_dotenv()
path = 'H:\Documents\SongInPictures\IMG'
DK = os.environ.get('GCS_DEVELOPER_KEY')
CX = os.environ.get('GCS_DEVELOPER_CK')

#print("Type the artist:")
#artist = input()
#text = Get_lyrics(artist,song)
#print(text)

print("Type Term:")
term = input()
Searcher(term)

