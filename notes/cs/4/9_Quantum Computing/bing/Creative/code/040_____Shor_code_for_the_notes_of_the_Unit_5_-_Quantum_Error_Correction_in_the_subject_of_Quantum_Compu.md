# Unit 5 - Quantum Error Correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- Quantum information is stored in a quantum error-correcting code, which is a subspace in a larger Hilbert space.
- A quantum error-correcting code can correct errors if they affect only a small number of qubits and if they are independent and random.
- A quantum error-correcting code is characterized by three parameters: the number of physical qubits n, the number of logical qubits k, and the distance d, which is the minimum number of physical qubits that must be corrupted to cause an undetectable error.
- The rate of a quantum error-correcting code is defined as k/n, which measures the efficiency of the code in encoding quantum information.
- The threshold theorem states that if the error rate per physical qubit and gate is below a certain value, called the threshold, then there exists a quantum error-correcting code that can correct errors with arbitrarily high accuracy.
- The threshold value depends on the model of noise, the type of quantum error-correcting code, and the overhead of the error correction protocol.
- Some examples of quantum error-correcting codes are the Shor code, the Steane code, the surface code, the toric code, and the Bacon-Shor code.
- Quantum error correction protocols will play a central role in the realisation of quantum computing; the choice of error correction code will influence the full quantum computing stack, from the layout of qubits at the physical level to gate compilation strategies at the software level.
- Quantum error correction is also used to protect information in quantum communication, where quantum states pass through noisy channels.