import csv


file_path: str = "exemplo.csv"

file_csv: list = []

with open(file=file_path, mode="r", encoding="utf-8") as myfile:
    csv_reader = csv.DictReader(myfile)

    for line in csv_reader:
        file_csv.append(line)

print(file_csv)