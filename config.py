import os
from dotenv import load_dotenv


load_dotenv()

db_host = os.getenv("FSTR_DB_HOST")
db_port = os.getenv("FSTR_DB_PORT")
db_login = os.getenv("FSTR_DB_LOGIN")
db_pass = os.getenv("FSTR_DB_PASS")
