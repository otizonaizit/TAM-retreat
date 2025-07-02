#!/usr/bin/python3
import os
import sys

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['font.family'] = ['Exo 2', 'sans-serif']

from bench import NSERIES

def get_xlabels(x):
    xlabels = []
    for value in x:
        b = int(2**value)
        if b < 1024:
            xlabels.append(f'{b}B')
        elif b < 1048576:
            xlabels.append(f'{b//1024}K')
        elif b < 1073741824:
            xlabels.append(f'{b//1024//1024}M')
        else:
            xlabels.append(f'{b//1024//1024//1024}G')
    return xlabels

def get_ylabels(y):
    ylabels = []
    for power in y:
        power = int(np.log10(power))
        if power < -6:
            value = 10**(power+9)
            ylabels.append(f'{value}ns')
        elif power < -3:
            value = 10**(power+6)
            ylabels.append(f'{value}μs')
        elif power < 0:
            value = 10**(power+3)
            ylabels.append(f'{value}ms')
        else:
            value = 10**power
            ylabels.append(f'{value}s')
    return ylabels

prefix = 'results_ns'
maxy = 1e1
miny = 1e-6
for results in (f for f in os.listdir('.') if f.startswith(prefix)):
    num_series = results.removeprefix(prefix)

    sizes, bads, goods = [], [], []
    with open(results, 'r') as fh:
        for line in fh:
            size, good, bad = line.split()
            bads.append(float(bad))
            goods.append(float(good))
            sizes.append(int(size))
    goods = np.array(goods)
    bads = np.array(bads)
    x = np.log2(sizes)
    y1 = goods
    y2 = bads
    # generate two plots: good+bad timings and slowdown plot
    plt.figure(figsize=(8.5, 7.5))
    p1, = plt.semilogy(x, y1, 'o')
    p2, = plt.semilogy(x, y2, 'o')
    plt.xlabel('size of one time series')
    plt.ylabel('loading time')
    plt.grid(None)
    plt.grid(which='both', axis='both')
    plt.xticks(x, get_xlabels(x), rotation=60)
    plt.ylim(miny, maxy)
    yticks = np.logspace(int(np.log10(miny)),
                         int(np.log10(maxy)),
                         num=int(np.log10(maxy/miny))+1)
    plt.yticks(yticks, get_ylabels(yticks))
    plt.tick_params(axis='y', labelright=True, right=True)
    lgd = plt.legend((p1, p2), ('good', 'bad'), frameon=True)
    lgd.get_frame().set_edgecolor('black')
    plt.title(f'Timings\n{num_series} time series')
    plt.savefig(f'loading-timings-ns{num_series}.svg')

    # slowdown plot
    plt.figure(figsize=(8.5, 7.5))
    p1, = plt.plot(x, bads/goods, 'og', label=r'$\frac{\mathrm{time\_bad}}{\mathrm{time\_good}}$')
    plt.xlabel('size of one time series')
    plt.ylabel('slowdown')
    plt.grid(None)
    plt.grid(which='both', axis='both')
    plt.xticks(x, get_xlabels(x), rotation=60)
    plt.tick_params(axis='y', which='both', reset=True, labelright=True, right=True)
    lmaxy = (bads/goods).max()
    yticks = range(0, int(np.ceil(lmaxy))+1)
    yticks_labels = []
    for i in yticks:
        if not i%5:
            yticks_labels.append(str(i))
        else:
            yticks_labels.append('')
    plt.yticks(yticks, yticks_labels)
    #plt.legend((p1,), ('time_bad/time_good',))
    lgd = plt.legend(frameon=True, fontsize=16)
    lgd.get_frame().set_edgecolor('black')
    plt.title(f'Slowdown\n{num_series} time series')
    plt.savefig(f'loading-slowdown-ns{num_series}.svg')
