### Conditions for Quantum Computation for the notes of the Unit 3 - Quantum Computers in the subject of Quantum Computing

Quantum computation is the process of using quantum systems, such as qubits, to perform operations on data, such as logic gates, that exploit quantum phenomena, such as superposition and entanglement, to achieve speedup or efficiency over classical computation.

To construct a quantum computer, there are some conditions that need to be satisfied, according to the theoretical physicist David P. DiVincenzo, who proposed them in 2000. These conditions are known as DiVincenzo's criteria and they are:

- A scalable physical system with well-characterized qubits: This means that the quantum computer should be able to use a large number of qubits that can be individually controlled and manipulated, and that their properties and interactions are well understood and predictable.
- The ability to initialize the state of the qubits to a simple fiducial state: This means that the quantum computer should be able to prepare the qubits in a known and simple state, such as the |0> state, before performing any computation.
- Long relevant decoherence times: This means that the quantum computer should be able to preserve the quantum state of the qubits for a long time, without losing their coherence due to noise or interference from the environment or other qubits.
- A "universal" set of quantum gates: This means that the quantum computer should be able to perform any quantum operation on the qubits, using a finite and fixed set of elementary quantum gates, such as the Hadamard, Pauli, and CNOT gates.
- A qubit-specific measurement capability: This means that the quantum computer should be able to measure the state of any individual qubit, without disturbing the state of the other qubits, and obtain a classical output, such as 0 or 1.

These five criteria are necessary for quantum computation, but not sufficient. There are two more criteria that are desirable for practical quantum computation:

- The ability to interconvert stationary and flying qubits: This means that the quantum computer should be able to transfer the quantum state of a qubit from one physical system to another, such as from a trapped ion to a photon, without losing the quantum information. This is useful for communication and networking between different quantum devices.
- The ability to faithfully transmit flying qubits between specified locations: This means that the quantum computer should be able to send and receive flying qubits, such as photons, over long distances, without losing or corrupting the quantum information. This is useful for distributed quantum computation and quantum cryptography.

These seven criteria are the main conditions for quantum computation, but there may be other factors that affect the performance and feasibility of a quantum computer, such as error correction, fault tolerance, scalability, cost, and security.

A possible mnemonic to remember the seven criteria is:

**S**calable system
**I**nitializable state
**L**ong coherence
**U**niversal gates
**M**easurable qubits
**S**tationary-flying conversion
**T**ransmission of flying qubits

SILUMST

Some examples of physical systems that can implement quantum computation are:

- Superconducting qubits: These are circuits made of superconducting materials that can behave as qubits by using different energy levels or currents. They have high scalability, long coherence, and fast gates, but they require very low temperatures and are sensitive to noise.
- Trapped ions: These are atoms or molecules that are trapped and isolated by electric or magnetic fields, and can behave as qubits by using different electronic or vibrational states. They have high fidelity, long coherence, and universal gates, but they have low scalability and slow gates.
- Photons: These are particles of light that can behave as qubits by using different polarization or frequency states. They have high coherence, fast transmission, and easy conversion, but they have low scalability, difficult initialization, and inefficient measurement.