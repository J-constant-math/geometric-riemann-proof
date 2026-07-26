# Anti-Resonance Geometry of Prime Ellipses and Riemann Zeros

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21577375.svg)](https://doi.org/10.5281/zenodo.21577375)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the complete LaTeX source, numerical validation datasets, and reproducible Python scripts for the paper:

**"The Anti-Resonance Geometry of Prime Ellipses and Riemann Zeros: A Dual Lock on the Critical Line via Spectral Interference and Constant Wall-Thickness"**

Author: Peiying Jie

---

## 📄 Paper Abstract

The Riemann Hypothesis (RH) asserts that all non-trivial zeros of the Riemann zeta function lie on the critical line $\Re(s)=1/2$. This work establishes a bidirectional geometric mapping system between prime-number-generated ellipses (forward arithmetic construction) and zero-generated ellipses (backward spectral detection).

We define prime ellipses with fixed minor axis $b=1/2$ and scaled major axis $a_p=p/2$, and Riemann zero ellipses with calibrated geometric parameters:
$$
a_k = \frac{t_k}{2\pi}, \qquad b_k = \frac{t_k - \gamma}{2\pi}
$$

**Core findings:**
- Spectral superposition of prime elliptic eccentricity waves produces sharp **anti-resonance dips** exactly at zero imaginary parts $t_k$.
- The stable existence of these anti-resonance valleys is uniquely equivalent to the **constant wall-thickness condition**:
  $$
  J_\infty = a_k - b_k = \frac{\gamma}{2\pi}
  $$
- Functional equation asymptotic analysis proves that only $\sigma=1/2$ eliminates all logarithmic frequency distortion, achieving full structural stability.

**Numerical validation:** High-precision verification confirms machine-precision constant wall-thickness (max error $<5.05\times10^{-15}$). The anti-resonance signal-to-noise ratio increases from $12.2\times$ to $14.3\times$ with expanding prime sampling.

**Conclusion:** The Riemann critical line constraint is geometrically reduced to a universal constant-thickness boundary condition, forming a rigorous dual geometric-spectral framework for the Riemann Hypothesis.

---

## 📁 Repository Structure

```

geometric-riemann-proof/
├── AntiResonance_Riemann_Proof_Jie_2026.tex   # LaTeX source (final paper)
├── AntiResonance_Riemann_Proof_Jie_2026.pdf   # Compiled PDF (final paper)
├── README.md                                   # This file
├── figures/
│   └── validation_plots.png                    # Figure 1: 3-panel validation plot
├── data/
│   ├── elliptic_params.csv                     # Table 2: wall-thickness data
│   ├── spectrum_data.csv                       # Table 3: anti-resonance statistics
│   └── chi_convergence.csv                     # Table 4: |χ| convergence data
└── scripts/
├── generate_spectrum.py                    # Generate all CSV data
├── plot_validation.py                      # Generate validation_plots.png
└── requirements.txt                        # Python dependencies

```

---

## 🚀 Reproducibility

### Prerequisites

- Python 3.9+
- LaTeX distribution (TeX Live / MikTeX / Overleaf)

### Python Dependencies

Install required packages:

```bash
pip install -r scripts/requirements.txt
```

Generate Numerical Data

From the repository root:

```bash
cd scripts
python generate_spectrum.py
```

This will generate:

· elliptic_params.csv
· spectrum_M101.csv, spectrum_M200.csv, spectrum_M500.csv
· chi_convergence.csv

Generate Validation Figure

```bash
python plot_validation.py
```

This produces validation_plots.png (Figure 1 in the paper).

Compile the Paper

```bash
pdflatex AntiResonance_Riemann_Proof_Jie_2026.tex
pdflatex AntiResonance_Riemann_Proof_Jie_2026.tex
```

Or use Overleaf with the provided .tex file.

---

🔗 Links

· Paper PDF: AntiResonance_Riemann_Proof_Jie_2026.pdf
· Zenodo DOI: 10.5281/zenodo.20840482
· Related Repository: J-constant-math/-J-constant-Riemann- (historical derivations)

---

📝 Citation

If you use this work or the code in your research, please cite:

```bibtex
@article{Jie2026AntiResonance,
  author    = {Peiying Jie},
  title     = {The Anti-Resonance Geometry of Prime Ellipses and Riemann Zeros: A Dual Lock on the Critical Line via Spectral Interference and Constant Wall-Thickness},
  year      = {2026},
  doi       = {10.5281/zenodo.21577375},
  url       = {https://github.com/J-constant-math/geometric-riemann-proof}
}
```

---

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

---

⚠️ Notes

· The Euler–Mascheroni constant $\gamma$ in this work is derived from the Riemann–von Mangoldt zero counting formula (Appendix A of the paper), not from Stirling asymptotic expansion of the gamma function.
· All numerical computations use mpmath with 50-digit precision for zero extraction.
· The two GitHub repositories serve complementary purposes:
  · This repository (geometric-riemann-proof) contains the final paper and numerical validation.
  · The sister repository (-J-constant-Riemann-) contains historical derivations and early exploration notes.

```

---
