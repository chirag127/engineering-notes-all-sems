##### 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying any linear circuit, regardless of its complexity, to an equivalent circuit with a single voltage source and a series resistance.  
- Thevenin's theorem can be applied to both AC and DC circuits. 
- Thevenin's theorem can be used to make circuit analysis simpler and to study a circuit's initial-condition and steady-state response. 
- Thevenin's theorem can also be used to calculate the maximum power transfer from a circuit to a load. 

The steps to apply Thevenin's theorem are:

1. Remove the load resistor and replace it with an open circuit. 
2. Calculate the Thevenin voltage, which is the voltage across the open circuit. 
3. Calculate the Thevenin resistance, which is the equivalent resistance seen from the open circuit terminals. 
4. Replace the original circuit with the Thevenin equivalent circuit, which consists of the Thevenin voltage source in series with the Thevenin resistance.  
5. Connect the load resistor to the Thevenin equivalent circuit and calculate the current and voltage across it.  

An example of applying Thevenin's theorem is shown below:

![Thevenin example](https://www.allaboutcircuits.com/uploads/articles/How-to-Use-Thevenins-Theorem-Example-1.jpg)

- The original circuit has a 20 V voltage source, a 10 Ω resistor, a 20 Ω resistor, and a 40 Ω load resistor. 
- The first step is to remove the load resistor and replace it with an open circuit. 
- The second step is to calculate the Thevenin voltage, which is the voltage across the open circuit. This can be done by applying the voltage divider rule: Vth = 20 V * 20 Ω / (10 Ω + 20 Ω) = 13.33 V. 
- The third step is to calculate the Thevenin resistance, which is the equivalent resistance seen from the open circuit terminals. This can be done by replacing the voltage source with a short circuit and applying the parallel resistance formula: Rth = 10 Ω || 20 Ω = 6.67 Ω. 
- The fourth step is to replace the original circuit with the Thevenin equivalent circuit, which consists of a 13.33 V voltage source in series with a 6.67 Ω resistor. 
- The fifth step is to connect the load resistor to the Thevenin equivalent circuit and calculate the current and voltage across it. This can be done by applying Ohm's law: I = Vth / (Rth + Rl) = 13.33 V / (6.67 Ω + 40 Ω) = 0.286 A, Vl = I * Rl = 0.286 A * 40 Ω = 11.43 V.