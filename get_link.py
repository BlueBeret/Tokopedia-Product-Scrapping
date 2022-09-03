done = []
not_done = []
out = []

with open('done.txt', 'r') as fi:
    links = fi.read()
    done = links.splitlines()

with open('out.txt', 'r') as fi:
    links = fi.read()
    out = links.splitlines()


with open('not_done.txt', 'w') as fo:
    for i in out:
        if i not in done:
            fo.write(i+ "\n")