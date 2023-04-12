

## Unit 1 - Fundamental Concepts

- In this unit, you will learn about some of the basic concepts and principles of computer science, such as data, information, algorithms, abstraction, and complexity.
- Data is any representation of facts, concepts, or instructions in a formalized manner suitable for communication, interpretation, or processing by humans or by automatic means.
- Information is data that has been processed, organized, structured, or presented in a given context to make it meaningful and useful.
- An algorithm is a finite sequence of well-defined, unambiguous, and executable steps that produces a result and halts in a finite amount of time.
- Abstraction is the process of hiding or suppressing the details or complexity of a system or phenomenon, and focusing on the essential features or properties that are relevant for a given purpose or perspective.
- Complexity is a measure of the difficulty or cost of solving a problem or performing a task, in terms of the resources required, such as time, space, or energy.



### Global Perspectives for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing

- Quantum computing is the use of quantum mechanical phenomena, such as superposition and entanglement, to perform computation.
- Quantum computers can potentially solve certain problems faster and more efficiently than classical computers, such as factoring large numbers, simulating quantum systems, and optimizing complex functions.
- Quantum computing is an emerging and rapidly evolving field, with multiple companies, governments, and research institutions developing and testing quantum hardware and software.
- Quantum computing has various applications and implications across different industries and domains, such as cryptography, artificial intelligence, chemistry, physics, medicine, and finance.
- Quantum computing also poses significant challenges and risks, such as scalability, error correction, interoperability, security, and ethical issues.

Some points to remember:

- Quantum bits (qubits) are the basic units of information in quantum computing, which can exist in a superposition of two states, 0 and 1, until measured.
- Quantum volume is a metric that measures the number and reliability of qubits available for computation, which is expected to double every year according to Deloitte Global.
- Quantum algorithms are the rules and steps that quantum computers follow to perform computation, which exploit quantum phenomena such as interference, entanglement, and measurement.
- Quantum supremacy is the milestone when a quantum computer can perform a task that is infeasible for a classical computer, which was claimed by Google in 2019 using a 53-qubit processor.
- Quantum advantage is the practical benefit that a quantum computer can provide over a classical computer for a real-world problem, which is yet to be achieved.



### Quantum Bits

- A quantum bit or qubit is the basic unit of quantum information, which is the quantum analog of the classic binary bit  .
- A qubit is a two-state or two-level quantum-mechanical system, such as an electron or photon, that can exist in a superposition of two states  .
- A superposition means that a qubit can be in a linear combination of both states at the same time, with some probability amplitude for each state  .
- A qubit can be represented by a vector in a two-dimensional complex Hilbert space, with a basis of |0> and |1>, corresponding to the classical states of 0 and 1 .
- A qubit can be manipulated by applying unitary transformations, which are reversible and preserve the norm of the vector .
- A qubit can be measured in a specific basis, which collapses the superposition and gives a definite outcome of either 0 or 1, with some probability determined by the state vector   .
- A qubit can encode more information than a classical bit, because it can be in a superposition of states, rather than a single state .
- A qubit can also exhibit quantum entanglement, which means that two or more qubits can share a quantum state and influence each other, even when they are physically separated  .
- A qubit is the fundamental building block of quantum computing, which aims to exploit the quantum properties of qubits to perform computations that are faster or more efficient than classical computers   .



### Quantum Computation

- Quantum computation is a type of computation that harnesses the collective properties of quantum states, such as superposition, interference, and entanglement, to perform calculations.
- Quantum states are the states of subatomic particles, such as electrons or photons, that can exist in two or more possible values simultaneously, such as 0 and 1.
- Quantum computation uses quantum devices, known as quantum computers, that manipulate quantum states to encode and process information.
- Quantum computation can solve problems that are too complex or intractable for classical computers, such as factoring large numbers, simulating quantum systems, or optimizing combinatorial problems.
- Quantum computation can be described as a network of quantum logic gates and measurements, where quantum logic gates are the basic operations that change the quantum states of one or more qubits, and measurements are the processes that extract classical information from the quantum states.
- Quantum computation can also be expressed in terms of quantum algorithms, which are the sequences of quantum logic gates and measurements that achieve a specific computational goal.
- Quantum computation is a rapidly-emerging technology that has many potential applications in various fields, such as cryptography, artificial intelligence, chemistry, physics, and medicine .



### Quantum Algorithms

Quantum algorithms are algorithms that run on quantum computers, which use the principles of quantum mechanics to manipulate information. Quantum algorithms can offer significant speedups over classical algorithms for some problems, such as factoring large numbers, searching unsorted databases, and simulating quantum systems. Quantum algorithms can also provide novel ways of solving problems that are not possible or efficient on classical computers, such as quantum cryptography, quantum machine learning, and quantum error correction.

Some of the main concepts and techniques that are used in quantum algorithms are:

- **Qubits**: The basic unit of quantum information, which can exist in a superposition of two states, denoted by |0> and |1>. A qubit can be realized by a physical system that has two distinguishable quantum states, such as an electron spin, a photon polarization, or a nuclear magnetic resonance.
- **Quantum gates**: The elementary operations that can be performed on one or more qubits, such as the Hadamard gate, the Pauli-X gate, the CNOT gate, and the Toffoli gate. Quantum gates are reversible and unitary, meaning that they preserve the total probability and the inner product of quantum states. A quantum gate can be represented by a matrix that acts on the vector space of qubits.
- **Quantum circuits**: The sequences of quantum gates that implement a quantum algorithm. A quantum circuit can be represented by a directed acyclic graph, where the nodes are quantum gates and the edges are qubits. A quantum circuit can also be described by a quantum circuit diagram, where the horizontal lines are qubits and the boxes are quantum gates. A quantum circuit can be measured at the end to obtain a classical output, or it can be used as a subroutine in a larger quantum algorithm.
- **Quantum complexity**: The study of the resources required to run a quantum algorithm, such as the number of qubits, the number of quantum gates, the depth of the quantum circuit, and the probability of error. Quantum complexity classes are defined by the types of quantum algorithms that can be executed within certain resource bounds, such as BQP, QMA, and QIP. Quantum complexity also compares the power of quantum algorithms with classical algorithms, such as the polynomial-time hierarchy, the oracle separation, and the quantum speedup.
- **Quantum Fourier transform**: A quantum algorithm that performs the discrete Fourier transform on a quantum state, which is a linear transformation that maps a vector of complex amplitudes to another vector of complex amplitudes. The quantum Fourier transform can be implemented by a quantum circuit that uses only Hadamard gates and controlled phase shift gates. The quantum Fourier transform is a key component of many quantum algorithms, such as Shor's algorithm, Grover's algorithm, and quantum phase estimation.
- **Quantum phase estimation**: A quantum algorithm that estimates the phase of a unitary operator, which is a complex number that represents the rotation angle of the operator. The quantum phase estimation algorithm uses a quantum Fourier transform and a controlled unitary operator to obtain an approximation of the phase with high probability. The quantum phase estimation algorithm can be used to find the eigenvalues and eigenvectors of a unitary operator, which are important for quantum simulation, quantum chemistry, and quantum machine learning.
- **Quantum search**: A quantum algorithm that finds a marked element in an unsorted database, which is a function that maps a set of inputs to a set of outputs. The quantum search algorithm uses a quantum oracle, which is a black box that performs a query on the database and flips the sign of the output if it is marked. The quantum search algorithm also uses a Grover operator, which is a quantum gate that amplifies the amplitude of the marked state and reduces the amplitude of the unmarked states. The quantum search algorithm can find a marked element with a quadratic speedup over classical algorithms, using only O(sqrt(N)) queries, where N is the size of the database.
- **Quantum simulation**: A quantum algorithm that simulates the evolution of a quantum system, which is a collection of qubits that interact with each other according to a Hamiltonian, which is a Hermitian operator that describes the energy of the system. The quantum simulation algorithm uses a Trotter-Suzuki decomposition, which is a method of approximating the exponential of a Hamiltonian by a product of simpler unitary operators. The quantum simulation algorithm can simulate a quantum system with a polynomial speedup over classical algorithms, using only O(poly(log(N))) qubits and gates, where N is the dimension of the Hilbert space of the system.



### Quantum Information

- Quantum information is the information of the state of a quantum system. It is the basic entity of study in quantum information theory, and can be manipulated using quantum information processing techniques.
- Quantum information refers to both the technical definition in terms of Von Neumann entropy and the general computational term.
- Quantum information, like classical information, can be processed using digital computers, transmitted from one location to another, manipulated with algorithms, and analyzed with computer science and mathematics.
- Just like the basic unit of classical information is the bit, quantum information deals with qubits. A qubit is a two-state quantum system that can exist in a superposition of two basis states, such as |0> and |1>.
- Quantum information science aims to explore the nature of information at the quantum level, a world in which bits can be both zero and one at the same time and perfect copying is impossible.
- Quantum information science also powers forms of secure communication that are provably impossible in a “classical” world, such as quantum cryptography and quantum key distribution.
- Quantum information science research at NIST explores ways to employ phenomena exclusive to the quantum world to measure, encode and process information for useful purposes, from powerful data encryption to computers that could solve problems intractable with classical computers.



### Postulates of Quantum Mechanics

Quantum mechanics is the branch of physics that describes the behavior of matter and energy at the atomic and subatomic scales. Quantum mechanics is based on a set of postulates, or basic assumptions, that relate the physical quantities to the mathematical structures used to describe them. Here are some of the main postulates of quantum mechanics:

- **Postulate 1**: The state of a quantum system is completely specified by a wave function, which is a complex-valued function of the coordinates and time of the system. The wave function contains all the information that can be known about the system, and its square modulus gives the probability density of finding the system in a given region of space and time.

- **Postulate 2**: To every physical observable, such as position, momentum, energy, angular momentum, etc., there corresponds a linear, Hermitian operator, which acts on the wave function of the system. The possible outcomes of measuring an observable are the eigenvalues of the corresponding operator.

- **Postulate 3**: When an observable is measured on a system, the system collapses to one of the eigenstates of the operator, with a probability given by the square of the inner product of the wave function and the eigenstate. The expected value of the observable is given by the average of the eigenvalues weighted by the probabilities.

- **Postulate 4**: The time evolution of a quantum system is governed by the Schrödinger equation, which is a partial differential equation that relates the wave function at different times. The Schrödinger equation is derived from the principle of least action, and it preserves the normalization and linearity of the wave function.

These postulates form the basis of quantum mechanics, and they can be used to derive various theorems and applications of the theory. However, they are not the only possible way to formulate quantum mechanics, and there are alternative approaches that use different mathematical structures, such as matrix mechanics, path integrals, or quantum logic.



## Unit 2 - Quantum Computation

