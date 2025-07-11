# What every scientist should know about computer architecture

## Introduction
  - [Puzzle](puzzle.ipynb) – [Browser executable version](https://jupyterlite.mintgruen.tu-berlin.de/sites/mathesis-videospiel/2025-tam-retreat/)
  - Question: how come that swapping dimensions in a for-loop makes out for a huge slowdown?
  - Let students play around with the notebook and try to find the "bug"
  - A more thorough [benchmark](benchmark_python/)


## A digression in CPU architecture and the memory hierarchy

  - Go to [A Primer in CPU architecture](architecture/)
  - Measure size and timings for the memory hierarchy on my machine with a low level [C benchmark](benchmark_low_level/)

## Analog programming

  - [Two exercises to activate the body and the mind](analog_programming.md)


## Back to the Python benchmark (second try)

  - can we explain what is happening?
  - it must have to do with the good (or bad) use of cache properties
  - but how are numpy arrays laid out in memory?

## Anatomy of a numpy array

  - [memory layout of numpy arrays](numpy/)

## Back to the Python benchmark (third try)
  - can we explain what is happening now? Yes, more or less ;-)
  - quick fix for the [puzzle](puzzle.ipynb): try and add `order='F'` in the "bad" snippet and see that it "fixes" the bug ➔ why?
  - the default memeory layout is called "C-contiguous" or "row-major": 
      ```python
      np.zeros((2,2)).flags.c_contiguous == True
      np.zeros((2,2)).flags.f_contiguous == False
      ```
  - note that for one-dimensional arrays it makes no difference:
      ```python
      np.zeros(2).flags.c_contiguous == True
      np.zeros(2).flags.f_contiguous == True
      ```
  - rule of thumb for multi-dimensional numpy arrays:
    - the right-most index should be the inner-most loop in a series of nested loops over the dimensions of a multi-dimensional array
    - the previous rule can be remembered as *the right-most index changes the faster* in a series of nested loops
    - the logically contiguous data, for example the data points of a single time series, should be stored along the right-most dimension: 
        ```python
          x = np.zeros((n_series, lenght_of_one_series)) # ➔ good!
          y = np.zeros((length_of_one_series, n_series)) # ➔ bad!
        ```
    - … unless of course you plan to mostly loop *across* time series :)
    - watch out when migrating code from MATLAB® : it stores data in memory using the opposite convention, the column-major order!
    - **DANGER**: watch out when working with [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html):
        
        ➔ the data are stored in memory using different conventions depending on how the `DataFrame` was initialized! Be sure to
        check the `DataFrame.values.flags` attribute!

## A final exercise to put it all together
  - fork this repo to your account and clone your fork on the laptop
  - create a branch `ex` and switch to it
  - work on the [exercise](exercise.ipynb)– [Browser executable version](https://jupyterlite.mintgruen.tu-berlin.de/sites/mathesis-videospiel/2025-tam-retreat/)
  - push your solution to your fork and create a Pull Request to this repo


## Notes on the benchmarks

  - while running the benchmarks attached to one core on my laptop, the core was running under a constant load of 100% (almost completely user-time) and at a fixed frequency of 3.8 GHz, where the theoretical max would be 5.2 GHz
    
    ➔ the CPU does not "starve" because it scales its speed down to match the memory throughput? Or I am misinterpreting this? This problem which at first sight should be perfectly memory-bound, becomes CPU-bound, or actually, exactly balanced? From the [Intel documentation](https://lenovopress.lenovo.com/lp1836-tuning-uefi-settings-4th-gen-intel-xeon-scalable-processor):
    > **Energy Efficient Turbo**
    >
    > When `Energy Efficient Turbo` is enabled, the CPU’s optimal turbo
    > frequency will be tuned dynamically based on CPU utilization. The actual
    > turbo frequency the CPU is set to is proportionally adjusted based on the
    > duration of the turbo request. Memory usage of the OS is also monitored.
    > If the OS is using memory heavily and the CPU core performance is limited
    > by the available memory resources, the turbo frequency will be reduced
    > until more memory load dissipates, and more memory resources become
    > available. The power/performance bias setting also influences energy
    > efficient turbo. `Energy Efficient Turbo` is best used when attempting to
    > maximize power consumption over performance.

## Concluding remarks
  - how is all of this relevant for the users of a computing cluster?
  - Never trust benchmarks! See for example [Producing Wrong Data Without Doing Anything Obviously Wrong!](https://users.cs.northwestern.edu/~robby/courses/322-2013-spring/mytkowicz-wrong-data.pdf)

## Additional material if there's time left
- [Excerpts of parallel Python](parallel)
- how does memory *allocation* to processes work at the OS level?
  - virtual memory
  - swap
  - optimistic over-committing allocation policies
  - the oom-killer watchdog
