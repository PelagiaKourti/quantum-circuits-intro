import sys
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt

from qiskit import QuantumCircuit

from qiskit.quantum_info import Pauli

from qiskit_aer.primitives import Estimator

import matplotlib.pyplot as plt


def get_qc_for_n_qubit_GHZ_state(n):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i,i+1)
    return qc

n = 10
qc = get_qc_for_n_qubit_GHZ_state(n)
qc.draw(output='mpl')
plt.show()

from qiskit.quantum_info import SparsePauliOp

operator_strings =['Z'+'I' * i + 'Z' +'I' * (n-2-i) for i in range(n-1)]
print(operator_strings)
print(len(operator_strings))


operators = [SparsePauliOp(operator_string) for operator_string in operator_strings]


#Optimize the problem for quantum execution

from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# from qiskit_ibm_runtime import QiskitRuntimeService
# backend_name = "ibm_brisbane"
# backend = QiskitRuntimeService().get_backend(backend_name)

from qiskit_ibm_runtime.fake_provider import FakeBrisbane
backend = FakeBrisbane()

pass_manager = generate_preset_pass_manager(optimization_level = 1, backend = backend)

qc_transpiled = pass_manager.run(qc)
operators_transpiled_list = [op.apply_layout(qc_transpiled.layout) for op in operators]


print("πριν: ", qc.count_ops(), "βάθος:", qc.depth())
print("μετά: ", qc_transpiled.count_ops(), "βάθος:", qc_transpiled.depth())



#Execute on the backend
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime.options import EstimatorOptions

options = EstimatorOptions()
options.resilience_level = 1
options.optimization_level = 0
options.dynamical_decoupling.sequence_type = "XY4"

estimator = Estimator(backend, options = options)

job = estimator.run([(qc_transpiled, operators_transpiled_list)])
job_id = job.job_id()
print(job_id)