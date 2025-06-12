import sys
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
x = np.zeros((N, N), dtype="float64")

y = x @ x
