CREATE TABLE IF NOT EXISTS Weather (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  city TEXT NOT NULL,
  temperature REAL NOT NULL,
  humidity INTEGER NOT NULL,
  description TEXT NOT NULL,
  units TEXT NOT NULL CHECK(units IN ('metric', 'imperial')),
  timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Forecast (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  city TEXT NOT NULL,
  temperature REAL NOT NULL,
  humidity INTEGER NOT NULL,
  description TEXT NOT NULL,
  units TEXT NOT NULL CHECK(units IN ('metric', 'imperial')),
  timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  forecast_date DATE NOT NULL
);