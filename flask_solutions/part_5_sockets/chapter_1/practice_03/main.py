import socketio
from aiohttp import web

users_online = []

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


async def push_online_count():
    """ Отправляет всем обновленное количество онлайна"""
    online_count = len(users_online)
    await sio.emit("message", {"online": online_count})


# подключение
@sio.event
async def connect(sid, environ):

    # Записываем
    users_online.append(sid)
    await push_online_count()


# отключение
@sio.event
async def disconnect(sid):

    # Удаляем
    users_online.remove(sid)
    await push_online_count()



# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)