- Quantum computation is a type of computation that harnesses the collective properties of quantum states, such as superposition, interference, and entanglement, to perform calculations.
- Quantum states are the states of subatomic particles, such as electrons or photons, that can exist in a superposition of two or more values, such as spin up or down, or polarization horizontal or vertical.
- Quantum computation uses quantum bits, or qubits, as the basic unit of information. A qubit can be in a superposition of 0 and 1, meaning it can represent both values simultaneously until it is measured.
- Quantum computation can perform certain tasks faster or more efficiently than classical computation, such as factoring large numbers, searching databases, simulating quantum systems, or solving optimization problems.
- Quantum computation requires quantum hardware, such as superconducting circuits, trapped ions, or photonic devices, that can manipulate and measure qubits with high fidelity and coherence.
- Quantum computation can be described as a network of quantum logic gates and measurements. Quantum logic gates are operations that change the state of one or more qubits, such as the Hadamard gate, the Pauli-X gate, or the CNOT gate. Measurements are operations that reveal the value of one or more qubits, such as the Z-measurement or the X-measurement.
- Quantum computation can be implemented using various models, such as the circuit model, the measurement-based model, the adiabatic model, or the topological model. Each model has its own advantages and challenges in terms of scalability, error correction, and universality.



### Quantum Circuits

- A quantum circuit is a model for quantum computation, similar to classical circuits, in which a computation is a sequence of quantum gates, measurements, initializations of qubits to known values, and possibly other actions.
- A quantum gate is a basic unitary operation that acts on one or more qubits. Quantum gates are reversible, unlike classical gates, and can be represented by unitary matrices. Some examples of quantum gates are the Hadamard gate, the Pauli-X gate, the CNOT gate, and the Toffoli gate.
- A quantum wire is a physical medium that carries quantum information between quantum gates. Quantum wires can be implemented by optical fibers, superconducting wires, or other physical systems that preserve quantum coherence.
- A quantum circuit can be represented by a directed acyclic graph (DAG), where the nodes are quantum gates and the edges are quantum wires. The input and output qubits are labeled by the leftmost and rightmost nodes, respectively. The order of the gates in the circuit corresponds to the order of the matrix multiplication of the unitary matrices that represent them.
- A quantum circuit can be used to implement a unitary transformation, U, on a quantum state, |ψ⟩, by applying the sequence of quantum gates that correspond to U. The output state is U|ψ⟩. Alternatively, a quantum circuit can be used to perform a measurement on a quantum state, by applying a measurement gate at the end of the circuit. The measurement gate projects the state onto a basis of eigenstates, and the outcome is a random eigenvalue with a probability given by the Born rule.
- Quantum circuits are imperfect, which prevents us from running well-known quantum algorithms using the gates-based quantum computing approach. To overcome this problem, a new breed of quantum algorithms has been introduced, employing the parametrized shallow quantum circuits, which can be called variational (quantum) circuits. These circuits are designed to optimize a cost function that depends on the output of the circuit, and can be used for tasks such as quantum machine learning, quantum simulation, and quantum optimization.



### Quantum algorithms

Quantum algorithms are algorithms that run on quantum computers, which use the principles of quantum mechanics to manipulate information. Quantum algorithms can offer significant speedups over classical algorithms for certain problems, such as factoring large numbers, searching unsorted databases, and simulating quantum systems. Quantum algorithms can also provide novel ways of solving problems that are not possible or efficient on classical computers, such as quantum cryptography, quantum machine learning, and quantum error correction.

Some of the main concepts and techniques that are used in quantum algorithms are:

- **Qubits**: The basic unit of quantum information, which can exist in a superposition of two states, denoted by |0> and |1>. A qubit can be realized by a physical system that has two distinguishable quantum states, such as an electron spin, a photon polarization, or a nuclear magnetic resonance.
- **Quantum gates**: The elementary operations that can be performed on one or more qubits, such as the Hadamard gate, the Pauli-X gate, the CNOT gate, and the Toffoli gate. Quantum gates are reversible and unitary, meaning that they preserve the total probability and the inner product of quantum states. A quantum gate can be represented by a matrix that acts on the state vector of the qubits.
- **Quantum circuits**: The sequences of quantum gates that implement a quantum algorithm. A quantum circuit can be represented by a directed acyclic graph, where the nodes are quantum gates and the edges are qubits. A quantum circuit can also be described by a quantum circuit diagram, where the horizontal lines are qubits and the symbols are quantum gates. A quantum circuit can be measured at the end to obtain a classical output, or it can be used as a subroutine in a larger quantum algorithm.
- **Quantum complexity**: The study of the resources required to run a quantum algorithm, such as the number of qubits, the number of quantum gates, the depth of the quantum circuit, and the probability of error. Quantum complexity classes are defined by the types of quantum algorithms that can be executed within certain resource bounds, such as BQP, QMA, and QIP. Quantum complexity also compares the power of quantum algorithms with classical algorithms, such as the polynomial-time hierarchy, the oracle separation, and the quantum speedup.
- **Quantum Fourier transform**: A quantum algorithm that performs the discrete Fourier transform on a quantum state, which is a linear transformation that maps a complex vector of length N to another complex vector of length N. The quantum Fourier transform can be implemented by a quantum circuit that uses O(log N) qubits and O(N log N) quantum gates, which is exponentially faster than the classical Fourier transform that uses O(N log N) bits and O(N^2 log N) operations. The quantum Fourier transform is a key component of many quantum algorithms, such as Shor's algorithm, Grover's algorithm, and quantum phase estimation.
- **Quantum phase estimation**: A quantum algorithm that estimates the phase of a unitary operator, which is a complex number that represents the rotation angle of the operator. The quantum phase estimation algorithm uses a quantum Fourier transform and a controlled unitary operator to obtain an approximation of the phase with high probability. The quantum phase estimation algorithm can be used to find the eigenvalues and eigenvectors of a unitary operator, which are important for quantum simulation, quantum chemistry, and quantum machine learning.
- **Quantum search**: A quantum algorithm that finds a marked item in an unsorted database of N items, which is a function that maps each item to either 0 or 1, where 1 indicates that the item is marked. The quantum search algorithm uses a quantum oracle, which is a black-box that performs the function evaluation, and a Grover operator, which is a quantum gate that amplifies the amplitude of the marked item. The quantum search algorithm can find a marked item with high probability using O(sqrt(N)) oracle queries and O(sqrt(N)) quantum gates, which is quadratically faster than the classical search algorithm that uses O(N) queries and O(N) operations. The quantum search algorithm can also be generalized to find multiple marked items, to search with partial information, and to optimize a function.
- **Quantum simulation**: A quantum algorithm that simulates the dynamics of a quantum system, which is a collection of particles that interact according to the laws of quantum mechanics. The quantum simulation algorithm uses a quantum computer to encode the state of the quantum system, and applies a sequence of quantum gates that approximate the evolution of the system under a given Hamiltonian, which is a mathematical operator that describes the energy and the interactions of the system



### Single Orbit Operations

- Single orbit operations are quantum gates that act on a single qubit, which is the basic unit of quantum information.
- A single qubit can be represented by a two-dimensional complex vector, or a linear combination of two basis states, usually denoted as |0> and |1>.
- A single orbit operation can be represented by a 2x2 unitary matrix, which preserves the norm and the orthogonality of the qubit vector.
- A unitary matrix U satisfies UU^† = U^†U = I, where U^† is the adjoint or the complex conjugate transpose of U, and I is the identity matrix.
- A unitary matrix can be decomposed into a product of simpler matrices, such as the Pauli matrices, the Hadamard matrix, and the phase shift matrix.
- The Pauli matrices are X, Y, and Z, which correspond to the rotations of the qubit vector around the x, y, and z axes of the Bloch sphere, respectively. They are defined as:

X = |0><1| + |1><0| = [[0, 1], [1, 0]]

Y = -i|0><1| + i|1><0| = [[0, -i], [i, 0]]

Z = |0><0| - |1><1| = [[1, 0], [0, -1]]

- The Hadamard matrix H is a special case of the rotation matrix R_x(θ) around the x axis, with θ = π/2. It creates a superposition of the basis states, such that H|0> = (|0> + |1>)/√2 and H|1> = (|0> - |1>)/√2. It is defined as:

H = 1/√2 (|0><0| + |0><1| + |1><0| - |1><1|) = 1/√2 [[1, 1], [1, -1]]

- The phase shift matrix R_z(φ) is a special case of the rotation matrix R_z(φ) around the z axis, with φ being the phase angle. It adds a relative phase to the qubit vector, such that R_z(φ)|0> = |0> and R_z(φ)|1> = e^iφ |1>. It is defined as:

R_z(φ) = |0><0| + e^iφ |1><1| = [[1, 0], [0, e^iφ]]

- Single orbit operations can be used to manipulate the state of a single qubit, and to prepare it for further operations, such as measurement or entanglement with other qubits.
- Single orbit operations are reversible, meaning that they can be undone by applying their inverse or adjoint operation. For example, X^† = X, H^† = H, and R_z(φ)^† = R_z(-φ).
- Single orbit operations are also universal, meaning that any unitary matrix can be approximated by a finite sequence of single orbit operations. For example, any rotation matrix R(θ, n) around an arbitrary axis n can be decomposed into a product of X, Y, Z, and H matrices.



### Control Operations

- Control operations are quantum operations that depend on the state of one or more control qubits.
- Control operations are essential for implementing quantum logic gates, quantum algorithms, quantum error correction, and quantum feedback control.
- Control operations can be realized by applying electric, magnetic, or electromagnetic control fields to the quantum system.
- Control operations can be classified into two types: coherent control and measurement-based control.
- Coherent control is the manipulation of quantum states without destroying their coherence or entanglement. Coherent control can be achieved by applying unitary or nonunitary operations to the quantum system.
- Measurement-based control is the manipulation of quantum states based on the outcomes of measurements performed on the quantum system or its environment. Measurement-based control can be used to implement quantum feedback, quantum teleportation, quantum error correction, and quantum metrology.
- Control operations can be optimized by using quantum optimal control techniques, which aim to find the optimal control fields that achieve the desired quantum dynamics with minimum cost or maximum fidelity .
- Control operations can be implemented by using various control hardware platforms, such as field-programmable gate arrays (FPGAs), digital-to-analog converters (DACs), analog-to-digital converters (ADCs), and microwave generators .
- Control operations are subject to various sources of noise and errors, such as decoherence, control imperfections, measurement errors, and environmental disturbances. Control operations can be improved by using error-robust control methods, such as dynamical decoupling, composite pulses, and quantum error correction  .



### Measurement for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Measurement is a fundamental operation in quantum computation, where the state of a quantum system is observed and recorded.
- Measurement can be used to perform logic operations, manipulate entanglement, and extract information from quantum systems.
- Measurement can also be used to drive the computation, as in the framework of measurement-based quantum computation (MBQC)  .
- In MBQC, the computation is performed by preparing a highly entangled state of qubits, called the cluster state, and then measuring individual qubits in a specific order and basis  .
- The cluster state is a universal resource for quantum computation, meaning that any quantum circuit can be implemented by measuring the cluster state .
- The measurement outcomes determine the next measurements to be performed, and the final outcomes encode the result of the computation  .
- MBQC has several advantages over the standard circuit model of quantum computation, such as fault-tolerance, parallelism, and reduced communication complexity .
- Measurement can also be used to probe the properties of quantum systems, such as coherence, entanglement, and nonlocality .
- Measurement can also cause the collapse of the quantum state, resulting in the loss of quantum information and the generation of randomness .
- Measurement can be described by the Born rule, which assigns probabilities to the possible outcomes of a measurement, and the projection postulate, which describes how the state of the system changes after a measurement .



