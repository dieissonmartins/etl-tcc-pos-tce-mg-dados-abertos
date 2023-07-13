import csv
import os

local_path = os.path.dirname(os.path.realpath(__file__))

filepath = os.path.join(local_path, 'tmp/2022/3107406/orgao/2022.3107406.orgao.orgao.csv')

with open(filepath, mode='r') as csv_file:
    reader = csv.DictReader(csv_file)

    row = next(reader)
    print(row)
