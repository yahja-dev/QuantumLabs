import numpy as np
from qiskit.circuit.library import QFT


def initialize(circuit, measurements, target):
    """
    :param circuit: quantum circuit
    :param measurements: measurement qubits
    :param target: target qubits
    :return: void
    """
    circuit.h(measurements)
    circuit.x(target)
    circuit.draw(output='mpl', filename='illustrations/init.png')


def unitary(circuit, control, target, theta):
    """
    :param circuit: quantum circuit
    :param control: control qubit for the quantum gate
    :param target: target qubit for the quantum gate
    :param theta: qubits initial phase
    :return: void
    """
    circuit.cu1(2 * np.pi * theta, control, target)
    circuit.draw(output='mpl', filename='illustrations/unitary.png')


def exponent(circuit, control, target, theta, exp):
    """
    :param circuit: quantum circuit
    :param control: control qubit for the quantum gate
    :param target: target qubit for the quantum gate
    :param theta: qubits initial phase
    :param exp: number of repetitions of the gate in the circuit
    :return: void
    """
    circuit.cu1(2 * np.pi * theta * exp, control, target)
    circuit.draw(output='mpl', filename='illustrations/exponent.png')


def iqft(circuit, measurements, n):
    """
    :param circuit: quantum circuit
    :param measurements: measurement qubits
    :param n: number of qubits
    :return: void
    """
    circuit.append(QFT(n).inverse(), measurements)
    circuit.draw(output='mpl', filename='illustrations/iqft.png')