### Universal Quantum Gates

- A quantum gate is a basic quantum circuit operating on a small number of qubits.
- A quantum gate can perform a unitary transformation on the quantum state of the qubits.
- A set of universal quantum gates is any set of gates that can generate any unitary transformation on any number of qubits, up to a global phase .
- A universal quantum gate set is not unique, and there are many possible choices of such a set.
- One simple set of two-qubit universal quantum gates is the Hadamard gate (H), a phase rotation gate R (cos<sup>-1</sup>(3/5)), and the controlled-NOT gate (CNOT), a special case of controlled-U such that U = X.
- Another set of two-qubit universal quantum gates is the CNOT gate and any single-qubit gate.
- A single-gate set of universal quantum gates can also be formulated using the three-qubit Deutsch gate, D(θ), which is a generalization of the Toffoli gate.
- The Toffoli gate, or the controlled-controlled-NOT (CCNOT) gate, is a key logical gate in classical computing because it is universal for classical reversible computation.
- The Toffoli gate can be implemented using six CNOT gates and nine single-qubit gates.
- The iToffoli gate is a variant of the Toffoli gate that applies the inverse of the X gate on the target qubit if both control qubits are in the |1> state.
- The iToffoli gate can be implemented using a single step in a superconducting quantum information processor, and has a high fidelity of 0.993.



### Simulation of Quantum Systems

- Quantum simulators are controllable quantum systems that can be used to simulate other quantum systems.
- Quantum simulators can tackle problems that are intractable on classical computers, such as quantum many-body physics, quantum chemistry, and quantum field theory .
- Quantum simulators can also provide a means of exploring new physical phenomena and testing quantum algorithms.
- A quantum system of many particles could be simulated by a quantum computer using a number of quantum bits (qubits) similar to the number of particles in the original system.
- However, this approach is limited by the availability and scalability of qubits, as well as the effects of noise and decoherence.
- Alternatively, a quantum system can be simulated by another quantum system that has a similar Hamiltonian, such as cold atoms, trapped ions, superconducting circuits, or photons.
- This approach is called analog quantum simulation and it relies on the ability to engineer and manipulate the interactions between the quantum components of the simulator.
- Another approach is called digital quantum simulation, where a quantum system is simulated by applying a sequence of quantum gates to a set of qubits.
- This approach is more flexible and universal, but it requires a high degree of control and error correction to achieve high fidelity.
- The direct simulation of quantum systems on classical computers is very difficult because of the huge amount of memory required to store the explicit state of the quantum system.
- This is due to the fact that quantum states are described by a number of parameters that grows exponentially with the system size.
- Therefore, classical simulations often rely on approximations and numerical methods, such as tensor networks, Monte Carlo methods, or variational algorithms.
- However, these methods have limitations and trade-offs in terms of accuracy, efficiency, and scalability.
- A recent method for simulating open quantum systems with arbitrary environments that consist of a set of independent degrees of freedom is based on automated compression of the environment state.
- This method reduces the large dimensionality of the environment state by exploiting its entanglement structure and applying a sequence of unitary transformations.
- This method can simulate the dynamics of open quantum systems with high accuracy and low computational cost.



### Quantum Fourier transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT acts on a quantum state vector (a quantum register), and the DFT acts on a vector. Both types of vectors can be written as lists of complex numbers.
- In the quantum case, the vector is a sequence of probability amplitudes for all the possible outcomes upon measurement (called basis states, or eigenstates).
- The QFT can be defined as follows:

  - Let $|x\rangle$ be an $n$-qubit state, where $x$ is an $n$-bit integer. Then the QFT maps $|x\rangle$ to $|y\rangle$, where $y$ is another $n$-bit integer, such that:

    $$|y\rangle = \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}e^{2\pi ixy/2^n}|x\rangle$$

  - The QFT can be implemented by a single unitary transformation, which can be decomposed into a product of simpler gates, such as Hadamard gates and controlled phase shift gates .
  - The QFT can be inverted by applying the inverse of the unitary transformation, which is the complex conjugate of the QFT matrix.
  - The QFT can be used to transform a quantum state from the computational basis to the Fourier basis, and vice versa.
  - The QFT can be used to perform efficient arithmetic operations, such as addition, multiplication, and modular exponentiation, on quantum states.
  - The QFT can be used to extract information about the periodicity or the phase of a quantum state, which is essential for many quantum algorithms.



### Phase estimation

- Phase estimation is a quantum algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
- The objective of the algorithm is to find θ in U|ψ> = e<sup>2πiθ</sup>|ψ>, where U is a unitary operator and |ψ> is an eigenvector of U with eigenvalue e<sup>2πiθ</sup>.
- The algorithm uses two quantum registers: one for the input state |ψ> and one for the output state |0><sup>n</sup>, where n is the number of qubits used to store the estimate of θ.
- The algorithm consists of the following steps:
  - Apply a Hadamard gate to each qubit in the output register, creating an equal superposition of all possible states.
  - Apply a controlled-U<sup>2<sup>k</sup></sup> gate to the k-th qubit in the output register and the input register, where U<sup>2<sup>k</sup></sup> is the unitary operator U repeated 2<sup>k</sup> times. This creates a phase shift of 2<sup>k</sup>θ on the k-th qubit in the output register.
  - Apply an inverse quantum Fourier transform (QFT<sup>†</sup>) to the output register, transforming the phase shifts into a binary representation of θ.
  - Measure the output register, obtaining an n-bit approximation of θ.
- The algorithm has a success probability of at least 4/π<sup>2</sup> ≈ 40.5% for any choice of n. The accuracy of the estimate can be improved by increasing n or repeating the algorithm multiple times.
- Phase estimation is a central building block for many quantum algorithms, such as Shor's algorithm, quantum counting, quantum amplitude amplification, and quantum simulation . It can also be used to implement a measurement for essentially any Hermitian operator.



### Applications of Quantum Computation

Quantum computation is the use of quantum-mechanical phenomena, such as superposition and entanglement, to perform operations on data. Quantum computers are different from classical computers, which operate on binary digits (bits). Quantum computers operate on quantum bits (qubits), which can be in a superposition of both 0 and 1 states. Quantum computers can potentially solve some problems faster and more efficiently than classical computers, such as factoring large numbers, simulating quantum systems, and optimizing complex functions.

Some of the applications of quantum computation are:

- **Artificial intelligence**: Quantum computers can enhance the capabilities of artificial intelligence systems, such as machine learning, natural language processing, computer vision, and speech recognition. Quantum computers can process large amounts of data, perform parallel computations, and exploit quantum interference to find optimal solutions. Quantum algorithms, such as quantum neural networks, quantum support vector machines, and quantum variational circuits, can potentially improve the accuracy, speed, and scalability of artificial intelligence applications .
- **Better batteries**: Quantum computers can help design and optimize new materials for batteries, such as lithium-air and lithium-sulfur batteries, which have higher energy density and lower environmental impact than conventional batteries. Quantum computers can simulate the chemical reactions and properties of these materials, and find the optimal parameters for their performance and stability.
- **Cleaner fertilization**: Quantum computers can help reduce the environmental and economic costs of producing fertilizers, such as ammonia, which are essential for agriculture. Quantum computers can simulate the catalytic processes and molecular structures involved in the production of fertilizers, and find the optimal conditions and catalysts for achieving higher efficiency and lower emissions.
- **Cybersecurity**: Quantum computers can pose a threat to the security of classical cryptographic systems, such as RSA and ECC, which rely on the hardness of factoring large numbers and computing discrete logarithms. Quantum computers can potentially break these systems using quantum algorithms, such as Shor's algorithm and Grover's algorithm. However, quantum computers can also provide new methods for enhancing cybersecurity, such as quantum key distribution, quantum digital signatures, and quantum-resistant cryptography  .
- **Drug development**: Quantum computers can help accelerate the discovery and development of new drugs, such as vaccines, antibiotics, and antivirals. Quantum computers can simulate the interactions and dynamics of molecules, proteins, and enzymes, and find the optimal candidates for drug targets and drug design. Quantum computers can also help analyze the effects and side effects of drugs, and optimize their dosage and delivery  .
- **Electronic materials discovery**: Quantum computers can help discover and design new materials for electronic devices, such as transistors, sensors, and solar cells. Quantum computers can simulate the electronic properties and behaviors of these materials, such as band structure, conductivity, and magnetism, and find the optimal compositions and configurations for achieving desired functionalities and performance .
- **Financial modeling**: Quantum computers can help improve the accuracy and efficiency of financial modeling, such as portfolio optimization, risk analysis, pricing, and trading. Quantum computers can process large and complex financial data, perform parallel and stochastic computations, and exploit quantum interference and entanglement to find optimal solutions. Quantum algorithms, such as quantum Monte Carlo, quantum linear programming, and quantum amplitude estimation, can potentially enhance the speed and quality of financial modeling applications  .
- **Solar capture**: Quantum computers can help improve the efficiency and sustainability of solar energy capture and conversion, such as photovoltaic cells and artificial photosynthesis. Quantum computers can simulate the quantum effects and processes involved in these systems, such as exciton formation, charge separation, and energy transfer, and find the optimal materials and conditions for maximizing solar capture and conversion.
- **Traffic optimization**: Quantum computers can help optimize the routing and scheduling of traffic, such as vehicles, trains, and airplanes, and reduce congestion, pollution, and accidents. Quantum computers can process large and dynamic traffic data, perform parallel and probabilistic computations, and exploit quantum interference and entanglement to find optimal solutions. Quantum algorithms, such as quantum annealing, quantum search, and quantum walks, can potentially improve the speed and quality of traffic optimization applications.
- **Weather forecasting and climate change**: Quantum computers can help improve the accuracy and timeliness of weather forecasting and climate change modeling, such as predicting storms, hurricanes, and floods, and assessing the impacts of greenhouse gas



### Quantum search algorithms

Quantum search algorithms are quantum algorithms that can find a target element in a large unsorted database faster than classical algorithms. They are based on the principles of quantum superposition, interference and measurement.

Some of the main quantum search algorithms are:

- **Grover's algorithm**: This algorithm can find a unique element that satisfies a given condition in a database of N elements using only O(sqrt(N)) queries to the database, compared to O(N) queries for a classical algorithm. It uses two main operations: an oracle that marks the target element with a negative sign, and a diffusion operator that amplifies the amplitude of the target element. The algorithm iterates these operations until the probability of measuring the target element is high enough.
- **Quantum walk algorithms**: These algorithms use quantum walks, which are quantum analogues of random walks, to explore the database. Quantum walks can be discrete or continuous, depending on whether the walker moves in discrete steps or in a continuous manner. Quantum walk algorithms can achieve quadratic or even exponential speedups over classical algorithms for some search problems, such as finding a marked vertex in a graph.
- **Hybrid quantum-classical algorithms**: These algorithms combine quantum and classical components to perform search tasks. For example, one can use a quantum algorithm to generate a candidate solution, and then use a classical algorithm to verify and refine it. This can reduce the quantum resources and the error rate of the algorithm. Hybrid algorithms can also exploit the advantages of different quantum models, such as quantum annealing or quantum machine learning.



