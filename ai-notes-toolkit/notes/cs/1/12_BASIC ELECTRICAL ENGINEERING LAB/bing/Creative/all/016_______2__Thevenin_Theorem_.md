# 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying any linear circuit, regardless of its complexity, to an equivalent circuit with a single voltage source and a series resistance  .
- Thevenin's theorem can be applied to both AC and DC circuits.
- Thevenin's theorem can be used to make circuit analysis easier and to study a circuit's initial-condition and steady-state response.
- Thevenin's theorem and its dual, Norton's theorem, are widely used in circuit theory and engineering.

## Steps to apply Thevenin's theorem

- To apply Thevenin's theorem to any two-terminal linear circuit, we need to find the Thevenin's equivalent circuit, which consists of a voltage source Vth in series with a resistance Rth  .
- The steps to find the Thevenin's equivalent circuit are :
  - Step 1: Remove the load resistor (the resistor connected to the terminals of interest) and replace it with an open circuit.
  - Step 2: Calculate the Thevenin voltage (Vth), which is the voltage across the open circuit.
  - Step 3: Calculate the Thevenin resistance (Rth), which is the equivalent resistance seen from the terminals of the open circuit, with all independent sources turned off (voltage sources replaced by short circuits and current sources replaced by open circuits).
  - Step 4: Connect the Thevenin voltage source and the Thevenin resistance in series to form the Thevenin's equivalent circuit.

## Example of applying Thevenin's theorem

- Consider the following circuit, where we want to find the Thevenin's equivalent circuit across the terminals A and B.

![Circuit diagram](https://www.tutorialspoint.com/network_theory/images/thevenins_theorem.jpg)

- Step 1: Remove the load resistor R3 and replace it with an open circuit.

![Circuit diagram with open circuit](https://www.tutorialspoint.com/network_theory/images/thevenins_theorem_1.jpg)

- Step 2: Calculate the Thevenin voltage (Vth), which is the voltage across the open circuit. We can use the voltage divider rule to find Vth:

Vth = V1 * (R2 / (R1 + R2)) = 10 V * (3 Ω / (2 Ω + 3 Ω)) = 6 V

- Step 3: Calculate the Thevenin resistance (Rth), which is the equivalent resistance seen from the terminals of the open circuit, with all independent sources turned off. In this case, we replace V1 with a short circuit.

![Circuit diagram with short circuit](https://www.tutorialspoint.com/network_theory/images/thevenins_theorem_2.jpg)

Rth = R1 || R2 = (R1 * R2) / (R1 + R2) = (2 Ω * 3 Ω) / (2 Ω + 3 Ω) = 1.2 Ω

- Step 4: Connect the Thevenin voltage source and the Thevenin resistance in series to form the Thevenin's equivalent circuit.

![Thevenin's equivalent circuit](https://www.tutorialspoint.com/network_theory/images/thevenins_theorem_3.jpg)

- The Thevenin's equivalent circuit can be used to analyze the behavior of the original circuit with any load resistor connected to the terminals A and B. For example, if we reconnect R3 = 4 Ω, we can find the current through R3 as:

I3 = Vth / (Rth + R3) = 6 V / (1.2 Ω + 4 Ω) = 1.2 A

- This is the same current that would flow through R3 in the original circuit.