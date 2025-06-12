import os
import sys

# prefix is something like results_
results = sys.argv[1]
name = results.removeprefix('results_')
types = {}
results = open(results, 'rt')


for idx, line in enumerate(results):
    if line.startswith('Memory read bandwidth'):
        types['bwr'] = idx
    elif line.startswith('Memory write bandwidth'):
        types['bww'] = idx
    elif line.startswith('Memory load latency'):
        types['lseq'] = idx
    elif line.startswith('Random load latency'):
        types['lrnd'] = idx
    else:
        pass

for typ, idx in types.items():
    csv = open(f'{name}-{typ}.csv', 'wt')
    results.seek(0)
    for count, line in enumerate(results):
        if count <= idx:
            continue
        if line.startswith('"'):
            continue
        try:
            val1, val2 = line.split(" ")
        except ValueError:
            # we are at the end of the section
            csv.close()
            break
        csv.write(f'{val1},{val2}')


