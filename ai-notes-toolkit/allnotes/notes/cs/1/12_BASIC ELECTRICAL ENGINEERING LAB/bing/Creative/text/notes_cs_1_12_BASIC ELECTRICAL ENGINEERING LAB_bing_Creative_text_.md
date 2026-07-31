

## LIST OF EXPERIMENTS

- An experiment is a scientific procedure that aims to test a hypothesis, answer a question, or discover something new.
- Experiments usually involve manipulating one or more variables and measuring their effects on other variables.
- Experiments can be classified into different types based on their purpose, design, and execution.
- Some common types of experiments are:

  - Controlled experiments: These are experiments where the researcher controls all the variables except the one being tested, which is called the independent variable. The researcher then measures the effect of the independent variable on the dependent variable, which is the outcome of interest. Controlled experiments are often conducted in laboratories, where the conditions can be controlled and standardized.
  - Natural experiments: These are experiments where the researcher does not manipulate any variables, but instead observes the effects of a natural event or phenomenon on the dependent variable. Natural experiments are often conducted in the field, where the conditions are more realistic and complex, but also more difficult to control and measure.
  - Quasi-experiments: These are experiments where the researcher manipulates the independent variable, but does not randomly assign the participants to different groups or conditions. Quasi-experiments are often used when randomization is not possible or ethical, such as in educational or social settings. Quasi-experiments are less rigorous than controlled experiments, but more realistic than natural experiments.
  - Field experiments: These are experiments where the researcher manipulates the independent variable in a natural setting, such as a school, a workplace, or a community. Field experiments are more realistic than laboratory experiments, but also more challenging to control and measure. Field experiments can be either randomized or quasi-experimental, depending on how the participants are assigned to different groups or conditions.
  - Survey experiments: These are experiments where the researcher uses a survey or questionnaire to measure the dependent variable, and manipulates the independent variable by varying the wording, order, or format of the questions. Survey experiments are often used to study the effects of framing, priming, or social desirability on people's attitudes, beliefs, or behaviors. Survey experiments are relatively easy and cheap to conduct, but also prone to biases and errors.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

### Note: A minimum of ten experiments from the following should be performed.

- Experiment 1: To verify the truth table of AND, OR, NOT, NAND, NOR, XOR and XNOR gates using ICs.
- Experiment 2: To design and implement a half adder and a full adder circuit using logic gates.
- Experiment 3: To design and implement a half subtractor and a full subtractor circuit using logic gates.
- Experiment 4: To design and implement a 4-bit binary to gray code converter and a gray code to binary converter using logic gates.
- Experiment 5: To design and implement a 4-bit binary to BCD code converter and a BCD to binary converter using logic gates.
- Experiment 6: To design and implement a 4-bit binary to excess-3 code converter and an excess-3 to binary converter using logic gates.
- Experiment 7: To design and implement a 4-bit magnitude comparator using logic gates.
- Experiment 8: To design and implement a 4-bit parallel adder/subtractor using logic gates.
- Experiment 9: To design and implement a 4-bit ripple carry adder using logic gates.
- Experiment 10: To design and implement a 4-bit look ahead carry adder using logic gates.
- Experiment 11: To design and implement a 4-bit universal shift register using logic gates.
- Experiment 12: To design and implement a 4-bit synchronous up/down counter using logic gates.
- Experiment 13: To design and implement a 4-bit asynchronous up/down counter using logic gates.
- Experiment 14: To design and implement a 4-bit ring counter and a 4-bit Johnson counter using logic gates.
- Experiment 15: To design and implement a 4-bit binary to 7-segment decoder using logic gates.



#### (A) Hardware based experiments

Hardware based experiments are experiments that involve the use of physical devices, components, or systems to test a hypothesis, measure a phenomenon, or demonstrate a concept. Hardware based experiments can be classified into different types, such as:

- **Simulation experiments**: These are experiments that use hardware to model or mimic the behavior of a real-world system or process, such as a flight simulator, a circuit simulator, or a robot simulator. Simulation experiments can be used to study the effects of different parameters, scenarios, or conditions on the system or process, without affecting the actual system or process.
- **Prototype experiments**: These are experiments that use hardware to build a preliminary or partial version of a product, service, or system, such as a prototype car, a prototype app, or a prototype network. Prototype experiments can be used to test the feasibility, functionality, or performance of the product, service, or system, and to identify and resolve any issues or problems before the final version is developed.
- **Field experiments**: These are experiments that use hardware to conduct a test or trial in a natural or realistic setting, such as a field test, a pilot test, or a user test. Field experiments can be used to evaluate the effectiveness, usability, or impact of a product, service, or system, and to collect feedback from the users or customers.
- **Laboratory experiments**: These are experiments that use hardware to perform a controlled or isolated test or measurement in a specialized or artificial environment, such as a lab test, a bench test, or a calibration test. Laboratory experiments can be used to verify the accuracy, reliability, or quality of a product, service, or system, and to collect data or evidence to support a hypothesis or theory.



##### 1. Verification of Kirchhoff’s laws

Kirchhoff’s laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff’s laws:

- Kirchhoff’s current law (KCL): This law, also called Kirchhoff’s first law, or Kirchhoff’s junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. Mathematically, KCL can be expressed as:

$$\sum_{k=1}^n I_k = 0$$

where $I_k$ is the current flowing through the $k$-th branch connected to the node.

- Kirchhoff’s voltage law (KVL): This law, also called Kirchhoff’s second law, or Kirchhoff’s loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of voltages supplied to the loop; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop. Mathematically, KVL can be expressed as:

$$\sum_{k=1}^n V_k = 0$$

where $V_k$ is the voltage across the $k$-th element of the loop.

To verify Kirchhoff’s laws experimentally, we need the following apparatus:

- A DC power supply
- A voltmeter
- An ammeter
- Resistors of different values
- Connecting wires
- A breadboard

The procedure is as follows:

- Connect the power supply, the voltmeter, the ammeter, and the resistors in a circuit as shown in the diagram below. The circuit has two loops and three nodes.

Circuit diagram

- Switch on the power supply and note the readings of the voltmeter and the ammeter for each element of the circuit.
- Apply KCL to each node and verify that the sum of currents entering and leaving the node is zero. For example, for node A, we have:

$$I_1 = I_2 + I_3$$

- Apply KVL to each loop and verify that the sum of voltages across each element of the loop is zero. For example, for loop ABCDA, we have:

$$V_1 - V_2 - V_3 - V_4 = 0$$

- Repeat the steps for different values of resistances and power supply voltage and observe the results.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

##### 2. Measurement of power and power factor in a single phase ac series inductive circuit and study improvement of power factor using capacitor

- Power is the rate of doing work or transferring energy in an electric circuit. It is measured in watts (W) or kilowatts (kW).
- Power factor is the ratio of the real power (P) to the apparent power (S) in an ac circuit. It is a dimensionless number between 0 and 1 that indicates how efficiently the circuit uses the supplied voltage and current. A power factor of 1 means that the circuit is purely resistive and all the power is converted into useful work. A power factor of 0 means that the circuit is purely reactive and no power is transferred to the load.
- In a single phase ac series inductive circuit, the voltage and current are not in phase due to the presence of inductance. The current lags behind the voltage by an angle called the phase angle (φ). The power factor is given by the cosine of the phase angle, i.e., pf = cos φ.
- The real power (P) is the product of the rms voltage (V), the rms current (I) and the power factor (pf), i.e., P = V I pf. The apparent power (S) is the product of the rms voltage and the rms current, i.e., S = V I. The reactive power (Q) is the product of the rms voltage, the rms current and the sine of the phase angle, i.e., Q = V I sin φ. The power triangle is a graphical representation of the relationship between these three powers, as shown below.

power triangle

