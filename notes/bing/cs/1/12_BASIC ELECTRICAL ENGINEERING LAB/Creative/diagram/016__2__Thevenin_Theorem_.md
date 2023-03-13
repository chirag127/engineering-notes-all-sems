Thevenin's theorem is a method of simplifying a linear circuit that contains voltage sources, current sources, and resistors. It states that any such circuit can be replaced by an equivalent circuit that has only a voltage source and a resistor in series. The voltage source is called the Thevenin voltage and the resistor is called the Thevenin resistance. The Thevenin equivalent circuit has the same voltage and current at the terminals as the original circuit.

The following diagram illustrates the basic idea of Thevenin's theorem:

```
+-----+     +-----+     +-----+
|     |     |     |     |     |
|  V  |-----|  R  |-----|  RL |
|     |     |     |     |     |
+-----+     +-----+     +-----+
  |           |           |
  |           |           |
  +-----------+-----------+
          AB
```

The circuit on the left has a voltage source V, a resistor R, and a load resistor RL. The terminals A and B are the points of interest. The circuit on the right is the Thevenin equivalent circuit, which has a voltage source Vth and a resistor Rth. The terminals A and B are the same as before. The Thevenin voltage Vth is the open-circuit voltage at the terminals A and B, and the Thevenin resistance Rth is the equivalent resistance seen from the terminals A and B when all the independent sources are turned off.

To find the Thevenin equivalent circuit, we can follow these steps:

1. Identify the terminals A and B of the circuit.
2. Calculate the open-circuit voltage Vth by removing the load resistor RL and finding the voltage across the terminals A and B.
3. Calculate the short-circuit current Ith by shorting the terminals A and B and finding the current through the short.
4. Calculate the Thevenin resistance Rth by dividing Vth by Ith, or by finding the equivalent resistance seen from the terminals A and B when all the independent sources are turned off.
5. Draw the Thevenin equivalent circuit with Vth and Rth in series and connect the load resistor RL across the terminals A and B.

The Thevenin equivalent circuit can be used to analyze the behavior of the circuit with different load resistors, without having to solve the original circuit repeatedly. It can also be used to find the maximum power transfer to the load resistor, which occurs when RL equals Rth.