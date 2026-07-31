### Strong Subadditivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) is a property of the von Neumann entropy of quantum systems that relates the entropies of different subsystems of a larger system .
- SSA states that for any tripartite quantum system ABC, the following inequality holds :

$$
S(AB) + S(BC) \geq S(B) + S(ABC)
$$

where $S(X)$ denotes the von Neumann entropy of the subsystem X.

- SSA implies that the mutual information between two subsystems cannot increase by adding a third subsystem:

$$
I(A:C) \geq I(A:BC)
$$

where $I(X:Y) = S(X) + S(Y) - S(XY)$ denotes the mutual information between X and Y.

- SSA is a basic theorem in quantum information theory and has many applications and consequences, such as the quantum data processing inequality, the quantum Fannes-Audenaert inequality, the quantum conditional entropy bound, the quantum Markov chain condition, the quantum state merging protocol, and the quantum strong subadditivity chain rule .
- SSA can be proved using various methods, such as the operator convexity of the quantum relative entropy, the monotonicity of the quantum relative entropy under quantum channels, the concavity of the quantum entropy power, and the qudit-portrait method .
- SSA can be generalized to multipartite quantum systems with more than three subsystems, and to quantum systems with continuous variables.