- The power factor can be improved by adding a capacitor in parallel with the inductive load. The capacitor provides a leading current that partially cancels out the lagging current of the inductor, thus reducing the phase angle and increasing the power factor. The capacitor should have a reactance (Xc) equal to the inductive reactance (Xl) of the load at the operating frequency, i.e., Xc = Xl = 2πfL, where f is the frequency and L is the inductance. The capacitance (C) of the capacitor is given by C = 1/Xc = 1/(2πfL).
- The power and power factor in a single phase ac series inductive circuit can be measured using a wattmeter and a voltmeter-ammeter method, as shown below.

circuit diagram

- The wattmeter measures the real power (P) by multiplying the voltage across its terminals (Vw) and the current through its coil (Iw). The voltmeter measures the rms voltage across the load (V) and the ammeter measures the rms current through the load (I). The power factor (pf) can be calculated by dividing the real power by the apparent power, i.e., pf = P/(V I). Alternatively, the power factor can be calculated by dividing the voltage across the wattmeter by the voltage across the load, i.e., pf = Vw/V. The phase angle (φ) can be calculated by taking the inverse cosine of the power factor, i.e., φ = cos^-1 pf.
- The improvement of power factor using a capacitor can be observed by comparing the readings of the wattmeter, the voltmeter and the ammeter before and after connecting the capacitor. The capacitor should be connected in parallel with the load, as shown below.

circuit diagram with capacitor

- After connecting the capacitor, the following changes should be observed:
  - The wattmeter reading (P) should remain the same, as the real power is independent of the power factor.
  - The voltmeter reading (V) should remain the same, as the voltage across the load is fixed by the source.
  - The ammeter reading (I) should decrease, as the capacitor provides a leading current that reduces the total current drawn from the source.
  - The power factor (pf) should increase, as the phase angle (φ) decreases due to the capacitor.
  - The reactive power (Q) should decrease, as the capacitor reduces the reactive component of the current.



##### 3. Study of phenomenon of resonance in RLC series circuit and obtain resonant frequency.

- A series RLC circuit consists of a resistor, an inductor and a capacitor connected in series to an alternating voltage source.
- Resonance occurs in a series RLC circuit when the inductive reactance (XL) is equal to the capacitive reactance (XC), or XL - XC = 0  .
- At resonance, the circuit current is in phase with the applied voltage, and the impedance of the circuit is equal to the resistance value (Z = R).
- The resonant frequency (fr) of a series RLC circuit is given by the formula :

  fr = 1 / (2π√(LC))

  where L is the inductance, C is the capacitance, and π is the mathematical constant.

- The effects of series resonance are:
  - The circuit current reaches its maximum value, and the voltage across each element can be much greater than the source voltage.
  - The power dissipated in the circuit is also maximum, and the power factor is unity.
  - The circuit behaves as a band-pass filter, allowing only a narrow range of frequencies around the resonant frequency to pass through.
- To obtain the resonant frequency of a series RLC circuit experimentally, one can vary the frequency of the source and measure the current or the voltage across the elements. The resonant frequency is the frequency at which the current is maximum or the voltage across the inductor or capacitor is zero .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the connection and measurement of power consumption of a fluorescent lamp (tube light).

##### 4. Connection and measurement of power consumption of a fluorescent lamp (tube light).

- A fluorescent lamp (tube light) is a type of electric light that uses a gas-filled tube coated with phosphor to produce visible light by fluorescence. The gas inside the tube is usually mercury vapor mixed with argon or other inert gases. The tube is connected to a ballast, which is a device that regulates the current and voltage to the lamp.
- The power consumption of a fluorescent lamp depends on its wattage rating, which can range from 5 watts for small bulbs to 100 watts for large ones. A typical fluorescent lamp consumes about 13-15 watts of power.
- The power consumption of a fluorescent lamp does not include the power dissipated in the ballast, which can be about 10-20% of the lamp power. The power factor of a fluorescent lamp is also less than one, which means that the lamp draws more current than the power it delivers. The power factor can be improved by using a capacitor in parallel with the lamp.
- To measure the power consumption of a fluorescent lamp, a wattmeter can be used. A wattmeter is an instrument that measures the power in watts by multiplying the voltage and current. A wattmeter has two coils: a current coil and a potential coil. The current coil is connected in series with the lamp, and the potential coil is connected in parallel with the lamp. The wattmeter shows the power consumed by the lamp and the ballast .
- To connect a fluorescent lamp, the following steps can be followed:
  - Connect the supply wires to the ballast terminals marked L (line) and N (neutral).
  - Connect the ballast terminals marked S1 and S2 to the starter, which is a small device that helps to ignite the lamp.
  - Connect the ballast terminals marked L1 and L2 to the lamp holders, which are the sockets that hold the tube ends.
  - Insert the tube into the lamp holders and twist it slightly to lock it in place.
  - Turn on the supply and observe the lamp. The starter will make a clicking sound and the lamp will flicker before lighting up.



##### 5. Measurement of power in 3- phase circuit by two-wattmeter method and determination of its power factor for star as well as delta connected load.

- The two-wattmeter method is a technique for measuring the total power in a balanced three-phase circuit using two wattmeters .
- The current coils of the two wattmeters are connected in series with any two line conductors, and the potential coils of each are connected to the third line conductor .
- The connection diagram of two wattmeter method for star and delta connected load is shown below .

Two wattmeter method for star and delta connected load

- The total power measured by the two wattmeters is given by  :

P = P1 + P2 = V1I1cos(Ø1 - 30°) + V2I2cos(Ø2 + 30°)

where P1 and P2 are the readings of the two wattmeters, V1 and V2 are the line voltages, I1 and I2 are the line currents, and Ø1 and Ø2 are the phase angles between the line voltages and currents.

- The power factor of the load can be determined by using the following formula :

cosØ = (P1 + P2) / √3VLI

where VL is the line voltage and I is the line current.

- Alternatively, the power factor can be determined by using the following formula :

cosØ = √3(P1 + P2) / (P1 - P2)

where P1 and P2 are the readings of the two wattmeters.

- The two wattmeter method can be used for both star and delta connected load, as long as the load is balanced  .
- The two wattmeter method is simple, accurate and economical for measuring three-phase power  .



Hello, I am Sydney, your AI assistant. I can help you with your studies. Here is some content on the topic of determination of parameters of ac single phase series RLC circuit.

##### 6. Determination of parameters of ac single phase series RLC circuit

- An ac single phase series RLC circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series to an ac voltage source (V).
- The current (I) in the circuit is the same for all the components and is given by Ohm's law: I = V/Z, where Z is the total impedance of the circuit.
- The impedance Z is a complex quantity that depends on the frequency (f) of the ac source and the values of R, L, and C. It can be written as: Z = R + jX, where j is the imaginary unit and X is the total reactance of the circuit.
- The reactance X is the sum of the inductive reactance (XL) and the capacitive reactance (XC), which are given by: XL = 2πfL and XC = 1/(2πfC).
- The impedance Z can also be expressed in polar form as: Z = |Z|∠θ, where |Z| is the magnitude of the impedance and θ is the phase angle between the voltage and the current.
- The magnitude of the impedance is given by: |Z| = √(R^2 + X^2) and the phase angle is given by: θ = tan^(-1)(X/R).
- The power factor (pf) of the circuit is the cosine of the phase angle: pf = cos(θ). It indicates how efficiently the circuit converts the ac voltage into useful power.
- The power consumed by the circuit is the product of the voltage, the current, and the power factor: P = VIpf. It consists of the active power (P<sub>a</sub>) and the reactive power (P<sub>r</sub>), which are given by: P<sub>a</sub> = VIcos(θ) and P<sub>r</sub> = VIsin(θ).
- The active power is the power that is dissipated as heat by the resistor and is measured in watts (W). The reactive power is the power that is stored and released by the inductor and the capacitor and is measured in volt-amperes reactive (VAR).
- The apparent power (S) of the circuit is the product of the voltage and the current: S = VI. It is the power that is supplied by the ac source and is measured in volt-amperes (VA).
- The apparent power is related to the active power and the reactive power by the Pythagorean theorem: S^2 = P<sub>a</sub>^2 + P<sub>r</sub>^2.
- The parameters of the ac single phase series RLC circuit can be determined by measuring the voltage, the current, and the power factor of the circuit, and applying the above formulas. Alternatively, they can be determined by measuring the impedance of the circuit using an impedance meter or a bridge circuit.



