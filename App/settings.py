import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    mysql = DATABASE.get('mysql') or 'pymysql'
    username = DATABASE.get('username') or 'root'
    password = DATABASE.get('password') or '1234'
    host = DATABASE.get('host') or 'localhost'
    port = DATABASE.get('port') or '3306'
    db = DATABASE.get('db') or 'a2'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,mysql,username,password,host,port,db)


class Config():
    TEST = False
    DEBUG = False
    #思考? 书写方式 是 app.config【‘SECRET_KEY’】 = 110  OR SECRET_KEY = '110'
    SECRET_KEY = '100'
    SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'mysql' : 'pymysql',
        'username':'root',
        'password':'1234',
        'host':'localhost',
        'port':'3306',
        'db':'a2'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

env = {
    'develop':DevelopConfig
}