from aiohttp import web
import os

# Обработчик старта приложения
async def on_startup(app):
    # Твой код инициализации, например, настройка соединений
    print("Приложение запускается...")

# Обработчик маршрута
async def handle(request):
    return web.Response(text="Hello, world")

# Настройка приложения
app = web.Application()

# Регистрируем on_startup как функцию с аргументом
app.on_startup.append(on_startup)

# Регистрируем маршруты
app.router.add_get('/', handle)

# Запускаем сервер на заданном порту (например, PORT = 8080)
PORT = int(os.environ.get("PORT", 8080))
web.run_app(app, port=PORT)

