# Coordinate Converter 🗺️

A Python utility for converting coordinates between WGS84 (GPS) and ITM (Turkish National Grid System).

## Features
- Convert WGS84 (lat/lon) to ITM (x/y)
- Convert ITM (x/y) to WGS84 (lat/lon)
- Simple command-line interface
- Easy to integrate into other projects

## 🚀 Batch Conversion (NEW!)

Convert multiple coordinates at once using CSV files.

### Usage
```python
from batch_converter import batch_wgs84_to_itm

# Convert multiple GPS coordinates to ITM
batch_wgs84_to_itm('input_wgs84.csv', 'output_itm.csv')
```

### Input CSV Format
```
latitude,longitude
41.0082,28.9784
39.9208,32.8541
```

### Output
```
x,y
658247.32,4538011.45
```

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
## 🧪 Testing

Run tests:
```bash
pip install pytest
python -m pytest test_converter.py -v
```

All tests should pass ✅

### Test Coverage

- ✅ Valid coordinate conversions
- ✅ Invalid input validation
- ✅ Round-trip accuracy
- ✅ Coordinate precision checks
```
## 📚 Examples

See the `examples/` folder for detailed usage examples:

### Basic Usage
```bash
python examples/basic_usage.py
```

### Batch Conversion
```bash
python examples/batch_example.py
```

## 🎓 Tutorial

### Converting a Single Coordinate
```python
from converter import wgs84_to_itm

# Your GPS coordinates (e.g., from smartphone)
lat, lon = 41.0082, 28.9784

# Convert to Turkish Grid (ITM)
x, y = wgs84_to_itm(lat, lon)

print(f"ITM coordinates: {x:.2f}, {y:.2f}")
```

### Converting Multiple Coordinates
```python
from converter import wgs84_to_itm

cities = [
    (41.0082, 28.9784),  # Istanbul
    (39.9208, 32.8541),  # Ankara
]

for lat, lon in cities:
    x, y = wgs84_to_itm(lat, lon)
    print(f"({lat}, {lon}) → ITM: ({x:.2f}, {y:.2f})")
```

### Batch Processing from CSV
```python
from batch_converter import batch_wgs84_to_itm

batch_wgs84_to_itm('input.csv', 'output.csv')

## Background
This tool was created to simplify coordinate conversions for GIS projects in Turkey. The ITM (Turkish National Grid) is commonly used in Turkish geospatial applications.

## License
MIT License - feel free to use in your projects!

## Author
Arife Mutlu - [LinkedIn](https://linkedin.com/in/arife-mutlu-75020942)