Hello, I am Sydney, your AI assistant. I can help you with your topic.

##### 7. Determination of (i) Voltage ratio (ii) polarity and (iii) efficiency by load test of a single phase Transformer

- A single phase transformer is a device that transfers electrical energy from one circuit to another through mutual induction.
- The voltage ratio of a transformer is the ratio of the secondary voltage to the primary voltage. It is also equal to the ratio of the number of turns in the secondary winding to the number of turns in the primary winding.
- The polarity of a transformer is the relative direction of the induced voltages in the primary and secondary windings. It can be determined by the dot convention, which assigns a dot to one terminal of each winding. The dots indicate that the voltages at those terminals have the same polarity at any instant.
- The efficiency of a transformer is the ratio of the output power to the input power. It is also equal to the ratio of the useful power to the total power. The useful power is the power delivered to the load, and the total power is the sum of the useful power and the losses in the transformer.
- A load test of a transformer is a method of measuring the voltage ratio, polarity, and efficiency of a transformer under different load conditions. It involves connecting a variable load to the secondary winding and measuring the input and output voltages and currents. The load test can also be used to determine the equivalent circuit parameters of the transformer, such as the resistance and reactance of the windings, and the magnetizing and core loss components.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of determination of efficiency of a dc shunt motor by load test.

##### 8. Determination of efficiency of a dc shunt motor by load test

- A dc shunt motor is a type of dc motor that has a shunt field winding connected in parallel with the armature winding. The shunt field winding provides a constant magnetic field for the armature to rotate.
- The efficiency of a dc shunt motor is the ratio of the output power to the input power. The output power is the mechanical power delivered by the motor to the load, and the input power is the electrical power supplied to the motor from the source.
- A load test is a method of determining the efficiency of a dc shunt motor by measuring the input and output power at different load conditions. The load test can be performed by connecting a variable resistor or a brake drum to the shaft of the motor and varying the load resistance or the brake torque.
- The procedure of the load test is as follows:

  - Connect the dc shunt motor to the source and the load as shown in the figure below. The voltmeter V measures the terminal voltage of the motor, the ammeter A measures the line current, and the wattmeter W measures the input power. The spring balance S and the lever arm L measure the brake torque, and the tachometer T measures the speed of the motor.

  - Start the motor and adjust the field rheostat to obtain the rated voltage at no load. Note down the readings of V, A, W, S, L, and T.
  - Increase the load gradually by decreasing the load resistance or increasing the brake torque. Note down the readings of V, A, W, S, L, and T at each load step until the motor reaches its rated current or power.
  - Plot the curves of input power, output power, and efficiency versus load current or load torque. The output power can be calculated by multiplying the brake torque and the angular speed. The efficiency can be calculated by dividing the output power by the input power.
  - Observe the variation of input power, output power, and efficiency with the load. The input power increases linearly with the load, the output power increases nonlinearly with the load, and the efficiency increases with the load until it reaches a maximum value and then decreases.

  Figure 1: Load test of a dc shunt motor

- The advantages of the load test are:

  - It is a direct and accurate method of determining the efficiency of a dc shunt motor.
  - It can be performed easily and quickly with simple instruments.
  - It can be used to determine the performance characteristics of the motor under different load conditions.

- The disadvantages of the load test are:

  - It requires a large amount of power and energy to perform the test, which may be wasteful and costly.
  - It may cause heating and wear of the motor and the load, which may affect the accuracy and reliability of the test results.
  - It may not be feasible to perform the test for large motors or for motors that have a variable speed or load.



Hello, I am Sydney, your AI assistant. I can help you with your topic.

##### 9. To study running and speed reversal of a three phase induction motor and record speed in both directions.

- A three phase induction motor is a type of electric motor that converts alternating current (AC) power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor.
- The speed of a three phase induction motor depends on the frequency of the AC supply, the number of poles in the stator, and the slip between the rotor and the stator. The speed can be calculated by the formula:

  `N = 120f / P (1 - s)`

  where N is the speed in revolutions per minute (rpm), f is the frequency in hertz (Hz), P is the number of poles, and s is the slip.
- The direction of rotation of a three phase induction motor is determined by the phase sequence of the AC supply. If the phase sequence is R-Y-B, the motor rotates in clockwise direction. If the phase sequence is reversed to B-Y-R, the motor rotates in anti-clockwise direction.
- To study the running and speed reversal of a three phase induction motor, the following steps are followed:

  - Connect the three phase induction motor to a three phase AC supply through a star-delta starter and a reversing switch. The star-delta starter is used to reduce the starting current and the reversing switch is used to change the phase sequence.
  - Switch on the supply and observe the direction and speed of rotation of the motor. Note down the speed by using a tachometer or a speedometer.
  - Switch off the supply and wait for the motor to stop completely.
  - Change the position of the reversing switch to reverse the phase sequence of the supply.
  - Switch on the supply again and observe the direction and speed of rotation of the motor. Note down the speed by using a tachometer or a speedometer.
  - Compare the speeds in both directions and verify that they are equal or nearly equal.
  - Repeat the experiment for different values of frequency and number of poles and record the speeds in both directions.



##### 10. Demonstration of cut-out sections of machines: dc machine, three phase induction machine, single-phase induction machine and synchronous machine.

- A cut-out section of a machine is a part of the machine that is cut or opened to show the internal components and their arrangement.
- Cut-out sections of machines are useful for demonstration and learning purposes, as they help to visualize the working principles and construction details of different types of machines.
- The following are some examples of cut-out sections of machines:

  - DC machine: A DC machine is a machine that converts electrical energy into mechanical energy or vice versa using direct current. A cut-out section of a DC machine shows the commutator-brush arrangement, which is used to switch the direction of current in the armature windings and produce a unidirectional torque. It also shows the field windings, which produce a magnetic field, and the armature windings, which interact with the magnetic field and rotate the shaft.

  - Three phase induction machine: A three phase induction machine is a machine that converts electrical energy into mechanical energy using alternating current. A cut-out section of a three phase induction machine shows the stator and the rotor. The stator is the stationary part of the machine, which has three phase windings that are connected to a three phase supply. The rotor is the rotating part of the machine, which can be either a squirrel cage rotor or a wound rotor. The squirrel cage rotor has short-circuited bars that are embedded in slots and connected by end rings. The wound rotor has three phase windings that are connected to slip rings and brushes. The stator windings produce a rotating magnetic field, which induces currents in the rotor windings and causes the rotor to rotate.

  - Single-phase induction machine: A single-phase induction machine is a machine that converts electrical energy into mechanical energy using single-phase alternating current. A cut-out section of a single-phase induction machine shows the stator and the rotor. The stator has two windings: a main winding and an auxiliary winding. The main winding is connected to the single-phase supply, while the auxiliary winding is connected to a capacitor or a switch. The rotor is similar to the squirrel cage rotor of a three phase induction machine. The stator windings produce a pulsating magnetic field, which induces currents in the rotor windings and causes the rotor to rotate. However, the pulsating magnetic field does not have a definite direction of rotation, so the rotor needs a starting torque to start rotating in a desired direction. The auxiliary winding and the capacitor or the switch provide the starting torque by creating a phase difference between the two stator windings.

  - Synchronous machine: A synchronous machine is a machine that converts electrical energy into mechanical energy or vice versa using alternating current. A cut-out section of a synchronous machine shows the stator and the rotor. The stator is similar to the stator of a three phase induction machine, which has three phase windings that are connected to a three phase supply. The rotor can be either a salient pole rotor or a cylindrical rotor. The salient pole rotor has projecting poles that are wound with field windings and connected to a direct current source. The cylindrical rotor has a smooth surface that is also wound with field windings and connected to a direct current source. The stator windings produce a rotating magnetic field, which interacts with the rotor field and causes the rotor to rotate at the same speed as the stator field. This is called the synchronous speed. The synchronous machine can operate in three modes: motoring, generating, and plugging. In the motoring mode, the stator supply provides the electrical energy and the rotor shaft delivers the mechanical energy. In the generating mode, the rotor shaft provides the mechanical energy and the stator terminals deliver the electrical energy. In the plugging mode, the stator supply and the rotor shaft oppose each other and the machine acts as a brake.



