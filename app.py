from flask import Flask
from config import GlobalConfig, FactoryConfig

cnf = FactoryConfig(GlobalConfig().ENV_STATE)()
print(cnf.__repr__())

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = cnf.NAME

    return f'Hello, {name} world!'