##### 1. Verification of Kirchhoff’s laws

Kirchhoff’s laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff’s laws:

- Kirchhoff’s current law (KCL): This law, also called Kirchhoff’s first law, or Kirchhoff’s junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. Mathematically, KCL can be written as:

$$\sum_{k=1}^n I_k = 0$$

where $I_k$ is the current flowing through the $k$-th branch connected to the node.

- Kirchhoff’s voltage law (KVL): This law, also called Kirchhoff’s second law, or Kirchhoff’s loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of voltages supplied by the sources; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop. Mathematically, KVL can be written as:

$$\sum_{k=1}^n V_k = 0$$

where $V_k$ is the voltage across the $k$-th element of the loop.

To verify Kirchhoff’s laws experimentally, one can use a simple circuit consisting of a battery, a resistor, and an ammeter. The circuit diagram is shown below:

![Circuit diagram](https://www.sciencefacts.net/wp-content/uploads/2020/08/Kirchhoffs-Law-Verification-Experiment.png)

The steps to verify Kirchhoff’s laws are:

- Connect the battery, the resistor, and the ammeter in series as shown in the diagram.
- Measure the current $I$ flowing through the circuit using the ammeter.
- Measure the voltage $V_B$ across the battery and the voltage $V_R$ across the resistor using a voltmeter.
- Apply KCL at the node where the battery, the resistor, and the ammeter are connected. The current flowing into the node is $I$, and the current flowing out of the node is also $I$. Therefore, the sum of currents at the node is zero, which verifies KCL.
- Apply KVL to the closed loop formed by the battery, the resistor, and the ammeter. The voltage supplied by the battery is $V_B$, and the voltage dropped across the resistor is $V_R$. Therefore, the sum of voltages around the loop is $V_B - V_R$, which should be zero, which verifies KVL. Alternatively, one can use Ohm’s law to write $V_R = IR$, where $R$ is the resistance of the resistor, and then substitute it into the KVL equation to get $V_B - IR = 0$, which also verifies KVL.