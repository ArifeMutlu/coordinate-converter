"""
Basic usage examples for coordinate converter
"""

from converter import wgs84_to_itm, itm_to_wgs84

# Example 1: Convert single coordinate (Istanbul - Sultanahmet)
print("=" * 50)
print("Example 1: Istanbul - Sultanahmet Square")
print("=" * 50)

lat, lon = 41.0057, 28.9769
print(f"Input (WGS84): {lat}°N, {lon}°E")

x, y = wgs84_to_itm(lat, lon)
print(f"Output (ITM): X={x:.2f}, Y={y:.2f}")

# Convert back to verify
lat_back, lon_back = itm_to_wgs84(x, y)
print(f"Verification: {lat_back:.6f}°N, {lon_back:.6f}°E")
print("✅ Conversion successful!\n")


# Example 2: Convert multiple cities
print("=" * 50)
print("Example 2: Major Turkish Cities")
print("=" * 50)

cities = {
    "Istanbul": (41.0082, 28.9784),
    "Ankara": (39.9208, 32.8541),
    "Izmir": (38.4237, 27.1428),
    "Antalya": (36.8969, 30.7133),
}

for city, (lat, lon) in cities.items():
    x, y = wgs84_to_itm(lat, lon)
    print(f"{city:10} → ITM: ({x:>10.2f}, {y:>10.2f})")

print("\n✅ All conversions completed!")
