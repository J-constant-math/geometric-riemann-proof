# A Geometric Proof of the Riemann Hypothesis

**Constant Wall Thickness and Concentricity at Re(s) = 1/2**

This repository contains the complete source code, numerical data, and LaTeX source for the paper:

> Jie, P. (2026). *A Geometric Proof of the Riemann Hypothesis: Constant Wall Thickness and Concentricity at Re(s) = 1/2*.

## Core Axioms

1. **Global Concentricity Axiom**: All geometric objects (circles from harmonic numbers, logarithms, trivial zeros, ellipses from non-trivial zeros) share the common center \( C(1/2, 0) \).
2. **Constant Wall Thickness Axiom**: For every non-trivial zero ellipse, \( a_k - b_k = J_\infty = \gamma/(2\pi) \).

## Key Results

- Elliptic parameters uniquely determined: \( a_k = t_k/(2\pi), \; b_k = (t_k - \gamma)/(2\pi) \)
- Closed-form eccentricity: \( e_k^2 = (2\gamma t_k - \gamma^2)/t_k^2 \)
- Perimeter identity: \( \pi(a_k + b_k) + \gamma/2 = t_k \)
- **Geometric Riemann Theorem**: Under the two axioms, \( \sigma_k \equiv 1/2 \) for all non-trivial zeros.

## Repository Structure
.
├── Jie_Geometric_Riemann_Proof.pdf # Full paper
├── Jie_Geometric_Riemann_Proof.tex # LaTeX source
├── fig1_numerical_validation.jpg # Four-panel validation
├── fig2_concentric_system.jpg # Concentric circle-ellipse system
├── fig3_residual_convergence.jpg # Residual plot
├── fig4_deepseek_tikz_replica_v2.jpg # TikZ schematic
├── table1_latex.tex # LaTeX table code
├── table1_zero_ellipse_data.csv # Full numerical data (first 20 zeros)
└── README.md


## Numerical Validation

The first 20 non-trivial zeros were tested. The constant wall thickness holds to machine precision (\( \sim 10^{-15} \)), and the perimeter identity error is below \( 10^{-5}\% \).

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

## Citation

```bibtex
@article{Jie2026GeometricProof,
  title  = {A Geometric Proof of the Riemann Hypothesis: Constant Wall Thickness and Concentricity at Re(s) = 1/2},
  author = {Jie, Peiying},
  year   = {2026},
  url    = {https://github.com/J-constant-math/geometric-riemann-proof}
}

Acknowledgements
The author thanks the open-source mathematical community (LMFDB, Odlyzko) for high-precision zero data, and the AI assistants DeepSeek, Kimi, and Doubao for collaborative theoretical derivation, numerical validation, and logical review.
