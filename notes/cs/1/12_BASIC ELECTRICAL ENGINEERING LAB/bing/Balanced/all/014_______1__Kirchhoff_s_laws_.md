# Kirchhoff's laws

Kirchhoff's laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff's laws:

- Kirchhoff's current law (KCL): This law, also called Kirchhoff's first law, or Kirchhoff's junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current flowing through the $k$-th branch connected to the node.

- Kirchhoff's voltage law (KVL): This law, also called Kirchhoff's second law, or Kirchhoff's loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of voltages supplied by the sources in the loop; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage across the $k$-th element of the loop.

The following diagrams illustrate the application of Kirchhoff's laws to simple circuits:

![KCL diagram](https://www.sciencefacts.net/wp-content/uploads/2020/08/Kirchhoffs-Current-Law-Diagram.png)

In this circuit, applying KCL to the node A gives:

$$I_1 + I_2 + I_3 = 0$$

![KVL diagram](https://www.sciencefacts.net/wp-content/uploads/2020/08/Kirchhoffs-Voltage-Law-Diagram.png)

In this circuit, applying KVL to the loop ABCDA gives:

$$V_1 - V_2 - V_3 - V_4 = 0$$

Kirchhoff's laws are the foundation of advanced circuit analysis. They can be used to solve complex circuits with multiple loops, branches, and sources. They can also be combined with the equations for individual components, such as resistors, capacitors, and inductors, to analyze the behavior of circuits in different domains, such as DC, AC, or transient.