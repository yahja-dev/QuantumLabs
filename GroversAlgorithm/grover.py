from qiskit import QuantumCircuit
from methods import *


def Grover(nqubits, marked):
    """
    :param nqubits: number of qubits
    :param marked: list of indices marked with a phase of -1
    :return: grover_circuit
    """
    # Create a quantum circuit on n qubits
    grover_circuit = QuantumCircuit(nqubits, nqubits)

    # Determine r
    r = int(np.floor(np.pi / 4 * np.sqrt(2 ** nqubits / len(marked))))
    print(f'{nqubits} qubits, basis states {marked} marked, {r} rounds')

    # step 1: apply Hadamard gates on all qubits
    grover_circuit.h(range(nqubits))

    # step 2: apply r rounds of the phase oracle and the diffuser
    for _ in range(r):
        grover_circuit.append(oracle(nqubits, marked), range(nqubits))
        grover_circuit.append(diffuser(nqubits), range(nqubits))

    # step 3: measure all qubits
    grover_circuit.measure(range(nqubits), range(nqubits))

    return grover_circuit


if __name__ == '__main__':
    circuit = Grover(6, [1, 42])
    circuit.draw(output='mpl', filename='illustrations/grover.png')
