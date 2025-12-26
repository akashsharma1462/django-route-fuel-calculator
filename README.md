# Django Route Fuel Calculator API

This project is a Django REST API created as part of a backend coding assessment.
The API calculates fuel stops and total fuel cost for a road trip inside the USA
using fuel price data provided in a CSV file.

The main goal of this project is to keep the logic simple, readable, and easy to understand.

---

## 🚀 What This Project Does

- Accepts a **start** and **end** location
- Assumes the trip is within the USA
- Uses the following vehicle assumptions:
  - Maximum range: **500 miles**
  - Mileage: **10 miles per gallon**
- Reads fuel prices from a provided CSV file
- Calculates:
  - Fuel stops required during the trip
  - Total fuel cost
- Returns the result in **JSON format**

---

## 🛠 Technologies Used

- Python
- Django (latest stable version)
- Django REST Framework
- CSV file for fuel price data
- Postman for API testing

---

## 📁 Project Structure

![Project Structure](images/project-structure.png)

---

## ⚙️ How to Run the Project Locally

## 1️⃣ Clone the repository
```bash
git clone https://github.com/akashsharma1462/django-route-fuel-calculator.git
cd django-route-fuel-calculator

## 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate

## 3️⃣ Install required packages
```bash
pip install django djangorestframework

## 4️⃣ Run the Django server
```bash
python manage.py runserver

## The server will start at:
http://127.0.0.1:8000/

## 📡 API Endpoint Details
POST /api/route/

## Request Body (JSON)
{
  "start": "New York",
  "end": "Los Angeles"
}

## Sample Response
{
  "start": "New York",
  "end": "Los Angeles",
  "distance_miles": 2800,
  "fuel_stops": [
    {
      "city": "Harrold",
      "state": "TX",
      "price": 2.68733333
    }
  ],
  "total_fuel_cost": 682.5
}

## 🧠 How the Logic Works (Simple Explanation)

The total trip distance is calculated (fixed example for simplicity).
The vehicle can travel 500 miles on a full tank.
Fuel prices are loaded from the CSV file.
Fuel stations are sorted by cheapest price.
Whenever the remaining distance exceeds vehicle range, a fuel stop is added.
Total fuel cost is calculated based on mileage and fuel price.

## 🧪 Testing the API Using Postman
Open Postman
Create a new POST request
Enter URL:
http://127.0.0.1:8000/api/route/
Go to Body → raw → JSON
Add request body and click Send
View the JSON response

---

# 🔍 Assumptions Made

- The trip is assumed to be within the USA
- Vehicle range is fixed at 500 miles
- Mileage is fixed at 10 miles per gallon
- Fuel prices are taken directly from the provided CSV file
- Distance calculation is kept simple for clarity

---

# Thanks.......

---
