from enum import unique
import json
from os import listdir
from os.path import isfile, join

# loop file json dan simpan ke array
onlyfiles = [f for f in listdir('./data_details') if isfile(join('./data_details', f))]
json_files = []
for file in onlyfiles:
    with open(f'./data_details/{file}', errors="ignore") as fi:
        json_files.append(json.load(fi))

all_data = []
for data in json_files:
    all_data += data



for i,j in enumerate(all_data):
    if j['product_name'] == "" or j['spesifikasi'] == "" or j['deskripsi'] == "":
        del all_data[i]

with open('data_clean.json', 'a') as of:
    json.dump(all_data, of)