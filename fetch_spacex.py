import requests
from download import download_file


def get_spacex():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    for id, images_link in enumerate(response.json()['links']['flickr_images'], 1):
        download_file(images_link, "Space-{}.jpeg".format(id))
