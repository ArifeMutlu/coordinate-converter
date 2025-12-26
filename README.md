# Coordinate Converter 🗺️

A Python utility for converting coordinates between WGS84 (GPS) and ITM (Turkish National Grid System).

## Features
- Convert WGS84 (lat/lon) to ITM (x/y)
- Convert ITM (x/y) to WGS84 (lat/lon)
- Simple command-line interface
- Easy to integrate into other projects

## Tech Stack
- Python 3.x
- pyproj (coordinate transformation library)

## Installation
```bash
# Clone the repository
git clone https://github.com/ArifeMutlu/coordinate-converter.git
cd coordinate-converter

# Install dependencies
pip install -r requirements.txt
```

## Usage
```python
from converter import wgs84_to_itm, itm_to_wgs84

# Convert GPS coordinates to ITM
x, y = wgs84_to_itm(41.0082, 28.9784)  # Istanbul coordinates
print(f"ITM: {x}, {y}")

# Convert ITM back to GPS
lat, lon = itm_to_wgs84(x, y)
print(f"WGS84: {lat}, {lon}")
```

## Background
This tool was created to simplify coordinate conversions for GIS projects in Turkey. The ITM (Turkish National Grid) is commonly used in Turkish geospatial applications.

## License
MIT License - feel free to use in your projects!

## Author
Arife Mutlu - [LinkedIn](https://linkedin.com/in/arife-mutlu-75020942)
