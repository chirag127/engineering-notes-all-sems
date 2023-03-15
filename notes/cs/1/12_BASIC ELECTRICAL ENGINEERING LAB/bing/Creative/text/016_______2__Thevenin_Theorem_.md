##### 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying any linear circuit, regardless of its complexity, to an equivalent circuit with a single voltage source and a series resistor.  
- Thevenin's theorem can be applied to both AC and DC circuits. 
- Thevenin's theorem can be used to make circuit analysis simpler and to study a circuit's initial-condition and steady-state response. 
- Thevenin's theorem can also be used to calculate the maximum power transfer from a circuit to a load. 

The steps to apply Thevenin's theorem are:

1. Identify the two terminals of the circuit where the load is connected and remove the load.
2. Calculate the open-circuit voltage across the two terminals. This is the Thevenin voltage, Vth.
3. Calculate the equivalent resistance seen from the two terminals with all the independent sources turned off. This is the Thevenin resistance, Rth.
4. Replace the original circuit with the Thevenin equivalent circuit, which consists of Vth in series with Rth, and reconnect the load.
5. Analyze the simplified circuit to find the desired quantities, such as current, voltage, or power.  

Here is an example of applying Thevenin's theorem to a simple circuit:

![Thevenin example](https://www.allaboutcircuits.com/uploads/articles/thevenin-example.png)

The Thevenin equivalent circuit is:

![Thevenin equivalent](https://www.allaboutcircuits.com/uploads/articles/thevenin-equivalent.png)

The Thevenin voltage is:

Vth = 28 V - 4 V - 2 V = 22 V

The Thevenin resistance is:

Rth = 2 Ω + 4 Ω = 6 Ω

The current through the load resistor is:

I = Vth / (Rth + R) = 22 V / (6 Ω + 10 Ω) = 1.38 A

The voltage across the load resistor is:

V = IR = 1.38 A x 10 Ω = 13.8 V

The power dissipated by the load resistor is:

P = VI = 1.38 A x 13.8 V = 19.04 W

The maximum power transfer occurs when the load resistance is equal to the Thevenin resistance, i.e., R = Rth = 6 Ω. In that case, the power delivered to the load is:

Pmax = Vth^2 / (4Rth) = 22^2 / (4 x 6) = 20.17 W