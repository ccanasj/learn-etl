from sqlalchemy import Column, Date, Time, Integer, Float
from models import Base


class Weather(Base):
    __tablename__ = "weather"

    temperature = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)

    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)

    def __repr__(self) -> str:
        return f"{self.date}|{self.time} |{self.temperature}°C |{self.humidity}%"
