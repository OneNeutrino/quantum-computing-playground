# Basic Quantum Gates Tutorial

'''
This tutorial introduces the fundamental quantum gates used in quantum computing.
We'll cover the following gates:
- Hadamard (H)
- Pauli-X (NOT)
- Pauli-Y
- Pauli-Z
- CNOT
'''

# Required imports
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_bloch_multivector

def create_bell_state():
    # Create a quantum circuit with 2 qubits
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    circuit = QuantumCircuit(qr, cr)
    
    # Apply Hadamard gate to first qubit
    circuit.h(0)
    
    # Apply CNOT with control=first qubit, target=second qubit
    circuit.cx(0, 1)
    
    return circuit

def main():
    print('Creating a Bell State using Hadamard and CNOT gates')
    bell_state = create_bell_state()
    print(bell_state.draw())

if __name__ == '__main__':
    main()