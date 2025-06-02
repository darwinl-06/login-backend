from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.types import TypeDecorator

class UTCDateTime(TypeDecorator):
    impl = DateTime
    
    def process_bind_param(self, value, dialect):
        if value is not None:
            return value.replace(microsecond=0)
        return value

Base = declarative_base()

def get_colombia_time():
    # Obtener la hora actual
    return datetime.now()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    salt = Column(String)
    is_admin = Column(Boolean, default=False)
    last_login = Column(UTCDateTime, default=datetime.now) 