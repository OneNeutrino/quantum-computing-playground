# Quantum Fourier Transform Implementation

'''
This script implements the Quantum Fourier Transform (QFT), a quantum analog
of the classical discrete Fourier transform. The QFT is a key component in
many quantum algorithms including Shor's factoring algorithm.
'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import AerSimulator
import numpy as np

def create_qft_circuit(n_qubits):
    """Creates a Quantum Fourier Transform circuit"""
    qr = QuantumRegister(n_qubits)
    circuit = QuantumCircuit(qr)
    
    def qft_rotations(circuit, n):
        """Applies QFT rotations to all qubits"""
        if n == 0:
            return circuit
        n -= 1
        circuit.h(n)
        for qubit in range(n):
            circuit.cp(np.pi/2**(n-qubit), qubit, n)
        qft_rotations(circuit, n)
    
    def swap_registers(circuit, n):
        """Swaps qubits to return correct order"""
        for qubit in range(n//2):
            circuit.swap(qubit, n-qubit-1)
        return circuit
    
    qft_rotations(circuit, n_qubits)
    swap_registers(circuit, n_qubits)
    return circuit

def create_inverse_qft_circuit(n_qubits):
    """Creates an inverse QFT circuit"""
    qft = create_qft_circuit(n_qubits)
    inverse_qft = qft.inverse()
    return inverse_qft

def demonstrate_qft():
    # Create a circuit to demonstrate QFT
    n_qubits = 3
    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_qubits)
    circuit = QuantumCircuit(qr, cr)
    
    # Prepare initial state
    circuit.h(0)
    circuit.x(1)
    
    # Apply QFT
    qft = create_qft_circuit(n_qubits)
    circuit = circuit.compose(qft)
    
    # Measure
    circuit.measure(qr, cr)
    
    # Simulate
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=1000)
    result = job.result()
    
    print('QFT Circuit:')
    print(circuit.draw())
    print('\nMeasurement Results:')
    print(result.get_counts())

if __name__ == '__main__':
    demonstrate_qft()