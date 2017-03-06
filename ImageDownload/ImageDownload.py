import urllib.request
import random


def download(image):
	name = random.randrange(1, 100)
	full_name = str(name) + '.jpg'
	urllib.request.urlretrieve(url, full_name)

url = input('Please enter an url: ')

download(url)
