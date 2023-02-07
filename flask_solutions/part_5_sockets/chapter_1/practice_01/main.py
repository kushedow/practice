# import eventlet
import socketio
from aiohttp import web

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')

# подключение
@sio.event
async def connect(sid, environ):
    print(sid, "connected")
    await sio.emit("message", data="welcome to the server", sid=sid)

# создаем экземпляр aiohttp приложения
app = web.Application()
# Связываем приложение с сокетио
sio.attach(app)
# Запускаем aiohttp сервер
web.run_app(app)

