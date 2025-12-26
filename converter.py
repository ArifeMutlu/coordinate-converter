
"""
Coordinate Converter: WGS84 <-> ITM (Turkish National Grid)
Author: Arife Mutlu
"""

from pyproj import Transformer

# ITM (EPSG:5254) projection parameters
# WGS84 (EPSG:4326) is the standard GPS coordinate system

def wgs84_to_itm(latitude, longitude):
    """
    Convert WGS84 (GPS) coordinates to ITM (Turkish Grid).
    
    Args:
        latitude (float): Latitude in decimal degrees
        longitude (float): Longitude in decimal degrees
    
    Returns:
        tuple: (x, y) in ITM coordinates
    
    Example:
        >>> x, y = wgs84_to_itm(41.0082, 28.9784)
        >>> print(f"ITM: {x:.2f}, {y:.2f}")
    """
    # Create transformer from WGS84 to ITM
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:5254", always_xy=True)
    
    # Transform coordinates
    x, y = transformer.transform(longitude, latitude)
    
    return x, y


def itm_to_wgs84(x, y):
    """
    Convert ITM (Turkish Grid) coordinates to WGS84 (GPS).
    
    Args:
        x (float): X coordinate in ITM
        y (float): Y coordinate in ITM
    
    Returns:
        tuple: (latitude, longitude) in WGS84
    
    Example:
        >>> lat, lon = itm_to_wgs84(658000, 4537000)
        >>> print(f"GPS: {lat:.6f}, {lon:.6f}")
    """
    # Create transformer from ITM to WGS84
    transformer = Transformer.from_crs("EPSG:5254", "EPSG:4326", always_xy=True)
    
    # Transform coordinates
    longitude, latitude = transformer.transform(x, y)
    
    return latitude, longitude


def main():
    """
    Example usage of the coordinate converter.
    """
    print("=" * 50)
    print("Coordinate Converter: WGS84 <-> ITM")
    print("=" * 50)
    
    # Example 1: Istanbul coordinates (Taksim Square)
    print("\n📍 Example 1: Istanbul - Taksim Square")
    lat, lon = 41.0370, 28.9850
    print(f"WGS84 Input: {lat}, {lon}")
    
    x, y = wgs84_to_itm(lat, lon)
    print(f"ITM Output: {x:.2f}, {y:.2f}")
    
    # Convert back
    lat_back, lon_back = itm_to_wgs84(x, y)
    print(f"WGS84 (converted back): {lat_back:.6f}, {lon_back:.6f}")
    
    # Example 2: Ankara coordinates
    print("\n📍 Example 2: Ankara - Kızılay")
    lat2, lon2 = 39.9208, 32.8541
    print(f"WGS84 Input: {lat2}, {lon2}")
    
    x2, y2 = wgs84_to_itm(lat2, lon2)
    print(f"ITM Output: {x2:.2f}, {y2:.2f}")
    
    print("\n" + "=" * 50)
    print("✅ Conversion completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