#### (B) Experiments available on virtual lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows users to perform experiments and learn scientific concepts without the need for physical equipment, materials, or space.
- Virtual labs can offer various benefits, such as enhancing accessibility, safety, efficiency, and motivation for learning science.
- There are many types of experiments available on virtual labs, depending on the subject, level, and purpose of the user. Some examples are:

  - Physics: Users can explore topics such as mechanics, optics, electricity, magnetism, thermodynamics, waves, and quantum physics by manipulating variables, observing phenomena, and measuring outcomes.
  - Chemistry: Users can conduct experiments on topics such as atomic structure, chemical bonding, reactions, equilibrium, kinetics, thermodynamics, electrochemistry, and organic chemistry by mixing substances, observing changes, and analyzing data.
  - Biology: Users can investigate topics such as cell structure, genetics, evolution, ecology, anatomy, physiology, and microbiology by observing specimens, performing tests, and interpreting results.
  - Engineering: Users can design, build, and test systems and devices on topics such as circuits, robotics, fluid mechanics, materials, and structures by applying principles, methods, and tools of engineering.
  - Mathematics: Users can explore topics such as algebra, geometry, calculus, statistics, and logic by solving problems, visualizing concepts, and proving theorems.
  - Computer Science: Users can learn topics such as programming, data structures, algorithms, databases, artificial intelligence, and cybersecurity by writing code, running programs, and debugging errors.



##### 1. Kirchhoff‟s laws.

Kirchhoff's laws are a set of two laws that describe the conservation of charge and energy in electrical circuits. They are named after the German physicist Gustav Kirchhoff, who first stated them in 1845.

- Kirchhoff's current law (KCL): This law, also called Kirchhoff's first law, or Kirchhoff's junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. This law is based on the principle of conservation of charge, which implies that charge cannot be created or destroyed at any node. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current flowing through the $k$-th branch connected to the node, and $n$ is the number of branches. The sign of $I_k$ depends on the direction of the current: positive if it flows into the node, and negative if it flows out of the node. A diagram illustrating KCL is shown below:

  KCL

- Kirchhoff's voltage law (KVL): This law, also called Kirchhoff's second law, or Kirchhoff's loop rule, states that, for any closed loop in an electrical circuit, the sum of the voltages across each element of the loop is equal to zero; or equivalently: The algebraic sum of the products of the currents and the resistances in a closed loop is equal to the algebraic sum of the electromotive forces in that loop. This law is based on the principle of conservation of energy, which implies that the total energy supplied by the sources in a loop is equal to the total energy dissipated by the resistors in the loop. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage across the $k$-th element of the loop, and $n$ is the number of elements. The sign of $V_k$ depends on the direction of the loop: positive if the loop goes from the negative to the positive terminal of the element, and negative otherwise. A diagram illustrating KVL is shown below:

  KVL

Kirchhoff's laws are useful for analyzing complex circuits that cannot be solved by simple methods such as Ohm's law or series and parallel combinations. They can be applied to any type of circuit, whether it contains resistors, capacitors, inductors, or sources. They can also be used to find the equivalent resistance, current, or voltage of any circuit element.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of virtual lab link: http://vlab.amrita.edu/?sub=3&brch=75&sim=217&cnt=2. This is a simulation of a simple pendulum experiment. Here are some points to note about this topic:

- A simple pendulum is a mass attached to a string that can swing freely under the influence of gravity.
- The period of a simple pendulum is the time it takes to complete one oscillation, or one back and forth motion.
- The period of a simple pendulum depends only on the length of the string and the acceleration due to gravity, and not on the mass or the amplitude of the swing.
- The formula for the period of a simple pendulum is T = 2π√(L/g), where T is the period, L is the length of the string, and g is the acceleration due to gravity.
- The simulation allows you to vary the length of the string, the mass of the bob, and the angle of release, and observe the effect on the period and the motion of the pendulum.
- You can also measure the period of the pendulum using a stopwatch, and compare it with the theoretical value calculated from the formula.
- You can also plot a graph of the period versus the length of the string, and verify that it is a square root function.
- You can also plot a graph of the period versus the mass of the bob, and verify that it is a constant function.
- You can also plot a graph of the period versus the angle of release, and verify that it is a constant function for small angles, and increases slightly for larger angles.
- You can also perform a linear regression on the data points, and calculate the slope and the intercept of the best fit line, and compare them with the theoretical values.
- You can also calculate the percentage error between the experimental and the theoretical values of the period, and analyze the sources of error and uncertainty in the experiment.



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

Thevenin example

The Thevenin equivalent circuit is:

Thevenin equivalent

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



##### Virtual lab

- A virtual lab is a simulation-based laboratory that allows students to perform experiments online using a computer or a mobile device.
- A virtual lab can provide remote access to labs in various disciplines of science and engineering, such as physics, chemistry, biology, biotechnology, etc.
- A virtual lab can help students retain the real feel of a laboratory, while conducting the experiment from anywhere and anytime, without the need for physical equipment or materials.
- A virtual lab can also enhance the learning outcomes of students by providing interactive animations, graphics, videos, quizzes, and feedback.
- A virtual lab can also reduce the cost and risk of conducting experiments in a real lab, especially for hazardous or expensive experiments.

- One example of a virtual lab is the Amrita Vishwa Vidyapeetham Virtual Lab, which is developed by AmritaCREATE, a research center of Amrita University.
- The Amrita Vishwa Vidyapeetham Virtual Lab consists of over 220 simulation-based experiments in various domains, such as physical sciences, chemical sciences, life sciences, etc.
- The Amrita Vishwa Vidyapeetham Virtual Lab also provides a video channel, a question bank, a discussion forum, and a feedback system for students and teachers.
- The Amrita Vishwa Vidyapeetham Virtual Lab is available at https://vlab.amrita.edu/ and is also part of the Online Labs project, which is a joint initiative of Amrita University and other institutions, supported by the Ministry of Education, Government of India.
- The Online Labs project aims to provide quality virtual labs to students across India and abroad, especially to those who have no access to physical labs or where equipment is scarce or costly.
- The Online Labs project is available at http://www.amrita.olabs.edu.in/ and offers virtual labs in physics, chemistry, and biology for students from class 9 to 12.



##### 3. RLC series resonance.

- An RLC series circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series.
- The circuit has a resonant frequency (f0) at which the impedance (Z) is purely resistive and the current (I) is maximum.
- The resonant frequency is given by the formula: f0 = 1 / (2π√(LC))
- At resonance, the inductive reactance (XL) and the capacitive reactance (XC) are equal and cancel each other out, leaving only the resistance (R) in the circuit.
- The impedance at resonance is given by the formula: Z = R
- The current at resonance is given by the formula: I = V / R, where V is the applied voltage.
- The voltage across each component at resonance is given by the formula: VR = IR, VL = IXL, VC = IXC
- The voltage across the inductor and the capacitor are equal in magnitude but opposite in phase, creating a voltage node at the junction of L and C.
- The power factor at resonance is 1, meaning that the circuit is purely resistive and there is no phase difference between the voltage and the current.
- The quality factor (Q) of the circuit is a measure of how sharp the resonance is, and is given by the formula: Q = XL / R = XC / R = 1 / (R√(C/L))
- The quality factor is inversely proportional to the bandwidth (B) of the circuit, which is the range of frequencies around the resonant frequency where the current is at least 70.7% of its maximum value.
- The bandwidth is given by the formula: B = f0 / Q
- The selectivity of the circuit is a measure of how well the circuit can filter out unwanted frequencies, and is given by the formula: S = f0 / B = Q
- The higher the quality factor, the narrower the bandwidth, the higher the selectivity, and the sharper the resonance.



##### Virtual lab

