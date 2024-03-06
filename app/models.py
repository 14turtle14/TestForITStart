from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class DeviceStatistics(Base):
    __tablename__ = 'device_statistics'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, index=True)
    timestamp = Column(DateTime, index=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
