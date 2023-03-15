# 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying any linear circuit, regardless of its complexity, to an equivalent circuit with a single voltage source and a series resistor  .
- Thevenin's theorem can be applied to both AC and DC circuits.
- Thevenin's theorem can be used to make circuit analysis easier and to study a circuit's initial-condition and steady-state response.
- Thevenin's theorem has some limitations, such as it cannot be applied to nonlinear circuits or circuits with time-varying sources.

## Steps to apply Thevenin's theorem

- Step 1: Identify the two terminals of the circuit where the load is connected and remove the load resistor.
- Step 2: Calculate the Thevenin voltage, which is the voltage across the open circuit terminals. This can be done by using any circuit analysis technique, such as nodal analysis, mesh analysis, or superposition .
- Step 3: Calculate the Thevenin resistance, which is the equivalent resistance seen from the open circuit terminals. This can be done by replacing all independent voltage sources with short circuits and all independent current sources with open circuits, and then finding the total resistance between the terminals .
- Step 4: Draw the Thevenin equivalent circuit, which consists of a voltage source equal to the Thevenin voltage and a series resistor equal to the Thevenin resistance, connected to the load resistor .
- Step 5: Analyze the Thevenin equivalent circuit to find the current, voltage, or power across the load resistor .

## Example of applying Thevenin's theorem

Consider the following circuit, where the load resistor is R_L = 40 Ω.

![Circuit diagram](https://www.allaboutcircuits.com/uploads/articles/How-to-Use-Thevenins-Theorem-DC-Network-Analysis-Example-1.jpg)

To apply Thevenin's theorem, we follow the steps as follows:

- Step 1: Remove the load resistor and replace it with an open circuit.

![Circuit diagram with open circuit](https://www.allaboutcircuits.com/uploads/articles/How-to-Use-Thevenins-Theorem-DC-Network-Analysis-Example-2.jpg)

- Step 2: Calculate the Thevenin voltage, which is the voltage across the open circuit terminals. We can use the voltage divider rule to find the voltage across R_2, which is V_2 = 20 V × (10 Ω / (10 Ω + 20 Ω)) = 6.67 V. Then, we can use Kirchhoff's voltage law to find the voltage across R_1, which is V_1 = 20 V - V_2 = 13.33 V. The Thevenin voltage is equal to V_1, so V_th = 13.33 V.

- Step 3: Calculate the Thevenin resistance, which is the equivalent resistance seen from the open circuit terminals. We can do this by replacing the voltage source with a short circuit and finding the total resistance between the terminals. The circuit becomes a parallel combination of R_1 and R_2, so R_th = (R_1 × R_2) / (R_1 + R_2) = (10 Ω × 20 Ω) / (10 Ω + 20 Ω) = 6.67 Ω.

- Step 4: Draw the Thevenin equivalent circuit, which consists of a voltage source equal to the Thevenin voltage and a series resistor equal to the Thevenin resistance, connected to the load resistor.

![Thevenin equivalent circuit](https://www.allaboutcircuits.com/uploads/articles/How-to-Use-Thevenins-Theorem-DC-Network-Analysis-Example-3.jpg)

- Step 5: Analyze the Thevenin equivalent circuit to find the current, voltage, or power across the load resistor. We can use Ohm's law to find the current, which is I = V_th / (R_th + R_L) = 13.33 V / (6.67 Ω + 40 Ω) = 0.286 A. The voltage across the load resistor is V_L = I × R_L = 0.286 A × 40 Ω =