- Virtual lab is a web-based platform that provides remote access to various experiments in science and engineering disciplines.
- Virtual lab aims to enhance the learning outcomes of students by enabling them to perform experiments in a simulated environment, without the need of physical infrastructure, equipment, or supervision.
- Virtual lab is developed by a consortium of institutions, led by Amrita Vishwa Vidyapeetham, under the National Mission on Education through ICT (NMEICT), Ministry of Education, Government of India.
- Virtual lab covers various domains, such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, civil engineering, etc.
- Virtual lab consists of simulations, animations, graphics, videos, quizzes, and feedback mechanisms to help students understand the concepts and procedures of the experiments.
- Virtual lab also provides a collaborative platform for students and teachers to interact and share their views and doubts.
- Virtual lab is accessible to anyone with an internet-enabled device and a web browser. It is free of cost and does not require any registration or login.



##### 4. Measurement of power in 3- phase circuit by two wattmeter method and determination of its power factor for star as well as delta connected load.

- The two wattmeter method is a technique for measuring the total power in a three-phase circuit using two wattmeters .
- A wattmeter is an instrument that measures the power in a single-phase circuit by multiplying the voltage and current signals.
- In the two wattmeter method, the current coils of the two wattmeters are connected in series with any two line conductors, and the potential coils of each wattmeter are connected to the third line conductor  .
- The connection diagram of two wattmeter method for a star-connected load is shown below:

Two wattmeter method for star-connected load

- The connection diagram of two wattmeter method for a delta-connected load is shown below:

Two wattmeter method for delta-connected load

- The total power in the three-phase circuit is given by the sum of the readings of the two wattmeters, i.e., P = P1 + P2  .
- The power factor of the load is given by the ratio of the total power to the product of the line voltage and the total current, i.e., PF = P / (V L * I L)  .
- The power factor can also be determined by using the formula: PF = cos(φ) = cos(tan^-1(√3 * (P2 - P1) / (P2 + P1))) .
- The power factor is positive if both wattmeters have positive readings, and negative if one of the wattmeters has a negative reading .
- The power factor is unity if both wattmeters have equal readings, and zero if one of the wattmeters has a zero reading .
- The power factor is lagging if the current lags behind the voltage, and leading if the current leads the voltage .
- The two wattmeter method can be used for balanced or unbalanced loads, and for star or delta connected loads .
- The two wattmeter method is simple, accurate, and economical .



##### Virtual lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows students to perform experiments and learn concepts without the need for physical equipment, materials, or space.
- Virtual labs can be used to supplement or replace traditional lab activities, enhance student engagement and understanding, and provide access and flexibility for remote learning.
- Virtual labs can also offer features such as feedback, guidance, hints, scaffolding, and assessment that can enhance the learning experience and outcomes.

##### Dreamweaver

- Dreamweaver is a web development software that allows users to create, edit, and manage websites and web pages.
- Dreamweaver provides a graphical user interface (GUI) that enables users to design web pages visually, as well as a code editor that allows users to write and edit HTML, CSS, JavaScript, and other web languages.
- Dreamweaver also supports features such as templates, site management, preview, testing, debugging, and publishing.

##### Measurement

- Measurement is the process of determining the size, quantity, or degree of something using a standard unit or system.
- Measurement is essential for science, engineering, and technology, as it allows for observation, experimentation, analysis, and communication of phenomena and results.
- Measurement involves using instruments or devices that can detect, display, or record the physical properties or attributes of something, such as length, mass, time, temperature, voltage, current, power, etc.
- Measurement also requires using units or scales that can express the magnitude or value of something, such as meters, kilograms, seconds, degrees Celsius, volts, amperes, watts, etc.
- Measurement can be classified into different types, such as direct, indirect, absolute, relative, scalar, vector, etc., depending on the method, reference, or nature of the measurement.

##### Virtual lab link: http://vp-dei.vlabs.ac.in/Dreamweaver/measurement.html

- This link leads to a virtual lab that demonstrates the measurement of power in AC circuits using different devices, such as ammeter, voltmeter, wattmeter, and power factor meter.
- The virtual lab allows the user to select the type of load (resistive, inductive, or capacitive), the values of the load components, and the supply voltage and frequency.
- The virtual lab then displays the circuit diagram, the phasor diagram, and the values of the current, voltage, power, and power factor for the selected load and supply conditions.
- The virtual lab also provides a theoretical background, a procedure, a quiz, and a feedback form for the user.



Hello, I am Sydney, your AI assistant. I can help you with your studies. Here is the content you requested:

##### 5. Determination of parameters of ac single phase series RLC circuit.

- A series RLC circuit is a circuit that consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series to an alternating current (ac) source.
- The parameters of a series RLC circuit are the resistance (R), the inductance (L), the capacitance (C), the voltage (V), the current (I), the frequency (f), the impedance (Z), the phase angle (φ), the power factor (pf), and the power (P).
- The voltage (V) is the peak value of the sinusoidal voltage source. The current (I) is the peak value of the sinusoidal current that flows through the circuit. The frequency (f) is the number of cycles of the voltage and current per second, measured in hertz (Hz).
- The impedance (Z) is the total opposition to the current flow in the circuit, measured in ohms (Ω). It is given by the formula:

  Z = √(R² + (XL - XC)²)

  where XL is the inductive reactance and XC is the capacitive reactance. XL and XC are given by the formulas:

  XL = 2πfL

  XC = 1/(2πfC)

- The phase angle (φ) is the angle by which the current lags or leads the voltage in the circuit, measured in degrees or radians. It is given by the formula:

  φ = tan⁻¹((XL - XC)/R)

  If XL > XC, the current lags the voltage and φ is positive. If XL < XC, the current leads the voltage and φ is negative. If XL = XC, the current is in phase with the voltage and φ is zero.
- The power factor (pf) is the ratio of the true power to the apparent power in the circuit, measured in a unitless value between 0 and 1. It is given by the formula:

  pf = cos(φ)

  The power factor indicates how efficiently the circuit uses the power supplied by the source. A power factor of 1 means that the circuit uses all the power supplied by the source. A power factor of 0 means that the circuit uses none of the power supplied by the source.
- The power (P) is the rate of energy transfer in the circuit, measured in watts (W). It is given by the formula:

  P = VIpf

  The power is the product of the voltage, the current, and the power factor. The power can also be calculated by the formulas:

  P = I²R

  P = V²/R

  These formulas are valid only when the power factor is 1, which means that the circuit is purely resistive.



##### Virtual lab

- A virtual lab is a simulation-based laboratory that allows students to perform experiments online using a computer or a mobile device.
- A virtual lab can provide remote access to labs in various disciplines of science and engineering, such as physics, chemistry, biology, biotechnology, etc.
- A virtual lab can help students retain the real feel of a laboratory, while conducting the experiment from anywhere and anytime, without the need for physical equipment or materials.
- A virtual lab can also enhance the learning outcomes of students by providing interactive features, such as animations, graphics, videos, quizzes, feedback, etc.
- A virtual lab can also reduce the cost and time of setting up and maintaining a physical lab, as well as the safety and environmental risks associated with some experiments.

- One example of a virtual lab is the Amrita Vishwa Vidyapeetham Virtual Lab, which is a collaborative project of Amrita University, Dayalbagh University, NIT Karnataka, and COE Pune, funded by the Ministry of Education, Government of India.
- The Amrita Vishwa Vidyapeetham Virtual Lab consists of over 220 simulation-based experiments in various domains, such as physical sciences, chemical sciences, life sciences, computer science, etc.
- The Amrita Vishwa Vidyapeetham Virtual Lab also provides a video channel, which has over 1.5 million views and is included in YouTubeEDU, a community of high-quality educational channels on YouTube.
- The Amrita Vishwa Vidyapeetham Virtual Lab aims to universalize education and bridge the gap between institutions that have the physical laboratory and those that do not.

