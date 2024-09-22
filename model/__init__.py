from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model.base import Base
from model.Glicose import Glicose

import os

db_path = "database/"

# Se a pasta não existir, crie uma.
if not os.path.exists(db_path):
   os.makedirs(db_path)

# database access url
db_url = 'sqlite:///%s/db.sqlite3' % db_path

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url) 

Base.metadata.create_all(engine)