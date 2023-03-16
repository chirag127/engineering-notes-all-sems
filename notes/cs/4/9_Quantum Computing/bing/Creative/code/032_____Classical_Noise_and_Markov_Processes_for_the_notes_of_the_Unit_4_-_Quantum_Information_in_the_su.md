### Classical Noise and Markov Processes for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing

- Classical noise is the random fluctuation or disturbance in a signal or a system that affects the quality or accuracy of the information transmitted or processed.
- Markov processes are stochastic processes that have the property of memorylessness, meaning that the future state of the system depends only on the present state and not on the past history.
- In quantum information theory, classical noise and Markov processes are used to model the interaction of a quantum system with a noisy environment, which can cause decoherence, dissipation, and errors in quantum computation and communication.
- A quantum system is an open system if it interacts with an external environment, which can be another quantum system or a classical system. The state of an open quantum system is described by a density matrix, which is a positive, Hermitian, and trace-one operator on the Hilbert space of the system.
- The dynamics of an open quantum system can be described by a quantum operation, which is a completely positive and trace-preserving (CPTP) map that transforms the initial density matrix of the system to the final density matrix after the interaction with the environment.
- A quantum operation can be represented by a set of Kraus operators, which are linear operators that satisfy the completeness relation, meaning that the sum of their adjoints times themselves is equal to the identity operator. The action of a quantum operation on a density matrix is given by the sum of the Kraus operators times the density matrix times their adjoints.
- A quantum operation is Markovian if it satisfies the semigroup property, meaning that the composition of two quantum operations is equal to another quantum operation with the same Kraus operators. A Markovian quantum operation can be described by a Lindblad master equation, which is a differential equation that governs the time evolution of the density matrix of the system. The Lindblad master equation has the form

$$\frac{d\rho}{dt} = -i[H,\rho] + \sum_k L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\},$$

where $H$ is the Hamiltonian of the system, $L_k$ are the Lindblad operators that describe the effect of the environment on the system, and $\{\cdot,\cdot\}$ denotes the anticommutator.
- A quantum operation is non-Markovian if it does not satisfy the semigroup property, meaning that the composition of two quantum operations is not equal to another quantum operation with the same Kraus operators. A non-Markovian quantum operation can be described by a time-local master equation, which is a differential equation that depends on the current time and the initial time of the interaction. The time-local master equation has the form

$$\frac{d\rho}{dt} = -i[H(t),\rho] + \int_0^t dt' K(t,t') \rho(t') K^\dagger(t,t') - \frac{1}{2}\{K^\dagger(t,t') K(t,t'), \rho(t)\},$$

where $H(t)$ is the time-dependent Hamiltonian of the system, $K(t,t')$ are the memory kernels that describe the effect of the environment on the system at different times, and $\{\cdot,\cdot\}$ denotes the anticommutator.
- Non-Markovian quantum operations can exhibit memory effects, meaning that the future state of the system depends on the past history of the interaction. Memory effects can lead to the revival of quantum coherence, entanglement, and information that were lost due to the environment. Memory effects can also enhance the performance of quantum algorithms, protocols, and metrology.