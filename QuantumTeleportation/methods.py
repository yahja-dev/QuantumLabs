def initialize(circuit, qubit, alpha, beta):
    """
    :param circuit: the quantum circuit
    :param qubit: index of qubit to be initialized
    :param alpha: coefficient of |0>
    :param beta: coefficient of |1>
    :return: circuit
    """
    circuit.initialize([alpha, beta], qubit)
    circuit.draw(output='mpl', filename='illustrations/init.png')
    return circuit


def entangle(circuit, sender, receiver):
    """
    :param circuit: the quantum circuit
    :param sender: index of the qubit transmitting the state
    :param receiver: index of the qubit receiving the state
    :return: circuit
    """
    circuit.h(sender)
    circuit.cx(sender, receiver)
    circuit.draw(output='mpl', filename='illustrations/entanglement.png')
    return circuit


def bell_measurement(circuit, initial, sender, cbit1, cbit2):
    """
    :param circuit: The quantum circuit
    :param initial: index of the qubit holding the state to be teleported
    :param sender: index of the qubit transmitting the state
    :param cbit1: classical bit 1
    :param cbit2: classical bit 2
    :return: circuit
    """
    circuit.cx(initial, sender)
    circuit.h(initial)
    circuit.barrier()
    circuit.measure(initial, cbit1)
    circuit.measure(sender, cbit2)
    circuit.draw(output='mpl', filename='illustrations/bellmeasurement.png')
    return circuit


def controlled_operations(circuit, receiver, cbit1, cbit2):
    """
    :param circuit: the quantum circuit
    :param receiver: index of the qubit of the qubit receiving the state
    :param cbit1: classical bit 1
    :param cbit2: classical bit 2
    :return: circuit
    """
    circuit.x(receiver).c_if(cbit2, 1)
    circuit.z(receiver).c_if(cbit1, 1)
    return circuit
