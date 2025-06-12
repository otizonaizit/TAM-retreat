# The dangers and joys of automatic parallelization (like in numpy linear algebra routines) and the use of clusters/schedulers (but also on your laptop)
- Go through the [notebook](parallel.ipynb) to play around with numpy auto-parallelization, CPU affinity and OpenMP thread pool control

- Now we want to submit our code to a cluster, or even just running it in parallel on our own laptop:
  - run [`overcommit.py`](overcommit.py) while monitoring with htop
  - try the [`submit.sh`](submit.sh) script
  - see problems with overcomitting
  - explain the PSI (Pressure Stalled Information) fields in `htop`. Useful readings:
    - https://docs.kernel.org/accounting/psi.html
    - https://facebookmicrosites.github.io/psi/docs/overview
- Discuss implications for local and cluster workflows

# Hands on
- Let's try to make it more quantitative:
  - Write a benchmark in the style of [benchmark_python](../benchmark_python/bench.py)
  - We want to assess the performance of matrix multiplication as a function of:
    - the size of the matrix `N`
    - the number of openMP threads `T`, controlled with `threadpoolctl` or by environment variable `OMP_NUM_THREADS`
    - the number of processes `P`, controlled by the [`submit.sh`](submit.sh) script or something similar
- The results will of course depend on the particular architecture of the machine on which you are running
- Submit your benchmark, together with some plotting routines, as a PR to this repo!



