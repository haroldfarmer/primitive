import urllib.request
import json
from re import search

def getImage(url, filePath):
    print("This is file path" + filePath)
    urllib.request.urlretrieve(url, filePath)

        
    
def getExtension(url):
    if search(".png", url):
        return '.png'
    elif search(".jpg", url):
        return '.jpg'
    elif search(".svg", url):
        return '.svg'
    elif search(".gif", url):
        return '.gif'
    else:
        return ''
    
