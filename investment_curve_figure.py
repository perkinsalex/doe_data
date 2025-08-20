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
y_max = 6.5   # max investment value on x-axis
cap = 60      # asymptote for reduction (%)

# Generate y (investment) values
y = np.linspace(0, y_max, 400)

# Rescaled log function: tops out at 60
x_pct = cap * np.log(y/theta + 1) / np.log(y_max/theta + 1)

# Reference points
y1, y2 = 0.6487, 2.317
x1_pct = cap * np.log(y1/theta + 1) / np.log(y_max/theta + 1)
x2_pct = cap * np.log(y2/theta + 1) / np.log(y_max/theta + 1)

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
plt.axhline(cap, color='blue', linestyle='--', alpha=0.8)

# Place the label inside the plot area, near the right edge
plt.text(y[-1]*0.85, cap+1, "60% reduction", va='bottom', ha='left',
         color='blue', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))


# Labels and title
plt.title("Inverse Exponential Investment Function")
plt.xlabel("y (total investment)")
plt.ylabel("x (reduction in fuel use, %)")
plt.legend()

# Extend y-axis slightly above 60 to show it's a cap
plt.ylim(0, 70)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
