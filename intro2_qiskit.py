import sys
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
    
qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0,1)

qc.cx(1,0)

qc.x(0)
qc.cx(1,0)
qc.y(1)

#qc.draw(output='mpl')
#plt.show()


from qiskit.quantum_info import Pauli

ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')

observables = [ZZ, ZI, IZ, XX, XI, IX]

from qiskit_aer.primitives import Estimator

estimator = Estimator()

job = estimator.run([qc] * len(observables), observables)


import matplotlib.pyplot as plt

data = ['ZZ', 'ZI', 'IZ','XX','XI','IX']
values = job.result().values
print(values)


#plt.plot(data, values, '-o')
#plt.xlabel('Observables')
#plt.ylabel('Expectation value')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
qc.draw(output='mpl', ax=ax1)
ax2.plot(data, values, '-o')
plt.show()