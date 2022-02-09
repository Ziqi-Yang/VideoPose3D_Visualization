#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(projection="3d")

a = np.random.randn(3,2,4)
print(a)
print(a[:,:,0])
