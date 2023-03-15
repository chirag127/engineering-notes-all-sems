##### 1. Verification of Kirchhoff’s laws

Kirchhoff’s laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff’s laws:

- Kirchhoff’s current law (KCL): This law, also called Kirchhoff’s first law, or Kirchhoff’s junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. Mathematically, KCL can be expressed as:

$$\sum_{k=1}^n I_k = 0$$

where $I_k$ is the current flowing through the $k$-th branch connected to the node.

- Kirchhoff’s voltage law (KVL): This law, also called Kirchhoff’s second law, or Kirchhoff’s loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of voltages supplied to the loop; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop. Mathematically, KVL can be expressed as:

$$\sum_{k=1}^n V_k = 0$$

where $V_k$ is the voltage across the $k$-th element of the loop.

To verify Kirchhoff’s laws experimentally, we need the following apparatus:

- A DC power supply
- A voltmeter
- An ammeter
- Resistors of different values
- Connecting wires
- A breadboard

The procedure is as follows:

- Connect the power supply, the voltmeter, the ammeter, and the resistors in a circuit as shown in the diagram below. The circuit has two loops and three nodes.

![Circuit diagram](https://www.sciencefacts.net/wp-content/uploads/2020/07/Kirchhoffs-Law-Diagram-1.png)

- Switch on the power supply and note the readings of the voltmeter and the ammeter for each element of the circuit.
- Apply KCL to each node and verify that the sum of currents entering and leaving the node is zero. For example, for node A, we have:

$$I_1 = I_2 + I_3$$

- Apply KVL to each loop and verify that the sum of voltages across each element of the loop is zero. For example, for loop ABCDA, we have:

$$V_1 - V_2 - V_3 - V_4 = 0$$

- Repeat the steps for different values of resistances and power supply voltage and observe the results.