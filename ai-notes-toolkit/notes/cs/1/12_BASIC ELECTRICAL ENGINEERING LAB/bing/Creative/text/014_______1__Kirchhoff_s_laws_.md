##### 1. Kirchhoff‟s laws.

Kirchhoff's laws are a set of two laws that describe the conservation of charge and energy in electrical circuits. They are named after the German physicist Gustav Kirchhoff, who first stated them in 1845.

- Kirchhoff's current law (KCL): This law, also called Kirchhoff's first law, or Kirchhoff's junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. This law is based on the principle of conservation of charge, which implies that charge cannot be created or destroyed at any node. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current flowing through the $k$-th branch connected to the node, and $n$ is the number of branches. The sign of $I_k$ depends on the direction of the current: positive if it flows into the node, and negative if it flows out of the node. A diagram illustrating KCL is shown below:

  ![KCL](https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/a/ee-kirchhoffs-laws/ckc-circuits-resistance-article-1.png)

- Kirchhoff's voltage law (KVL): This law, also called Kirchhoff's second law, or Kirchhoff's loop rule, states that, for any closed loop in an electrical circuit, the sum of the voltages across each element of the loop is equal to zero; or equivalently: The algebraic sum of the products of the currents and the resistances in a closed loop is equal to the algebraic sum of the electromotive forces in that loop. This law is based on the principle of conservation of energy, which implies that the total energy supplied by the sources in a loop is equal to the total energy dissipated by the resistors in the loop. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage across the $k$-th element of the loop, and $n$ is the number of elements. The sign of $V_k$ depends on the direction of the loop: positive if the loop goes from the negative to the positive terminal of the element, and negative otherwise. A diagram illustrating KVL is shown below:

  ![KVL](https://www.khanacademy.org/science/physics/circuits-topic/circuits-resistance/a/ee-kirchhoffs-laws/ckc-circuits-resistance-article-2.png)

Kirchhoff's laws are useful for analyzing complex circuits that cannot be solved by simple methods such as Ohm's law or series and parallel combinations. They can be applied to any type of circuit, whether it contains resistors, capacitors, inductors, or sources. They can also be used to find the equivalent resistance, current, or voltage of any circuit element.