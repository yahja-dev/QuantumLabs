from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from methods import *
import numpy as np


if __name__ == '__main__':
    # Setup
    to_transmit = QuantumRegister(1)
    qubit_Alice = QuantumRegister(1)
    qubit_Bob = QuantumRegister(1)
    cbit1 = ClassicalRegister(1)
    cbit2 = ClassicalRegister(1)

    ### quantum teleportation circuit here
    # Initialize
    circuit = QuantumCircuit(to_transmit, qubit_Alice, qubit_Bob, cbit1, cbit2)
    initialize(circuit, 0, np.sqrt(0.7), np.sqrt(0.3))
    circuit.barrier()
    # Entangle
    entangle(circuit, 1, 2)
    circuit.barrier()
    # Bell measurement
    bell_measurement(circuit, to_transmit[0], qubit_Alice[0], cbit1, cbit2)
    circuit.barrier()
    # Controlled operations
    controlled_operations(circuit, qubit_Bob[0], cbit1, cbit2)

    ### Look at the complete circuit
    circuit.draw(output='mpl', filename='illustrations/teleportation.png')
