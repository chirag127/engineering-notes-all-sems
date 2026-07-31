### Single Orbit operations

Single-qubit operations are the basic building blocks of quantum computation. These operations are performed using single-qubit gates, which provide a level of control over the state of a qubit . For example, the X-gate is a single-qubit gate that switches the amplitudes of |1⟩ and |0⟩ in a qubit, effectively flipping its state .

Single-qubit operations can be classified into two categories: Clifford gates and non-Clifford gates. Non-Clifford gates consist only of the T-gate (also known as the π/8 gate) . The standard set of single-qubit Clifford gates is included by default in many quantum programming languages, such as Q# .

Single-qubit operations, along with CNOT gates, form a universal set of operations for quantum computation . This means that any quantum computation can be performed using only single-qubit operations and CNOT gates .