### Quantum counting

Quantum counting is a quantum algorithm for efficiently counting the number of solutions for a given search problem. The algorithm is based on the quantum phase estimation algorithm and on Grover's search algorithm. Counting problems are common in diverse fields such as statistical estimation, statistical physics, networking, etc.

Some key points about quantum counting are:

- Quantum counting can estimate the number of solutions with an error of at most $\epsilon$ using $O(\sqrt{N}\log(1/\epsilon))$ queries to the oracle, where $N$ is the size of the search space and the oracle is a unitary operator that marks the solutions.
- Quantum counting uses a quantum circuit that consists of two registers: a counting register and a search register. The counting register is initialized to the equal superposition of all possible states, and the search register is initialized to the zero state. The circuit then applies the quantum phase estimation algorithm on the Grover operator, which is a combination of the oracle and the Grover diffusion operator. The Grover operator amplifies the amplitude of the marked states in the search register, and induces a phase shift in the counting register that depends on the number of solutions. The circuit then measures the counting register and obtains an estimate of the phase shift, which can be used to calculate the number of solutions.
- Quantum counting can be generalized to amplitude amplification, which is a technique that can boost the success probability of any quantum algorithm that uses an oracle. Amplitude amplification can also be used to speed up the Grover search algorithm, reducing the number of queries from $O(\sqrt{N})$ to $O(\sqrt{N/M})$, where $M$ is the number of solutions. Amplitude amplification can also be used to implement quantum algorithms for other problems, such as element distinctness, collision finding, and minimum finding.



### Speeding up the solution of NP – complete problems

- NP-complete problems are problems that are both in NP and NP-hard, meaning that they can be verified in polynomial time, but no efficient algorithm is known to find a solution in polynomial time.
- Quantum computing is a paradigm of computation that uses quantum mechanical phenomena, such as superposition and entanglement, to perform operations on data.
- Quantum computing has the potential to speed up the solution of some NP-complete problems, but not all of them. There are different models of quantum computing, such as quantum circuit model, quantum annealing, and quantum adiabatic computation, that have different capabilities and limitations.
- Quantum circuit model is the most general and powerful model of quantum computing, where a quantum algorithm consists of a sequence of quantum gates applied to a set of qubits. Quantum circuit model can implement any classical algorithm, as well as some quantum algorithms that are faster than classical ones, such as Shor's algorithm for factoring and Grover's algorithm for search.
- Grover's algorithm can be used to speed up the solution of some NP-complete problems, such as 3-SAT, by reducing the number of queries to the oracle from O(2^n) to O(2^(n/2)), where n is the number of variables. However, this is still exponential in n, and does not imply that NP-complete problems can be solved in polynomial time by quantum computers.
- Quantum annealing is a model of quantum computing that uses quantum fluctuations to find the global minimum of a cost function. Quantum annealing can be used to solve some optimization problems, such as the traveling salesman problem, by encoding the problem as a quadratic unconstrained binary optimization (QUBO) problem, and finding the lowest energy state of a quantum system.
- Quantum annealing computers are commercially available, such as the D-Wave systems, but they are not universal quantum computers, and their performance depends on the problem structure and the hardware specifications. Quantum annealing can also be simulated by classical algorithms, such as simulated annealing, and it is not clear whether quantum annealing can offer a significant speedup over classical methods for NP-complete problems.
- Quantum adiabatic computation is a model of quantum computing that uses the adiabatic theorem to transform the initial state of a quantum system to the final state that encodes the solution of a problem. Quantum adiabatic computation can be used to solve the same class of problems as quantum annealing, by applying a slowly varying Hamiltonian that interpolates between the initial and the final Hamiltonian.
- Quantum adiabatic computation is theoretically equivalent to quantum circuit model, but it may require more physical resources and longer running time to implement. Quantum adiabatic computation can also suffer from decoherence and noise, which can affect the quality of the solution. Quantum adiabatic computation can also be simulated by classical algorithms, such as quantum Monte Carlo methods, and it is not clear whether quantum adiabatic computation can offer a significant speedup over classical methods for NP-complete problems.
- In summary, quantum computing can speed up the solution of some NP-complete problems, but not all of them, and not necessarily in polynomial time. Quantum computing can offer a quadratic speedup for some problems, such as 3-SAT, by using Grover's algorithm, and a possible speedup for some optimization problems, such as the traveling salesman problem, by using quantum annealing or quantum adiabatic computation. However, these speedups are not guaranteed, and depend on the problem structure, the hardware specifications, and the noise and decoherence effects. Quantum computing cannot solve NP-complete problems in polynomial time, unless P=NP, which is widely believed to be false.



### Quantum Search for an Unstructured Database

- Quantum search is a technique that uses quantum algorithms to find a target item in an unstructured collection of data, such as a database or a list.
- The most famous quantum search algorithm is Grover's algorithm, which can find a target item in a database of size N with O(sqrt(N)) queries to the database, compared to O(N) queries for a classical linear search.
- Grover's algorithm relies on an oracle function, which is a black box that can recognize the target item and mark it with a phase flip. The oracle function can be implemented as a quantum circuit that performs some computation on the database items and applies a conditional phase shift to the target item.
- The oracle function can be combined with a diffusion operator, which is a quantum circuit that performs an inversion about the mean of the amplitudes of the quantum states. The diffusion operator amplifies the amplitude of the target state and reduces the amplitude of the non-target states.
- By applying the oracle and the diffusion operator repeatedly, Grover's algorithm can increase the probability of measuring the target state to near unity, as long as the number of iterations is approximately sqrt(N/4).
- Grover's algorithm can be generalized to find multiple target items in a database, or to find an item that satisfies some criteria, such as being the minimum or maximum value in the database.
- Grover's algorithm can also be modified to search a real unstructured database, which is a physical device that stores the data in a classical memory. The oracle function can access the memory by using a quantum register that encodes the address of the memory location, and a quantum bus that transfers the data from the memory to the quantum circuit. The oracle function can then perform the phase flip on the target item and return the data to the memory.
- Quantum search can offer a quadratic speedup over classical search, which can be significant for large databases or hard problems. However, quantum search cannot solve NP-complete problems in polynomial time, as it still requires an exponential number of queries to the oracle function in the worst case. Quantum search can also be affected by noise and decoherence, which can reduce the fidelity and accuracy of the algorithm.



## Unit 3 - Quantum Computers

- A quantum computer is a computer that exploits quantum mechanical phenomena. At small scales, physical matter exhibits properties of both particles and waves, and quantum computing leverages this behavior using specialized hardware.
- Quantum computers use quantum bits or qubits as the basic units of information. Unlike classical bits that can only be in one of two states (0 or 1), qubits can be in superposition of both states simultaneously, meaning they can store more information and perform more operations.
- Quantum computers can also take advantage of another quantum phenomenon called entanglement, which is a special correlation between two or more qubits that allows them to share information and influence each other, even when they are physically separated.
- Quantum computers can potentially solve problems that are too complex for classical computers, such as factoring large numbers, simulating quantum systems, optimizing complex functions, and breaking encryption schemes.
- Quantum computers are still in the early stages of development and face many challenges, such as maintaining coherence and fidelity of qubits, scaling up the number and quality of qubits, and creating efficient and reliable quantum algorithms and error correction methods.
- Quantum computers are elegant machines, smaller and requiring less energy than supercomputers. An IBM Quantum processor is a wafer not much bigger than the one found in a laptop.
- Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers. Today, IBM Quantum makes real quantum hardware -- a tool scientists only began to imagine three decades ago -- available to hundreds of thousands of developers.



### Guiding Principles for the notes of the Unit 3 - Quantum Computers in the subject of Quantum Computing

- The notes should cover the following topics:
  - The basic concepts of quantum mechanics, such as superposition, entanglement, measurement, and interference.
  - The quantum circuit model, including qubits, gates, and algorithms.
  - The physical implementation of quantum computers, such as trapped ions, superconducting qubits, and photonic qubits.
  - The main challenges and limitations of quantum computing, such as decoherence, noise, and error correction.
  - The current state and future prospects of quantum computing, such as quantum supremacy, quantum advantage, and quantum applications.
- The notes should be concise, clear, and accurate, using appropriate terminology and notation.
- The notes should include examples, diagrams, and exercises to illustrate and reinforce the concepts and techniques.
- The notes should provide references and links to relevant sources and materials for further reading and exploration.
- The notes should be organized and structured in a logical and coherent way, using headings, subheadings, and bullet points.



### Conditions for Quantum Computation

Quantum computation is the process of using quantum systems, such as atoms, photons, or electrons, to perform operations on data encoded in quantum bits, or qubits. Quantum computation exploits some of the unique features of quantum mechanics, such as superposition, entanglement, and interference, to perform tasks that are intractable or impossible for classical computers. However, quantum computation also faces many challenges, such as decoherence, noise, and scalability, that require certain conditions to be met in order to implement efficient and reliable quantum algorithms. Some of the conditions for quantum computation are:

- **Long coherence time**: Coherence is the property of quantum systems that allows them to maintain their quantum state and interference patterns. Coherence time is the duration for which a qubit can remain in a coherent superposition of 0 and 1 before it loses its quantum information due to interaction with the environment. Long qubit coherence times are a prerequisite for quantum computing, as they allow more operations to be performed on the qubits before they decohere and become useless. Different physical implementations of qubits have different coherence times, ranging from nanoseconds to seconds. The longer the coherence time, the better the qubit quality.

- **High scalability**: Scalability is the ability to increase the number of qubits and operations in a quantum computer without compromising its performance and reliability. High scalability is essential for quantum computing, as many quantum algorithms require a large number of qubits and operations to achieve a significant speedup over classical computers. However, scaling up a quantum computer is not trivial, as it involves increasing the complexity of the hardware, the control, and the error correction. Moreover, adding more qubits also increases the susceptibility to decoherence and noise, which can degrade the quantum advantage. Therefore, high scalability requires finding a balance between the qubit quantity and quality.

- **High fault tolerance and quantum error correction**: Fault tolerance is the ability of a quantum computer to tolerate errors and faults that occur during the computation without affecting the output. Quantum error correction is the technique of encoding and manipulating quantum information in such a way that errors can be detected and corrected without disturbing the quantum state. High fault tolerance and quantum error correction are crucial for quantum computing, as quantum systems are very sensitive to errors and faults caused by decoherence, noise, and imperfections. Unlike classical computers, quantum computers cannot use simple copying or repetition to correct errors, as this would violate the no-cloning theorem of quantum mechanics. Therefore, high fault tolerance and quantum error correction require designing and implementing sophisticated codes and protocols that can protect and recover the quantum information.

- **Ability to initialize qubits**: Initialization is the process of preparing the qubits in a known and desired state before the computation begins. Ability to initialize qubits is important for quantum computing, as it ensures that the qubits are ready to receive and process the input data. Initialization can be done by applying certain operations or measurements on the qubits that can reset them to a standard state, such as 0 or 1. Different physical implementations of qubits have different methods and challenges for initialization. The ability to initialize qubits should be fast, reliable, and scalable.

