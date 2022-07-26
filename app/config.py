

class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOT_TOKEN = '5372356992:AAFRe16dnNsEySkAEhTUyK6SNyHlDu2J6Eg'
    
class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///debug.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///debug.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

Default_Config = ProductionConfig()
