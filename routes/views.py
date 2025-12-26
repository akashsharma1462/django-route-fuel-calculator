import csv
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

# vehicle details
MAX_DISTANCE = 500     # miles
MILEAGE = 10           # miles per gallon


def get_fuel_data():
    data = []

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(
        base_dir,
        "routes",
        "data",
        "fuel-prices-for-be-assessment.csv"
    )

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append({
                "city": row["City"],
                "state": row["State"],
                "price": float(row["Retail Price"])
            })

    return data


@api_view(["POST"])
def route_api(request):
    start = request.data.get("start")
    end = request.data.get("end")

    if not start or not end:
        return Response({"message": "start and end required"}, status=400)

    # fixed distance example (simple and explainable)
    total_distance = 2800  # miles

    fuel_stations = get_fuel_data()

    # sort by cheapest price
    fuel_stations.sort(key=lambda x: x["price"])

    remaining_distance = total_distance
    fuel_stops = []
    total_cost = 0

    for station in fuel_stations:
        if remaining_distance <= MAX_DISTANCE:
            break

        gallons_needed = MAX_DISTANCE / MILEAGE
        cost = gallons_needed * station["price"]

        total_cost += cost
        remaining_distance -= MAX_DISTANCE

        fuel_stops.append({
            "city": station["city"],
            "state": station["state"],
            "price": station["price"]
        })

    return Response({
        "start": start,
        "end": end,
        "distance_miles": total_distance,
        "fuel_stops": fuel_stops,
        "total_fuel_cost": round(total_cost, 2)
    })