- **Universal quantum gates**: Quantum gates are the basic operations that can be performed on one or more qubits to manipulate their quantum state. Universal quantum gates are a set of quantum gates that can be used to approximate any quantum operation to any desired accuracy. Universal quantum gates are necessary for quantum computing, as they enable the construction and implementation of any quantum algorithm. Universal quantum gates can be implemented by applying certain physical interactions or fields on the qubits. Different physical implementations of qubits have different sets of native quantum gates that can be performed easily and efficiently. However, any set of quantum gates that includes at least one single-qubit gate and one two-qubit gate is universal.

- **Efficient qubit-state measurement capability**: Measurement is the process of extracting the output data from the qubits after the computation is completed. Efficient qubit-state measurement capability is essential for quantum computing, as it determines the success and usefulness of the quantum algorithm. Measurement can be done by applying certain operations or devices on the qubits that can reveal their state, such as 0 or 1. Different physical implementations of qubits have different methods and challenges for measurement. The efficient qubit-state measurement capability should be fast, accurate, and scalable.

- **Faithful transmission of flying qubits and interconversion between stationary and “flying” qubits**: Flying qubits are qubits that can travel between different locations



### Harmonic Oscillator Quantum Computer

- A harmonic oscillator quantum computer is a proposed model of quantum computation that uses the energy eigenstates of a simple harmonic oscillator as quantum bits.
- A simple harmonic oscillator is a system that exhibits periodic motion under a restoring force that is proportional to the displacement from the equilibrium position.
- The energy eigenstates of a simple harmonic oscillator are equally spaced and can be labeled by a non-negative integer n, such that E_n = (n + 1/2)hbar omega, where hbar is the reduced Planck constant and omega is the angular frequency of the oscillator.
- A finite subset of these energy eigenstates can be used to represent quantum bits, such that |0> corresponds to the ground state (n = 0), |1> corresponds to the first excited state (n = 1), and so on.
- These quantum bits can be manipulated by applying external fields or coupling them to other oscillators, which can induce transitions between different energy levels.
- The advantages of using harmonic oscillator quantum bits are that they have long lifetimes, high scalability, and easy initialization and readout.
- The challenges of using harmonic oscillator quantum bits are that they require high precision and coherence, and that they are susceptible to noise and decoherence.
- An example of a physical realization of a harmonic oscillator quantum computer is a cavity quantum electrodynamics (QED) system, where the electromagnetic field inside a cavity acts as the harmonic oscillator and the atoms passing through the cavity act as the external fields or couplers.
- Another example of a physical realization of a harmonic oscillator quantum computer is a superconducting circuit, where the LC oscillator acts as the harmonic oscillator and the Josephson junction acts as the external field or coupler.
- A generalization of the harmonic oscillator quantum computer is the anharmonic oscillator quantum computer, where the potential of the oscillator is not quadratic but higher order, such as quartic. This allows for more flexibility and control over the energy levels and transitions of the quantum bits.



### Optical Photon Quantum Computer

- Optical photon quantum computer is a type of quantum computer that uses photons as qubits and linear optical elements as quantum gates.
- Photons are particles of light that can carry quantum information in their polarization, frequency, or spatial modes.
- Linear optical elements are devices that manipulate the properties of photons without changing their number, such as mirrors, beam splitters, phase shifters, and polarizers.
- Optical photon quantum computer can perform universal quantum computation, meaning that it can simulate any quantum algorithm or circuit.
- Optical photon quantum computer has several advantages over other types of quantum computers, such as low decoherence, high speed, easy scalability, and compatibility with existing optical communication networks .
- Optical photon quantum computer also faces several challenges, such as the difficulty of generating and detecting single photons, the probabilistic nature of linear optical gates, and the need for quantum memories and error correction .
- Optical photon quantum computer is an active area of research and development, with several recent breakthroughs and applications, such as the first photonic quantum computer on the cloud, the programmable photonic chip that can execute various quantum algorithms, and the high-performance photon detectors that can combat data theft and spies .



### Optical cavity quantum electrodynamics

- Optical cavity quantum electrodynamics (QED) is the study of the interaction between light confined in a reflective cavity and atoms or other particles, under conditions where the quantum nature of photons is significant.
- Optical cavity QED can be used to implement quantum logic gates, quantum state transfer, quantum metrology, and quantum simulation.
- The simplest model in optical cavity QED deals with a single two-level atom interacting with a single mode of the radiation field. This is known as the Jaynes-Cummings model.
- The interaction between the atom and the cavity mode can be characterized by the coupling strength g, the cavity decay rate κ, and the atomic decay rate γ. Depending on the relative values of these parameters, the system can be in different regimes of optical cavity QED:
  - Weak coupling regime: g < κ, γ. The atom and the cavity mode are weakly coupled and can be treated as independent systems.
  - Strong coupling regime: g > κ, γ. The atom and the cavity mode are strongly coupled and form hybrid states called dressed states or polaritons.
  - Ultrastrong coupling regime: g > κc, where κc is the critical cavity decay rate for the onset of the ultrastrong coupling regime. The atom and the cavity mode are so strongly coupled that the rotating wave approximation breaks down and the counter-rotating terms in the Hamiltonian become important.
  - Deep strong coupling regime: g > ω, where ω is the frequency of the cavity mode or the atomic transition. The atom and the cavity mode are so strongly coupled that the energy splitting between the dressed states exceeds the bare energies of the atom and the cavity mode.
- Optical cavity QED has allowed for a number of key experimental advances in quantum optics, including the observation of an enhancement of spontaneous emission, the demonstration of the photon blockade effect and vacuum-induced transparency, the generation of non-classical states of light and matter, and the realization of quantum feedback and measurement  .



### Ion traps for the notes of the Unit 3 - Quantum Computers in the subject of Quantum Computing

- Ion traps are devices that can confine and manipulate charged particles, such as ions, using electric and magnetic fields .
- Ion traps can be used to implement quantum computing, where qubits are stored in the electronic states of the ions and quantum gates are performed by applying laser pulses or microwave fields to the ions .
- Ion traps have several advantages for quantum computing, such as:
  - High-fidelity qubit manipulation and readout .
  - Long coherence times (up to hours) of the qubits .
  - Scalability to large numbers of qubits using modular architectures or ion shuttling techniques  .
  - Compatibility with different types of ions and ion species .
- Ion traps also face some challenges for quantum computing, such as:
  - Complexity and stability of the trapping and control systems .
  - Crosstalk and noise from the environment and the trap electrodes .
  - Heating and decoherence of the motional modes of the ions .
  - Materials issues and fabrication limitations of the trap chips .
- Several companies and research groups are working on developing trapped-ion quantum computers, such as:
  - IonQ, which claims to have the world's most powerful quantum computer with 32 fully connected qubits and a quantum volume of 4 million.
  - Honeywell, which has demonstrated a 10-qubit system with a quantum volume of 512 and plans to increase it by an order of magnitude every year.
  - Alpine Quantum Technologies, which is developing a scalable and modular trapped-ion quantum computer based on surface-electrode traps.
  - Universal Quantum, which is using microwave fields instead of lasers to manipulate the qubits and aims to build a million-qubit system.
  - NIST, which has pioneered many techniques and experiments in trapped-ion quantum computing, such as quantum error correction, quantum logic gates, quantum simulation, and quantum metrology.
  - MIT, which has developed a new type of ion trap that can trap multiple species of ions and enable quantum communication and networking.



### Nuclear Magnetic Resonance for the notes of the Unit 3 - Quantum Computers in the subject of Quantum Computing

- Nuclear magnetic resonance (NMR) is a physical phenomenon that occurs when nuclei in a magnetic field absorb and re-emit electromagnetic radiation.
- NMR can be used to study the structure, dynamics, and interactions of molecules, as well as to manipulate and measure quantum states of nuclei.
- NMR quantum computing (NMRQC) is one of the several proposed approaches for constructing a quantum computer, that uses the spin states of nuclei within molecules as qubits.
- Qubits are the basic units of quantum information, that can exist in superpositions of two classical states, usually denoted as |0> and |1>.
- NMRQC relies on the fact that nuclei have a property called spin, which makes them behave like tiny magnets. When placed in a strong external magnetic field, the nuclei can align with or against the field, corresponding to |0> or |1> states.
- The nuclei can also be manipulated by applying radiofrequency pulses, which can change their spin states or create entanglement between them. Entanglement is a quantum phenomenon that allows two or more qubits to share a quantum state, such that measuring one affects the others.
- The quantum states of the nuclei can be probed by measuring the NMR signals, which depend on the frequency and intensity of the radiofrequency pulses, as well as the interactions between the nuclei and their environment.
- NMRQC has several advantages, such as being relatively easy to implement with existing technology, being robust to decoherence (the loss of quantum coherence due to noise), and being scalable to large numbers of qubits.
- NMRQC also has some limitations, such as requiring high purity and homogeneity of the samples, being sensitive to temperature and magnetic field fluctuations, and having a low signal-to-noise ratio.
- NMRQC has been used to demonstrate some basic quantum algorithms, such as Deutsch-Jozsa, Grover's, and Shor's algorithms, as well as to simulate quantum systems, such as the hydrogen molecule and the Ising model.
- NMRQC is also being explored for applications in quantum chemistry, quantum metrology, quantum machine learning, and quantum cryptography.



## Unit 4 - Quantum Information

- Quantum information is the information of the state of a quantum system. It is the basic entity of study in quantum information theory, and can be manipulated using quantum information processing techniques.
- Quantum information refers to both the technical definition in terms of Von Neumann entropy and the general computational term.
- Quantum information, like classical information, can be processed using digital computers, transmitted from one location to another, manipulated with algorithms, and analyzed with computer science and mathematics.
- Just like the basic unit of classical information is the bit, quantum information deals with qubits. A qubit is a two-state quantum system that can exist in a superposition of both states simultaneously.
- Quantum information science aims to explore the nature of information at the quantum level, a world in which bits can be both zero and one at the same time and perfect copying is impossible.
- At the practical level, quantum information powers forms of secure communication that are provably impossible in a “classical” world. For example, quantum cryptography uses quantum properties to ensure the security of key distribution and encryption.
- Quantum information science also investigates the potential of quantum computers, which could solve problems intractable with classical computers. For example, quantum algorithms could factor large numbers faster than classical algorithms, which has implications for cryptography and number theory.
- Quantum information science research at NIST explores ways to employ phenomena exclusive to the quantum world to measure, encode and process information for useful purposes. For example, NIST develops quantum standards, metrology, and sensors, as well as quantum devices and systems.



### Quantum noise and Quantum Operations

- Quantum noise is the uncertainty or randomness that arises from the quantum nature of physical systems, such as qubits, photons, electrons, etc. 
- Quantum noise can affect the performance and accuracy of quantum computers, which exploit quantum phenomena to perform computations that are otherwise impossible or intractable for classical computers.  
- Quantum noise can be caused by various factors, such as imperfect control signals, interference from the environment, and unwanted interactions between qubits.  
- Quantum noise can lead to quantum decoherence, which is the loss of quantum coherence or superposition of qubits, resulting in a loss of quantum information or computational power. 
- Quantum operations are mathematical transformations that describe how quantum systems evolve under the influence of noise, measurement, or manipulation. 
- Quantum operations are also called quantum channels, quantum maps, or superoperators. They are generalizations of unitary operators, which describe the ideal evolution of quantum systems in the absence of noise or measurement. 
- Quantum operations must satisfy certain properties, such as linearity, complete positivity, and trace preservation, to ensure that they are physically realizable and preserve the probabilistic interpretation of quantum states. 
- Quantum operations can be represented in different ways, such as Kraus operators, Choi matrices, Stinespring dilation, or process matrices. These representations are useful for different purposes, such as analyzing the effects of noise, designing quantum error correction codes, or verifying quantum protocols.



