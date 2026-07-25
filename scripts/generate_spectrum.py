#!/usr/bin/env python3
"""
generate_spectrum.py
Generate prime-elliptic spectrum data for anti-resonance verification.
Outputs: elliptic_params.csv, spectrum_M*.csv, chi_convergence.csv
"""

import mpmath as mp
import numpy as np
import csv

mp.dps = 50

GAMMA = mp.euler

def prime_sieve(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = False
    return [i for i in range(n+1) if sieve[i]]

def eccentricity(p):
    return np.sqrt(1 - 1.0 / (p*p))

def main():
    zeros = [mp.zetazero(k+1) for k in range(100)]
    t_vals = [float(z.imag) for z in zeros]

    primes = prime_sieve(4000)
    primes_101 = primes[:101]
    primes_200 = primes[:200]
    primes_500 = primes[:500]

    # elliptic_params.csv
    with open('elliptic_params.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k', 't_k', 'a_k', 'b_k', 'Delta_k', 'error'])
        for idx, t in enumerate(t_vals[:20], 1):
            a = t / (2*np.pi)
            b = (t - float(GAMMA)) / (2*np.pi)
            delta = a - b
            error = abs(delta - float(GAMMA)/(2*np.pi))
            writer.writerow([idx, t, a, b, delta, error])

    # spectrum_M*.csv
    for M, plist in [(101, primes_101), (200, primes_200), (500, primes_500)]:
        e_vals = [eccentricity(p) for p in plist]
        A = np.sqrt(sum((e*e / p) for e, p in zip(e_vals, plist)))
        filename = f'spectrum_M{M}.csv'
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['t_k', 'E(t_k)', 'E(t_k+0.5)', 'E/A_at_zero', 'E/A_at_offset'])
            for t in t_vals:
                E_zero = sum(e/np.sqrt(p) * np.cos(t * np.log(p)) for e, p in zip(e_vals, plist))
                E_off = sum(e/np.sqrt(p) * np.cos((t+0.5) * np.log(p)) for e, p in zip(e_vals, plist))
                writer.writerow([t, E_zero, E_off, E_zero/A, E_off/A])

    # chi_convergence.csv
    sigmas = np.arange(0.40, 0.61, 0.01)
    with open('chi_convergence.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sigma', 'mean_chi_mod', 'std_chi_mod'])
        for sigma in sigmas:
            mods = []
            for t in t_vals:
                s = complex(sigma, t)
                chi = mp.power(2, s) * mp.power(mp.pi, s-1) * mp.sin(mp.pi * s / 2) * mp.gamma(1 - s)
                mods.append(float(abs(chi)))
            writer.writerow([sigma, np.mean(mods), np.std(mods)])

    print("All CSV files generated successfully.")

if __name__ == "__main__":
    main()
