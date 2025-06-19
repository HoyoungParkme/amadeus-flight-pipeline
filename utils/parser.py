# utils/parser.py

def parse_flight_data(raw_data):
    results = []
    for offer in raw_data.get("data", []):
        price = offer.get("price", {}).get("total")
        itinerary = offer.get("itineraries", [])[0]
        segment = itinerary.get("segments", [])[0]
        departure = segment.get("departure", {})
        arrival = segment.get("arrival", {})

        results.append({
            "origin": departure.get("iataCode"),
            "destination": arrival.get("iataCode"),
            "departure_at": departure.get("at"),
            "arrival_at": arrival.get("at"),
            "price": price
        })
    return results
