import requests


def get_hubble(image_id, ext='jpeg'):
    status_ready = None
    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(image_id))
    data = response.json()['image_files']
    image_name = "Hubble-{}.{}".format(image_id, ext)
    loading_list = [image['file_url'] for image in data if image['file_url'].endswith(ext)]
    for picture_url in loading_list:
        download_file(picture_url, image_name)

def get_collection(collection_name, ext='jpeg'):
    response = requests.get('http://hubblesite.org/api/v3/images/{}'.format(collection_name))
    for image_id in response.json():
        get_hubble(image_id['id'], ext)


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
