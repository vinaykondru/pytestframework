import csv

def read_csv(file_path):
    with open(file_path) as f:
        return list(csv.DictReader(f))
