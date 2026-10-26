# Qiskit Explorations

First steps in Qiskit, working towards circuit optimisation and
equivalence checking.

---

## Contents

### Circuit equivalence and ZX rules

Numerical verification of ZX-calculus rewrite rules using `Operator.equiv`:

- **Spider fusion (S1)** — `Rz(π/4)·Rz(π/4) = Rz(π/2)`
- **Colour change (C)** — `H·Z·H = X`, and more generally
  `H·Rz(θ)·H = Rx(θ)`, tested over randomly sampled θ
- A longer alternating `H / Rz` sequence reduced to a shorter
  `Rx / Rz / Rx` form

This connects to the fourth chapter of my MSc thesis,
where these rules are derived
from the axioms of Hopf algebraic structures.

### States and operators

Statevectors, unitary operators and density matrices for single-qubit
circuits; Bloch sphere visualisation.

### Entanglement

Bell state preparation (`H` followed by `CNOT`) and measurement
statistics over 1024 shots — showing the `00`/`11` correlation.
Expectation values of the two-qubit Pauli observables
`ZZ, ZI, IZ, XX, XI, IX` for a circuit built from `H`, `CNOT`, `X`, `Y`.

### Transpilation

An *n*-qubit GHZ state transpiled for a simulated IBM backend
(`FakeBrisbane`), comparing gate counts and circuit depth before and
after. Illustrates how the abstract circuit is rewritten into the
device's native gate set and connectivity.

---

## Requirements

```
qiskit
qiskit-aer
qiskit-ibm-runtime
matplotlib
numpy
```
