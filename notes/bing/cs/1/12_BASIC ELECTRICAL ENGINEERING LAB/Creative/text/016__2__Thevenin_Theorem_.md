##### 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying a linear circuit that contains multiple sources and resistors into an equivalent circuit that has only one voltage source and one resistor in series with a load.  
- Thevenin's theorem can be applied to both AC and DC circuits. 
- Thevenin's theorem can be used to make circuit analysis easier and to study the initial and steady-state responses of a circuit. 
- Thevenin's theorem states that any two-terminal linear circuit can be replaced by an equivalent circuit that has the following components:   
  - A voltage source, Vth, that is equal to the open-circuit voltage across the terminals of the original circuit.
  - A resistor, Rth, that is equal to the equivalent resistance of the original circuit when all the independent sources are turned off and the dependent sources are replaced by their internal resistances.
  - A load resistor, RL, that is connected across the terminals of the equivalent circuit and represents the external device or component that is connected to the original circuit.
- The steps to find the Thevenin's equivalent circuit are:   
  - Identify the terminals of the original circuit where the load is connected and label them as A and B.
  - Remove the load from the original circuit and calculate the open-circuit voltage, Vth, across the terminals A and B using any circuit analysis technique, such as nodal analysis, mesh analysis, or superposition.
  - Turn off all the independent sources in the original circuit and replace the dependent sources by their internal resistances. Then, calculate the equivalent resistance, Rth, of the circuit as seen from the terminals A and B using any resistance combination technique, such as series-parallel reduction, delta-wye transformation, or source transformation.
  - Draw the Thevenin's equivalent circuit with Vth, Rth, and RL connected in series and label the terminals A and B.
  - Analyze the Thevenin's equivalent circuit to find the current, voltage, or power across the load or any other quantity of interest.