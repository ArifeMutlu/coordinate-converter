"""
Batch Coordinate Converter
Process multiple coordinates at once
"""

from converter import wgs84_to_itm, itm_to_wgs84
import csv

def batch_wgs84_to_itm(input_file, output_file):
    """
    Convert multiple WGS84 coordinates from CSV to ITM
    
    Input CSV format: latitude,longitude
    Output CSV format: x,y
    """
    results = []
    
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        
        for row in reader:
            lat, lon = float(row[0]), float(row[1])
            x, y = wgs84_to_itm(lat, lon)
            results.append([x, y])
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])
        writer.writerows(results)
    
    print(f"✅ Converted {len(results)} coordinates!")
    print(f"📁 Output saved to: {output_file}")

def batch_itm_to_wgs84(input_file, output_file):
    """
    Convert multiple ITM coordinates from CSV to WGS84
    
    Input CSV format: x,y
    Output CSV format: latitude,longitude
    """
    results = []
    
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        
        for row in reader:
            x, y = float(row[0]), float(row[1])
            lat, lon = itm_to_wgs84(x, y)
            results.append([lat, lon])
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['latitude', 'longitude'])
        writer.writerows(results)
    
    print(f"✅ Converted {len(results)} coordinates!")
    print(f"📁 Output saved to: {output_file}")


# Example usage
if __name__ == "__main__":
    print("=" * 50)
    print("Batch Coordinate Converter")
    print("=" * 50)
    
    # Example: Create sample input file
    sample_coords = [
        [41.0082, 28.9784],  # Istanbul
        [39.9208, 32.8541],  # Ankara
        [38.4237, 27.1428],  # Izmir
    ]
    
    with open('sample_wgs84.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['latitude', 'longitude'])
        writer.writerows(sample_coords)
    
    # Convert
    batch_wgs84_to_itm('sample_wgs84.csv', 'output_itm.csv')
    
    print("\n✨ Batch conversion completed!")
