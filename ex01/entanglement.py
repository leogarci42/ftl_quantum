from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator, noise
from qiskit.visualization import plot_histogram
import matplotlib as mplt
import matplotlib.pyplot as plt
import numpy as np
mplt.use('qtagg')

q = QuantumCircuit(2, 0) #defines a circuit of 1 qubit, 0 classic bit
q.h(0)
q.cx(0,1)
q.measure_all()
sim = AerSimulator()
result = sim.run(q, shots=500).result()
counts = result.get_counts()
probabilities = {state: count / sum(counts.values()) for state, count in counts.items()}
plot_histogram(probabilities, figsize=(6,4), color="blue", title="2-qubit in entanglement")
plt.show()
