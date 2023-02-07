import socketio
from aiohttp import web

users_online = {}

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


# подключение
@sio.event
async def connect(sid, environ):

    is_leader = len(users_online) == 0
    role = "leader" if is_leader else "observer"

    users_online[sid] = {"role": role}

    print(f"Клиент {sid} подключился с ролью {role}")

# отключение
@sio.event
async def disconnect(sid):

    is_leader = users_online[sid]["role"] == "leader"

    if is_leader:
        print("Отключаем всех пользователей")
        for users_id in list(users_online.keys()):
            await sio.disconnect(users_id)
    else:
        print("Отключаем одного пользователя")


# создаем экземпляр aiohttp приложения
app = web.Application()

# Связываем приложение с сокетио
sio.attach(app)

# Запускаем aiohttp сервер
web.run_app(app)
