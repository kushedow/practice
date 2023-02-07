# import eventlet
import socketio
from aiohttp import web

users_online = []

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


# подключение
@sio.event
async def connect(sid, environ):
    print("Клиент подключился")
    users_online.append(sid)
    print(users_online)

# отключение
@sio.event
async def disconnect(sid):
    print("Клиент отключился")
    users_online.remove(sid)
    print(users_online)

# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)

