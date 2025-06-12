#!/usr/bin/python3
# Commands and ideas from: https://llvm.org/docs/Benchmarking.html
# we assume that CPU 0 and 1 are together in an intel SMT-pair (hyperthreading)
# - Disable address space randomization:
#     echo 0 > /proc/sys/kernel/randomize_va_space
# - Set scaling governor to performance for CPU 0
#     echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
# - Reserve CPU 0 fro our benchmark
#     cset shield --cpu 0 --kthread=on
# - Disable the SMT-peer of CPU 0, i.e. CPU 1
#     echo 0 > /sys/devices/system/cpu/cpu1/online
# - Disable turbo mode (works only on Intel):
#     echo 1 > /sys/devices/system/cpu/intel_pstate/no_turbo
# - Run with
#    cset shield --exec -- ./bench.py
#

# To use the full power of the CPU, skip all the other steps and
# just run with
#    taskset --cpu-list 0 ./bench.py
import os
import sys
import timeit

import numpy as np

NSERIES = (128, )
POWS = 2**np.arange(2, 23, dtype=int)

# Size of one dimensional numpy arrays of dtype 'float64':
# A fix overhead of 96 bytes plus a variable size:
# (n_items x 8 bytes)

def load_data_row(x, time_series):
    """Store one time series per raw"""
    for row, ts in enumerate(time_series):
        x[row,:] = ts
    return x

def load_data_column(x, time_series):
    """Store one time series per column"""
    for column, ts in enumerate(time_series):
        x[:, column] = ts
    return x

if __name__ == '__main__':
    for nseries in NSERIES:
        print(30*'=', '\n', nseries)
        float_items = POWS
        byte_sizes = (float_items*8) #+ 96
        bads = []
        goods = []
        results = open(f'results_ns{nseries}', 'wt')
        for i, len_one_series in enumerate(float_items):
            time_series = np.zeros((nseries, len_one_series), dtype='float64')
            x = np.empty((nseries, len_one_series), dtype='float64')
            print('Timing good...')
            good = min(timeit.repeat(lambda: load_data_row(x, time_series), number=5))/5
            x = np.empty((len_one_series, nseries), dtype='float64')
            print('Timing bad...')
            bad = min(timeit.repeat(lambda: load_data_column(x, time_series), number=5))/5
            print(f'{len_one_series}/{POWS[-1]} {good} {bad}')
            bads.append(bad)
            goods.append(good)
            results.write(f'{byte_sizes[i]} {good} {bad}\n')
            results.flush()
        results.close()

