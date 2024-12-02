# Common Quantum Gates Implementation

'''
This module provides implementations and visualizations of common quantum gates
using Qiskit. It serves as a reference for understanding basic quantum operations.
'''

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import numpy as np

def create_basic_gates():
    """Creates and returns common single-qubit quantum gates"""
    
    # Hadamard Gate
    h_gate = QuantumCircuit(1)
    h_gate.h(0)
    H = Operator(h_gate)
    
    # Pauli-X (NOT) Gate
    x_gate = QuantumCircuit(1)
    x_gate.x(0)
    X = Operator(x_gate)
    
    # Pauli-Y Gate
    y_gate = QuantumCircuit(1)
    y_gate.y(0)
    Y = Operator(y_gate)
    
    # Pauli-Z Gate
    z_gate = QuantumCircuit(1)
    z_gate.z(0)
    Z = Operator(z_gate)
    
    # Phase Gate
    s_gate = QuantumCircuit(1)
    s_gate.s(0)
    S = Operator(s_gate)
    
    # T Gate
    t_gate = QuantumCircuit(1)
    t_gate.t(0)
    T = Operator(t_gate)
    
    return {
        'H': H.data,
        'X': X.data,
        'Y': Y.data,
        'Z': Z.data,
        'S': S.data,
        'T': T.data
    }

def create_controlled_gates():
    """Creates and returns common controlled quantum gates"""
    
    # CNOT (Controlled-X) Gate
    cx_gate = QuantumCircuit(2)
    cx_gate.cx(0, 1)
    CX = Operator(cx_gate)
    
    # Controlled-Z Gate
    cz_gate = QuantumCircuit(2)
    cz_gate.cz(0, 1)
    CZ = Operator(cz_gate)
    
    # Controlled-Phase Gate
    cp_gate = QuantumCircuit(2)
    cp_gate.cp(np.pi/2, 0, 1)
    CP = Operator(cp_gate)
    
    return {
        'CX': CX.data,
        'CZ': CZ.data,
        'CP': CP.data
    }

def print_gate_properties():
    """Prints properties and matrix representations of quantum gates"""
    basic_gates = create_basic_gates()
    controlled_gates = create_controlled_gates()
    
    print('Single-Qubit Gates:')
    for name, matrix in basic_gates.items():
        print(f'\n{name} Gate:')
        print(matrix)
    
    print('\nControlled Gates:')
    for name, matrix in controlled_gates.items():
        print(f'\n{name} Gate:')
        print(matrix)

if __name__ == '__main__':
    print_gate_properties()