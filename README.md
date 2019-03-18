# Космический Инстаграм

В данном проекте подгружаются фотографии с последнего запуска Spacex, или коллекции Хаббл в ваш аккаунт в Инстаграмме

### Как установить

Для начала Вам нужно создать файл .env, в котором должны быть прописаны значения
```Python3
username=your_username_in_instagram
password=your_password_in_instagram
```
и сохранить его в корневой папке.

Доступные коллекции hubble:
* `news`
* `holiday_cards`
* `wallpaper`
* `spacecraft`
* `printshop`
* `stsci_gallery`.

Доступные расширения для скачивания с hubble:
* png
* jpg
* tiff
* tif

Для spacex единственным расширением по умолчанию является `jpeg`

#### Пример запуска

* Использование hubble, расширения png и коллекции stsci_gallery:
```#
/spacegram$ Python3 spacegram.py hubble --extension png --collection stsci_gallery
```
* Использование hubble, расширения png и коллекции stsci_gallery:
```#
/spacegram$ Python3 spacegram.py hubble -e jpg -c printshop
```
* Использование spacex, скачивание фотографий с последнего запуска, (расширение по умолчанию jpeg):
```#
/spacegram$ Python3 spacegram.py spacex
```

### Цель проекта

Если данные введены правильно, при выполнении файла spacegram.py высветится: `INFO - Instabot Started`, `INFO - Logged-in successfully `
, что означает успешную авторизацию в Instagram.

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
