### Kirchhoff's laws for DC circuits

Kirchhoff's laws are two principles that govern the analysis of electric circuits. They are named after Gustav Kirchhoff, a German physicist who formulated them in 1845. They are:

- Kirchhoff's current law (KCL): This law states that the algebraic sum of the currents entering and leaving any node (or junction) in a circuit is zero. In other words, the total current entering a node is equal to the total current leaving the node. This is based on the conservation of electric charge. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current of the k-th branch connected to the node.

- Kirchhoff's voltage law (KVL): This law states that the algebraic sum of the voltages around any closed loop (or mesh) in a circuit is zero. In other words, the total voltage rise in a loop is equal to the total voltage drop in the loop. This is based on the conservation of energy. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage of the k-th element in the loop.

Kirchhoff's laws are used to find the values of current, voltage, and resistance in DC circuits. They can also be used to find the unknown resistance in a circuit using a Wheatstone bridge. They are the basis of mesh and node analysis, which are systematic methods to solve complex circuits. They are applicable to any circuit configuration, as long as the circuit is linear and time-invariant.

Some limitations of Kirchhoff's laws are:

- They do not account for the effects of electromagnetic induction, which can cause voltage and current to vary with time in a circuit.
- They do not account for the effects of radiation, which can cause energy loss or gain in a circuit.
- They do not account for the effects of quantum mechanics, which can cause discrete changes in voltage and current in a circuit.

Some examples of applying Kirchhoff's laws to DC circuits are:

- Example 1: Find the current through each resistor in the following circuit.

  ![Circuit 1](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/dccircuits-dccl1.gif)

  Solution: Applying KCL to node A, we get:

  $$I_1 + I_2 = I_3$$

  Applying KVL to loop ABCDA, we get:

  $$10 - 2I_1 - 3I_2 = 0$$

  Solving these two equations, we get:

  $$I_1 = 2.5 A$$
  $$I_2 = 1.67 A$$
  $$I_3 = 4.17 A$$

- Example 2: Find the voltage across each resistor in the following circuit.

  ![Circuit 2](https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/a/ee-kirchhoffs-laws/ee-kirchhoffs-laws-1.png)

  Solution: Applying KVL to loop ABFEDCBA, we get:

  $$V_1 + V_2 + V_3 - 12 = 0$$

  Applying Ohm's law to each resistor, we get:

  $$V_1 = 2I_1$$
  $$V_2 = 4I_2$$
  $$V_3 = 6I_3$$

  Applying KCL to node B, we get:

  $$I_1 = I_2 + I_3$$

  Substituting these expressions into the KVL equation, we get:

  $$2I_1 + 4I_2 + 6I_3 - 12 = 0$$

  Solving this equation, we get:

  $$I_1 = 1.5 A$$
  $$I_2 = 0.5 A$$
  $$I_3 = 1 A$$

  Therefore, the voltages across the resistors are:

  $$V_1 = 3 V$$
  $$V_2 = 2 V$$
  $$V_3 = 6 V$$