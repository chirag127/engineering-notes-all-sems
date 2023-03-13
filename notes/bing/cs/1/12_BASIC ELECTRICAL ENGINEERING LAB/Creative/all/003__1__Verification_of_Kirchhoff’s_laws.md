##### 1. Verification of Kirchhoff’s laws

Kirchhoff’s laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff’s laws:

- Kirchhoff’s current law (KCL): This law, also called Kirchhoff’s first law, or Kirchhoff’s junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero . Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current flowing through the $k$-th branch of the node, and $n$ is the number of branches connected to the node.

- Kirchhoff’s voltage law (KVL): This law, also called Kirchhoff’s second law, or Kirchhoff’s loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of the voltages supplied to the loop; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop . Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage across the $k$-th element of the loop, and $n$ is the number of elements in the loop.

To verify Kirchhoff’s laws experimentally, one can use a simple circuit consisting of a battery, a switch, and three resistors connected in a loop, as shown in the diagram below:

```
       +---R1---+
       |       |
       |       |
      R2      R3
       |       |
       |       |
       +-------+
       |       |
       |       |
      SW      BAT
       |       |
       |       |
       +-------+
```

The following steps can be followed to verify Kirchhoff’s laws:

- Connect the circuit as shown in the diagram, using a voltmeter to measure the voltage across each resistor, and an ammeter to measure the current through each resistor.
- Close the switch and record the readings of the voltmeter and the ammeter for each resistor.
- Calculate the sum of the currents entering and leaving the node at the top of the circuit, and compare it with zero. This verifies KCL.
- Calculate the sum of the voltages across each resistor, and compare it with the voltage of the battery. This verifies KVL.
- Repeat the experiment with different values of resistors and battery voltage, and observe that Kirchhoff’s laws are always valid.

A possible mnemonic to remember Kirchhoff’s laws is:

- KCL: Currents in and out of a node are equal.
- KVL: Voltages around a loop add up to zero.