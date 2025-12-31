"""
Unit tests for coordinate converter
Run: python -m pytest test_converter.py
"""

import pytest
from converter import wgs84_to_itm, itm_to_wgs84


class TestWGS84ToITM:
    """Test WGS84 to ITM conversion"""
    
    def test_istanbul_coordinates(self):
        """Test Istanbul (Taksim) coordinates"""
        lat, lon = 41.0370, 28.9850
        x, y = wgs84_to_itm(lat, lon)
        
        # Expected values (approximate)
        assert 655000 < x < 660000, "X coordinate out of expected range"
        assert 4540000 < y < 4545000, "Y coordinate out of expected range"
    
    def test_ankara_coordinates(self):
        """Test Ankara (Kızılay) coordinates"""
        lat, lon = 39.9208, 32.8541
        x, y = wgs84_to_itm(lat, lon)
        
        assert 730000 < x < 735000, "X coordinate out of expected range"
        assert 4420000 < y < 4425000, "Y coordinate out of expected range"
    
    def test_invalid_latitude_high(self):
        """Test invalid latitude (too high)"""
        with pytest.raises(ValueError):
            wgs84_to_itm(100, 28.9850)
    
    def test_invalid_latitude_low(self):
        """Test invalid latitude (too low)"""
        with pytest.raises(ValueError):
            wgs84_to_itm(-100, 28.9850)
    
    def test_invalid_longitude_high(self):
        """Test invalid longitude (too high)"""
        with pytest.raises(ValueError):
            wgs84_to_itm(41.0370, 200)
    
    def test_invalid_longitude_low(self):
        """Test invalid longitude (too low)"""
        with pytest.raises(ValueError):
            wgs84_to_itm(41.0370, -200)


class TestITMToWGS84:
    """Test ITM to WGS84 conversion"""
    
    def test_round_trip_istanbul(self):
        """Test round-trip conversion (Istanbul)"""
        original_lat, original_lon = 41.0370, 28.9850
        
        # Convert to ITM
        x, y = wgs84_to_itm(original_lat, original_lon)
        
        # Convert back to WGS84
        result_lat, result_lon = itm_to_wgs84(x, y)
        
        # Should be very close to original
        assert abs(result_lat - original_lat) < 0.0001
        assert abs(result_lon - original_lon) < 0.0001
    
    def test_round_trip_ankara(self):
        """Test round-trip conversion (Ankara)"""
        original_lat, original_lon = 39.9208, 32.8541
        
        x, y = wgs84_to_itm(original_lat, original_lon)
        result_lat, result_lon = itm_to_wgs84(x, y)
        
        assert abs(result_lat - original_lat) < 0.0001
        assert abs(result_lon - original_lon) < 0.0001


def test_coordinate_precision():
    """Test that conversions maintain reasonable precision"""
    test_coords = [
        (41.0082, 28.9784),  # Istanbul
        (39.9208, 32.8541),  # Ankara
        (38.4237, 27.1428),  # Izmir
    ]
    
    for lat, lon in test_coords:
        x, y = wgs84_to_itm(lat, lon)
        result_lat, result_lon = itm_to_wgs84(x, y)
        
        # Precision should be within 0.0001 degrees (~10 meters)
        assert abs(result_lat - lat) < 0.0001
        assert abs(result_lon - lon) < 0.0001


if __name__ == "__main__":
    # Run tests manually
    pytest.main([__file__, "-v"])
