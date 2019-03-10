import os
from instabot import Bot
from dotenv import load_dotenv
from fetch_spacex import get_spacex
from fetch_hubble import get_collection
import argparse

def make_dir_for_images(foldername='images'):
    os.makedirs(foldername)
    filepath = os.path.join(os.getcwd(), foldername)
    return filepath

def upload_photos(ext):
    username = os.getenv('username')
    password = os.getenv('password')
    bot = Bot()
    bot.login(username=username, password=password)
    picture_list = [pics for pics in os.listdir() if pics.endswith('.{}'.format(ext))]

    #filter_by_extension(files):
    #    return files.endswith('.{}'.format(extension))
    #picture_list = list(filter(filter_by_extension(files), files))
    for pics in picture_list:
        bot.upload_photo(pics, caption='Nice Pic')


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Defining hubble you have to give extension')
    parser.add_argument('-f', '--foldername', help='name of folder, which you can give the name')
    parser.add_argument('-e','--extension', type=str, help='you can give extension(format) of a photo like jpg, png, jpg, tiff' )
    parser.add_argument('definite', help='you have 2 defs: spacex or hubble')
    parser.add_argument('-c', '--collection', help='if you use hubble, you need to input name of collection')
    args = parser.parse_args()
    collection_name = args.collection
    extension = args.extension
    definition = args.definite
    foldername = args.foldername
    if foldername:
        os.chdir(make_dir_for_images(foldername))
    else:
        os.chdir(make_dir_for_images())
    if definition == 'spacex':
        get_spacex()
        extension = 'jpeg'
    elif definition == 'hubble':
        get_collection(collection_name, extension)
    else:
        print('choose a definition: download spacex or huuble shoots')
    upload_photos(extension)
