### Стартовый код

```
# import eventlet
import socketio
from aiohttp import web

# Создаем экземпляр сокет сервера
sio = socketio.AsyncServer(async_mode='aiohttp')


# подключение
@sio.event
async def connect(sid, environ):
    pass
    
# обработка любого события
@sio.on("message")
async def connect(sid, environ):
    pass

# отключение
@sio.event
async def disconnect(sid):
    pass

# отключение
@sio.event
async def disconnect(sid):
    pass

# создаем экземпляр aiohttp приложения
app = web.Application()
# Связываем приложение с сокетио
sio.attach(app)
# Запускаем aiohttp сервер
web.run_app(app)
```