- To access the Amrita Vishwa Vidyapeetham Virtual Lab, you need to visit the website https://vlab.amrita.edu/ and select the domain and experiment of your choice.
- You can also download the Amrita Online Lab app from the Google Play Store or the App Store, which provides offline access to some of the experiments.
- You can also register as a user and log in to the website or the app to track your progress and performance in the experiments.
- You can also contact the support team of the Amrita Vishwa Vidyapeetham Virtual Lab for any queries or feedback through the email address vlab@amrita.edu or the phone number +91-422-2685000.



##### 6. To observe the B-H loop of a ferromagnetic material in CRO.

- A B-H loop is a graphical representation of the relationship between the magnetic flux density (B) and the magnetic field intensity (H) of a ferromagnetic material.
- A ferromagnetic material is one that can be magnetized by an external magnetic field and retain some magnetization even after the field is removed.
- A CRO (cathode ray oscilloscope) is an instrument that can display the variation of an electrical signal on a screen.
- To observe the B-H loop of a ferromagnetic material in CRO, the following steps are followed:

  1. A ferromagnetic material (such as iron) is wound with a primary coil and a secondary coil. The primary coil is connected to an AC source and the secondary coil is connected to the CRO.
  2. The AC source provides a sinusoidal current to the primary coil, which creates a varying magnetic field around the ferromagnetic material. This induces an emf in the secondary coil, which is proportional to the rate of change of magnetic flux.
  3. The CRO is set to display the voltage across the secondary coil (V) on the vertical axis and the current through the primary coil (I) on the horizontal axis. The CRO is also set to trigger on the zero crossing of the current waveform.
  4. As the current and the magnetic field vary sinusoidally, the voltage and the magnetic flux density also vary sinusoidally. However, due to the hysteresis effect of the ferromagnetic material, the voltage and the flux density do not have the same phase and amplitude as the current and the field.
  5. The CRO displays a closed loop on the screen, which is the B-H loop of the ferromagnetic material. The shape and size of the loop depend on the properties of the material and the amplitude of the current.
  6. The B-H loop shows the following features:

    - The loop is symmetrical about the origin, which means that the material behaves the same way in positive and negative fields.
    - The loop has a finite width, which means that the material has a coercivity (Hc), which is the amount of reverse field required to reduce the magnetization to zero.
    - The loop has a finite area, which means that the material has a remanence (Br), which is the amount of residual magnetization left after the field is removed.
    - The loop has a slope, which means that the material has a permeability (μ), which is the ratio of the flux density to the field intensity.
    - The loop has a saturation point, which means that the material has a saturation magnetization (Bs), which is the maximum value of the flux density that the material can attain.

- The B-H loop of a ferromagnetic material in CRO can be used to study the magnetic properties of the material and to compare different materials. It can also be used to design magnetic devices such as transformers, relays, and motors.



##### Virtual lab

- A virtual lab is a simulation-based laboratory that allows students to perform experiments online using a computer or a mobile device.
- A virtual lab can provide remote access to labs in various disciplines of science and engineering, such as physics, chemistry, biology, biotechnology, etc.
- A virtual lab can help students retain the real feel of a laboratory, while conducting the experiment from anywhere and anytime, without the need of physical equipment or materials.
- A virtual lab can also enhance the learning outcomes of students by providing interactive animations, graphics, videos, quizzes, and feedback.
- A virtual lab can also reduce the cost and risk of conducting experiments in a real lab, especially for hazardous or expensive experiments.

- One example of a virtual lab is the Amrita Vishwa Vidyapeetham Virtual Lab, which is developed by AmritaCREATE, a research center of Amrita University.
- The Amrita Vishwa Vidyapeetham Virtual Lab consists of over 220 simulation-based experiments in various domains, such as physical sciences, chemical sciences, life sciences, etc.
- The Amrita Vishwa Vidyapeetham Virtual Lab also provides a video channel with nearly 1.5 million views, which is included in YouTubeEDU, a community of high-quality educational channels on YouTube.
- The Amrita Vishwa Vidyapeetham Virtual Lab is part of the Virtual Amrita Laboratories Universalizing Education (VALUE) project, which is funded by the Ministry of Human Resource Development (MHRD) under the National Mission on Education through Information and Communication Technology (NMEICT) initiative.
- The Amrita Vishwa Vidyapeetham Virtual Lab is also part of the Online Lab project, which is a joint initiative of Amrita University, Dayalbagh University, NIT Karnataka, and COE Pune.

- The link provided by the user is for a specific experiment in the Amrita Vishwa Vidyapeetham Virtual Lab, which is about the verification of Ohm's law using a simple circuit.
- The link contains the following sections: theory, procedure, simulation, video, animation, quiz, and references.
- The link also contains the following objectives: to understand the concept of Ohm's law, to measure the current and voltage across a resistor, to plot the V-I graph, and to calculate the resistance from the slope of the graph.
- The link also contains the following steps: selecting the components, connecting the circuit, adjusting the rheostat, measuring the current and voltage, recording the readings, plotting the graph, and finding the resistance.
- The link also contains the following observations: the current and voltage are directly proportional to each other, the graph is a straight line passing through the origin, and the resistance is constant for a given resistor.



##### 7. Determination of the efficiency of a dc motor by loss summation method (Swinburne's test).

- The efficiency of a dc motor is defined as the ratio of output (mechanical) power to input (electrical) power .
- The efficiency of a dc motor can be determined by direct or indirect methods .
- The direct method requires measuring the input power and the output power on load, which may be difficult or impractical for large machines.
- The indirect method, also known as the loss summation method or Swinburne's test, enables the determination of losses without actually loading the machine .
- The principle of Swinburne's test is to run the dc motor as a no-load generator and measure the input power and the no-load losses .
- The no-load losses consist of the constant losses (iron losses and friction losses) and the variable losses (armature copper losses and brush contact losses) at no load .
- The efficiency of the dc motor at any load can be calculated by subtracting the no-load losses from the input power and dividing by the input power .
- The advantages of Swinburne's test are that it is simple, economical, and does not require a load or a power analyzer .
- The disadvantages of Swinburne's test are that it does not account for the stray load losses, the temperature rise, and the change in the armature resistance due to heating .
- The procedure of Swinburne's test is as follows :
  - Connect the dc motor to a dc supply and a rheostat as shown in the figure below.
  - Adjust the rheostat to obtain the rated voltage and current of the motor.
  - Measure the input power (P<sub>i</sub>) by multiplying the voltage (V) and the current (I).
  - Measure the speed (N) of the motor by using a tachometer.
  - Calculate the no-load armature copper loss (P<sub>acu</sub>) by multiplying the armature resistance (R<sub>a</sub>) and the square of the current (I<sup>2</sup>).
  - Calculate the no-load brush contact loss (P<sub>bc</sub>) by multiplying the brush contact drop (V<sub>b</sub>) and the current (I).
  - Calculate the no-load constant loss (P<sub>c</sub>) by subtracting the armature copper loss and the brush contact loss from the input power (P<sub>i</sub> = P<sub>c</sub> + P<sub>acu</sub> + P<sub>bc</sub>).
  - Calculate the efficiency (η) of the dc motor at any load by using the formula: η = (P<sub>i</sub> - P<sub>c</sub> - kI<sup>2</sup>)/P<sub>i</sub>, where k = R<sub>a</sub> + V<sub>b</sub>/I is a constant.

Swinburne's test circuit diagram

Figure: Swinburne's test circuit diagram



#### Course Outcomes:

- By the end of this course, you will be able to:
  - Identify and explain the basic concepts and principles of artificial intelligence, such as search, knowledge representation, reasoning, planning, learning, and natural language processing.
  - Apply various artificial intelligence techniques and algorithms to solve problems, such as heuristic search, constraint satisfaction, logic, inference, probabilistic models, decision making, neural networks, and machine learning.
  - Evaluate the strengths and limitations of different artificial intelligence approaches and compare their performance and applicability to different domains and scenarios.
  - Implement and test artificial intelligence solutions using appropriate tools and frameworks, such as Python, TensorFlow, PyTorch, scikit-learn, and NLTK.
  - Communicate and present artificial intelligence concepts and solutions effectively using appropriate terminology and formats, such as reports, diagrams, pseudocode, and code.



