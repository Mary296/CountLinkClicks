# Обрезка ссылок с помощью битли

  Программа получает ссылку, если ссылка является битлинком, она вернет колличество кликов по ней за всё время. Если ссылка не битлинк, пограмма возвращает сокращенную ссылку.
  
  Для запуска требуется Ваш токен API Bitly. Чтобы cпрятать личные данные в программе, необходимо воспользоваться `environment vatiables` (переменными окружения). Создайте рядом с `main.py` файл `.env` и запишите в него переменную, хранящую значение токена.
  Выгрузка этой переменной в память осуществляется при помощи функции `load_dotenv()` (`from dotenv import load_dotenv`).
  
  Затем используйте модуль `os`, чтобы считать токен:
  ```python
  import os

  token = os.environ['BITLY_TOKEN']
  ```
### Как установить

  У вас должен быть установлен python3.
  Далее используйте `pip` (или `pip3`) для установки зависимостей.

  Введите в терминале: 
  ```
  pip install -r requirements.txt
  ```
  Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

###Примеры запуска

  ```
  username:~/ProjectTitle$ python3 main.py https://yandex.ru
  Битлинк: https://bit.ly/3mIqrLV
  ```
  ```
  username:~/ProjectTitle$ python3 main.py https://bit.ly/3mIqrLV
  Количество кликов = 1
  ```

### Цель проекта

  Проект написан в учебных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).