# Grover's Algorithm Implementation

'''
This script implements Grover's search algorithm, which provides quadratic
speedup over classical search algorithms for finding marked elements in an
unstructured database.
'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import AerSimulator
import numpy as np

class GroverSearch:
    def __init__(self, n_qubits, marked_states):
        self.n_qubits = n_qubits
        self.marked_states = marked_states
        self.n_iterations = int(np.pi/4 * np.sqrt(2**n_qubits))
    
    def create_oracle(self, circuit, qubits):
        """Creates oracle that marks target states with phase flip"""
        for marked_state in self.marked_states:
            # Convert marked state to binary and flip according to 0s
            bin_state = format(marked_state, f'0{self.n_qubits}b')
            for i, bit in enumerate(bin_state):
                if bit == '0':
                    circuit.x(qubits[i])
            
            # Multi-controlled Z gate
            circuit.h(qubits[-1])
            circuit.mcx(qubits[:-1], qubits[-1])
            circuit.h(qubits[-1])
            
            # Uncompute X gates
            for i, bit in enumerate(bin_state):
                if bit == '0':
                    circuit.x(qubits[i])
    
    def create_diffusion(self, circuit, qubits):
        """Implements diffusion (inversion about mean) operator"""
        # H gates on all qubits
        for qubit in qubits:
            circuit.h(qubit)
        
        # X gates on all qubits
        for qubit in qubits:
            circuit.x(qubit)
        
        # Multi-controlled Z
        circuit.h(qubits[-1])
        circuit.mcx(qubits[:-1], qubits[-1])
        circuit.h(qubits[-1])
        
        # Uncompute X gates
        for qubit in qubits:
            circuit.x(qubit)
        
        # Uncompute H gates
        for qubit in qubits:
            circuit.h(qubit)
    
    def create_circuit(self):
        """Creates complete Grover's algorithm circuit"""
        # Create registers
        qr = QuantumRegister(self.n_qubits, 'q')
        cr = ClassicalRegister(self.n_qubits, 'c')
        circuit = QuantumCircuit(qr, cr)
        
        # Initialize superposition
        for qubit in qr:
            circuit.h(qubit)
        
        # Apply Grover iterations
        for _ in range(self.n_iterations):
            self.create_oracle(circuit, qr)
            self.create_diffusion(circuit, qr)
        
        # Measure all qubits
        circuit.measure(qr, cr)
        
        return circuit

def run_grover_search(n_qubits=3, marked_state=6):
    # Create and run the circuit
    grover = GroverSearch(n_qubits, [marked_state])
    circuit = grover.create_circuit()
    
    # Simulate the circuit
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=1000)
    result = job.result()
    
    print(f'Searching for state |{marked_state}⟩ in {n_qubits}-qubit system')
    print('\nCircuit:')
    print(circuit.draw())
    print('\nMeasurement Results:')
    print(result.get_counts())

if __name__ == '__main__':
    run_grover_search()