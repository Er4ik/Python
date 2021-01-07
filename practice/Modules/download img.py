from random import randrange
import urllib.request

names = []

def dwnld_img(url):
    global name
    name = randrange(1, 10)
    name = str(name) + "jpg"
    urllib.request.urlretrieve(url, name)

def chek_name(name):
    if name in names:
        return dwnld_img()
    else:
        names.append(name)
try:
    dwnld_img("https://images.alphacoders.com/665/thumb-350-665091.jpg")
except urllib.error.HTTPError:
    print("Image cannot be loaded.\nPlease try to download another picture")
