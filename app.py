from flask import Flask
from settings import Settings, SettingsFactory

# Settings
settings = SettingsFactory(Settings().env_state)()
print(settings.__repr__())

# Flask App
app = Flask(__name__)
@app.route('/')
def hello_world():
    base_url = settings.base_url
    name = settings.name

    link = f'<a href="{base_url}" target="_blank">Link</a>'

    return f'Hello, {name} world - visit this {link}!'