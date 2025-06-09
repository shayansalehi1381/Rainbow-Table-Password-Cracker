import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    name_pass = OrderedDict()
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name_pass[row[0]] = hashToPass(row[1])

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, value in name_pass.items():
            writer.writerow([key, value])

def hashToPass(HASH):
    pass_hash_dict = OrderedDict()
    for i in range(10000):
        formatted_number = str(i).zfill(4)  # 7 --> 0007, 123 --> 0123
        hashed = hashlib.sha256(formatted_number.encode()).hexdigest()
        pass_hash_dict[hashed] = formatted_number
        if HASH == hashed:
            return formatted_number

