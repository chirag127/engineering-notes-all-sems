### Strong Sub Additivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) of quantum entropy is a fundamental inequality that relates the von Neumann entropies of different subsystems of a quantum state.
- SSA states that for any tripartite quantum state \\rho _ {ABC} on a Hilbert space \\mathcal { {H}}_ {ABC}=\\mathcal { {H}}_A\\otimes \\mathcal { {H}}_B\\otimes \\mathcal { {H}}_C, the following holds:

\\begin {aligned} S (A,B,C) + S (B) \\le S (A,B) + S (B,C), \\end {aligned}

where S (X) = -\\text {Tr}\\left ( \\rho _ {X} \\log \\rho _ {X} \\right) is the von Neumann entropy of the reduced state \\rho _ {X} obtained by tracing out the other subsystems.

- SSA implies the positivity of the conditional mutual information, defined as:

\\begin {aligned} I (A:C\\vert B) = S (A,B) + S (B,C) - S (A,B,C) - S (B) \\ge 0, \\end {aligned}

which measures the amount of correlation between A and C given the knowledge of B.

- SSA has many applications in quantum information theory, such as:

  - Quantum data processing inequality: SSA implies that the conditional mutual information cannot increase under local quantum operations and classical communication (LOCC), i.e.,

  \\begin {aligned} I (A:C\\vert B) \\ge I (A':C'\\vert B'), \\end {aligned}

  where \\rho _ {A'B'C'} is obtained from \\rho _ {ABC} by some LOCC protocol.

  - Quantum Markov chain: SSA implies that if A, B and C form a quantum Markov chain, i.e.,

  \\begin {aligned} \\rho _ {ABC} = \\rho _ {AB} \\otimes \\rho _ {BC}, \\end {aligned}

  then the conditional mutual information vanishes, i.e.,

  \\begin {aligned} I (A:C\\vert B) = 0. \\end {aligned}

  - Quantum Fannes-Audenaert inequality: SSA implies that the von Neumann entropy is Lipschitz continuous, i.e.,

  \\begin {aligned} |S (\\rho ) - S (\\sigma )| \\le \\sqrt {n \\eta } \\log (n+1), \\end {aligned}

  where \\rho  and \\sigma  are n-dimensional density matrices and \\eta  is their trace distance.

- A simple mnemonic to remember SSA is to think of the entropy as a measure of uncertainty or ignorance. SSA then says that the total uncertainty of a system and a part of it is less than or equal to the uncertainty of the system and another part of it plus the uncertainty of the two parts. In other words, knowing more about a part of a system reduces the uncertainty of the whole system.

- A simple proof of SSA is based on the joint concavity of the quantum relative entropy, defined as:

\\begin {aligned} S (\\rho \\vert \\vert \\sigma ) = \\text {Tr}\\left ( \\rho \\log \\rho \\right) - \\text {Tr}\\left ( \\rho \\log \\sigma \\right), \\end {aligned}

which measures the distinguishability of two quantum states. The proof goes as follows:

  - By the joint concavity of the quantum relative entropy, we have:

  \\begin {aligned} S (\\rho _ {ABC} \\vert \\vert \\rho _ {AB} \\otimes \\rho _ {BC}) \\le S (\\rho _ {B} \\vert \\vert \\rho _ {B}). \\end {aligned}

  - By the definition of the quantum relative entropy, we have:

  \\begin {aligned} S (\\rho _ {ABC} \\vert \\vert \\rho _ {AB} \\otimes \\rho _ {BC}) = S (A,B,C) + S (A,B) + S (B,C) - S (B) - S (A,B,C). \\end {aligned}

  - By the positivity of the quantum relative entropy, we have:

  \\begin {aligned} S (\\rho _ {B} \\vert \\vert \\