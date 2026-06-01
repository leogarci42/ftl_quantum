from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator, noise
from qiskit.visualization import plot_histogram
import matplotlib as mplt
import matplotlib.pyplot as plt
mplt.use('qtagg')

q = QuantumCircuit(1, 0) #defines a circuit of 1 qubit, 0 classic bit
q.h(0)
q.measure_all()
sim = AerSimulator()
result = sim.run(q, shots=500).result()
counts = result.get_counts()
probabilities = {state: count / sum(counts.values()) for state, count in counts.items()}
plot_histogram(probabilities, figsize=(5,4), color="blue", title="1-qubit in superposition")
plt.show()