### Classical Noise and Markov Processes for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing

- Classical noise is a random fluctuation or disturbance in a signal or a system that affects the quality or accuracy of the information transmitted or processed.
- Markov processes are stochastic processes that have the property of memorylessness, meaning that the future state of the system depends only on the present state and not on the past history.
- In quantum information theory, classical noise and Markov processes are used to model the effects of decoherence, dissipation, and errors on quantum systems that interact with their environment.
- Quantum noise is the quantum analogue of classical noise, where the fluctuations or disturbances are due to the inherent uncertainty and indeterminacy of quantum mechanics.
- Quantum operations are mathematical transformations that describe how quantum systems evolve under the influence of quantum noise and external control.
- Quantum operations formalism is a framework that allows one to characterize and manipulate quantum systems in terms of their input and output states, as well as their effects on the environment.
- Quantum operations formalism can be derived from the following assumptions:
  - The input and output states of the quantum system are represented by density operators, which are positive, Hermitian, and trace-one matrices.
  - The quantum operation is a completely positive and trace-preserving (CPTP) map, which means that it preserves the positivity and the trace of the density operator, and that it can be extended to a larger system without introducing negative probabilities.
  - The quantum operation can be expressed as a linear combination of Kraus operators, which are matrices that satisfy the completeness relation, meaning that their sum is equal to the identity matrix.
  - The quantum operation can also be expressed as a unitary transformation on a larger system that includes an ancilla, which is an auxiliary quantum system that acts as the environment or the noise source.
- A quantum channel is a special case of a quantum operation that describes the transmission of quantum information from a sender to a receiver through a noisy medium.
- A quantum channel is also a CPTP map, but it has the additional property of being linear and additive, meaning that it preserves the superposition and the tensor product of quantum states.
- A quantum channel can be characterized by its capacity, which is the maximum amount of information that can be reliably transmitted per use of the channel.
- There are different types of capacities for quantum channels, depending on the nature and the encoding of the information, such as the classical capacity, the quantum capacity, the private capacity, and the entanglement-assisted capacity.
- The classical capacity of a quantum channel is the maximum amount of classical information that can be reliably transmitted per use of the channel, using quantum states as the carriers of the information.
- The classical capacity of a quantum channel can be affected by the presence of correlations or memory in the noise, which can either enhance or degrade the transmission rate.
- A Markovian quantum channel is a quantum channel that has no memory, meaning that the noise affecting the quantum states is independent and identically distributed (i.i.d.) for each use of the channel.
- A non-Markovian quantum channel is a quantum channel that has memory, meaning that the noise affecting the quantum states is dependent and non-identically distributed for each use of the channel.
- A Markovian quantum channel can be modeled by a Markov chain, which is a sequence of random variables that satisfy the Markov property, meaning that the next state of the chain depends only on the current state and not on the previous states.
- A Markov chain can be described by a transition matrix, which is a matrix that specifies the probabilities of transitioning from one state to another in the chain.
- A Markov chain can have different properties, such as being irreducible, aperiodic, recurrent, transient, ergodic, or stationary, depending on the structure and the behavior of the transition matrix.
- A Markov chain can also have different classes, such as communicating classes, closed classes, absorbing classes, or essential classes, depending on the accessibility and the persistence of the states in the chain.
- The classical capacity of a Markovian quantum channel can be evaluated by using the Holevo-Schumacher-Westmoreland (HSW) theorem, which states that the capacity is equal to the maximum of the Holevo quantity over all possible input ensembles, where the Holevo quantity is a measure of the mutual information between the input and the output states of the channel.
- The classical capacity of a non-Markovian quantum channel can be evaluated by using the memory-assisted H



### Quantum Operations

- Quantum operations are mathematical transformations that describe how a quantum system can evolve or change over time. They are also used to manipulate quantum bits (qubits) in a quantum circuit.  
- Quantum operations are formulated in terms of the density operator, which is a matrix that represents the state of a quantum system. A density operator can be written as a weighted sum of pure states, which are vectors that describe the possible outcomes of a quantum measurement. 
- A quantum operation is a linear, completely positive map from the set of density operators into itself. This means that a quantum operation preserves the properties of being a density operator, such as being positive, trace one, and Hermitian. 
- A quantum operation can be represented by a unitary matrix, which is a matrix that preserves the length and angle of vectors. A unitary matrix can be decomposed into a product of quantum gates, which are elementary quantum operations that act on one or more qubits. Examples of quantum gates are the Pauli-X, Y, and Z gates, the Hadamard gate, the CNOT gate, and the Toffoli gate.  
- A quantum operation can also be represented by a Kraus decomposition, which is a set of operators that satisfy a certain condition. A Kraus decomposition can be used to model quantum noise, decoherence, and measurement. A Kraus decomposition can be converted into a unitary matrix by adding an ancillary system. 
- A quantum operation can also be represented by a quantum circuit, which is a graphical notation that shows the sequence of quantum gates and measurements applied to a quantum system. A quantum circuit can be used to implement quantum algorithms, which are computational procedures that solve problems using quantum principles. Examples of quantum algorithms are Shor's algorithm, Grover's algorithm, and quantum Fourier transform.



### Examples of Quantum noise and Quantum Operations

- Quantum noise is the uncertainty or randomness that arises from the quantum nature of physical systems, such as qubits, photons, electrons, etc. 
- Quantum noise can affect the performance and accuracy of quantum computers, as it can cause errors, decoherence, and loss of information.  
- Quantum operations are the mathematical descriptions of how quantum systems evolve under the influence of external factors, such as measurements, interactions, or noise. 
- Quantum operations can be represented by matrices, such as unitary operators, Kraus operators, or superoperators, that act on the quantum states of the system. 
- Some examples of quantum operations are:
  - Quantum gates: These are the basic building blocks of quantum circuits, which are sequences of quantum operations that perform quantum computations. Quantum gates are unitary operators that manipulate one or more qubits, such as the Hadamard gate, the Pauli-X gate, or the CNOT gate. 
  - Quantum measurements: These are the processes of extracting information from a quantum system, such as the state or the outcome of a computation. Quantum measurements are non-unitary operators that collapse the quantum state into one of the possible outcomes, with some probability. For example, measuring a qubit in the computational basis can yield either 0 or 1, with some probability depending on the state of the qubit. 
  - Quantum noise: These are the effects of the environment or the imperfections of the quantum devices on the quantum system, such as decoherence, relaxation, or dephasing. Quantum noise can be modeled by Kraus operators or superoperators, which describe how the quantum state is transformed by the noise. For example, a bit-flip channel can flip a qubit from 0 to 1 or vice versa, with some probability.



### Applications of Quantum Operations

Quantum operations are mathematical transformations that describe how quantum systems evolve over time. They are also known as quantum gates or quantum circuits. Quantum operations can be used to manipulate quantum information, such as qubits, which are the basic units of quantum computing. Quantum operations can also be used to implement quantum algorithms, which are computational procedures that exploit quantum phenomena, such as superposition and entanglement, to solve problems that are hard or impossible for classical computers.

Some of the applications of quantum operations are:

- **Quantum chemistry**: Quantum operations can be used to simulate the behavior of molecules and materials at the quantum level, which can lead to new discoveries in fields such as drug design, catalysis, and renewable energy .
- **Quantum cryptography**: Quantum operations can be used to create and distribute secure keys for encryption and decryption, which can protect information from eavesdropping and hacking. Quantum operations can also be used to verify the authenticity and integrity of data and messages.
- **Quantum machine learning**: Quantum operations can be used to enhance the performance and efficiency of machine learning algorithms, such as classification, clustering, and optimization, by using quantum resources, such as parallelism, interference, and entanglement.
- **Quantum optimization**: Quantum operations can be used to find the optimal solutions for complex and combinatorial problems, such as scheduling, routing, and resource allocation, which are often NP-hard for classical computers.
- **Quantum metrology**: Quantum operations can be used to improve the precision and accuracy of measurements and sensors, such as clocks, thermometers, and magnetometers, by using quantum states that are sensitive to external parameters, such as time, temperature, and magnetic field.

These are some of the applications of quantum operations that are currently being explored and developed by researchers and practitioners in various domains. Quantum operations have the potential to revolutionize many fields and industries by providing new capabilities and advantages that are beyond the reach of classical computing.



### Limitations of the Quantum Operations Formalism

- The quantum operations formalism is a mathematical framework for describing the dynamics of open quantum systems, i.e., quantum systems that interact with their environment.
- The formalism assumes that the system and the environment are initially uncorrelated, and that the interaction is weak and Markovian, i.e., memoryless.
- The formalism also assumes that the system can be prepared and measured in a fixed basis, and that the environment does not affect the preparation and measurement devices.
- These assumptions are often violated in realistic scenarios, such as when the system and the environment have strong or non-Markovian interactions, or when the system is subject to feedback or adaptive control.
- In such cases, the quantum operations formalism may fail to capture the essential features of the quantum dynamics, and may lead to incorrect or incomplete predictions.
- Some of the limitations of the quantum operations formalism are:

  - It does not account for the back-action of the measurement on the system, which may induce non-unitary or non-linear effects.
  - It does not account for the entanglement between the system and the environment, which may lead to decoherence or information loss.
  - It does not account for the contextuality or non-locality of quantum measurements, which may depend on the choice of the measurement basis or the spatial arrangement of the devices.
  - It does not account for the quantum-to-classical transition, which may involve irreversibility or randomness.
  - It does not account for the quantum Zeno effect, which may suppress or enhance the quantum dynamics by frequent measurements.
  - It does not account for the quantum speed limit, which may constrain the rate of change of the quantum state.

- Some of the possible ways to overcome or generalize the quantum operations formalism are:

  - Using quantum process tomography, which is a technique for reconstructing the quantum operation from experimental data.
  - Using quantum trajectories, which are stochastic descriptions of the quantum dynamics conditioned on the measurement outcomes.
  - Using quantum feedback control, which is a technique for manipulating the quantum dynamics by applying external fields or measurements based on the system state.
  - Using quantum causal models, which are graphical representations of the causal relations between quantum variables.
  - Using quantum information theory, which is a framework for quantifying and manipulating the information content of quantum systems.



### Distance Measures for Quantum Information

- A distance measure quantifies the extent to which two quantum states behave in the same way .
- A distance measure is related to the problem of distinguishing two systems, i.e., how well one can tell apart two quantum states by performing measurements .
- A distance measure is represented by a two-argument function d: S(H) x S(H) -> R, where S(H) is the set of density matrices on a Hilbert space H and R is the set of real numbers.
- A distance measure usually satisfies the following properties:
  - Positivity: d(ρ, σ) ≥ 0 with equality if and only if ρ = σ
  - Symmetry: d(ρ, σ) = d(σ, ρ)
  - Triangle inequality: d(ρ, τ) ≤ d(ρ, σ) + d(σ, τ)
  - Contractivity: d(E(ρ), E(σ)) ≤ d(ρ, σ) for any quantum operation E
