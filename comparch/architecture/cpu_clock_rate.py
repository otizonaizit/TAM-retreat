# CPU clock rate data from Wikipedia
# https://en.wikipedia.org/wiki/Microprocessor_chronology
# Table data extracted with: https://wikitable2csv.ggor.de/
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['font.family'] = ['Exo 2', 'sans-serif']

data = open('cpu_clock_rate.csv', 'rt')

# first, remove units and rescale everything to MHz
rescaled = []
for line in data:
    date, raw = line.split(',')
    try:
        value, unit = raw.split()
    except ValueError:
        # there are lines with multiple units, for example
        # 550 MHz-1.3 GHz
        # take the left most one
        raw = raw.split('-')[1]
        value, unit = raw.split()
    # if value is in the form X-Y, just use the biggest, i.e. Y
    if '-' in value:
        value = value.split('-')[1]
    value = float(value)
    # rescale value
    if unit == 'kHz':
        value = value/1000
    elif unit == 'GHz':
        value = value*1000
    elif unit == 'MHz':
        pass
    else:
        raise ValueError(f'Unit not understood! {unit}')
    rescaled.append((date, value))

dtype = [('year', np.float64), ('clock', np.float64)]
rescaled = np.array(rescaled, dtype=dtype)
# sort first by year and then by value
rescaled.sort(order=['year', 'clock'])

# add some jitter on values corresponding to the same year, so that the plot
# looks more understandable
old_year = rescaled[0][0]
count = 0
for row in range(rescaled.shape[0]):
    year = rescaled[row][0]
    count += 1
    if year != old_year:
        # add jitter to the values corresponding to the previous year
        prev_count = count-1
        if prev_count > 1:
            jitter = 1/prev_count
            for i in range(1, count):
                loc_year, loc_value = rescaled[row-count+i]
                rescaled[row-count+i] = (loc_year+(jitter*(i-1)), loc_value)
        # restart counting
        count = 1
        old_year = year

# plot the thing
plt.figure(figsize=(8.5,7.5))
plt.semilogy(rescaled['year'], rescaled['clock'], 'o')
# my laptop here
plt.semilogy([2020], [4900], 'o')
plt.grid(None)
plt.grid(which='both', axis='both')
plt.ylim(0.1, 10000)
plt.xlim(1968, 2025)
years = np.arange(1970, 2025, 5)
plt.xticks(years, years)
plt.yticks([0.1, 1,10,100,1000, 10000], ['1 kHz\n1 ms', '1 MHz\n1 µs', '10 MHz\n100 ns',
    '100 MHz\n10 ns', '1 GHz\n1 ns', '10 GHz\n0.1 ns'])
plt.tick_params(labelright=True, top=True, right=True)
plt.title('CPU clock rate')
plt.savefig('cpu_clock_rate.svg')




