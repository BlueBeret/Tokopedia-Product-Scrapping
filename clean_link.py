from enum import unique
import json
from os import listdir
from os.path import isfile, join

# loop file json dan simpan ke array
onlyfiles = [f for f in listdir('./raw_data') if isfile(join('./raw_data', f))]
json_files = []
for file in onlyfiles:
    with open(f'./raw_data/{file}') as fi:
        json_files.append(json.load(fi))

all_data = []
for data in json_files:
    all_data += data


# simpan hanya link yang distinct
unique_links = []
with open('./out.txt', 'r') as fi:
    for link in fi.readlines():
        unique_links.append(link.strip())
for x in all_data:
    i = x['Title_URL'].split('?sp_atk')[0]
    if i not in unique_links:
        unique_links.append(i.strip())


# simpan hasilnya di out.txt
print(len(unique_links))
with open('out.txt', 'w') as of:
    counter = 0
    for link in unique_links:
        counter +=1 
        of.write(link+'\n')
        
