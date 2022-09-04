import json

out = 'tokopedia/links.json'
not_done_fn = 'tokopedia/not_done_tokopedia.txt'
done_fn = 'tokopedia/not_done_tokopedia.txt'

with open(out, 'r') as fi:
    links = json.load(fi)
