# config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

# Amadeus API 설정
AMADEUS_CLIENT_ID = os.getenv("AMADEUS_CLIENT_ID")
AMADEUS_CLIENT_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")

# PostgreSQL 연결 URI
DATABASE_URL = os.getenv("DATABASE_URL")
