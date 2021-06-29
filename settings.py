from typing import Optional

from pydantic import BaseSettings, Field

#  Global configs - put here the  
class Settings(BaseSettings):
    base_url: Optional[str] = None
    env_state: Optional[str] = Field(None, env='env_state')
    name: str = Field(None, name='name')

    class Config:
        # Loads the dotenv file
        env_file: str = '.env'


class DevSettings(Settings):
    class Config:
        env_prefix: str = 'DEV_'


class UatSettings(Settings):
    class Config:
        env_prefix: str = 'UAT_'


# Return a Setting object depending on env_state value (dev|aut)
class SettingsFactory:
    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if not self.env_state:
            raise ValueError('env_state cannot be null - it must be env_state=dev|uat')

        state = self.env_state.lower()
        if state == 'dev':
            return DevSettings()

        elif state == 'uat':
            return UatSettings()

        else:
            raise ValueError(f'Invalid state "{state}" - make sure its "dev" or "uat".')

# Usage
# stt = SettingsFactory(Settings().env_state)()
# print(stt.__repr__())