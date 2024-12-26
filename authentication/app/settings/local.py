from .base import BaseConfig
import os

class LocalConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'postgresql://postgres:password@accounting_management_db:5432/accounting_management_db'
    )
