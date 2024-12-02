# Quantum Teleportation Tutorial

'''
This tutorial implements quantum teleportation - a fundamental quantum protocol
that demonstrates how quantum information can be transmitted using entanglement
and classical communication.
'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import AerSimulator

def create_teleportation_circuit():
    # Create quantum registers
    qr = QuantumRegister(3, 'q')    # 3 qubits: sender, auxiliary, receiver
    cr = ClassicalRegister(2, 'c')   # 2 classical bits for measurements
    circuit = QuantumCircuit(qr, cr)
    
    # Step 1: Prepare the state to teleport (on qubit 0)
    circuit.h(0)  # Create superposition
    circuit.t(0)  # Add some phase
    
    # Step 2: Create Bell pair between auxiliary and receiver (qubits 1 and 2)
    circuit.h(1)
    circuit.cx(1, 2)
    
    # Step 3: Sender's Bell measurement
    circuit.cx(0, 1)
    circuit.h(0)
    
    # Step 4: Measure sender's qubits
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    
    # Step 5: Apply corrections on receiver's qubit based on measurements
    with circuit.if_test((cr, 1), 1):
        circuit.x(2)
    with circuit.if_test((cr, 0), 1):
        circuit.z(2)
    
    return circuit

def run_teleportation():
    # Create and simulate the circuit
    circuit = create_teleportation_circuit()
    simulator = AerSimulator()
    
    # Run the simulation multiple times
    job = simulator.run(circuit, shots=1000)
    result = job.result()
    
    print('Quantum Teleportation Circuit:')
    print(circuit.draw())
    print('\nMeasurement Results:')
    print(result.get_counts())

if __name__ == '__main__':
    run_teleportation()