from .base import BaseConfig
import os

class ProdConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@prod-db:5432/accounting_management_db')
