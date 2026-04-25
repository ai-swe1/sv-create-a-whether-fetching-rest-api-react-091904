from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn
import sqlite3
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)

class Weather(BaseModel):
    id: int
    city: str
    temperature: float
    humidity: int
    description: str
    units: str
    timestamp: str

class Forecast(BaseModel):
    id: int
    city: str
    temperature: float
    humidity: int
    description: str
    units: str
    timestamp: str
    forecast_date: str

@app.get("/weather")
async def get_weather():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Weather')
    rows = cursor.fetchall()
    weather_list = []
    for row in rows:
        weather = Weather(
            id=row[0],
            city=row[1],
            temperature=row[2],
            humidity=row[3],
            description=row[4],
            units=row[5],
            timestamp=row[6]
        )
        weather_list.append(weather)
    return weather_list

@app.get("/forecast")
async def get_forecast():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Forecast')
    rows = cursor.fetchall()
    forecast_list = []
    for row in rows:
        forecast = Forecast(
            id=row[0],
            city=row[1],
            temperature=row[2],
            humidity=row[3],
            description=row[4],
            units=row[5],
            timestamp=row[6],
            forecast_date=row[7]
        )
        forecast_list.append(forecast)
    return forecast_list

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)