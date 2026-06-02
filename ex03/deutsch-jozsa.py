from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator, noise
from qiskit.visualization import plot_histogram
import matplotlib as mplt
import matplotlib.pyplot as plt
import numpy as np
from qiskit_ibm_runtime.fake_provider import FakeSherbrooke
mplt.use('qtagg')

n = 3
q = QuantumCircuit(n + 1, n)
q.x(n)
q.h(n)

for qubit in range(n) :
    q.h(qubit)

q.barrier()

q.cx(0, n)
q.cx(1, n)

q.barrier()

for qubit in range(n) :
    q.h(qubit)

q.measure(range(n), range(n))
real_device_backend = FakeSherbrooke()
transpiled_circuit = transpile(q, real_device_backend)
sim_noise = AerSimulator.from_backend(real_device_backend)
result = sim_noise.run(transpiled_circuit, shots=1000).result()
counts = result.get_counts()
probabilities = {state: count / sum(counts.values()) for state, count in counts.items()}
plot_histogram(probabilities, figsize=(6,4), color="blue", title="Deutsch-Josza Algorithm")
plt.show()
