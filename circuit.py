import qiskit
from qiskit.quantum_info import Operator
import numpy as np
def mcx_gate(num_qubits):
    mcx_gate = qiskit.circuit.library.MCXGate(num_qubits - 1)
    return np.real(Operator(mcx_gate).data)
import qiskit
from qiskit.quantum_info import Operator

def mcx_gate(num_qubits):
    mcx_gate = qiskit.circuit.library.MCXGate(num_qubits - 1)
    return np.real(Operator(mcx_gate).data)

def U3cry(num_qubits: int, num_layers: int, thetas: qiskit.circuit.ParameterVector, active_blocks: np.ndarray) -> tuple[qiskit.QuantumCircuit, np.ndarray]:
    qc = qiskit.QuantumCircuit(num_qubits)
    k = 0
    index_params = 0
    for _ in range(num_layers):
        for i in range(num_qubits):
            for j in range(i + 1, num_qubits):
                if active_blocks[k] == 1:
                    qc.u(thetas[index_params],thetas[index_params + 1],thetas[index_params + 2],i)
                    qc.u(thetas[index_params + 3],thetas[index_params + 4],thetas[index_params + 5],j)
                    qc.cx(j, i)
                    index_params += 6
                k += 1
                qc.barrier()
    return qiskit.quantum_info.Operator(qc).data # .draw('mpl')

def U3cry_qc(num_qubits: int, num_layers: int, thetas: qiskit.circuit.ParameterVector, active_blocks: np.ndarray) -> tuple[qiskit.QuantumCircuit, np.ndarray]:
    qc = qiskit.QuantumCircuit(num_qubits)
    k = 0
    index_params = 0
    for _ in range(num_layers):
        for i in range(num_qubits):
            for j in range(i + 1, num_qubits):
                if active_blocks[k] == 1:
                    qc.u(thetas[index_params],thetas[index_params + 1],thetas[index_params + 2],i)
                    qc.u(thetas[index_params + 3],thetas[index_params + 4],thetas[index_params + 5],j)
                    qc.cx(j, i)
                    index_params += 6
                k += 1
                qc.barrier()
    return qc

