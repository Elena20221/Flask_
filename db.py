from sqlalchemy import Column, String, Integer, DateTime, create_engine,func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import atexit

PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/netology'

engine = create_engine(PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)


class Advertisement(Base):

    __tablename__='Adv'
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    owner = Column(String(255), index=True, nullable=False)


Base.metadata.create_all(bind=engine)