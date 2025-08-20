#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 11:18:43 2025

@author: perkins
"""

import matplotlib.pyplot as plt
import numpy as np

# Parameters 
theta = 1
beta = 1

# Generate y (investment) values
y = np.linspace(0, 6.5, 400)
x = (1/beta) * np.log(y/theta + 1)

# Scale so that the max is 60% reduction
x_pct = 60 * x / np.max(x)

# Reference points
y1, y2 = 0.6487, 2.317
x1 = (1/beta) * np.log(y1/theta + 1)
x2 = (1/beta) * np.log(y2/theta + 1)
x1_pct, x2_pct = 60 * x1 / np.max(x), 60 * x2 / np.max(x)

# Plot
plt.figure(figsize=(8,6))
plt.plot(y, x_pct, 'k-', label=r'$x = \frac{1}{\beta}\ln\left(\frac{y}{\theta}+1\right)$')
plt.scatter([y1, y2], [x1_pct, x2_pct], color='red', zorder=5)

# Annotate the points
plt.text(y1, x1_pct-1.5, r'$(y_1,x_1)$')
plt.text(y2, x2_pct+1, r'$(y_2,x_2)$')

# Add dashed guide lines
plt.plot([y1, y1], [x1_pct, x2_pct], 'k--', alpha=0.6)
plt.plot([y1, y2], [x2_pct, x2_pct], 'k--', alpha=0.6)

# Δx and Δy labels
plt.annotate(r'$\Delta x$', xy=((y1+y2)/2, x2_pct+1), ha='center')
plt.annotate(r'$\Delta y$', xy=(y1-0.2, (x1_pct+x2_pct)/2), va='center', rotation=90)

# Add horizontal line at 60%
plt.axhline(60, color='blue', linestyle='--', alpha=0.8)
plt.text(y[-1]+0.1, 60, "60% reduction", va='center', color='blue')

# Labels and title
plt.title("Inverse Exponential Investment Function")
plt.xlabel("y (total investment)")
plt.ylabel("x (reduction in fuel use, %)")
plt.legend()
plt.ylim(0, 60)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
