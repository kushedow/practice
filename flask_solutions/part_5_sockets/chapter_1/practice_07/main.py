import socketio
from aiohttp import web

groups = []

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


async def append_to_group(groups, sid):
    """Добавляем пользователя в группу"""
    for group in groups:
        if len(group) == 1:
            group.append(sid)
            break
    else:
        groups.append([sid])

    # Возвращаем группы
    return groups

# подключение
@sio.event
async def connect(sid, environ):
    await append_to_group(groups, sid)
    print(f"Клиент {sid} подключился")
    print(groups)

# отключение
@sio.event
async def disconnect(sid):

    print(f"Клиент {sid} отключился")

# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)
