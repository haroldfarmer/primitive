import urllib.request
import json
from re import search

def getImage(url, filePath, fileName):
    ext = getExtension(url)
    if ext != '':
        full_path = filePath + '/' + fileName + '.' + ext
        print(full_path)
        urllib.request.urlretrieve(url, full_path)

        
    
def getExtension(url):
    if search("png", url):
        return 'png'
    elif search("jpg", url):
        return 'jpg'
    elif search("svg", url):
        return 'svg'
    elif search("gif", url):
        return 'gif'
    else:
        return ''
    
