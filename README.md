## API для телеграм бота GPT bot
### Описание и установка проекта gpt_bot_api
#### Это мой второй пэт-проект. Он написан на Django, Django Rest Framework.
#### Используется только для интеграции базы данных с телеграм ботом gpt bot для сохранения и извлечения информации о запросах и платежах.
---
## Установка и запуск проекта
1. Проект написан на чистейшем питоне, так что, если у вас он еще не установлен,
[милости просим](https://www.python.org/downloads/).

2. В комнадной строке клонируйте этот репозиторий себе на компьютер:
```
$ git clone git@github.com:makskhaliosa/gpt_bot_api.git
```

3. Перейдите в папку talkie_bot
```
$ cd talkie_bot
```

4. Создайте и активируйте виртуальное окружение:
```
$ python -m venv venv

$ source venv/Scripts/activate
```

5. Установите зависимости проекта:
```
$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

6. Выполните миграции:
```
$ python manage.py migrate
```

7. Запустите проект:
```
$ python manage.py runserver
```

### Документация доступна по адресу:
##### BASE_URL/api/v1/schema/swagger-ui/