- A distance measure that satisfies the above properties is called a metric.
- Some examples of distance measures for quantum information are   :
  - Trace distance: d_T(ρ, σ) = (1/2) tr|ρ - σ|, where |X| = (X^†X)^1/2 is the absolute value of X
  - Fidelity: F(ρ, σ) = tr(ρ^1/2σρ^1/2)^1/2
  - Quantum relative entropy: S(ρ||σ) = tr(ρ log ρ - ρ log σ)
  - Bures distance: d_B(ρ, σ) = 2(1 - F(ρ, σ))
  - Quantum Jensen-Shannon divergence: J(ρ||σ) = (1/2) S(ρ||(ρ + σ)/2) + (1/2) S(σ||(ρ + σ)/2)
- Different distance measures have different operational meanings and applications in quantum information theory, such as quantum state estimation, quantum hypothesis testing, quantum error correction, quantum cryptography, etc  .



## Unit 5 - Quantum Error Correction

- Quantum error correction (QEC) is a set of methods to protect quantum information—that is, quantum states—from unwanted environmental interactions (decoherence) and other forms of noise .
- Quantum information is stored in a quantum error-correcting code, which is a subspace in a larger Hilbert space. The code is designed to detect and correct errors that affect a subset of the physical qubits that encode the logical qubits .
- Quantum error correction is essential to achieve fault tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum measurements, and faulty classical processing .
- Quantum error correction is used to protect information in quantum communication (where quantum states pass through noisy channels) and quantum computation (where quantum states are transformed through a sequence of imperfect computational steps in the presence of environmental decoherence to solve a computational problem).
- Quantum error correction protocols will play a central role in the realisation of quantum computing; the choice of error correction code will influence the full quantum computing stack, from the layout of qubits at the physical level to gate compilation strategies at the software level.
- A long quantum computation will require many cycles of quantum error correction (QEC). Each cycle would consist of gates acting on encoded qubits (performing the computation), followed by syndrome measurements from which errors can be inferred, and corrections.
- Quantum error correction is based on the principles of quantum information theory, such as entanglement, superposition, and measurement. Quantum error correction codes are often derived from classical error correction codes, such as Hamming codes, Reed-Muller codes, and Reed-Solomon codes, by using quantum encoding and decoding circuits .
- Quantum error correction codes can be classified into different types, such as stabilizer codes, CSS codes, topological codes, surface codes, and quantum LDPC codes. Each type of code has different properties, such as the number of qubits required, the error threshold, the distance, the rate, and the complexity of the encoding and decoding circuits .
- Quantum error correction is an active area of research, with many open challenges and opportunities, such as finding optimal codes for different noise models, developing efficient decoding algorithms, implementing fault tolerant quantum gates, and demonstrating scalable quantum error correction on physical devices  .



### Introduction for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from noise and decoherence, which are inevitable sources of error in quantum systems.
- QEC is based on the idea of encoding a logical quantum state into a larger physical system, such that errors can be detected and corrected without disturbing the logical state.
- QEC is essential for the development of scalable and reliable quantum computing and communication, as well as for the study of fundamental aspects of quantum physics.
- QEC is a generalization of classical error correction, which uses redundancy and parity checks to correct bit-flip and phase-flip errors in classical information.
- QEC requires the use of quantum entanglement and quantum measurement, which introduce new challenges and possibilities for error correction.
- QEC can be implemented using various physical platforms, such as superconducting qubits, trapped ions, photonic qubits, etc.
- QEC can be classified into different types, such as active and passive QEC, stabilizer codes, topological codes, etc.
- QEC can also be combined with other techniques, such as quantum fault tolerance, quantum error mitigation, quantum error avoidance, etc.



### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from errors due to noise, decoherence, or other sources of error.
- QEC codes are based on encoding a logical qubit (the unit of quantum information) into a larger number of physical qubits, such that errors can be detected and corrected without disturbing the logical qubit.
- Shor code is one of the first and simplest QEC codes, proposed by Peter Shor in 1995  . It encodes one logical qubit into nine physical qubits, and can correct any single-qubit error (bit-flip, phase-flip, or both).
- Shor code works by first transferring the state of the logical qubit to three physical qubits using CNOT gates, then applying Hadamard gates to each of the three qubits to create a superposition of states. This process is repeated three times to obtain nine physical qubits in a highly entangled state.
- To detect and correct errors, Shor code uses syndrome measurements, which are multi-qubit measurements that do not disturb the logical qubit but reveal information about the error. The syndrome measurements consist of four parity checks: two for bit-flip errors and two for phase-flip errors.
- The parity checks are performed by applying CNOT gates between pairs of physical qubits and measuring the ancillary qubits. Depending on the outcome of the measurements, the error can be located and corrected by applying appropriate gates to the affected qubit.
- Shor code can also be generalized to encode more than one logical qubit, or to correct more than one error, by using larger blocks of physical qubits and more complex syndrome measurements. These codes are known as Bacon-Shor codes.
- Shor code and its variants are examples of stabilizer codes, which are a class of QEC codes that are defined by a set of operators that commute with the logical qubits and have eigenvalues of +1 or -1. The syndrome measurements are equivalent to measuring the eigenvalues of the stabilizer operators.
- Shor code can be implemented on a quantum computer using quantum circuits, such as the ones shown in the following figure:

Shor code circuit

- The left circuit shows the encoding of the logical qubit into nine physical qubits, the middle circuit shows the syndrome measurement for bit-flip errors, and the right circuit shows the syndrome measurement for phase-flip errors. The correction gates are not shown, but they can be inferred from the measurement outcomes.



### Theory of Quantum Error –Correction

- Quantum error correction is the process of detecting and correcting errors that occur in quantum systems due to noise or decoherence.
- Quantum error correction is essential for achieving fault-tolerant quantum computing, which can perform reliable and scalable quantum algorithms.
- Quantum error correction is based on the principle of encoding quantum information in a larger Hilbert space, such that errors can be identified and corrected without disturbing the logical state.
- Quantum error correction codes are designed to correct a specific set of errors, such as bit-flip, phase-flip, or depolarizing errors, that can be modeled by the Pauli operators.
- Quantum error correction codes can be classified into different types, such as stabilizer codes, CSS codes, topological codes, or surface codes, depending on their structure and properties.
- Quantum error correction codes can be characterized by their parameters, such as the number of physical qubits, the number of logical qubits, the distance, the rate, and the threshold.
- Quantum error correction codes can be implemented by using quantum circuits that consist of encoding, syndrome measurement, and recovery operations.
- Quantum error correction codes can be analyzed by using mathematical tools, such as the stabilizer formalism, the quantum Hamming bound, the quantum Singleton bound, or the Knill-Laflamme condition.



### Constructing Quantum Codes

- Quantum codes are methods of encoding quantum information (qubits) in such a way that errors due to noise or decoherence can be detected and corrected without disturbing the encoded state.
- Quantum codes can be classified into two main types: quantum block codes and quantum convolutional codes.
- Quantum block codes encode a fixed number of qubits into a larger number of qubits using a unitary transformation. The encoded qubits form a subspace of the Hilbert space that is invariant under certain error operators. The error operators can be detected and corrected by measuring some observables that commute with the encoded state, called stabilizers.
- Quantum convolutional codes encode a stream of qubits into another stream of qubits using a repeated unitary transformation that has a memory structure. The encoded qubits form a subspace of the Hilbert space that is invariant under certain error operators that act on a sliding window of qubits. The error operators can be detected and corrected by measuring some observables that commute with the encoded state, called check operators.
- Quantum codes can be constructed from classical codes using various techniques, such as the Calderbank-Shor-Steane (CSS) construction, the Gottesman-Knill theorem, the stabilizer formalism, and the quantum Fourier transform  .
- Quantum codes can also be constructed from entanglement properties, such as the Schmidt decomposition, the entanglement spectrum, and the entanglement entropy.
- Quantum codes can be evaluated by their parameters, such as the code length, the code dimension, the code distance, the code rate, the code threshold, and the code performance  .
- Quantum codes can be applied to various tasks, such as quantum communication, quantum computation, quantum cryptography, quantum metrology, and quantum simulation   .



### Stabilizer codes

- Stabilizer codes are a class of quantum error-correcting codes that use the stabilizer formalism to encode and decode quantum states .
- Stabilizer codes append ancilla qubits to the qubits that need to be protected from noise and errors. A unitary encoding circuit rotates the global state into a subspace of a larger Hilbert space. This highly entangled, encoded state corrects for local noisy errors .
- Stabilizer codes can be constructed from classical binary or quaternary codes, as long as they satisfy the dual-containing or self-orthogonality constraint. This means that the code space is orthogonal to its dual space under the symplectic inner product  .
- Stabilizer codes can be represented by a stabilizer group, which is a subgroup of the Pauli group that commutes with all its elements and contains the identity. The stabilizer group specifies the set of errors that can be detected and corrected by the code  .
- Stabilizer codes can also be described by a parity check matrix, which is a matrix whose rows are the binary or quaternary representations of the generators of the stabilizer group. The parity check matrix can be used to encode, decode, and perform fault-tolerant operations on the code .
- Stabilizer codes can be generalized to qudit stabilizer codes, which use qudits (d-level quantum systems) instead of qubits. Qudit stabilizer codes can achieve better error correction capability than qubit stabilizer codes, especially when using preshared entanglement.



### Fault – Tolerant Quantum Computation

- Fault-tolerant quantum computation is the ability to perform quantum operations on encoded quantum states without compromising the protection against errors provided by quantum error correction schemes .
- Fault-tolerance is essential for scalable quantum computation, as physical qubits are prone to errors due to noise, decoherence, and imperfect control .
- The quantum threshold theorem states that a quantum computer with a physical error rate below a certain threshold can suppress the logical error rate to arbitrarily low levels by applying quantum error correction schemes.
- The threshold depends on the details of the quantum error correction scheme, the noise model, and the architecture of the quantum computer.
- Fault-tolerant quantum computation requires the following elements :
  - A quantum error-correcting code that can correct any error affecting a small fraction of qubits in the code block.
  - A method to encode and decode the logical qubits using physical qubits.
  - A set of fault-tolerant logical gates that can implement any quantum operation on the encoded qubits without introducing errors.
  - A method to measure the logical qubits and perform error correction and syndrome extraction without disturbing the encoded information.
  - A method to initialize and reset the physical qubits to a known state.
- Fault-tolerant quantum computation can be achieved by various methods, such as  :
  - Using ancillary qubits and gadgets to protect gates against correlated faults.
  - Using topological quantum codes and anyonic excitations to perform operations by braiding and fusing the anyons.
  - Using concatenated quantum codes and transversal or teleportation-based gates to implement operations on different levels of encoding.



### Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system .
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as

