from models.dao.dbcon import DB
from models.dao.login import LoginDao

GLOBAL_DB = DB()
LOGIN_DAO = LoginDao(GLOBAL_DB)
