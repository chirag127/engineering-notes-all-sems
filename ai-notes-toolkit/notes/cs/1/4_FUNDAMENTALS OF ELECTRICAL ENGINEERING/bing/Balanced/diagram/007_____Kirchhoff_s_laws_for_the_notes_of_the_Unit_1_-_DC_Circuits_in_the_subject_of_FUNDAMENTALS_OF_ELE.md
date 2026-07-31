### Kirchhoff's laws for DC circuits

Kirchhoff's laws are two principles that govern the analysis of electric circuits. They are named after Gustav Kirchhoff, a German physicist who formulated them in 1845. The laws are:

- **Kirchhoff's current law (KCL)**: This law states that the algebraic sum of the currents entering and leaving any node (or junction) in a circuit is zero. In other words, the total current entering a node is equal to the total current leaving the node. This is because charge is conserved and cannot be created or destroyed in a circuit. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current of the $k$-th branch connected to the node, and $n$ is the number of branches. The sign of the current depends on the direction assumed for the current. A common convention is to take the current entering the node as positive and the current leaving the node as negative.

- **Kirchhoff's voltage law (KVL)**: This law states that the algebraic sum of the voltages around any closed loop (or mesh) in a circuit is zero. In other words, the total voltage rise in a loop is equal to the total voltage drop in the loop. This is because energy is conserved and cannot be created or destroyed in a circuit. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage of the $k$-th element in the loop, and $n$ is the number of elements. The sign of the voltage depends on the polarity assigned to the element. A common convention is to take the voltage rise as positive and the voltage drop as negative.

Kirchhoff's laws are useful for solving circuits with multiple components, such as resistors, capacitors, inductors, sources, etc. By applying KCL to each node and KVL to each loop, we can obtain a system of linear equations that can be solved for the unknown currents and voltages in the circuit. Some examples of applications of Kirchhoff's laws are:

- Finding the values of current, voltage, and internal resistance in DC circuits.
- Finding the unknown resistance in a circuit using a Wheatstone bridge.
- Performing mesh and node analysis to simplify complex circuits.
- Analyzing circuits with dependent sources and superposition.

Some limitations of Kirchhoff's laws are:

- They are only valid for lumped circuits, where the physical dimensions of the circuit elements are much smaller than the wavelength of the signals in the circuit. For distributed circuits, such as transmission lines, Kirchhoff's laws do not hold and we need to use other methods, such as Maxwell's equations.
- They are only valid for linear circuits, where the current and voltage are proportional to each other. For nonlinear circuits, such as diodes and transistors, Kirchhoff's laws do not hold and we need to use other methods, such as graphical analysis or numerical methods.