$$
H(X) = -\sum_{x} p(x) \log p(x)
$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- Shannon entropy satisfies some desirable properties, such as being non-negative, being maximal for a uniform distribution, being additive for independent variables, and being invariant under permutations.
- Shannon entropy also has an operational interpretation as the optimal compression rate of a message source, i.e., the minimum number of bits per symbol needed to encode the source without loss of information.
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$ .
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as

$$
S(\rho) = -\text{Tr}(\rho \log \rho)
$$

where $\text{Tr}$ denotes the trace operation .
- Von Neumann entropy satisfies some properties analogous to Shannon entropy, such as being non-negative, being maximal for a maximally mixed state, being additive for uncorrelated systems, and being invariant under unitary transformations .
- Von Neumann entropy also has an operational interpretation as the optimal compression rate of a quantum source, i.e., the minimum number of qubits per quantum state needed to encode the source without loss of quantum information .
- However, von Neumann entropy also has some features that are distinct from Shannon entropy, such as being subadditive for correlated systems, being non-increasing under quantum operations, and being related to the entanglement of quantum states .
- Entanglement is a quantum phenomenon that allows two or more systems to share quantum correlations that cannot be explained by classical physics .
- Entanglement is a valuable resource for quantum information processing, such as quantum cryptography, quantum teleportation, and quantum computation .
- A measure of entanglement for pure bipartite quantum states is the entanglement entropy, defined as the von Neumann entropy of the reduced density matrix of either subsystem, i.e.,

$$
E(\rho_{AB}) = S(\rho_A) = S(\rho_B)
$$

where $\rho_{AB}$ is the pure state of the composite system $AB$, and $\rho_A$ and $\rho_B$ are the reduced states of the subsystems $A$ and $B$, obtained by tracing out the other subsystem .
- Entanglement entropy quantifies the amount of information that is inaccessible to local measurements on either subsystem, and that can only be revealed by global measurements on the composite system .
- A measure of entanglement for mixed bipartite quantum states is the entanglement of formation, defined as the minimum average entanglement entropy of a pure state decomposition of the mixed state, i.e.,

$$
E_F(\rho_{AB}) = \min_{\{p_i, \psi_i\}} \sum_i p_i E(\psi_i)
$$

where $\rho_{AB} = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ is an ensemble of pure states $|\psi_i\rangle$ with probabilities $p_i$ .
- Entanglement of formation quantifies the amount of entanglement that is needed to create the mixed state from a product state by local operations and classical communication .
- Entropy and entanglement are important concepts for quantum error correction, which is the process of protecting quantum information from noise and decoherence .
- Quantum error correction relies on encoding quantum information in entangled states that span a larger Hilbert space, and using redundancy and syndrome



### Shannon Entropy

- Shannon entropy is a measure of the uncertainty and the information content in the state of a physical system .
- It is defined as the average rate at which information is produced by a stochastic source of data .
- For a discrete random variable X with possible values x1, x2, ..., xn and probabilities p1, p2, ..., pn, the Shannon entropy is given by:

$$
H(X) = -\sum_{i=1}^n p_i \log_2 p_i
$$

- For a continuous random variable X with probability density function f(x), the Shannon entropy is given by:

$$
H(X) = -\int_{-\infty}^{\infty} f(x) \log_2 f(x) dx
$$

- The higher the Shannon entropy, the more random and unpredictable the system is, and the more information is given by a new value in the process .
- The lower the Shannon entropy, the more deterministic and predictable the system is, and the less information is given by a new value in the process .
- The Shannon entropy can be used to quantify the compressibility of a message stream, as it gives the minimum number of bits needed to encode the information in the stream.
- The Shannon entropy can also be used to measure the complexity and diversity of a system, as it gives the number of possible states or configurations that the system can have.

### Shannon Entropy in Quantum Computing

- In quantum computing, the Shannon entropy can be generalized to the von Neumann entropy, which measures the uncertainty and the information content in the state of a quantum system .
- The von Neumann entropy is defined as the Shannon entropy of the eigenvalues of the density matrix that describes the quantum system .
- For a quantum system with density matrix $\rho$, the von Neumann entropy is given by:

$$
S(\rho) = -\text{Tr}(\rho \log_2 \rho)
$$

- The von Neumann entropy can be used to quantify the compressibility of a quantum state, as it gives the minimum number of qubits needed to encode the information in the state .
- The von Neumann entropy can also be used to measure the entanglement of a quantum state, as it gives the amount of quantum correlations between the subsystems of the state .
- The von Neumann entropy can be controlled by quantum control methods, which can drive the quantum state to any target state by manipulating the probability density function of the system.
- The von Neumann entropy can be affected by quantum errors, which can increase the entropy and reduce the information and coherence of the quantum state.



### Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the intrinsic dispersion, uncertainty, or lack of information of a quantum state.
- Entropy is also related to the amount of chaos or disorder in a quantum system, and it is a measurable quantity in equilibrium.
- The most common entropy measure in quantum mechanics is the von Neumann entropy, which is defined as $S(\rho) = -\text{Tr}(\rho \log \rho)$, where $\rho$ is the density matrix of the quantum state.
- The von Neumann entropy satisfies some basic properties, such as non-negativity, concavity, additivity, subadditivity, and strong subadditivity.
- The von Neumann entropy can be interpreted as the average amount of information needed to specify the quantum state, or the optimal compression rate of quantum data.
- The von Neumann entropy can also be used to quantify the entanglement of quantum states, which is a key resource for quantum information processing and quantum error correction.
- Another important entropy measure in quantum information theory is the conditional entropy, which is defined as $S(A|B) = S(AB) - S(B)$, where $A$ and $B$ are quantum subsystems.
- The conditional entropy can be negative, which indicates the presence of quantum correlations between $A$ and $B$.
- The conditional entropy can be used to characterize the quantum discord, which is a measure of the quantumness of correlations beyond entanglement.
- The conditional entropy can also be used to compute the quantum capacity of a noisy quantum channel, which is the maximum rate of reliable quantum communication over the channel.



### Von Neumann quantum error correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- QEC is theorised as essential to achieve fault tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum measurements, and faulty quantum preparation.
- The problem of noise occurring in classical computation was considered by von Neumann in the 1950s.
- Von Neumann proposed a method of error correction using redundancy, where each bit of information is encoded into multiple bits, and a majority vote is used to correct errors.
- However, this method does not work for quantum information, because quantum states cannot be copied or measured without disturbing them, due to the no-cloning theorem and the measurement postulate.
- Therefore, QEC requires a different approach, where quantum information is encoded into entangled states of multiple qubits, and non-destructive measurements are performed on error syndromes, which are combinations of qubits that reveal the type and location of errors without revealing the encoded information .
- QEC schemes can be classified into two types: discrete and continuous .
- Discrete QEC schemes use projective von Neumann measurements on stabilizers to discretize the error syndromes into a finite set, and fast unitary gates are applied to recover the corrupted information .
- Continuous QEC schemes use weak measurements or homodyne detection to estimate the error syndromes continuously, and feedback control is applied to correct the errors in real time .
- QEC schemes can also be classified into two types: active and passive.
- Active QEC schemes require periodic measurements and corrections to maintain the encoded information.
- Passive QEC schemes use error-detecting codes or decoherence-free subspaces to avoid measurements and corrections, but they are more limited in the types of errors they can correct.



### Strong Subadditivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) of quantum entropy is a fundamental property of quantum information theory that relates the von Neumann entropies of different subsystems of a larger quantum system .
- SSA states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{AB}) + S(\rho_{BC}) \leq S(\rho_{ABC}) + S(\rho_B)
$$

where $S(\rho) = -\text{Tr}(\rho \log \rho)$ is the von Neumann entropy of a quantum state $\rho$.

- SSA implies that the mutual information between two subsystems cannot increase by adding a third subsystem, i.e.,

$$
I(A:B) \geq I(A:BC)
$$

where $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ is the quantum mutual information between subsystems $A$ and $B$.

- SSA also implies that the conditional entropy of a subsystem given another subsystem is always non-positive, i.e.,

$$
S(A|B) \leq 0
$$

where $S(A|B) = S(\rho_{AB}) - S(\rho_B)$ is the quantum conditional entropy of subsystem $A$ given subsystem $B$.

- SSA has many applications in quantum information theory, such as proving the Holevo bound, the quantum Fano inequality, the quantum data processing inequality, the quantum strong converse theorem, the quantum state merging protocol, and the quantum reverse Shannon theorem .



### Data Compression for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Data compression is the process of reducing the amount of information needed to store or transmit data.
- Quantum data compression is the quantum analogue of data compression, where quantum information contained in a set of quantum bits (qubits) is reduced to a smaller set of qubits, without losing any information.
- Quantum data compression is possible because of the quantum no-cloning theorem, which states that an unknown quantum state cannot be copied exactly. Therefore, there may be some redundancy in the quantum data that can be eliminated by compression.
- Quantum data compression can be divided into two types: lossless and lossy. Lossless quantum data compression preserves the exact quantum information, while lossy quantum data compression allows some distortion or error in the quantum information.
- Lossless quantum data compression can be achieved by using quantum error correction codes, which encode a logical qubit into a larger number of physical qubits, and then compress the physical qubits into a smaller number of logical qubits. For example, a three-qubit repetition code can encode a logical qubit into three physical qubits, and then compress the three physical qubits into one logical qubit, if the three physical qubits are in the same state.
- Lossy quantum data compression can be achieved by using quantum state merging, which is a protocol that allows two parties to compress their joint quantum state into a smaller quantum state, by sending some qubits from one party to another. For example, a quantum state merging protocol can compress three identical qubits into two qubits, by sending one qubit from one party to another.
- Quantum data compression has applications in quantum communication, quantum cryptography, quantum machine learning, and quantum metrology. Quantum data compression can reduce the cost and complexity of quantum communication, enhance the security and efficiency of quantum cryptography, improve the accuracy and scalability of quantum machine learning, and increase the precision and sensitivity of quantum metrology  .



### Entanglement as a physical resource

- Quantum entanglement is a physical resource, like energy, associated with the peculiar nonclassical correlations that are possible between separated quantum systems.
- Entanglement can be measured, transformed, and purified.
- Entanglement enables tasks such as quantum cryptography, superdense coding, and teleportation.
- Entanglement improves the processing speed of quantum computers, as changing the state of an entangled qubit will change the state of the paired qubit immediately.
- Entanglement is also essential for quantum error correction, as it allows for detecting and correcting errors in quantum information without destroying the quantum coherence.
- The utility of a quantum state for quantum computing and communication is often directly related to the degree or type of entanglement present in the state.
- Therefore, efficiently quantifying and characterizing multipartite entanglement is of great importance for quantum information science.
- One way to create entangled states is by using quantum gates, such as the controlled-NOT (CNOT) gate, which flips the target qubit depending on the state of the control qubit.
- Another way to create entangled states is by using measurements, such as the Bell state measurement, which projects two qubits into one of the four maximally entangled Bell states.
- Entangled states can be verified by using entanglement witnesses, which are operators that have negative expectation values only for entangled states.
- Entangled states can also be verified by using entanglement criteria, such as the Peres-Horodecki criterion, which states that a state is entangled if and only if its partial transpose is not positive semidefinite.

