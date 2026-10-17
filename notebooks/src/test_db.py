import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
user = os.getenv("DB_USER")
pwd = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}")
with engine.connect() as conn:
    print("Connected. MySQL version:", conn.execute(text("SELECT VERSION()")).scalar())