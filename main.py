from api.amadeus_client import get_access_token, search_flights
from utils.parser import parse_flight_data
from db.insert import insert_flights
from datetime import date, timedelta
import time

# 전 세계 주요 공항 리스트
AIRPORTS = [
    # 미주
    "JFK", "LAX", "SFO", "SEA", "ORD", "ATL", "DFW", "MIA", "BOS", "IAD",
    "DEN", "YYZ", "YVR", "YUL", "YYC", "MEX",
    # 유럽
    "LHR", "CDG", "FRA", "AMS", "MAD", "BCN", "ZRH", "VIE", "WAW", "HEL",
    "IST", "CPH", "OSL", "ARN",
    # 아시아
    "NRT", "HND", "ICN", "PVG", "PEK", "CAN", "HKG", "TPE", "SIN", "BKK",
    "KUL", "DEL", "BOM", "DOH", "DXB", "AUH",
    # 오세아니아
    "SYD", "MEL", "AKL"
]

# 수집 기간 설정 (2023.07.01 ~ 2025.06.30)
START_DATE = date(2025, 6, 19)
END_DATE = date(2025, 6, 19)
NUM_DAYS = (END_DATE - START_DATE).days + 1  # 총 730일

def run_pipeline():
    token = get_access_token()

    for origin in AIRPORTS:
        for destination in AIRPORTS:
            if origin == destination:
                continue  # 출발지와 도착지가 같으면 제외

            for i in range(NUM_DAYS):
                travel_date = (START_DATE + timedelta(days=i)).isoformat()

                print(f"수집 중: {origin} → {destination}, 날짜: {travel_date}")

                raw_data = search_flights(token, origin=origin, destination=destination, date=travel_date)
                parsed = parse_flight_data(raw_data)

                if parsed:
                    insert_flights(parsed)
                    print(f"{len(parsed)}건 적재 완료")
                else:
                    print("데이터 없음")

                time.sleep(0.3)  # 속도 제한 방지

    print("전체 수집 완료")

if __name__ == "__main__":
    run_pipeline()
