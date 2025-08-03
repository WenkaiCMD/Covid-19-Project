import os

file_path = "owid-covid-malaysia.csv"

if os.path.exists(file_path):
    print("✅ File found!")
else:
    print("❌ File NOT found. Please check the name and location again.")
