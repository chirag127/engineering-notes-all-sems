# Verification of Kirchhoff’s laws

Kirchhoff’s laws are two rules that describe the conservation of electric current and electric potential in electrical circuits. They are named after Gustav Kirchhoff, a German physicist who formulated them in 1845. The laws are:

- Kirchhoff’s current law (KCL): The algebraic sum of all currents entering and exiting a node must equal zero. This means that the amount of charge flowing into a junction is equal to the amount of charge flowing out of it.   

- Kirchhoff’s voltage law (KVL): The algebraic sum of all the voltages around a closed loop must equal zero. This means that the total energy gained or lost by the charges in a circuit loop is zero.   

To verify these laws experimentally, we need the following apparatus:

- A DC power supply
- A voltmeter
- An ammeter
- Resistors of different values
- Connecting wires
- A breadboard or a circuit board

The procedure is as follows:

- Connect the power supply, the voltmeter, the ammeter and the resistors in series and parallel combinations according to a given circuit diagram. Make sure the polarity of the devices is correct and the connections are tight.
- Switch on the power supply and adjust the voltage to a suitable value.
- Measure the current at each branch and the voltage across each resistor using the ammeter and the voltmeter respectively. Record the readings in a table.
- Apply KCL at each node and KVL at each loop and check if the equations are satisfied. If the equations are not satisfied, there may be some errors in the measurements or the connections.   

Some examples of circuit diagrams and the corresponding KCL and KVL equations are shown below:

![Circuit 1](https://i.imgur.com/6Z0o7wL.png)

KCL at node A: I1 = I2 + I3

KVL at loop ABCDA: V - I1R1 - I2R2 = 0

KVL at loop ABCFA: V - I1R1 - I3R3 - I3R4 = 0

![Circuit 2](https://i.imgur.com/0yL0X9t.png)

KCL at node A: I1 = I2 + I3

KCL at node B: I2 = I4 + I5

KVL at loop ABCDA: V - I1R1 - I2R2 - I3R3 = 0

KVL at loop BCDEB: -I2R2 - I4R4 - I5R5 = 0

KVL at loop ADEFA: V - I1R1 - I4R4 - I3R3 - I3R6 = 0