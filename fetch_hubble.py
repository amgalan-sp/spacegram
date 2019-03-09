import requests


def get_hubble(image_id, ext='jpeg'):
    status_ready = None
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(image_id))
    data = response.json()['image_files']
    url = 'file_url'
    image_name = "Hubble-{}.{}".format(image_id, ext)
    get_load = [download_file(image['file_url'], image_name) for image in data if image['file_url'].split('.')[-1] == ext]


def get_collection(collection_name, ext='jpeg'):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection_name))
    for image_id in response.json():
        get_hubble(image_id['id'], ext)


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
