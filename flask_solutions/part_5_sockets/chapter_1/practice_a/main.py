import asyncio
import socketio
from aiohttp import web

users_online = {}

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')

#######################


async def disconnect_after_3(sid):
    """ Асинхронная функция отключающая клиента через 3 секунды"""
    await asyncio.sleep(3)
    await sio.disconnect(sid)
    print(f"Клиент {sid} отсоединился")


# используем осинки
@sio.event
async def connect(sid, environ):

    print(f"Клиент {sid} подключился, ждем 3 секунды")
    loop = asyncio.get_running_loop()
    loop.create_task(disconnect_after_3(sid))


# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)

