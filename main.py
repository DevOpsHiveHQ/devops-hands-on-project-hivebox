from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
from datetime import datetime, timedelta
import uvicorn

app = FastAPI()

# Setting up the Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Version endpoint
@app.get("/version", response_class=HTMLResponse)
def version_page(request: Request):
    return templates.TemplateResponse("version.html", {"request": request, "version": "0.1.0"})

# Function to fetch & filter temperature data
def get_avg_temperature():
    url = "https://api.opensensemap.org/boxes?phenomenon=temperature"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch data from OpenSenseMap API"}

    data = response.json()
    temperatures = []
    now = datetime.utcnow()

    # Extract recent temperature data
    for box in data:
        for sensor in box.get("sensors", []):
            title = sensor.get("title")  # Get the title

            # Ensure title is not None before calling lower()
            if title and title.lower() == "temperature":
                last_measurement = sensor.get("lastMeasurement")

                # Check if last_measurement is a dictionary
                if isinstance(last_measurement, dict):
                    last_time = last_measurement.get("createdAt")
                    if last_time:
                        try:
                            last_time = datetime.strptime(last_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                            if now - last_time <= timedelta(hours=1):
                                temperatures.append(float(last_measurement["value"]))
                        except ValueError:
                            continue  # Skip if timestamp is invalid

    # Calculate average temperature
    if temperatures:
        avg_temperature = sum(temperatures) / len(temperatures)
        return round(avg_temperature, 2)
        
    return None

# Temperature endpoint
@app.get("/temperature", response_class=HTMLResponse)
def temperature_page(request: Request):
    avg_temp = get_avg_temperature()
    return templates.TemplateResponse("temperature.html", {"request": request, "average_temperature": avg_temp})

# Index endpoint
@app.get("/", response_class=HTMLResponse)
def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Start FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
