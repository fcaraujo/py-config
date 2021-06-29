from typing import Optional

from pydantic import BaseSettings, Field

class GlobalConfig(BaseSettings):
    # Global configs
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    BASE_URL: Optional[str] = None

    NAME: str = Field('Default', name="NAME")

    class Config:
        # Loads the dotenv file
        env_file: str = '.env'


class DevConfig(GlobalConfig):
    # Dev config

    class Config:
        env_prefix: str = 'DEV_'


class UatConfig(GlobalConfig):
    # UAT config

    class Config:
        env_prefix: str = 'UAT_'


class FactoryConfig:
    # Return a config depending on ENV_STATE variable
    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        state = self.env_state

        if state == 'dev':
            return DevConfig()

        elif state == 'uat':
            return UatConfig()

        else:
            raise Exception(f'Invalid state "{state}" - make sure its "dev" or "uat".')

# Usage
cnf = FactoryConfig(GlobalConfig().ENV_STATE)()
print(cnf.__repr__())