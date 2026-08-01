from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# constates
from .constants import BASE_DIR, ENV_PATH


class Settings(BaseSettings):
    # about bot
    BOT_NAME: str
    VERSION: str

    # author and team
    AUTHOR: str
    TEAM: str

    # discord
    DISCORD_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=ENV_PATH
    )


settings = Settings()