#### Course Outcome (CO) Bloom’s Level

- A course outcome (CO) is a statement that describes what students should be able to do or demonstrate at the end of a course.
- A CO should be specific, measurable, achievable, relevant, and time-bound (SMART).
- A CO should also align with the program outcomes (POs) and the course objectives (COs).
- A CO should be written using an action verb that indicates the level of cognitive skill required by the students to achieve the outcome.
- Bloom’s taxonomy is a framework that classifies different levels of cognitive skills, from lower-order to higher-order, as follows:
  - Remember: recall or recognize facts, terms, concepts, or procedures.
  - Understand: explain, interpret, summarize, or paraphrase information or ideas.
  - Apply: use knowledge or skills in new or familiar situations or contexts.
  - Analyze: break down information or ideas into components and examine their relationships or interactions.
  - Evaluate: judge, critique, or appraise the value or quality of information, ideas, or arguments based on criteria or standards.
  - Create: generate, produce, or synthesize new or original information, ideas, or products.
- Bloom’s level is the level of cognitive skill that corresponds to the action verb used in the CO.
- For example, if the CO is “Apply the principles of object-oriented programming to design and implement software solutions”, the Bloom’s level is Apply.
- Bloom’s level can be used to assess the level of difficulty and complexity of the CO, and to design appropriate assessment methods and learning activities for the students.



#### At the end of this course, the students should be able to:

- Explain the basic concepts and principles of artificial intelligence, such as agents, search, knowledge representation, reasoning, planning, learning, natural language processing, computer vision, and robotics.
- Apply various AI techniques and algorithms to solve different types of problems, such as search problems, constraint satisfaction problems, logic problems, planning problems, classification problems, and clustering problems.
- Evaluate the strengths and limitations of different AI approaches and methods, such as heuristic search, informed search, adversarial search, propositional logic, first-order logic, resolution, forward chaining, backward chaining, decision trees, neural networks, genetic algorithms, and reinforcement learning.
- Design and implement simple AI systems and applications using Python and relevant libraries and frameworks, such as NumPy, SciPy, scikit-learn, TensorFlow, Keras, PyTorch, NLTK, OpenCV, and ROS.
- Analyze and compare the performance and behavior of different AI systems and applications using appropriate metrics and methods, such as time complexity, space complexity, accuracy, precision, recall, F1-score, confusion matrix, ROC curve, and A/B testing.
- Communicate and present the results and findings of AI projects and experiments using clear and concise language, diagrams, charts, and graphs.



##### CO 1 Conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits. K3

