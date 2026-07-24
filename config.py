from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent

# CSV File
CSV_FILE = BASE_DIR / "dealers.csv"

# Template Folder
TEMPLATE_DIR = BASE_DIR / "templates"

# Static Folder
STATIC_DIR = BASE_DIR / "static"

# API Details
APP_NAME = "Dealer Finder API"

VERSION = "1.0.0"

DESCRIPTION = """
A mobile-first dealer finder application built using FastAPI.

Features:
- Search by pincode
- Search by dealer name
- Search nearest dealers
- Geolocation support
"""

# Maximum nearest dealers returned
MAX_RESULTS = 5

# Earth Radius (km)
EARTH_RADIUS = 6371