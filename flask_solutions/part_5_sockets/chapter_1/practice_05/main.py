# import eventlet
import datetime

import socketio
from aiohttp import web

users_online = {}

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


# подключение
@sio.event
async def connect(sid, environ):

    # Записываем
    users_online[sid] = datetime.datetime.now()
    print(f"Клиент {sid} подключился")

# отключение
@sio.event
async def disconnect(sid):

    # Достаем информацию из словаря
    user_joined_at = users_online[sid]
    timedelta = datetime.datetime.now() - user_joined_at

    # Вычисляем прошедшее время
    sec_delta = timedelta.total_seconds()

    # Вычисляем минутки и секунды
    minutes = round(sec_delta // 60)
    seconds = str(round(sec_delta % 60)).rjust(2,"0")
    delta_format = f"{minutes}:{seconds}"

    # Выводим результат
    print(f"Клиент {sid} отключился {delta_format}")


# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)

