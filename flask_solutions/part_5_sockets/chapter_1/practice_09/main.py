import asyncio

import socketio
from aiohttp import web

LIMIT_ON_SERVER = 2
users_online = []

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')

# подключение
@sio.event
async def connect(sid, environ):

    print(f"Клиент {sid} подключился")

    if len(users_online) < LIMIT_ON_SERVER:

        # Если места свободны
        users_online.append(sid)
        await sio.emit("message", {"online": len(users_online)})

    else:

        # Если места занять
        print(f"Принудительно отключаем клиента {sid}")
        await sio.disconnect(sid)

# отключение
@sio.event
async def disconnect(sid):

    if sid in users_online:
        users_online.remove(sid)

    print(f"Клиент {sid} отключился")


# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)
