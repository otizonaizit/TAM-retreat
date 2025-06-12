# Storage interfaces rates from
# https://en.wikipedia.org/wiki/List_of_interface_bit_rates#Storage
# Table data extracted with: https://wikitable2csv.ggor.de/
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['font.family'] = ['Exo 2', 'sans-serif']

data = open('storage.csv', 'rt')
# remove units and rescale everything to MB/s
b_to_mb = 1/(1024*1024)
kb_to_mb = 1/1024
gb_to_mb = 1024
rescaled = []
for line in data:
    typ, rate, year = line.split(',')
    value, unit = rate.split()
    value = float(value)
    if unit == 'B/s':
        value = value*b_to_mb
    elif unit == 'KB/s':
        value = value*kb_to_mb
    elif unit == 'MB/s':
        pass
    elif unit == 'GB/s':
        value = value*gb_to_mb
    else:
        raise ValueError(f'Unit not understood! {unit}')
    rescaled.append((int(year), value))

dtype = [('year', np.float64), ('speed', np.float64)]
rescaled = np.array(rescaled, dtype=dtype)
# sort first by year and then by value
rescaled.sort(order=['year', 'speed'])

# plot the thing
plt.figure(figsize=(8.5,7.5))
plt.semilogy(rescaled['year'], rescaled['speed'], 'o')
# my laptop here
plt.semilogy([2023], [6585], 'o')
plt.grid(None)
plt.grid(which='both', axis='y')
plt.grid(which='both', axis='x')
plt.ylim(b_to_mb, 100*gb_to_mb)
plt.xlim(1960, 2025)
years = range(1960,2026,5)
plt.xticks(years, years, rotation=45, ha='center')
plt.yticks([b_to_mb, kb_to_mb, 1, 10, 100,  gb_to_mb, 10*gb_to_mb, 100*gb_to_mb],
           ['1 B/s', '1 KB/s', '1 MB/s', '10 MB/s', '100 MB/s', '1 GB/s', '10 GB/s', '100 GB/s'])
plt.tick_params(labeltop=False, labelright=True, top=True, right=True)
plt.title('Storage (read) speed')
plt.savefig('storage.svg')
