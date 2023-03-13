### Examples of Quantum noise and Quantum Operations for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing

Quantum noise is the uncertainty or fluctuations in the values of physical quantities that are inherent to quantum systems. Quantum noise can arise from various sources, such as imperfect control signals, interference from the environment, and unwanted interactions between qubits . Quantum noise can limit the accuracy and reliability of quantum computations, and therefore it is important to understand and mitigate its effects.

Quantum operations are mathematical transformations that describe how quantum systems evolve under the influence of noise, measurement, or other external factors. Quantum operations are also known as quantum channels or quantum processes, and they can be represented by matrices, tensors, or diagrams. Quantum operations can be classified into different types, such as unitary, non-unitary, reversible, irreversible, deterministic, probabilistic, etc.

Some examples of quantum noise and quantum operations are:

- **Depolarizing noise**: This is a type of noise that affects all qubits equally and randomly, and reduces the purity of the quantum state. A depolarizing noise operation can be written as:

  E(ρ)=pρ+(1−p)I2n{displaystyle E(rho )=p rho +(1-p){frac {I}{2^{n}}}}

  where ρ{displaystyle rho } is the density matrix of the n-qubit system, p is the probability of no error, and I is the identity matrix.

- **Bit-flip noise**: This is a type of noise that flips the value of a qubit from 0 to 1 or vice versa with some probability. A bit-flip noise operation can be written as:

  E(ρ)=pρ+(1−p)XρX{displaystyle E(rho )=p rho +(1-p)X rho X}

  where ρ{displaystyle rho } is the density matrix of the qubit, p is the probability of no error, and X is the Pauli-X matrix.

- **Phase-flip noise**: This is a type of noise that flips the phase of a qubit from + to - or vice versa with some probability. A phase-flip noise operation can be written as:

  E(ρ)=pρ+(1−p)ZρZ{displaystyle E(rho )=p rho +(1-p)Z rho Z}

  where ρ{displaystyle rho } is the density matrix of the qubit, p is the probability of no error, and Z is the Pauli-Z matrix.

- **Amplitude damping noise**: This is a type of noise that models the loss of energy or photons from a qubit due to interaction with the environment. An amplitude damping noise operation can be written as:

  E(ρ)=E0ρE0†+E1ρE1†{displaystyle E(rho )=E_{0} rho E_{0}^{dagger }+E_{1} rho E_{1}^{dagger }}

  where ρ{displaystyle rho } is the density matrix of the qubit, and E0 and E1 are the Kraus operators defined as:

  E0=|0⟩⟨0|+√1−γ|1⟩⟨1|{displaystyle E_{0}=|0rangle langle 0|+sqrt {1-gamma }|1rangle langle 1|}

  E1=√γ|0⟩⟨1|{displaystyle E_{1}=sqrt {gamma }|0rangle langle 1|}

  where γ{displaystyle gamma } is the probability of losing a photon.

- **Measurement operation**: This is a type of operation that extracts information from a quantum system by projecting it onto a set of orthogonal states. A measurement operation can be written as:

  M(ρ)=∑iMiρMi†{displaystyle M(rho )=sum _{i}M_{i} rho M_{i}^{dagger }}

  where ρ{displaystyle rho } is the density matrix of the quantum system, and Mi are the measurement operators that satisfy:

  ∑iMi†Mi=I{displaystyle sum _{i}M_{i}^{dagger }M_{i}=I}

  The outcome of the measurement is i with probability:

  pi=Tr(MiρMi†){displaystyle p_{i}=operatorname {Tr} (M_{