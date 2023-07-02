from dotenv import load_dotenv

load_dotenv()

from ETL import get_weather, clean_data, save_data
from models import Base
from utils import engine


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    raw_data = get_weather(92)

    data = clean_data(raw_data)

    save_data(data)
