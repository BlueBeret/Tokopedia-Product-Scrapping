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

clean_data = []

done_links = open('done.txt','w')

for i,j in enumerate(all_data):
    if j['product_name'] == "" or j['spesifikasi'] == "" or j['deskripsi'] == "" or j['product_name'] == "null" or j['spesifikasi'] == "null" or j['deskripsi'] == "null":
        continue
    done_links.write(j['Page_URL'] + '\n')
    clean_data.append(j)


print(len(clean_data))
with open('data_clean.json', 'w') as of:
    json.dump(clean_data, of)