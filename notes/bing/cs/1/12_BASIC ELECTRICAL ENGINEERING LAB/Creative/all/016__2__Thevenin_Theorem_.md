##### 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying a linear circuit that contains multiple sources and resistors into an equivalent circuit that has only one voltage source and one resistor in series with a load.
- Thevenin's theorem can be applied to both AC and DC circuits, and it can be used to analyze the initial and steady-state responses of a circuit.
- Thevenin's theorem states that any two-terminal linear circuit can be replaced by an equivalent circuit that has the following components :
  - A voltage source, Vth, that is equal to the open-circuit voltage across the terminals of the original circuit.
  - A resistor, Rth, that is equal to the equivalent resistance of the original circuit when all the independent sources are turned off and the dependent sources are replaced by their internal resistances.
  - A load resistor, RL, that is connected across the terminals of the equivalent circuit and represents the external device or component that is connected to the original circuit.
- The steps to find the Thevenin's equivalent circuit are  :
  - Identify the terminals of the circuit where the load is connected and label them as A and B.
  - Remove the load from the circuit and calculate the open-circuit voltage, Vth, across the terminals A and B using any circuit analysis technique, such as nodal analysis, mesh analysis, or superposition.
  - Turn off all the independent sources in the circuit and replace them by their internal resistances. If the sources are ideal, they have zero internal resistance and can be replaced by short circuits. If the circuit has dependent sources, do not turn them off, but replace them by their internal resistances if they have any.
  - Calculate the equivalent resistance, Rth, of the circuit seen from the terminals A and B using any circuit analysis technique, such as parallel and series combinations, delta-wye transformations, or source transformations.
  - Draw the Thevenin's equivalent circuit with Vth, Rth, and RL connected in series.
  - Calculate the current, I, and the voltage, VL, across the load using Ohm's law and voltage division.
- The advantages of using Thevenin's theorem are :
  - It reduces the complexity of a circuit and makes it easier to analyze and understand.
  - It allows us to study the effect of varying the load on the circuit performance without having to solve the whole circuit again.
  - It helps us to design circuits that can deliver the maximum power to the load.
- The limitations of using Thevenin's theorem are:
  - It can only be applied to linear circuits that obey the superposition principle and Ohm's law.
  - It can be tedious and time-consuming to find the Thevenin's equivalent circuit for circuits that have many sources and resistors.
  - It does not account for the internal resistance of the load, which may affect the accuracy of the results.
- An example of applying Thevenin's theorem is shown below:

![Thevenin's theorem example](https://i.imgur.com/2wvZ1Q7.png)

- The original circuit has two voltage sources, V1 and V2, and three resistors, R1, R2, and R3, connected to a load resistor, RL. The terminals of the circuit are labeled as A and B.
- To find the Thevenin's equivalent circuit, we first remove the load and calculate the open-circuit voltage, Vth, across the terminals A and B. Using the voltage division rule, we get:

Vth = V2 * R1 / (R1 + R2) + V1 * R2 / (R1 + R2)

- Next, we turn off the voltage sources and replace them by short circuits. The circuit becomes a parallel combination of R1 and R2 in series with R3. Using the parallel and series resistance formulas, we get:

Rth = (R1 * R2 / (R1 + R2)) + R3

- The Thevenin's equivalent circuit is then drawn with Vth, Rth, and RL connected in series. Using Ohm's law and voltage division, we can calculate the current, I, and the voltage, VL, across the load as:

I = Vth / (Rth + RL)

VL = I * RL

- A possible mnemonic to remember the steps of Thevenin's theorem is:

**V