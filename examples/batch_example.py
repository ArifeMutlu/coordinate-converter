"""
Batch conversion example with CSV files
"""

from batch_converter import batch_wgs84_to_itm
import csv

# Create sample input file
print("Creating sample CSV file...")
sample_data = [
    ["latitude", "longitude", "name"],
    [41.0082, 28.9784, "Istanbul"],
    [39.9208, 32.8541, "Ankara"],
    [38.4237, 27.1428, "Izmir"],
    [36.8969, 30.7133, "Antalya"],
    [37.8667, 32.4833, "Konya"],
]

with open('examples/sample_cities.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(sample_data)

print("✅ Sample file created: examples/sample_cities.csv")

# Convert batch
print("\nConverting batch...")
batch_wgs84_to_itm(
    'examples/sample_cities.csv',
    'examples/sample_cities_itm.csv'
)

print("\n✅ Batch conversion completed!")
print("Output saved to: examples/sample_cities_itm.csv")
