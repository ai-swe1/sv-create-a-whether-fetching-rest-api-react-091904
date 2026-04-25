from alembic import op
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'Weather'
    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    units = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=func.current_timestamp())

class Forecast(Base):
    __tablename__ = 'Forecast'
    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    units = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=func.current_timestamp())
    forecast_date = Column(Date, nullable=False)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
