"""
Coordinate Converter: WGS84 <-> ITM (Turkish National Grid)
Author: Arife Mutlu
Version: 1.1.0 - Added error handling
"""

from pyproj import Transformer
import sys

def wgs84_to_itm(latitude, longitude):
    """
    Convert WGS84 (GPS) coordinates to ITM (Turkish Grid).
    
    Args:
        latitude (float): Latitude in decimal degrees (-90 to 90)
        longitude (float): Longitude in decimal degrees (-180 to 180)
    
    Returns:
        tuple: (x, y) in ITM coordinates
        
    Raises:
        ValueError: If coordinates are out of valid range
    
    Example:
        >>> x, y = wgs84_to_itm(41.0082, 28.9784)
        >>> print(f"ITM: {x:.2f}, {y:.2f}")
    """
    # Validate input
    if not -90 <= latitude <= 90:
        raise ValueError(f"Invalid latitude: {latitude}. Must be between -90 and 90.")
    
    if not -180 <= longitude <= 180:
        raise ValueError(f"Invalid longitude: {longitude}. Must be between -180 and 180.")
    
    try:
        # Create transformer from WGS84 to ITM
        transformer = Transformer.from_crs("EPSG:4326", "EPSG:5254", always_xy=True)
        
        # Transform coordinates
        x, y = transformer.transform(longitude, latitude)
        
        return x, y
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}", file=sys.stderr)
        raise


def itm_to_wgs84(x, y):
    """
    Convert ITM (Turkish Grid) coordinates to WGS84 (GPS).
    
    Args:
        x (float): X coordinate in ITM
        y (float): Y coordinate in ITM
    
    Returns:
        tuple: (latitude, longitude) in WGS84
        
    Raises:
        ValueError: If coordinates are invalid
    
    Example:
        >>> lat, lon = itm_to_wgs84(658000, 4537000)
        >>> print(f"GPS: {lat:.6f}, {lon:.6f}")
    """
    try:
        # Create transformer from ITM to WGS84
        transformer = Transformer.from_crs("EPSG:5254", "EPSG:4326", always_xy=True)
        
        # Transform coordinates
        longitude, latitude = transformer.transform(x, y)
        
        return latitude, longitude
        
    except Exception as e:
        print(f"❌ Error during conversion: {e}", file=sys.stderr)
        raise


def main():
    """
    Example usage with error handling.
    """
    print("=" * 50)
    print("Coordinate Converter: WGS84 <-> ITM")
    print("=" * 50)
    
    try:
        # Example 1: Valid coordinates
        print("\n📍 Example 1: Istanbul - Taksim Square")
        lat, lon = 41.0370, 28.9850
        print(f"WGS84 Input: {lat}, {lon}")
        
        x, y = wgs84_to_itm(lat, lon)
        print(f"ITM Output: {x:.2f}, {y:.2f}")
        
        # Convert back
        lat_back, lon_back = itm_to_wgs84(x, y)
        print(f"WGS84 (converted back): {lat_back:.6f}, {lon_back:.6f}")
        print("✅ Conversion successful!")
        
        # Example 2: Invalid coordinates (will raise error)
        print("\n📍 Example 2: Testing error handling")
        try:
            invalid_x, invalid_y = wgs84_to_itm(100, 200)  # Invalid!
        except ValueError as e:
            print(f"⚠️ Caught error as expected: {e}")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        return 1
    
    print("\n" + "=" * 50)
    print("✅ All examples completed!")
    print("=" * 50)
    return 0


if __name__ == "__main__":
    sys.exit(main())

