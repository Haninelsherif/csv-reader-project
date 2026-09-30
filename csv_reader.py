import csv

file_path = input("Enter the path of your CSV file: ")

try:
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            if i >= 3:
                break
            print(row)

except FileNotFoundError:
    print("Error: File not found.")