##### 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying any linear circuit, regardless of how complex it is, to an equivalent circuit with a single voltage source and a series resistance.  
- Thevenin's theorem can be applied to both AC and DC circuits. 
- Thevenin's theorem can be used to make circuit analysis simpler and to study a circuit's initial-condition and steady-state response. 
- Thevenin's theorem and its dual, Norton's theorem, are widely used in network analysis and design. 

The steps to find the Thevenin equivalent circuit are:

1. Remove the load resistor and replace it with an open circuit. 
2. Calculate the Thevenin voltage (Vth) - the voltage across the open circuit. 
3. Calculate the Thevenin resistance (Rth) - the equivalent resistance seen from the open circuit terminals. 
4. Connect Vth and Rth in series to form the Thevenin equivalent circuit. 
5. Connect the load resistor to the Thevenin equivalent circuit and analyze the circuit as needed. 

An example of applying Thevenin's theorem is shown below:

![Thevenin example](https://www.allaboutcircuits.com/uploads/articles/thevenin-example.png)

The Thevenin equivalent circuit is:

![Thevenin equivalent](https://www.allaboutcircuits.com/uploads/articles/thevenin-equivalent.png)

The current flowing in the circuit is:

![Thevenin current](https://www.allaboutcircuits.com/uploads/articles/thevenin-current.png)