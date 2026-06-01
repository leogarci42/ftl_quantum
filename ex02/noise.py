from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator, noise
from qiskit.visualization import plot_histogram
import matplotlib as mplt
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke
mplt.use('qtagg')

q = QuantumCircuit(2, 0) #defines a circuit of 1 qubit, 0 classic bit
q.h(0)
q.cx(0,1)
q.measure_all()
real_device_backend = FakeSherbrooke()
transpiled_circuit = transpile(q, real_device_backend)
sim_noise = AerSimulator.from_backend(real_device_backend)
result = sim_noise.run(transpiled_circuit, shots=1000).result()
counts = result.get_counts()
probabilities = {state: count / sum(counts.values()) for state, count in counts.items()}
plot_histogram(probabilities, figsize=(6,4), color="blue", title="2-qubit in entanglement")
plt.show()
