import sys
sys.stdout.reconfigure(encoding='utf-8')


from qiskit import QuantumCircuit
    
qc = QuantumCircuit(2,2) #Make cirquit with 2 qubits and 2 classical bits. they all begin in |0>


qc.h(0) #hadamard on qubit 0. So |0> goes to (|0> + |1>)/sqrt2
#so right now if i measure, it is 50% and 50% to be 0 or 1

qc.cx(0,1) #cnot with control the qubit 0 and target the qubit 1. If control is |1> it flips the target.
#since qubit 0 is in entanglement now, cnot doesnt choose. 
#the system becomes (|00>+|11>)/sqrt2 

qc.measure_all()

print(qc.draw())


from qiskit_aer import AerSimulator

sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
#runs the cirquit 1024 times. every time from the beginning, zero qubits, gates, measurement


print(result.get_counts())