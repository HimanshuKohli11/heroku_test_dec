from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
SQLALCHEMY_DATABASE_URL = "postgres://hvvrxmkbzwbufr:95261e73a335ec62a4e24ee2ae89e23c904e677d30ce5f55a5cb0a6458effa0d@ec2-3-227-68-43.compute-1.amazonaws.com:5432/d2ffh79jt5que7"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
