import urllib.request
import json
import tkinter as tk
from re import search
import PIL
from PIL import ImageTk as a
from PIL import Image


def getImage(url, filePath):
    print("This is file path" + filePath)
    urllib.request.urlretrieve(url, filePath)

def previewImage(path):
    img = Image.open(path)
    img = img.resize((250,250),Image.ANTIALIAS)
    img = a.PhotoImage(img)
    return img

def checkOutPath(path):
    if search("png", path):
        return True
    elif search("jpg", path):
        return True
    elif search("svg", path):
        return True
    elif search("gif", path):
        return True
    else:
        return False


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
    
