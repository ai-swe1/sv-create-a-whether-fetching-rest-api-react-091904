# Weather App
This is a simple weather app that uses FastAPI as the backend and OpenWeatherMap API to fetch weather data.

## Setup
1. Install dependencies by running `pip install -r requirements.txt`
2. Replace `YOUR_API_KEY` in `main.py` with your actual OpenWeatherMap API key
3. Run the app by executing `uvicorn main:app --host 0.0.0.0 --port 8000`

## Usage
1. Open `http://localhost:8000` in your browser
2. Enter a city name in the input field and click the "Get Weather" button
3. The app will display the current weather description for the entered city