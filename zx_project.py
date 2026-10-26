from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
import numpy as np

qc = QuantumCircuit(1)

alpha = np.pi / 2

qc.rz(alpha, 0)
qc.h(0)

# Simulation
backend = Aer.get_backend('statevector_simulator')
compiled = transpile(qc, backend)
result = backend.run(compiled).result()

state = result.get_statevector()

print("Final statevector:")
print(state)