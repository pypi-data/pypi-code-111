import importlib
import os
import sys
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    AUTH_USER_MODEL_NAME: str = "User"
    AUTH_APP_NAME: str = "fast_tmp"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    FASTAPI_SETTINGS_MODULE: Optional[str]
    DATABASE_URL: str
    DEBUG: bool = True
    LOGIN_URL: str = "/api-token-auth"
    LOCAL_STATIC: bool = False

    @validator("DEBUG", pre=True, allow_reuse=True)
    def get_debug(cls, v: str) -> bool:
        if isinstance(v, str):
            if v != "True":
                return False
        return True

    @validator("BACKEND_CORS_ORIGINS", pre=True, allow_reuse=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SENTRY_DSN: Optional[HttpUrl] = None
    SENTRY_ENVIROMENT: str = "development"

    @validator("SENTRY_DSN", pre=True, allow_reuse=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if v and len(v) > 0:
            return v
        return None

    DB_TYPE: str = "mysql"
    # 额外的配置信息
    EXTRA_SETTINGS: Dict[str, Any] = {}

    # cas相关配置
    CAS_SERVER_URL: str = "/cas/"

    class Config:
        case_sensitive = True
        env_file = ".env"

    def __init__(self):
        super(Settings, self).__init__()

        workdir = os.getcwd()  # 把工作路径加入到代码执行里面
        for path in sys.path:
            if path == workdir:
                break
        else:
            sys.path.append(workdir)
        if self.FASTAPI_SETTINGS_MODULE:
            try:
                mod = importlib.import_module(self.FASTAPI_SETTINGS_MODULE)
                for setting in dir(mod):
                    if setting.isupper():
                        setting_value = getattr(mod, setting)
                        if hasattr(self, setting):
                            setattr(self, setting, setting_value)
                        else:
                            self.EXTRA_SETTINGS[setting] = setting_value
            except Exception as e:
                raise ImportError(f"导入settings报错:{e}")

        if self.SENTRY_DSN:
            import sentry_sdk

            sentry_sdk.init(
                dsn=self.SENTRY_DSN,
                environment=self.SENTRY_ENVIROMENT,
            )


settings = Settings()
