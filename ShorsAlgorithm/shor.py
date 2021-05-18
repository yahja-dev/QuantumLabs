from methods import *
from qiskit import Aer, execute
from qiskit.visualization import plot_histogram
from math import gcd


def shor(n, m, a):
    # set up quantum circuit
    shor_circuit = QuantumCircuit(n + m, n)

    # initialize the qubits
    initialize(shor_circuit, n, m)
    shor_circuit.barrier()

    # apply modular exponentiation
    modular_exponentiation(shor_circuit, n, m, a)
    shor_circuit.barrier()

    # apply inverse QFT
    iqft(shor_circuit, range(n))

    # measure the first n qubits
    shor_circuit.measure(range(n), range(n))

    return shor_circuit


if __name__ == '__main__':
    n = 4
    m = 4
    a = 7
    # Shor's algorithm
    circuit = shor(n, m, a)
    circuit.draw(output='mpl', filename='illustrations/shor.png')
    # Get measurement results
    simulator = Aer.get_backend('qasm_simulator')
    counts = execute(circuit, backend=simulator, shots=1000).result().get_counts(circuit)
    # Plot the results
    plot_histogram(counts, figsize=(10,10)).savefig("illustrations/results_histogram.png")
    # Classical post-processing
    for measured_value in counts:
        measured_value_decimal = int(measured_value[::-1], 2)
        print(f"Measured {measured_value_decimal}")

        if measured_value_decimal % 2 != 0:
            print("Failed. Measured value is not an even number")
            continue
        x = int((a ** (measured_value_decimal / 2)) % 15)
        if (x + 1) % 15 == 0:
            print("Failed. x + 1 = 0 (mod N) where x = a^(r/2) (mod N)")
            continue
        guesses = gcd(x + 1, 15), gcd(x - 1, 15)
        print(guesses)


