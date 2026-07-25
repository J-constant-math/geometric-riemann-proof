#!/usr/bin/env python3
"""
plot_validation.py
Generate the three-panel validation plot from CSV data.
Output: validation_plots.png
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_params = pd.read_csv('elliptic_params.csv')
df_spectrum = pd.read_csv('spectrum_M500.csv')
df_chi = pd.read_csv('chi_convergence.csv')

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Panel A
k = df_params['k']
error = df_params['error']
axes[0].scatter(k, error, s=20, color='black')
axes[0].set_yscale('log')
axes[0].set_xlabel('Zero index $k$')
axes[0].set_ylabel('$|\Delta_k - J_\infty|$')
axes[0].axhline(y=1e-14, color='gray', linestyle='--', label='$10^{-14}$')
axes[0].legend()
axes[0].set_title('(a) Wall-thickness constancy')

# Panel B
E_zero = df_spectrum['E/A_at_zero']
E_off = df_spectrum['E/A_at_offset']
axes[1].scatter(range(len(E_zero)), E_zero, s=15, color='red', alpha=0.7, label='$t=t_k$ (zero)')
axes[1].scatter(range(len(E_off)), E_off, s=15, color='blue', alpha=0.5, label='$t=t_k+0.5$ (off-zero)')
axes[1].axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
axes[1].axhline(y=-1, color='gray', linestyle='--', linewidth=0.8)
axes[1].set_xlabel('Zero index $k$')
axes[1].set_ylabel('$E_M(t)/A_M$')
axes[1].legend(loc='lower left')
axes[1].set_title('(b) Anti-resonance valley ($M=500$)')

# Panel C
sigma = df_chi['sigma']
mean_chi = df_chi['mean_chi_mod']
std_chi = df_chi['std_chi_mod']
axes[2].errorbar(sigma, mean_chi, yerr=std_chi, fmt='o-', color='black', capsize=3)
axes[2].axhline(y=1.0, color='gray', linestyle='--', linewidth=0.8)
axes[2].axvline(x=0.5, color='gray', linestyle='--', linewidth=0.8)
axes[2].set_xlabel('$\\sigma$')
axes[2].set_ylabel('$\\langle |\\chi(\\sigma+it)| \\rangle$')
axes[2].set_title('(c) $|\\chi|$ convergence')

plt.tight_layout()
plt.savefig('validation_plots.png', dpi=300, bbox_inches='tight')
print("Figure saved as validation_plots.png")
