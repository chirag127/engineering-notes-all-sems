### Optical cavity Quantum electrodynamics for the notes of the Unit 3 - Quantum Computers in the subject of Quantum Computing

- Optical cavity Quantum electrodynamics (QED) is the study of the interaction between light confined in a reflective cavity and atoms or other particles, under conditions where the quantum nature of photons is significant.
- The interaction between a quantum emitter and a single optical cavity mode, termed cavity QED, has allowed for a number of key experimental advances in quantum optics, including the observation of an enhancement of spontaneous emission, the demonstration of the photon blockade effect and vacuum-induced transparency.
- Cavity QED can be used to construct a quantum computer by encoding quantum information in the states of the atoms or the photons, and manipulating them with laser pulses or microwave fields.
- Cavity QED can also be used to explore fundamental quantum phenomena, such as entanglement, decoherence, quantum measurement and quantum feedback.
- Cavity QED can be realized in different physical systems, such as optical or microwave cavities coupled to atoms, ions, quantum dots, superconducting qubits or mechanical resonators .
- Cavity QED can be classified into two regimes: the weak coupling regime and the strong coupling regime, depending on the ratio of the coupling strength between the cavity and the emitter to the decay rates of the cavity and the emitter.
- In the weak coupling regime, the coupling strength is much smaller than the decay rates, and the cavity and the emitter can be treated as independent systems. The cavity QED effects are mainly manifested as a modification of the emission spectrum or the decay rate of the emitter.
- In the strong coupling regime, the coupling strength is much larger than the decay rates, and the cavity and the emitter form a hybrid system with new eigenstates and eigenenergies. The cavity QED effects are mainly manifested as a coherent exchange of energy and information between the cavity and the emitter, or the generation of nonclassical states of light and matter.
- A mnemonic to remember the difference between the weak and the strong coupling regimes is: Weak coupling = Weak interaction, Strong coupling = Strong interaction.
- An example of a cavity QED system in the strong coupling regime is a single atom trapped in a high-finesse optical cavity, where the atom can absorb and emit photons from the cavity mode, and the cavity can reflect and transmit photons from the atom. The atom and the cavity can be described by the Jaynes-Cummings model, which is a simple and solvable model of cavity QED.
- The Jaynes-Cummings model assumes that the atom has two levels, the ground state |g> and the excited state |e>, and the cavity has a single mode with frequency w. The atom and the cavity are coupled with a strength g, and the atom is driven by a laser with frequency wL and amplitude E. The Hamiltonian of the system is given by:

```
H = hw(a^+a + 1/2) + hw0|e><e| + g(a^+|g><e| + a|e><g|) + E(a^+e^-iwLt + ae^iwLt)
```

where a and a^+ are the annihilation and creation operators of the cavity mode, w0 is the atomic transition frequency, and |g> and |e> are the atomic states.

- The eigenstates and eigenenergies of the system depend on the number of photons in the cavity, n. For n = 0, the system has two eigenstates, |g,0> and |e,0>, with eigenenergies 0 and hw0, respectively. For n > 0, the system has two eigenstates, |+,n> and |-,n>, with eigenenergies hw(n + 1/2) + 1/2 sqrt[4g^2n + (w - w0)^2] and hw(n + 1/2) - 1/2 sqrt[4g^2n + (w - w0)^2], respectively. These eigenstates are superpositions of the atomic and the cavity states, and are called the dressed states.
- A mnemonic to remember the expression for the eigenenergies of the dressed states is: E = hw(n + 1/2) + 1/2 sqrt[4g^2n + (w - w0)^2] = hw(n + 1/2