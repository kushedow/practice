import socketio
from aiohttp import web

users_online = []

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


async def print_server_status(users_online):
    """Пишет количество онлайна"""

    online_count = len(users_online)

    if online_count >= 2:
        status = "Команда в сборе"
    elif online_count == 1:
        status = "Пользователь один"
    elif online_count == 0:
        status = "Сервер пуст"

    print(status)


# подключение
@sio.event
async def connect(sid, environ):

    # Записываем
    users_online.append(sid)
    print(f"Клиент {sid} подключился")
    await print_server_status(users_online)


# отключение
@sio.event
async def disconnect(sid):

    # Удаляем
    users_online.remove(sid)
    print(f"Клиент {sid} отключился")
    await print_server_status(users_online)



# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)

