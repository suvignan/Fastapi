from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}" # database url for postgresql database

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# Host = local host and db name is just ur db name from postgress and user is your username and password is your password for the database
# cursor_factory = RealDictCursor is used to get the result in the form of dictionary instead of tuple

# while True:
#     try:
#         conn = psycopg2.connect(host ='',database = '', user = '', 
#                             password = '',cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ",error)
#         time.sleep(2) # wait for 2 seconds before trying to connect again
#     print("Error: ",error)