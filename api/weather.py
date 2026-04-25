import logging
import sqlite3
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
logging.basicConfig(level=logging.INFO)

class WeatherRequest(BaseModel):
    city: str

@router.post("/weather")
def get_weather(req: WeatherRequest):
    try:
        conn = sqlite3.connect("weather.db")
        cur = conn.cursor()
        cur.execute("SELECT data FROM weather WHERE city=?", (req.city,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(404, "City not found")
        return {"weather": row[0]}
    except Exception as e:
        logging.exception("Error in get_weather endpoint")
        raise HTTPException(500, str(e))
