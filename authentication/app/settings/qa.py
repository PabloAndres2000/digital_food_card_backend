from .base import BaseConfig
import os

class QAConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@accounting_management_db:5432/accounting_management_db')
