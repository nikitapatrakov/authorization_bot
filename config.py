from pydantic import AnyUrl

from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="ignore")
    token_bot: str 
    url_group : AnyUrl


setting = Setting()

