from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread" : False})
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base
