# Проект Check Number
### Описание
Web-сервис для проверки наличия телефона в стоп-листе
### Технологии
* asgiref 3.4.1
* Django 3.2.8
* djangorestframework 3.12.4
* pytz 2021.3
* sqlparse 0.4.2
* xlrd 1.2.0

### Запуск проекта в dev-режиме
1. Установите и активируйте виртуальное окружение
2. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
3. Инициализируйте и создайте миграции
 ```
python manage.py migrate
python manage.py makemigrations
```
4. В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
5. Для загрузки данных из excel-документа замените файл "DATA.xlsx" в корень проекта,
затем выполните команду:
```
python manage.py add_number
```
### Автор
Кудрявцев Д.И. (Vurgul)