# RAM clock rate and transfer rate data from Wikipedia
# https://en.wikipedia.org/wiki/DDR_SDRAM
# Table data extracted with: https://wikitable2csv.ggor.de/
import numpy as np
import pandas
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['font.family'] = ['Exo 2', 'sans-serif']


data = pandas.read_csv('memory.csv')
#data = data.sort_values('Memory clock (MHz)')
_types = list(data['Type'])
_transfers = list(data['Data rate (MT/s)'])
_cycle_times = list(data['Cycle time (ns)'])
_latencies = list(data['Eighth word (ns)'])

# remove redundant data
types = []
transfers = []
cycle_times = []
latencies = []
for idx, typ in enumerate(_types):
    # just select the first occurence of this type
    if typ in types:
        continue
    # filter DDR4 inferior to DDR4-3333
    prefix = 'DDR4-'
    if typ.startswith(prefix) and int(typ.removeprefix(prefix)) < 3333:
        continue
    types.append(typ)
    transfers.append(_transfers[idx])
    cycle_times.append(_cycle_times[idx])
    latencies.append(_latencies[idx])

# transform transfers from MT/s to GB/s
transfers = np.array(transfers, dtype='float64')*8/1024
plt.figure(figsize=(8.5,7.5))
plt.title('Memory Bandwidth [GB/s] (1995-2023)')
# my laptop first
me = types.index('DDR5-5200')
plt.plot(range(len(types)), transfers, 'o')
plt.plot(me, transfers[me], 'o')
plt.xticks(range(len(types))[::3], types[::3], rotation=30, ha='right')
yticks = range(0,56)
ylabels = []
for t in yticks:
    if not t%5:
        ylabels.append(str(t))
    else:
        ylabels.append('')
plt.yticks(yticks, ylabels)
plt.ylabel('GB/s')
plt.tick_params(axis='y', which='both', reset=True, labelright=True, right=True)
plt.savefig('memory_bandwidth.svg')

plt.figure(figsize=(8.5,7.5))
plt.title('Memory Cycle Time [ns] (1995-2023)')
# my laptop first
me = types.index('DDR5-5200')
plt.semilogy(range(len(types)), cycle_times, 'o')
plt.semilogy(me, cycle_times[me], 'o')
plt.xticks(range(len(types))[::3], types[::3], rotation=30, ha='right')
plt.ylim(0.1, 11)
line = np.arange(0,10).astype('float64')
yticks = list(line[1:]*0.1)+list(line[1:])+list(line[1:2]*10)
ylabels = []
for value in yticks:
    if value in (0.1, 0.5, 1., 1.5, 5., 10.):
        ylabels.append(f'{value} ns')
    else:
        ylabels.append('')
plt.yticks(yticks, ylabels)
plt.tick_params(axis='y', which='both', reset=True, labelright=True, right=True)
plt.savefig('memory_clock.svg')

# transform transfers from MT/s to GB/s
plt.figure(figsize=(8.5,7.5))
plt.title('Memory Latency [ns] (1998-2023)')
# my laptop first
me = types.index('DDR5-5200')
mel = latencies[me]
y = latencies[2:]
x = types[2:]
plt.plot(range(len(x)), y, 'o')
plt.plot(me, mel, 'o')
plt.xticks(range(len(x))[::3], x[::3], rotation=30, ha='right')
plt.ylim(8,40)
yticks = range(8,41)
ylabels = []
for t in yticks:
    if not t%5:
        ylabels.append(str(t)+' ns')
    else:
        ylabels.append('')
plt.yticks(yticks, ylabels)
plt.tick_params(axis='y', which='both', reset=True, labelright=True, right=True)
plt.savefig('memory_latency.svg')