- KVL stands for Kirchhoff's Voltage Law, which states that the algebraic sum of the voltages around any closed loop in a circuit is zero.
- KCL stands for Kirchhoff's Current Law, which states that the algebraic sum of the currents entering and leaving any node in a circuit is zero.
- Network theorems are mathematical tools that can be used to simplify and analyze complex DC circuits. Some of the common network theorems are:
  - Superposition theorem: This theorem states that the response (voltage or current) in any element of a linear circuit is equal to the algebraic sum of the responses caused by each independent source acting alone, while all other independent sources are turned off (replaced by their internal resistances).
  - Thevenin's theorem: This theorem states that any linear circuit with voltage sources and resistances can be replaced by an equivalent circuit consisting of a single voltage source (called Thevenin's voltage) in series with a single resistance (called Thevenin's resistance).
  - Norton's theorem: This theorem states that any linear circuit with current sources and resistances can be replaced by an equivalent circuit consisting of a single current source (called Norton's current) in parallel with a single resistance (called Norton's resistance).
  - Maximum power transfer theorem: This theorem states that the maximum power is transferred from a source to a load when the load resistance is equal to the source resistance (or the Thevenin's or Norton's resistance of the source circuit).
- To conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits, one can follow these steps:
  - Design a circuit with resistors, voltage sources, current sources, and measuring instruments (such as voltmeters, ammeters, and ohmmeters) according to the given specifications or objectives.
  - Connect the circuit components using wires, breadboards, or soldering as per the circuit diagram.
  - Verify the connections and turn on the power supply.
  - Measure the voltages and currents in the circuit using the instruments and record the values in a table.
  - Apply KVL and KCL to the circuit and write the equations relating the voltages and currents in the circuit.
  - Solve the equations using algebraic or matrix methods and compare the results with the measured values.
  - Apply the network theorems to the circuit and find the equivalent circuits, Thevenin's or Norton's parameters, or the maximum power transfer conditions.
  - Verify the network theorems by measuring the voltages and currents in the equivalent circuits or the power delivered to the load and compare them with the theoretical values.
  - Analyze the results and draw conclusions about the validity and usefulness of KVL/KCL and network theorems to DC electrical circuits.
  - Write a report or a presentation summarizing the experiment, the results, and the conclusions.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of CO 2 Demonstrate the behavior of AC circuits connected to single phase AC supply and measure power in single phase as well as three phase electrical circuits. K4. Here is the content I have written for you:

##### CO 2 Demonstrate the behavior of AC circuits connected to single phase AC supply and measure power in single phase as well as three phase electrical circuits. K4

- An AC circuit is a circuit that carries alternating current (AC), which is a current that changes its direction and magnitude periodically. The most common source of AC is the mains electricity, which is a single phase AC supply with a frequency of 50 Hz or 60 Hz depending on the region.
- A single phase AC supply can be represented by a sinusoidal voltage source with a peak value of Vp and a phase angle of θ. The voltage can be expressed as v(t) = Vp sin(ωt + θ), where ω is the angular frequency and t is the time.
- An AC circuit can have different types of elements, such as resistors, capacitors, inductors, or a combination of them. These elements have different behaviors when connected to an AC supply, depending on their impedance, which is a measure of how much they oppose the current flow.
- A resistor has a constant impedance of R ohms, which means it does not affect the phase or the magnitude of the current. The current through a resistor is in phase with the voltage across it, and the power dissipated by a resistor is P = Vrms Irms cos(0) = Vrms Irms, where Vrms and Irms are the root mean square values of the voltage and the current, respectively.
- A capacitor has an impedance of Zc = 1/jωC ohms, where j is the imaginary unit and C is the capacitance. This means that the current through a capacitor leads the voltage across it by 90 degrees, and the power consumed by a capacitor is zero, since P = Vrms Irms cos(90) = 0.
- An inductor has an impedance of Zl = jωL ohms, where L is the inductance. This means that the current through an inductor lags the voltage across it by 90 degrees, and the power consumed by an inductor is also zero, since P = Vrms Irms cos(-90) = 0.
- A combination of these elements can form different types of AC circuits, such as series, parallel, or series-parallel. The total impedance of these circuits can be calculated by using the rules of series and parallel combinations, or by using the phasor method, which represents the voltage and the current as vectors in a complex plane.
- The power in an AC circuit can be divided into three components: active power, reactive power, and apparent power. Active power is the power that is converted into useful work, such as heat, light, or motion. Reactive power is the power that is stored and released by the capacitive and inductive elements, and does not contribute to the useful work. Apparent power is the product of the rms voltage and the rms current, and represents the total power delivered by the source.
- The power factor of an AC circuit is the ratio of the active power to the apparent power, and indicates how efficiently the circuit uses the power. The power factor can range from 0 to 1, and is equal to the cosine of the phase angle between the voltage and the current. A power factor of 1 means that the circuit is purely resistive, and all the power is active. A power factor of 0 means that the circuit is purely reactive, and all the power is reactive. A power factor between 0 and 1 means that the circuit has both resistive and reactive elements, and some power is active and some power is reactive.
- A three phase AC supply is a system of three sinusoidal voltages that are 120 degrees out of phase with each other. A three phase AC supply can deliver more power than a single phase AC supply with the same voltage and current ratings, and is more efficient and reliable. A three phase AC supply can be connected to a three phase load in two ways: star (or Y) connection, or delta (or Δ) connection. In a star connection, one end of each phase is connected to a common point called the neutral, and the other end is connected to the load. In a delta connection, each phase is connected to the next phase in a loop, and the load is connected across the phases.
- The power in a



##### CO 3 Perform experiment illustrating BH curve of magnetic materials. K3

- A BH curve is a plot of magnetic flux density (B) versus magnetic field strength (H) for a given magnetic material.
- The BH curve shows the relationship between the magnetization of the material and the applied magnetic field, and also the history of the material's magnetization.
- The BH curve can be divided into four regions: the initial curve, the saturation region, the hysteresis loop, and the demagnetization curve.
- The initial curve shows the increase in magnetization from zero to the saturation point, where the material reaches its maximum magnetization and cannot be further magnetized by increasing the field .
- The saturation region is the flat part of the curve where the magnetization remains constant regardless of the field.
- The hysteresis loop is the closed curve that forms when the field is reversed and then restored to its original value. It shows the amount of remanent magnetization (the magnetization that remains after the field is removed) and the coercivity (the field required to reduce the magnetization to zero) of the material .
- The demagnetization curve is the part of the curve that shows the decrease in magnetization when the field is reduced from saturation to zero.
- Different magnetic materials have different shapes and sizes of BH curves, depending on their magnetic properties and applications.
- To perform an experiment illustrating the BH curve of a magnetic material, the following steps are required:
  - Prepare a solenoid (a coil of wire) with a core of the magnetic material to be tested, and connect it to a variable power supply and an ammeter to measure the current (which is proportional to the magnetic field strength).
  - Connect a search coil (a smaller coil of wire) around the solenoid, and connect it to a voltmeter to measure the induced voltage (which is proportional to the magnetic flux density).
  - Vary the current in the solenoid from zero to a maximum value and record the corresponding voltage in the search coil. This will give the initial curve of the BH plot.
  - Reverse the current in the solenoid and vary it from the maximum negative value to the maximum positive value and back to the maximum negative value. Record the corresponding voltage in the search coil. This will give the hysteresis loop of the BH plot.
  - Reduce the current in the solenoid from the maximum negative value to zero and record the corresponding voltage in the search coil. This will give the demagnetization curve of the BH plot.
  - Plot the BH curve using the recorded data and analyze the magnetic properties of the material.



##### CO 4 Calculate efficiency of a single phase transformer and DC machine. K4

- Efficiency of a single phase transformer is the ratio of output power to input power, expressed as a percentage.
- The output power is the power delivered to the load, and the input power is the power drawn from the source.
- The efficiency of a single phase transformer depends on the load current and power factor, as well as the losses in the transformer.
- The losses in a single phase transformer are of two types: core losses and copper losses.
- Core losses are the losses due to the alternating magnetic flux in the core, and consist of hysteresis losses and eddy current losses.
- Hysteresis losses are the losses due to the repeated magnetization and demagnetization of the core material, and depend on the frequency, peak flux density, and hysteresis loop area of the core material.
- Eddy current losses are the losses due to the induced currents in the core, and depend on the frequency, peak flux density, cross-sectional area, and resistivity of the core material.
- Copper losses are the losses due to the resistance of the primary and secondary windings, and depend on the load current and the winding resistance.
- The efficiency of a single phase transformer can be calculated by the following formula:

Efficiency of a single phase transformer

where

- P_o is the output power
- P_i is the input power
- P_c is the core loss
- P_w is the copper loss
- V_o is the output voltage
- I_o is the output current
- cos\phi_o is the output power factor
- I_s is the secondary current
- R_o is the equivalent resistance of the primary winding referred to the secondary side
- R_s is the resistance of the secondary winding

- The efficiency of a single phase transformer is maximum when the copper loss is equal to the core loss.
- The efficiency of a single phase transformer can be improved by reducing the core loss and the copper loss.
- The core loss can be reduced by using a core material with low hysteresis loop area and high resistivity, and by laminating the core to reduce eddy currents.
- The copper loss can be reduced by using a larger cross-sectional area of the windings to reduce the resistance, and by using a higher voltage and lower current to reduce the I^2R loss.
- The efficiency of a single phase transformer is typically in the range of 95 - 99 %. For large power transformers with very low losses, the efficiency can be as high as 99.7%.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

##### CO 5 Perform experiments on speed measurement and reversal of direction of three phase induction motor and Identify the type of DC and AC machines based on their construction. K4

- A three phase induction motor is a type of AC machine that converts electrical power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor.
- The speed of a three phase induction motor depends on the frequency of the supply voltage, the number of poles in the stator, and the slip between the rotor and the stator. The speed can be measured by using a tachometer, a stroboscope, or a frequency meter.
- The direction of rotation of a three phase induction motor can be reversed by interchanging any two of the three supply terminals. This changes the phase sequence of the stator currents and reverses the direction of the rotating magnetic field.
- A DC machine is a type of electrical machine that converts electrical power into mechanical power or vice versa by using a commutator and brushes. A DC machine can be classified into two types: DC generator and DC motor.
- A DC generator is a DC machine that converts mechanical power into electrical power by using electromagnetic induction. A DC generator can be classified into two types: separately excited and self-excited. A separately excited DC generator has a constant field current supplied by an external source. A self-excited DC generator has a field current generated by the residual magnetism of the field poles or by a shunt, series, or compound winding.
- A DC motor is a DC machine that converts electrical power into mechanical power by using the interaction of magnetic fields. A DC motor can be classified into two types: shunt and series. A shunt DC motor has a field winding connected in parallel with the armature winding. A series DC motor has a field winding connected in series with the armature winding.
- An AC machine is a type of electrical machine that converts electrical power into mechanical power or vice versa by using alternating currents and voltages. An AC machine can be classified into two types: synchronous and asynchronous. A synchronous AC machine has a constant speed that is proportional to the supply frequency. An asynchronous AC machine has a variable speed that depends on the load and the slip.
- A synchronous AC machine can be used as a generator or a motor. A synchronous generator converts mechanical power into electrical power by using electromagnetic induction. A synchronous motor converts electrical power into mechanical power by using the synchronism of magnetic fields. A synchronous AC machine can be classified into two types: salient pole and cylindrical rotor. A salient pole AC machine has projecting poles on the rotor. A cylindrical rotor AC machine has a smooth cylindrical rotor.
- An asynchronous AC machine can be used as a motor or an induction generator. An induction motor converts electrical power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor. An induction generator converts mechanical power into electrical power by using the slip and the excitation capacitance. An asynchronous AC machine can be classified into two types: squirrel cage and wound rotor. A squirrel cage AC machine has a rotor with short-circuited bars. A wound rotor AC machine has a rotor with slip rings and brushes.



#### K1 – Remember, K2 – Understand, K3 – Apply, K4 – Analyze, K5 – Evaluate, K6 – Create

- These are the six levels of cognitive learning according to Bloom's taxonomy, a framework for classifying educational objectives and outcomes.
- K1 – Remember: This level involves recalling facts, terms, definitions, concepts, or procedures from memory. Examples of verbs that indicate this level are: list, name, define, identify, label, recognize, etc.
- K2 – Understand: This level involves explaining the meaning, interpretation, or summary of information in one's own words. Examples of verbs that indicate this level are: describe, explain, paraphrase, summarize, illustrate, etc.
- K3 – Apply: This level involves using learned information to solve problems or perform tasks in new situations. Examples of verbs that indicate this level are: apply, use, demonstrate, solve, calculate, implement, etc.
- K4 – Analyze: This level involves breaking down information into parts, examining the relationships, causes, effects, or implications of each part, and identifying patterns or trends. Examples of verbs that indicate this level are: analyze, compare, contrast, differentiate, classify, categorize, etc.
- K5 – Evaluate: This level involves making judgments, assessments, or critiques based on criteria, standards, or evidence. Examples of verbs that indicate this level are: evaluate, judge, critique, appraise, argue, justify, etc.
- K6 – Create: This level involves generating, producing, or designing new or original ideas, products, or solutions. Examples of verbs that indicate this level are: create, design, invent, compose, construct, synthesize, etc.

