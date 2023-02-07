import socketio
from aiohttp import web

groups = []

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


async def append_to_groups(groups, sid):
    """Добавляем пользователя в группу"""
    for group in groups:
        if len(group) == 1:
            group.append(sid)
            break
    else:
        groups.append([sid])

    # Возвращаем группы
    return groups


async def remove_from_groups(groups, sid):
    """Удаляем пользователя из группы, где он был"""

    for group in groups:
        if sid in group:
            group.remove(sid)
            return groups

# подключение
@sio.event
async def connect(sid, environ):
    await append_to_groups(groups, sid)
    print(f"Клиент {sid} подключился")
    print(groups)

# отключение
@sio.event
async def disconnect(sid):

    await remove_from_groups(groups, sid)
    print(f"Клиент {sid} отключился")
    print(groups)

# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)
