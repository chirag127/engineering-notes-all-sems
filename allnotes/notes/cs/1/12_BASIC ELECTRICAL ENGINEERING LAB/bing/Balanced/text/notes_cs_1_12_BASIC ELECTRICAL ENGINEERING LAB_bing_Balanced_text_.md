

## LIST OF EXPERIMENTS

- An experiment is a scientific procedure that aims to test a hypothesis, answer a question, or discover something new.
- Experiments usually involve manipulating one or more variables, measuring their effects, and comparing them with a control group.
- Experiments can be classified into different types based on their purpose, design, and execution.
- Some common types of experiments are:

  - **Observational experiment**: An experiment that involves observing and recording the natural or existing behavior of a subject or phenomenon, without any intervention or manipulation. For example, observing the behavior of animals in their natural habitat, or measuring the temperature of a lake over time.
  - **Quasi-experiment**: An experiment that involves comparing two or more groups that are not randomly assigned, but have some similarity or common characteristic. For example, comparing the academic performance of students from different schools, or the health outcomes of patients from different hospitals.
  - **Randomized controlled experiment**: An experiment that involves randomly assigning subjects to two or more groups, and applying a different treatment or intervention to each group, while keeping other factors constant. For example, testing the effectiveness of a new drug by giving it to one group of patients, and giving a placebo to another group of patients, while controlling for age, gender, and medical history.
  - **Factorial experiment**: An experiment that involves manipulating two or more independent variables, and measuring their effects on one or more dependent variables. For example, testing the effects of different levels of temperature and humidity on the growth of plants, or the effects of different types of music and lighting on the mood of customers.
  - **Single-subject experiment**: An experiment that involves applying a treatment or intervention to a single subject, and measuring its effects over time, using a baseline and a post-test. For example, testing the effects of a new therapy on a patient with depression, or the effects of a new training program on an athlete's performance.



### Note: A minimum of ten experiments from the following should be performed.

- Experiment 1: To study the characteristics of a common emitter transistor amplifier.
- Experiment 2: To study the frequency response of a RC coupled amplifier.
- Experiment 3: To design and implement a Hartley oscillator using transistor.
- Experiment 4: To design and implement a Colpitts oscillator using transistor.
- Experiment 5: To design and implement an astable multivibrator using 555 timer IC.
- Experiment 6: To design and implement a monostable multivibrator using 555 timer IC.
- Experiment 7: To design and implement a binary counter using 7490 IC.
- Experiment 8: To design and implement a BCD to seven segment decoder using 7447 IC and display the output on a seven segment LED.
- Experiment 9: To design and implement a 4-bit adder/subtractor using 7483 IC.
- Experiment 10: To design and implement a 4-bit magnitude comparator using 7485 IC.
- Experiment 11: To design and implement a 4-bit shift register using 7495 IC.
- Experiment 12: To design and implement a 4-bit synchronous counter using 7476 IC.
- Experiment 13: To design and implement a 4-bit asynchronous counter using 7473 IC.
- Experiment 14: To design and implement a D flip-flop using NAND gates.
- Experiment 15: To design and implement a JK flip-flop using NAND gates.



#### (A) Hardware based experiments

- Hardware based experiments are experiments that involve the use of physical devices, components, or systems to test a hypothesis, measure a phenomenon, or demonstrate a concept.
- Hardware based experiments can be classified into different types, such as:
  - **Simulation experiments**: These are experiments that use software or hardware models to mimic the behavior of a real system or environment. For example, a flight simulator can be used to test the performance of an aircraft or a pilot under different conditions.
  - **Laboratory experiments**: These are experiments that use controlled settings and equipment to isolate and manipulate variables of interest. For example, a circuit board can be used to test the functionality of an electronic device or a component.
  - **Field experiments**: These are experiments that use natural or artificial settings and conditions to observe or measure the effects of a treatment or intervention. For example, a solar panel can be used to test the efficiency of a renewable energy source or a device.
- Hardware based experiments can have various advantages and disadvantages, such as:
  - **Advantages**:
    - They can provide realistic and accurate data and results that reflect the actual performance or behavior of a system or device.
    - They can allow for direct observation and manipulation of physical phenomena and variables.
    - They can facilitate the development and testing of new technologies and innovations.
  - **Disadvantages**:
    - They can be costly and time-consuming to design, implement, and maintain.
    - They can be affected by external factors and sources of error that are difficult to control or eliminate.
    - They can pose ethical, safety, or environmental risks or challenges.



##### 1. Verification of Kirchhoff’s laws

- Kirchhoff’s laws are two rules that relate the currents and voltages in an electrical circuit.
- Kirchhoff’s current law (KCL) states that the algebraic sum of the currents entering a node (or a closed boundary) is zero.
- Kirchhoff’s voltage law (KVL) states that the algebraic sum of the voltages around a loop (or a closed path) is zero.
- To verify Kirchhoff’s laws experimentally, one can use a simple circuit consisting of a battery, a resistor, and a voltmeter and an ammeter.
- The steps are as follows:
  - Connect the battery, the resistor, the voltmeter, and the ammeter in series, as shown in the figure below.
  - Measure the current (I) through the ammeter and the voltage (V) across the resistor using the voltmeter.
  - Apply KCL at the node where the battery, the resistor, and the ammeter are connected. The current entering the node is equal to the current leaving the node, which is equal to I. Therefore, KCL is verified.
  - Apply KVL around the loop formed by the battery, the resistor, the voltmeter, and the ammeter. The voltage around the loop is equal to the sum of the voltage drops across the components, which is equal to V - I*R, where R is the resistance of the resistor. Therefore, KVL is verified.

```
  +-----+     +-----+     +-----+
  |     |     |     |     |     |
  |     |     |     |     |     |
  |     |     |     |     |     |
  |     |     |     |     |     |
  |     |     |     |     |     |
  +-----+     +-----+     +-----+
    |           |           |
    |           |           |
    |           |           |
    |           |           |
    |           |           |
    +-----------+-----------+
        |               |
        |               |
        |               |
        |               |
        |               |
        V               I
      +---+           +---+
      |   |           |   |
      |   |           |   |
      |   |           |   |
      |   |           |   |
      |   |           |   |
      +---+           +---+
      Voltmeter      Ammeter
```



##### 2. Measurement of power and power factor in a single phase ac series inductive circuit and study improvement of power factor using capacitor

- Power factor for a single-phase in an alternating current circuit is defined as a measure of energy efficiency. It is usually expressed as a number ranging from 0 to 1. It is the ratio of working power (or actual power) to apparent power.
- The value of the power factor for a single-phase is always less than 1. While for a pure resistance circuit, its value is 1. Formula P = W/A where, P is the power factor, W is the working power, and A is the apparent power.
- The power factor in ac circuit may also be defined as: the cosine of the phase angle between voltage and current i.e. cos φ or the ratio of the resistance to impedance cos φ = R/Z or the ratio of the true to apparent power i.e. power factor, cos φ = true power/apparent power.
- Real power, measured in watts, defines the power consumed by the resistive part of a circuit. Then real power, (P) in an AC circuit is the same as power, P in a DC circuit. So just like DC circuits, it is always calculated as I 2 *R, where R is the total resistive component of the circuit.
- Reactive power, measured in volt-amperes reactive (VAR), defines the power stored in and discharged by the inductive and capacitive parts of a circuit. Reactive power is always calculated as I 2 *X, where X is the total reactive component of the circuit.
- Apparent power, measured in volt-amperes (VA), defines the power supplied to the circuit. Apparent power is always calculated as I 2 *Z, where Z is the total impedance of the circuit.
- The power factor can be improved by adding a capacitor in parallel with the inductive load. The capacitor provides a leading current that cancels out some of the lagging current of the inductor. This reduces the phase angle between voltage and current, and increases the power factor.
- To measure the power and power factor in a single phase ac series inductive circuit, we can use a wattmeter, an ammeter, and a voltmeter. The wattmeter measures the true power, the ammeter measures the current, and the voltmeter measures the voltage. The power factor can be calculated as P/(VI), where P is the true power, V is the voltage, and I is the current.
- To study the improvement of power factor using capacitor, we can connect a variable capacitor in parallel with the inductive load and observe the changes in the readings of the wattmeter, ammeter, and voltmeter. As we increase the capacitance, the power factor should increase, the current should decrease, and the voltage should remain constant.



##### 3. Study of phenomenon of resonance in RLC series circuit and obtain resonant frequency.

- A RLC series circuit consists of a resistor (R), an inductor (L) and a capacitor (C) connected in series to an alternating voltage source (V).
- The current (I) in the circuit is the same for all the components, but the voltage across each component (VR, VL and VC) may differ in magnitude and phase.
- The total impedance (Z) of the circuit is given by Z = R + j(XL - XC), where XL = ωL is the inductive reactance, XC = 1/ωC is the capacitive reactance and j is the imaginary unit.
- The phase difference (φ) between the current and the voltage is given by tan φ = (XL - XC)/R.
- The power factor (cos φ) of the circuit is a measure of how efficiently the circuit converts the input voltage to useful power.
- The phenomenon of resonance occurs when the inductive reactance and the capacitive reactance are equal, i.e., XL = XC. This implies that ω = 1/√LC, where ω is the angular frequency of the source.
- The resonant frequency (f) is the frequency at which resonance occurs, i.e., f = ω/2π = 1/2π√LC.
- At resonance, the impedance of the circuit is purely resistive, i.e., Z = R. This means that the current and the voltage are in phase, i.e., φ = 0. The power factor is maximum, i.e., cos φ = 1. The current is maximum, i.e., I = V/R. The voltage across the inductor and the capacitor are equal and opposite, i.e., VL = -VC.
- To study the phenomenon of resonance in a RLC series circuit and obtain the resonant frequency, the following steps can be followed:
  - Connect a RLC series circuit to an alternating voltage source with a variable frequency. Use an ammeter to measure the current, a voltmeter to measure the voltage across the resistor, and an oscilloscope to measure the voltage across the capacitor.
  - Vary the frequency of the source and observe the changes in the current, the voltage across the resistor, and the phase difference between the current and the voltage across the capacitor.
  - Plot a graph of current versus frequency and identify the peak value of the current. This corresponds to the resonant frequency of the circuit.
  - Plot a graph of voltage across the resistor versus frequency and identify the peak value of the voltage. This also corresponds to the resonant frequency of the circuit.
  - Plot a graph of phase difference versus frequency and identify the value of the phase difference at the resonant frequency. This should be zero or very close to zero.
  - Compare the experimental value of the resonant frequency with the theoretical value calculated from the formula f = 1/2π√LC. The values should be in agreement within the experimental errors.



##### 4. Connection and measurement of power consumption of a fluorescent lamp (tube light).

- A fluorescent lamp (tube light) is a type of electric light that uses a gas discharge to produce visible light. The gas inside the tube is ionized by a high voltage applied across the electrodes at the ends of the tube. The ionized gas emits ultraviolet radiation, which is converted into visible light by a phosphor coating on the inner surface of the tube.
- A fluorescent lamp requires a ballast to regulate the current and voltage in the circuit. The ballast can be either magnetic or electronic. A magnetic ballast consists of a transformer, a capacitor, and a starter. An electronic ballast uses a high-frequency oscillator to generate the required voltage and current.
- The power consumption of a fluorescent lamp depends on the wattage rating of the lamp, the type of ballast, and the power factor of the circuit. The power factor is a measure of how efficiently the power is used in the circuit. It is the ratio of the real power (watts) to the apparent power (volt-amperes). A low power factor means that more reactive power is needed to maintain the voltage and current in the circuit, which increases the power losses and the electricity cost.
- To measure the power consumption of a fluorescent lamp, a wattmeter can be used. A wattmeter is a device that measures the real power in a circuit. It has two coils: a current coil and a potential coil. The current coil is connected in series with the load, and the potential coil is connected in parallel with the load. The wattmeter has a pointer that indicates the power on a scale.
- To connect the wattmeter to the fluorescent lamp, the following steps can be followed:

  - Disconnect the power supply from the circuit.
  - Connect one terminal of the current coil to the live wire of the power supply, and the other terminal to one end of the ballast.
  - Connect one terminal of the potential coil to the same end of the ballast, and the other terminal to the neutral wire of the power supply.
  - Connect the other end of the ballast to one electrode of the fluorescent lamp, and the other electrode to the earth wire of the power supply.
  - Reconnect the power supply and switch on the circuit.
  - Observe the reading on the wattmeter, which indicates the power consumption of the fluorescent lamp.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use as study material.

##### 5. Measurement of power in 3- phase circuit by two-wattmeter method and determination of its power factor for star as well as delta connected load.

- The two-wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The two wattmeters are connected across two of the three phase voltages, and their currents are taken from the third phase.
- The total power is given by the sum of the readings of the two wattmeters, and the power factor is given by the ratio of the difference and the sum of the readings.
- For a star-connected load, the two wattmeters are connected as shown below:

star

- The readings of the two wattmeters are given by:

  - W1 = V1I1 cos(θ1 - 30°)
  - W2 = V2I2 cos(θ2 + 30°)

- Where V1 and V2 are the phase voltages, I1 and I2 are the line currents, and θ1 and θ2 are the phase angles between the respective voltages and currents.
- The total power is given by:

  - P = W1 + W2 = V1I1 cos(θ1 - 30°) + V2I2 cos(θ2 + 30°)

- The power factor is given by:

  - PF = (W1 - W2) / (W1 + W2) = (V1I1 cos(θ1 - 30°) - V2I2 cos(θ2 + 30°)) / (V1I1 cos(θ1 - 30°) + V2I2 cos(θ2 + 30°))

- For a balanced star-connected load, the phase voltages and currents are equal, and the phase angles are 120° apart. Therefore, the readings of the two wattmeters are equal, and the power factor is given by:

  - PF = cos(θ - 30°)

- Where θ is the common phase angle between the voltage and current of any phase.
- For a delta-connected load, the two wattmeters are connected as shown below:

delta

- The readings of the two wattmeters are given by:

  - W1 = V1I1 cos(θ1 - 30°)
  - W2 = V2I2 cos(θ2 + 30°)

- Where V1 and V2 are the line voltages, I1 and I2 are the phase currents, and θ1 and θ2 are the phase angles between the respective voltages and currents.
- The total power is given by:

  - P = W1 + W2 = V1I1 cos(θ1 - 30°) + V2I2 cos(θ2 + 30°)

- The power factor is given by:

  - PF = (W1 - W2) / (W1 + W2) = (V1I1 cos(θ1 - 30°) - V2I2 cos(θ2 + 30°)) / (V1I1 cos(θ1 - 30°) + V2I2 cos(θ2 + 30°))

- For a balanced delta-connected load, the line voltages and currents are equal, and the phase angles are 120° apart. Therefore, the readings of the two wattmeters are equal, and the power factor is given by:

  - PF = cos(θ - 30°)

- Where θ is the common phase angle between the voltage and current of any phase.



##### 6. Determination of parameters of ac single phase series RLC circuit

- An ac single phase series RLC circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series to an alternating voltage source (V).
- The current (I) in the circuit is the same for all the components and is given by Ohm's law: I = V/Z, where Z is the total impedance of the circuit.
- The impedance Z is a complex quantity that depends on the frequency (f) of the ac source and the values of R, L, and C. It can be written as: Z = R + jX, where j is the imaginary unit and X is the total reactance of the circuit.
- The reactance X is the sum of the inductive reactance (XL) and the capacitive reactance (XC), which are given by: XL = 2πfL and XC = 1/(2πfC).
- The impedance Z can also be expressed in polar form as: Z = |Z|∠θ, where |Z| is the magnitude of the impedance and θ is the phase angle between the voltage and the current.
- The magnitude of the impedance is given by: |Z| = √(R^2 + X^2) and the phase angle is given by: θ = tan^(-1)(X/R).
- The power factor (pf) of the circuit is the cosine of the phase angle: pf = cos(θ). It indicates how efficiently the circuit converts the ac voltage into useful power.
- The power consumed by the circuit is the product of the voltage, the current, and the power factor: P = V I pf. It is also equal to the sum of the power dissipated by the resistor (PR) and the power stored and released by the inductor and the capacitor (PLC): P = PR + PLC.
- The power dissipated by the resistor is given by: PR = I^2 R. It is always positive and represents the heat loss in the circuit.
- The power stored and released by the inductor and the capacitor is given by: PLC = I^2 X. It is positive when the circuit is inductive (XL > XC) and negative when the circuit is capacitive (XL < XC). It represents the energy that oscillates between the magnetic field of the inductor and the electric field of the capacitor.
- The power factor, the power consumed, and the power dissipated by the resistor can be used to determine the parameters of the circuit, such as R, L, and C, by solving a system of equations. Alternatively, the impedance, the reactance, and the phase angle can be used to determine the parameters by using the formulas given above.



##### 7. Determination of (i) Voltage ratio (ii) polarity and (iii) efficiency by load test of a single phase Transformer

- A single phase transformer is a device that transfers electrical energy from one circuit to another through electromagnetic induction.
- The voltage ratio of a transformer is the ratio of the secondary voltage to the primary voltage. It is also equal to the ratio of the number of turns in the secondary coil to the number of turns in the primary coil.
- The polarity of a transformer is the relative direction of the induced voltages in the primary and secondary coils. It can be determined by the dot convention, which assigns a dot to one terminal of each coil. The dots indicate that the voltages at those terminals have the same polarity at any instant.
- The efficiency of a transformer is the ratio of the output power to the input power. It is also equal to the ratio of the useful power to the total power loss in the transformer.

- To determine the voltage ratio, polarity and efficiency by load test of a single phase transformer, the following steps are followed:

  - Connect the primary winding of the transformer to a variable AC voltage source and the secondary winding to a resistive load and a voltmeter as shown in the figure below.

  - Adjust the primary voltage to a suitable value and measure the secondary voltage and the load current using the voltmeter and an ammeter.

  - Calculate the voltage ratio by dividing the secondary voltage by the primary voltage.

  - To determine the polarity, observe the direction of the deflection of the galvanometer connected across the terminals of the primary and secondary coils. If the deflection is positive, the polarity is additive, meaning the dots are on the same side of the transformer. If the deflection is negative, the polarity is subtractive, meaning the dots are on the opposite sides of the transformer.

  - To determine the efficiency, measure the input power by multiplying the primary voltage and the primary current. Measure the output power by multiplying the secondary voltage and the load current. Calculate the efficiency by dividing the output power by the input power and multiplying by 100%.

  - Repeat the above steps for different values of the load resistance and record the results in a table.

  - Plot a graph of efficiency versus output power and observe the variation of efficiency with load.

Figure



##### 8. Determination of efficiency of a dc shunt motor by load test

- The efficiency of a dc shunt motor is the ratio of the output power to the input power, expressed as a percentage.
- The output power of a dc shunt motor is the product of the torque and the angular speed, measured in watts.
- The input power of a dc shunt motor is the product of the terminal voltage and the armature current, measured in watts.
- The load test is a method of determining the efficiency of a dc shunt motor by applying a variable load to the motor and measuring the corresponding values of torque, speed, voltage and current.
- The load test can be performed using a brake drum, a spring balance, a tachometer, a voltmeter and an ammeter, as shown in the figure below.

Load test of a dc shunt motor

- The procedure of the load test is as follows:
  - Connect the dc shunt motor to the supply and adjust the field rheostat to obtain the rated voltage across the terminals.
  - Start the motor and let it run at no load. Measure the no-load speed, voltage and current and record them.
  - Apply a small load to the motor by tightening the brake drum. Measure the load speed, torque, voltage and current and record them.
  - Repeat the above step for different values of load until the motor reaches its rated current or speed.
  - Calculate the output power, input power and efficiency for each load and plot the efficiency versus output power curve.
  - The maximum efficiency of the motor can be obtained from the peak point of the curve.



##### 9. To study running and speed reversal of a three phase induction motor and record speed in both directions.

- A three phase induction motor is a type of electric motor that converts alternating current (AC) power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor.
- The speed of a three phase induction motor depends on the frequency of the AC supply, the number of poles in the stator, and the slip between the rotor and the stator. The speed can be expressed by the formula:

  `N = (120f / P) * (1 - s)`

  where N is the speed in revolutions per minute (rpm), f is the frequency in hertz (Hz), P is the number of poles, and s is the slip.

- The slip is the difference between the synchronous speed (the speed of the rotating magnetic field) and the actual speed of the rotor. The slip is usually expressed as a percentage of the synchronous speed. The slip can be calculated by the formula:

  `s = (Ns - N) / Ns`

  where Ns is the synchronous speed in rpm, and N is the actual speed in rpm.

- The direction of rotation of a three phase induction motor is determined by the phase sequence of the AC supply. If the phase sequence is R-Y-B, the motor rotates in the clockwise direction. If the phase sequence is reversed to B-Y-R, the motor rotates in the anti-clockwise direction.
- To study the running and speed reversal of a three phase induction motor, the following steps can be followed:

  - Connect the three phase induction motor to a three phase AC supply through a star-delta starter and a reversing switch. The star-delta starter is used to reduce the starting current and the reversing switch is used to change the phase sequence of the supply.
  - Switch on the supply and observe the direction and speed of rotation of the motor. Note down the speed by using a tachometer or a speedometer.
  - Switch off the supply and change the position of the reversing switch. Switch on the supply again and observe the direction and speed of rotation of the motor. Note down the speed by using a tachometer or a speedometer.
  - Compare the speeds in both directions and verify that they are equal or nearly equal. Also verify that the direction of rotation is reversed by changing the phase sequence of the supply.
  - Repeat the experiment for different values of frequency and number of poles by using a frequency converter and a pole changing switch. Note down the speeds in both directions for each case and verify the speed formula.



##### 10. Demonstration of cut-out sections of machines: dc machine, three phase induction machine, single-phase induction machine and synchronous machine.

- A cut-out section of a machine is a part of the machine that is cut or opened to show the internal components and their arrangement.
- Cut-out sections of machines are useful for demonstration and learning purposes, as they help to visualize the structure and working principle of the machines.
- The following are some examples of cut-out sections of machines:

  - DC machine: A DC machine is a device that converts electrical energy into mechanical energy or vice versa, using direct current (DC) as the input or output. A DC machine consists of two main parts: the stator and the rotor. The stator is the stationary part that contains the field windings, which produce a magnetic field. The rotor is the rotating part that contains the armature windings, which carry the current. The commutator and the brushes are used to connect the armature windings to the external circuit and to reverse the direction of the current in the windings every half cycle. A cut-out section of a DC machine shows the commutator-brush arrangement, the field and armature windings, and the air gap between the stator and the rotor.

  - Three phase induction machine: A three phase induction machine is a device that converts electrical energy into mechanical energy or vice versa, using alternating current (AC) as the input or output. A three phase induction machine consists of two main parts: the stator and the rotor. The stator is the stationary part that contains the stator windings, which are connected to a three phase supply and produce a rotating magnetic field. The rotor is the rotating part that contains the rotor windings, which are either short-circuited (squirrel cage rotor) or connected to an external resistance (wound rotor). The rotor windings are induced by the stator magnetic field and produce a torque on the rotor. A cut-out section of a three phase induction machine shows the stator and rotor windings, the air gap between the stator and the rotor, and the type of rotor (squirrel cage or wound).

  - Single-phase induction machine: A single-phase induction machine is a device that converts electrical energy into mechanical energy or vice versa, using single-phase AC as the input or output. A single-phase induction machine consists of two main parts: the stator and the rotor. The stator is the stationary part that contains the stator windings, which are connected to a single-phase supply and produce an alternating magnetic field. The rotor is the rotating part that contains the rotor windings, which are either short-circuited (squirrel cage rotor) or connected to a capacitor (capacitor start or capacitor run rotor). The rotor windings are induced by the stator magnetic field and produce a torque on the rotor. A cut-out section of a single-phase induction machine shows the stator and rotor windings, the air gap between the stator and the rotor, and the type of rotor (squirrel cage or capacitor).

  - Synchronous machine: A synchronous machine is a device that converts electrical energy into mechanical energy or vice versa, using AC as the input or output. A synchronous machine consists of two main parts: the stator and the rotor. The stator is the stationary part that contains the stator windings, which are connected to a three phase supply and produce a rotating magnetic field. The rotor is the rotating part that contains the rotor windings, which are excited by a DC supply and produce a constant magnetic field. The rotor magnetic field synchronizes with the stator magnetic field and rotates at the same speed. A cut-out section of a synchronous machine shows the stator and rotor windings, the air gap between the stator and the rotor, and the slip rings and brushes that connect the rotor windings to the DC supply.



#### (B) Experiments available on virtual lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows users to perform experiments and learn scientific concepts without the need for physical equipment, materials, or safety precautions.
- Virtual labs can be accessed online or offline, and can provide interactive feedback, guidance, and assessment to the users.
- Virtual labs can cover various disciplines and topics, such as physics, chemistry, biology, engineering, mathematics, and computer science.
- Some examples of experiments available on virtual labs are:

  - **Physics**: Measuring the speed of sound in air, exploring the properties of waves, investigating the laws of motion, studying the effects of gravity, magnetism, and electricity, analyzing the behavior of light and optics, etc.
  - **Chemistry**: Performing titrations, acid-base reactions, precipitation reactions, redox reactions, synthesis and decomposition reactions, etc. Measuring the pH, conductivity, and concentration of solutions, identifying unknown substances, etc.
  - **Biology**: Observing the structure and function of cells, tissues, organs, and organ systems, examining the diversity of life forms, exploring the processes of photosynthesis, respiration, digestion, circulation, etc. Investigating the principles of genetics, evolution, ecology, etc.
  - **Engineering**: Designing and testing circuits, bridges, robots, machines, etc. Applying the concepts of mechanics, thermodynamics, fluid dynamics, etc. Evaluating the performance, efficiency, and reliability of engineering systems, etc.
  - **Mathematics**: Solving equations, inequalities, and systems of equations, graphing functions and relations, exploring the properties of shapes, angles, and transformations, etc. Calculating the area, volume, perimeter, and surface area of various figures, etc.
  - **Computer Science**: Writing and executing programs in different languages, such as Python, Java, C++, etc. Learning the basics of algorithms, data structures, logic, and computation, etc. Developing applications, games, websites, etc.



##### 1. Kirchhoff‟s laws.

- Kirchhoff's laws are two rules that relate the currents and voltages in electrical circuits.
- Kirchhoff's current law (KCL) states that the algebraic sum of the currents entering any node (or junction) in a circuit is zero.
- Kirchhoff's voltage law (KVL) states that the algebraic sum of the voltages around any closed loop (or mesh) in a circuit is zero.
- Kirchhoff's laws can be used to analyze complex circuits and find the unknown currents and voltages.
- Kirchhoff's laws are based on the conservation of charge and energy in electrical systems.



##### Virtual Lab

- Virtual Lab is an online platform that provides remote access to various laboratories in science and engineering disciplines.
- Virtual Lab is a collaborative initiative of Amrita Vishwa Vidyapeetham and other institutions, supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality and accessibility of education by providing simulation-based experiments that can be performed from any internet-enabled computer terminal.
- Virtual Lab covers various domains such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, etc.
- Virtual Lab offers the following features and benefits:
  - It allows students to perform experiments in a virtual environment that mimics the real laboratory setting.
  - It provides interactive animations, graphics, videos, and feedback to help students understand the concepts and procedures of the experiments.
  - It enables students to repeat the experiments as many times as they want, without any time or resource constraints.
  - It supports self-learning and self-assessment by providing quizzes, assignments, and reports for each experiment.
  - It complements the existing physical laboratories and enhances the learning outcomes of the students.
  - It reduces the cost and maintenance of physical laboratories and saves the environment from hazardous waste disposal.
- Virtual Lab can be accessed from the following link: http://vlab.amrita.edu/



##### 2. Thevenin Theorem

- Thevenin's theorem is a method of simplifying any linear circuit, regardless of how complex it is, to an equivalent circuit with a single voltage source and a series resistance.  
- Thevenin's theorem can be applied to both AC and DC circuits. 
- Thevenin's theorem can be used to make circuit analysis simpler and to study a circuit's initial-condition and steady-state response. 
- Thevenin's theorem and its dual, Norton's theorem, are widely used in circuit design and analysis. 

The steps to apply Thevenin's theorem are:

1. Remove the load resistor and replace it with an open circuit. 
2. Calculate the Thevenin voltage—the voltage across the open circuit. 
3. Calculate the Thevenin resistance—the equivalent resistance seen from the open circuit terminals. 
4. Replace the original circuit with the Thevenin equivalent circuit—a voltage source equal to the Thevenin voltage in series with a resistor equal to the Thevenin resistance. 
5. Connect the load resistor to the Thevenin equivalent circuit and analyze the circuit as needed.



##### Virtual lab

- A virtual lab is a computer-based simulation of a real laboratory that allows students to perform experiments and learn concepts remotely.
- Virtual labs can provide access to equipment, data, and procedures that may be otherwise unavailable, costly, or hazardous in physical labs.
- Virtual labs can also enhance the learning experience by providing interactive feedback, visualization, and guidance to students.
- One example of a virtual lab is the Amrita Vishwa Vidyapeetham Virtual Lab, which offers online simulations of experiments in various disciplines of science and engineering.
- The Amrita Vishwa Vidyapeetham Virtual Lab has the following objectives:
  - To provide remote access to labs in various disciplines of science and engineering.
  - To enthuse students to conduct experiments by arousing their curiosity.
  - To help them in learning basic and advanced concepts through remote experimentation.
  - To provide a complete learning management system around the virtual labs where the students can avail the various tools for learning, including additional web-resources, video-lectures, animated demonstrations and self evaluation.
  - To share costly equipment and resources, which are otherwise available to limited number of users due to constraints on time and geographical distances.
- The Amrita Vishwa Vidyapeetham Virtual Lab consists of the following domains:
  - Physical Sciences
  - Chemical Sciences
  - Life Sciences
  - Computer Science and Engineering
  - Electrical Engineering
  - Electronics and Communications
  - Mechanical Engineering
  - Biomedical and Biotechnology Engineering
  - Civil Engineering
  - Earth and Environmental Sciences
- Each domain contains several labs that cover different topics and experiments related to that domain. For example, the Physical Sciences domain contains the following labs:
  - Optics Virtual Lab
  - Laser and Optics Virtual Lab
  - Modern Physics Virtual Lab
  - Electricity and Magnetism Virtual Lab
  - Heat and Thermodynamics Virtual Lab
  - Oscillations and Waves Virtual Lab
  - Solid State Physics Virtual Lab
  - Nuclear and Particle Physics Virtual Lab
- Each lab contains a set of experiments that can be accessed through a web browser. Each experiment has the following components:
  - Theory: This section provides the theoretical background and concepts related to the experiment.
  - Procedure: This section provides the step-by-step instructions on how to perform the experiment using the simulation interface.
  - Simulator: This section provides the interactive simulation of the experiment, where the user can manipulate the parameters and observe the results.
  - Quiz: This section provides a set of multiple choice questions to test the user's understanding of the experiment.
  - References: This section provides the links to additional resources and information related to the experiment.
  - Feedback: This section allows the user to provide feedback and suggestions to improve the virtual lab.
- The link provided in the topic is for one of the experiments in the Optics Virtual Lab, which is about the reflection of light by a plane mirror. The user can learn about the laws of reflection, the image formation by a plane mirror, and the concept of virtual image by performing this experiment.



##### 3. RLC series resonance.

- RLC series resonance is a phenomenon that occurs in a circuit containing a resistor (R), an inductor (L), and a capacitor (C) connected in series.
- When the circuit is driven by an alternating voltage source with a frequency that matches the natural frequency of the circuit, the circuit exhibits maximum current and minimum impedance.
- The natural frequency of the circuit is given by the formula:

$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

- At resonance, the inductive reactance and the capacitive reactance cancel each other, and the circuit behaves like a pure resistor with a resistance equal to R.
- The current in the circuit is in phase with the voltage source, and the voltage across each component is proportional to its impedance.
- The voltage across the resistor is equal to the source voltage, the voltage across the inductor leads the current by 90 degrees, and the voltage across the capacitor lags the current by 90 degrees.
- The total voltage across the circuit is the phasor sum of the voltages across each component, and it can be greater than the source voltage. This is called voltage magnification or resonance peak.
- The quality factor (Q) of the circuit is a measure of how sharp the resonance peak is, and it is given by the formula:

$$Q = \frac{f_0}{\Delta f} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

- The bandwidth ($\Delta f$) of the circuit is the range of frequencies for which the current is at least 70.7% of its maximum value. It is inversely proportional to the quality factor and the resistance of the circuit.
- The power factor (pf) of the circuit is the ratio of the real power to the apparent power, and it indicates how efficiently the circuit uses the power supplied by the source. At resonance, the power factor is 1, meaning that the circuit only consumes real power and no reactive power. Away from resonance, the power factor is less than 1, meaning that the circuit consumes both real and reactive power. The power factor can be improved by adding a series or parallel resistor to the circuit.



##### Virtual Lab

- Virtual Lab is an online platform that provides remote access to various laboratories in science and engineering disciplines.
- Virtual Lab is a collaborative initiative of Amrita Vishwa Vidyapeetham and other institutions, supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education and research by providing students and teachers with interactive simulations, animations, videos and assessments of laboratory experiments.
- Virtual Lab covers various domains such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, civil engineering and chemical engineering.
- Virtual Lab allows users to perform experiments in a virtual environment, observe the results, manipulate the parameters, and learn the underlying concepts and principles.
- Virtual Lab also provides feedback, guidance and additional resources to help users understand the experiments better.
- Virtual Lab can be accessed through the website https://vlab.amrita.edu/ or the mobile app Amrita Online Lab.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

##### 4. Measurement of power in 3- phase circuit by two wattmeter method and determination of its power factor for star as well as delta connected load.

- The two wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The two wattmeters are connected across two of the three phase voltages, and their currents are taken from the third phase.
- The total power is given by the sum of the two wattmeter readings, and the power factor is given by the ratio of the difference and the sum of the two wattmeter readings.
- For a star-connected load, the two wattmeter method can be applied as follows:

star

- The phase voltages are V<sub>AN</sub>, V<sub>BN</sub>, and V<sub>CN</sub>, and the line voltages are V<sub>AB</sub>, V<sub>BC</sub>, and V<sub>CA</sub>.
- The phase currents are I<sub>A</sub>, I<sub>B</sub>, and I<sub>C</sub>, and the line currents are the same as the phase currents.
- The phase impedances are Z<sub>A</sub>, Z<sub>B</sub>, and Z<sub>C</sub>, and the phase angles are &phi;<sub>A</sub>, &phi;<sub>B</sub>, and &phi;<sub>C</sub>.
- The power factor angle is &theta; = &phi;<sub>A</sub> + &phi;<sub>B</sub> + &phi;<sub>C</sub>.
- The two wattmeters are W<sub>1</sub> and W<sub>2</sub>, and their readings are P<sub>1</sub> and P<sub>2</sub>.
- The power measured by W<sub>1</sub> is P<sub>1</sub> = V<sub>AB</sub>I<sub>C</sub>cos(&phi;<sub>A</sub> - &phi;<sub>C</sub>).
- The power measured by W<sub>2</sub> is P<sub>2</sub> = V<sub>BC</sub>I<sub>A</sub>cos(&phi;<sub>B</sub> - &phi;<sub>A</sub>).
- The total power is P<sub>T</sub> = P<sub>1</sub> + P<sub>2</sub> = V<sub>AB</sub>I<sub>C</sub>cos(&phi;<sub>A</sub> - &phi;<sub>C</sub>) + V<sub>BC</sub>I<sub>A</sub>cos(&phi;<sub>B</sub> - &phi;<sub>A</sub>).
- The power factor is PF = cos(&theta;) = (P<sub>1</sub> - P<sub>2</sub>) / (P<sub>1</sub> + P<sub>2</sub>) = (V<sub>AB</sub>I<sub>C</sub>cos(&phi;<sub>A</sub> - &phi;<sub>C</sub>) - V<sub>BC</sub>I<sub>A</sub>cos(&phi;<sub>B</sub> - &phi;<sub>A</sub>)) / (V<sub>AB</sub>I<sub>C</sub>cos(&phi;<sub>A</sub> - &phi;<sub>C</sub>) + V<sub>BC</sub>I<sub>A</sub>cos(&phi;<sub>B</sub> - &phi;<sub>A</sub>)).

- For a delta-connected load, the two wattmeter method can be applied as follows:

delta

- The phase voltages are V<sub>AB</sub>, V<sub>BC</sub>, and V<sub>CA</sub>, and the line voltages are V<sub>AN</sub>, V<sub>BN</sub>, and V<sub>CN</sub>.
- The phase currents are I<sub>AB</sub>, I<sub>BC</sub>, and I<sub>CA</sub>, and the line currents are I<sub>A</sub>, I<sub>B</



##### Virtual lab

- A virtual lab is a web-based platform that allows users to perform experiments and simulations online, without the need for physical equipment or facilities.
- Virtual labs can be used for teaching, learning, research, and innovation in various domains of science and engineering.
- Virtual labs can provide access to high-quality educational resources, enhance the learning outcomes, and reduce the cost and time of conducting experiments.
- One example of a virtual lab is the Dreamweaver lab, which is designed to teach the basics of web design and development using Adobe Dreamweaver software.
- The Dreamweaver lab consists of four modules: Introduction, Measurement, Layout, and Interactivity.
- The Measurement module covers the following topics:
  - How to measure the dimensions of web elements using pixels, percentages, and ems.
  - How to use the ruler, grid, and guides tools in Dreamweaver to align and position web elements.
  - How to use the properties panel and the code view to modify the width, height, margin, padding, and border properties of web elements.
  - How to use the box model to understand the relationship between the content, padding, border, and margin areas of web elements.
  - How to use the CSS box-sizing property to change the way the width and height of web elements are calculated.
- The Measurement module includes a pre-test, a theory section, a procedure section, a simulation section, a post-test, and a feedback section.
- The pre-test assesses the user's prior knowledge of the topics covered in the module.
- The theory section provides the conceptual background and the definitions of the key terms and concepts related to the module.
- The procedure section provides the step-by-step instructions on how to perform the simulation using Dreamweaver.
- The simulation section allows the user to practice the skills and concepts learned in the module by creating and modifying a web page using Dreamweaver.
- The post-test evaluates the user's learning outcomes and understanding of the topics covered in the module.
- The feedback section allows the user to rate the module and provide comments and suggestions for improvement.



##### 5. Determination of parameters of ac single phase series RLC circuit.

- A series RLC circuit is a circuit that contains a resistor (R), an inductor (L), and a capacitor (C) connected in series with an alternating current (ac) source.
- The ac source provides a sinusoidal voltage of the form $v_s(t) = V_m \sin(\omega t + \phi)$, where $V_m$ is the peak voltage, $\omega$ is the angular frequency, and $\phi$ is the phase angle.
- The current in the circuit is the same for all components and is given by $i(t) = I_m \sin(\omega t + \theta)$, where $I_m$ is the peak current and $\theta$ is the current phase angle.
- The parameters of the circuit are the resistance $R$, the inductance $L$, the capacitance $C$, the impedance $Z$, the reactance $X$, the phase difference $\delta$, and the power factor $pf$.
- The impedance $Z$ is the total opposition to the current flow in the circuit and is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$, where $X_L = \omega L$ is the inductive reactance and $X_C = \frac{1}{\omega C}$ is the capacitive reactance.
- The reactance $X$ is the net reactance of the circuit and is given by $X = X_L - X_C$.
- The phase difference $\delta$ is the angle between the voltage and the current and is given by $\delta = \theta - \phi$.
- The power factor $pf$ is the ratio of the real power to the apparent power and is given by $pf = \cos \delta = \frac{R}{Z}$.
- The parameters of the circuit can be determined by measuring the voltage and the current and applying the following formulas:

  - $R = Z \cos \delta = Z \frac{v_s(t) \cdot i(t)}{v_s^2(t)}$
  - $L = \frac{X + \sqrt{R^2 + X^2} \sin \delta}{\omega} = \frac{X + Z \sin \delta}{\omega}$
  - $C = \frac{1}{\omega (X - \sqrt{R^2 + X^2} \sin \delta)} = \frac{1}{\omega (X - Z \sin \delta)}$
  - $Z = \frac{V_m}{I_m}$
  - $X = Z \sin \delta = Z \frac{v_s(t) \times i(t)}{v_s(t) \cdot i(t)}$
  - $\delta = \arctan \frac{X}{R} = \arctan \frac{v_s(t) \times i(t)}{v_s(t) \cdot i(t)}$
  - $pf = \frac{R}{Z} = \frac{v_s(t) \cdot i(t)}{v_s^2(t)}$



##### Virtual Lab

- Virtual Lab is an online platform that provides remote access to various laboratories in science and engineering disciplines.
- Virtual Lab is a collaborative initiative of Amrita Vishwa Vidyapeetham and other institutions, supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education and research by providing students and teachers with interactive simulations, animations, videos and assessments of laboratory experiments.
- Virtual Lab covers various domains such as biotechnology, physical sciences, chemical sciences, electrical sciences, mechanical sciences, computer science and engineering, civil engineering and metallurgy.
- Virtual Lab allows users to perform experiments, collect data, analyze results, and draw conclusions in a virtual environment, similar to a real laboratory.
- Virtual Lab also provides feedback, guidance, and additional resources to help users learn the concepts and principles behind the experiments.



##### 6. To observe the B-H loop of a ferromagnetic material in CRO.

- A B-H loop is a graphical representation of the relationship between the magnetic flux density (B) and the magnetic field intensity (H) of a ferromagnetic material.
- A ferromagnetic material is one that can be magnetized by an external magnetic field and retain some magnetization even after the field is removed.
- A CRO (cathode ray oscilloscope) is an electronic device that can display the variation of an electrical signal on a screen.
- To observe the B-H loop of a ferromagnetic material in CRO, the following steps are followed:

  - A ferromagnetic material (such as iron) is wound with a primary coil and a secondary coil. The primary coil is connected to an AC source and a variable resistor. The secondary coil is connected to the horizontal input of the CRO.
  - A search coil is also wound around the ferromagnetic material and connected to the vertical input of the CRO. The search coil is used to measure the magnetic flux density (B) of the material.
  - The AC source is switched on and the variable resistor is adjusted to vary the current in the primary coil. This changes the magnetic field intensity (H) of the material.
  - The CRO is set to display the variation of B and H on the screen. A Lissajous figure is obtained, which is a closed curve that represents the B-H loop of the ferromagnetic material.
  - The shape and size of the B-H loop depend on the properties of the material, such as its coercivity, remanence, saturation magnetization, and hysteresis loss.
  - The coercivity is the value of H required to reduce B to zero. The remanence is the value of B that remains after H is reduced to zero. The saturation magnetization is the maximum value of B that can be achieved by increasing H. The hysteresis loss is the energy dissipated as heat in the material due to the repeated reversal of its magnetization.
  - The B-H loop of a ferromagnetic material is shown below:

  ```
  |B
  |    /\
  |   /  \
  |  /    \
  | /      \    B_r
  |/        \_______
  |         |       \
  |         |        \
  |         |         \
  |         |          \
  |_________|___________\_________________ H
           -H_c         0                H_c
  ```

  - In the figure, B_r is the remanence, H_c is the coercivity, and the area enclosed by the loop is the hysteresis loss. The loop is symmetrical about the origin and the B-axis. The loop is wider for materials with higher coercivity and remanence, and narrower for materials with lower coercivity and remanence. The loop is also taller for materials with higher saturation magnetization and lower for materials with lower saturation magnetization. The loop is more rectangular for materials with higher hysteresis loss and more elliptical for materials with lower hysteresis loss.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of virtual lab. Here is the content:

# Virtual Lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows users to perform experiments, collect data, and analyze results without the need for physical equipment, materials, or space.
- A virtual lab can have various advantages, such as:
  - Reducing the cost, time, and risk of conducting experiments that may be dangerous, expensive, or inaccessible in real life.
  - Enhancing the learning outcomes and motivation of students by providing interactive, engaging, and personalized feedback.
  - Enabling the exploration of phenomena that are too complex, fast, slow, or small to observe directly in real life.
  - Supporting the development of scientific inquiry skills, such as hypothesis testing, data analysis, and problem-solving.
- A virtual lab can also have some limitations, such as:
  - Lacking the authenticity, realism, and unpredictability of a real laboratory environment.
  - Requiring adequate technological infrastructure, such as computers, internet access, and software.
  - Depending on the quality and accuracy of the simulation design and implementation.
  - Needing proper guidance and scaffolding from instructors or peers to ensure effective learning and avoid misconceptions.

## Example of a Virtual Lab

- One example of a virtual lab is the [Amrita Virtual Lab](https://vlab.amrita.edu/), which is a web-based platform that provides simulations of various experiments in science and engineering disciplines, such as physics, chemistry, biology, biotechnology, and computer science.
- The Amrita Virtual Lab aims to provide a comprehensive and interactive learning experience for students and teachers, by offering features such as:
  - Theory, procedure, animation, video, and quiz sections for each experiment.
  - A virtual lab manual that explains the objectives, principles, and steps of each experiment.
  - A virtual lab kit that allows users to manipulate the parameters and variables of each experiment.
  - A virtual lab notebook that records the observations, calculations, and results of each experiment.
  - A feedback and evaluation system that assesses the performance and understanding of each user.
- The Amrita Virtual Lab covers a wide range of topics and concepts, such as:
  - Newton's laws of motion, simple harmonic motion, optics, sound, heat, electricity, and magnetism in physics.
  - Acid-base titration, electrochemistry, chromatography, spectroscopy, and organic synthesis in chemistry.
  - Cell structure and function, molecular biology, genetics, microbiology, immunology, and ecology in biology.
  - DNA fingerprinting, PCR, gel electrophoresis, enzyme kinetics, and fermentation in biotechnology.
  - Data structures, algorithms, programming languages, databases, and networks in computer science.



##### 7. Determination of the efficiency of a dc motor by loss summation method (Swinburne's test).

- The efficiency of a dc motor is defined as the ratio of output (mechanical) power to input (electrical) power.
- The output power of a dc motor can be measured by using a dynamometer or a brake, and the input power can be measured by using a power analyzer or a wattmeter.
- However, this direct method of measuring the efficiency requires loading the motor to its rated capacity, which may not be feasible or economical for large motors.
- Therefore, an indirect method of measuring the efficiency is preferred, which is based on determining the losses of the motor instead of the output power.
- The losses of a dc motor can be classified into two categories: constant losses and variable losses.
- Constant losses are those losses that do not depend on the load current, such as core loss, friction loss and windage loss.
- Variable losses are those losses that depend on the load current, such as armature copper loss and field copper loss.
- The total loss of a dc motor can be expressed as the sum of the constant losses and the variable losses.
- The efficiency of a dc motor can be calculated by subtracting the total loss from the input power, or by using the following formula:

$$\eta = \frac{P_{out}}{P_{in}} = \frac{P_{in} - P_{loss}}{P_{in}} = 1 - \frac{P_{loss}}{P_{in}}$$

- Swinburne's test is an indirect method of measuring the efficiency of a dc motor by loss summation method.
- In this test, the motor is run at no load and rated speed, and the no load current and voltage are measured.
- The input power at no load is equal to the constant losses of the motor, since the variable losses are negligible at no load.
- The armature copper loss at any load can be calculated by using the armature resistance and the load current.
- The field copper loss can be assumed to be constant, since the field current is usually constant for a shunt or a compound motor.
- The total loss at any load can be obtained by adding the constant losses and the variable losses.
- The efficiency at any load can be calculated by using the formula given above.
- The advantages of Swinburne's test are that it is simple, convenient and economical, as it does not require loading the motor or measuring the output power.
- The disadvantages of Swinburne's test are that it does not account for the temperature rise and the stray load losses of the motor, which may affect the accuracy of the efficiency calculation.



#### Course Outcomes:

- By the end of this course, you will be able to:
  - Identify and explain the basic concepts and principles of artificial intelligence, such as search, knowledge representation, reasoning, planning, learning, and natural language processing.
  - Apply various artificial intelligence techniques and algorithms to solve problems and tasks, such as heuristic search, constraint satisfaction, logic programming, probabilistic inference, decision making, neural networks, and machine translation.
  - Evaluate the strengths and limitations of different artificial intelligence approaches and methods, and compare their performance and applicability to different domains and scenarios.
  - Design and implement simple artificial intelligence systems and applications, using appropriate tools and frameworks, such as Python, Prolog, TensorFlow, and NLTK.
  - Demonstrate ethical awareness and social responsibility when developing and using artificial intelligence systems and applications, and consider their potential impacts and implications on individuals, society, and the environment.



#### Course Outcome (CO) Bloom's Level

- A course outcome (CO) is a statement that describes what a student should be able to do or demonstrate after completing a course.
- A CO should be specific, measurable, achievable, relevant, and time-bound (SMART).
- A CO should align with the course objectives, content, activities, and assessments.
- A CO should also reflect the level of cognitive skills that a student is expected to develop and apply in the course.
- Bloom's taxonomy is a framework that classifies different levels of cognitive skills, from lower-order to higher-order, as follows:
  - Remember: recall facts and basic concepts
  - Understand: explain ideas or concepts
  - Apply: use information in new situations
  - Analyze: break down information into parts and examine relationships
  - Evaluate: justify a decision or course of action
  - Create: generate new ideas, products, or ways of doing things
- Bloom's level is a way of indicating the level of cognitive skills that a CO requires from a student.
- For example, a CO that states "Students will be able to identify the main components of a computer system" has a Bloom's level of Remember, while a CO that states "Students will be able to design and implement a simple program using a programming language" has a Bloom's level of Create.
- Bloom's level can help instructors to design appropriate learning activities and assessments that match the COs of the course.
- Bloom's level can also help students to understand the expectations and learning outcomes of the course.



#### At the end of this course, the students should be able to:

- Explain the basic concepts and principles of artificial intelligence, such as agents, search, knowledge representation, reasoning, planning, learning, natural language processing, computer vision, and robotics.
- Apply various AI techniques and algorithms to solve different types of problems, such as search problems, constraint satisfaction problems, logic problems, planning problems, classification problems, and natural language problems.
- Evaluate the strengths and limitations of different AI approaches and methods, and compare their performance and applicability to different domains and scenarios.
- Design and implement simple AI systems and applications using Python and relevant libraries and frameworks, such as NumPy, SciPy, scikit-learn, TensorFlow, PyTorch, NLTK, OpenCV, and ROS.
- Demonstrate ethical awareness and critical thinking skills when developing and using AI systems and applications, and consider the social and ethical implications of AI on human society and the environment.



##### CO 1 Conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits. K3

- KVL stands for Kirchhoff's Voltage Law, which states that the algebraic sum of the voltages around any closed loop in a circuit is zero.
- KCL stands for Kirchhoff's Current Law, which states that the algebraic sum of the currents entering and leaving any node in a circuit is zero.
- Network theorems are mathematical tools that can be used to simplify and analyze complex DC circuits. Some of the common network theorems are:
  - Superposition theorem: The voltage or current in any branch of a linear circuit is equal to the algebraic sum of the voltages or currents produced by each source acting alone, with all other sources replaced by their internal resistances.
  - Thevenin's theorem: Any linear circuit with two terminals can be replaced by an equivalent circuit consisting of a voltage source in series with a resistor, where the voltage source is equal to the open-circuit voltage across the terminals and the resistor is equal to the equivalent resistance seen from the terminals.
  - Norton's theorem: Any linear circuit with two terminals can be replaced by an equivalent circuit consisting of a current source in parallel with a resistor, where the current source is equal to the short-circuit current across the terminals and the resistor is equal to the equivalent resistance seen from the terminals.
  - Maximum power transfer theorem: The maximum power is transferred from a source to a load when the load resistance is equal to the source resistance.
  - Reciprocity theorem: The current in any branch of a linear, bilateral network due to a single voltage source in another branch is equal to the current in the second branch due to the same voltage source in the first branch, with all other sources replaced by their internal resistances.
- To conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits, one can follow these steps:
  - Design and construct a DC circuit using resistors, voltage sources, current sources, ammeters, voltmeters, and switches as needed.
  - Apply KVL and KCL to the circuit and write the equations for the voltages and currents in each branch and node.
  - Solve the equations using algebraic or matrix methods and compare the results with the measured values using the meters.
  - Verify the validity of the network theorems by replacing the circuit or parts of it with equivalent circuits and measuring the voltages and currents again.
  - Observe the effects of changing the values of the resistors, sources, and loads on the circuit behavior and power transfer.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write on the topic of CO 2 Demonstrate the behavior of AC circuits connected to single phase AC supply and measure power in single phase as well as three phase electrical circuits. K4. Here is the content I have written in markdown format:

##### CO 2 Demonstrate the behavior of AC circuits connected to single phase AC supply and measure power in single phase as well as three phase electrical circuits. K4

- An AC circuit is a circuit that carries alternating current (AC), which means the current changes direction periodically. The frequency of the current is measured in hertz (Hz), which is the number of cycles per second.
- A single phase AC supply is a type of AC supply that has only one voltage waveform. It is commonly used for domestic and commercial applications. A single phase AC supply can be represented by a sinusoidal voltage source with a peak value of Vp and a frequency of f.
- A three phase AC supply is a type of AC supply that has three voltage waveforms that are 120 degrees out of phase with each other. It is commonly used for industrial and high power applications. A three phase AC supply can be represented by three sinusoidal voltage sources with the same peak value of Vp and frequency of f, but with different phase angles of 0, 120, and 240 degrees.
- An AC circuit can be connected to a single phase AC supply or a three phase AC supply depending on the type and number of loads. A load is a device that consumes electrical power, such as a resistor, a capacitor, an inductor, or a combination of them.
- The behavior of an AC circuit depends on the impedance of the load, which is the opposition to the flow of AC current. The impedance of a load can be calculated by using the formula Z = R + jX, where R is the resistance, j is the imaginary unit, and X is the reactance. The reactance of a load depends on the frequency of the AC supply and the type of load. The reactance of a resistor is zero, the reactance of a capacitor is negative, and the reactance of an inductor is positive.
- The impedance of a load can also be expressed in polar form as Z = |Z|∠θ, where |Z| is the magnitude of the impedance and θ is the phase angle. The phase angle is the angle between the voltage and the current in the load. The phase angle can be positive, negative, or zero depending on the type of load. A positive phase angle means the current lags behind the voltage, a negative phase angle means the current leads ahead of the voltage, and a zero phase angle means the current and the voltage are in phase.
- The power in an AC circuit is the rate of energy transfer from the AC supply to the load. The power in an AC circuit can be calculated by using the formula P = VIcosφ, where V is the rms voltage, I is the rms current, and φ is the power factor angle. The power factor angle is the angle between the voltage and the current in the AC supply. The power factor angle can be equal to, greater than, or less than the phase angle depending on the type of load. The power factor is the cosine of the power factor angle, and it is a measure of how efficiently the AC circuit uses the power from the AC supply. The power factor can range from 0 to 1, where 1 means the AC circuit uses the power most efficiently and 0 means the AC circuit uses the power least efficiently.
- The power in a single phase AC circuit can be measured by using a wattmeter, which is a device that measures the product of the voltage and the current in the AC circuit. The wattmeter has two coils, one connected in series with the load and one connected in parallel with the load. The wattmeter shows the power in watts (W) on a scale.
- The power in a three phase AC circuit can be measured by using two or three wattmeters, depending on the type of connection of the load. The load can be connected in star (Y) or delta (Δ) configuration. In a star connection, the load has three terminals that are connected to the three phase AC supply, and one common terminal that is connected to the neutral point. In a delta connection, the load has three terminals that are connected to the three phase AC supply, and no common terminal. The power in a three phase AC circuit can be calculated by using the formula P = √3VIcosφ, where V is the line voltage, I is the line current, and φ is the power



##### CO 3 Perform experiment illustrating BH curve of magnetic materials. K3

- The objective of this experiment is to illustrate the BH curve of magnetic materials, which shows the relationship between magnetic field strength (H) and magnetic flux density (B) in a material.
- The experiment requires the following apparatus: a solenoid, a variable DC power supply, an ammeter, a voltmeter, a Hall probe, and a magnetic material sample (such as iron, steel, or nickel).
- The procedure of the experiment is as follows:
  - Connect the solenoid to the power supply and the ammeter, and place the Hall probe inside the solenoid.
  - Insert the magnetic material sample inside the solenoid, and adjust the power supply to vary the current through the solenoid.
  - Measure the current (I) through the solenoid and the voltage (V) across the Hall probe, and record the values in a table.
  - Repeat the steps for different values of current, both in the positive and negative directions, until the magnetic material sample is magnetized and demagnetized.
  - Calculate the magnetic field strength (H) inside the solenoid using the formula H = NI/L, where N is the number of turns of the solenoid, I is the current, and L is the length of the solenoid.
  - Calculate the magnetic flux density (B) inside the solenoid using the formula B = V/R, where V is the voltage across the Hall probe, and R is the Hall coefficient of the probe.
  - Plot the BH curve of the magnetic material sample by taking H as the x-axis and B as the y-axis, and label the curve with the name of the material.
  - Observe the shape and features of the BH curve, such as the saturation point, the coercivity, the remanence, and the hysteresis loop.
  - Compare the BH curves of different magnetic materials, and explain the differences in terms of their magnetic properties and applications.



##### CO 4 Calculate efficiency of a single phase transformer and DC machine. K4

- Efficiency is the ratio of output power to input power, expressed as a percentage.
- To calculate the efficiency of a single phase transformer, we need to know the output voltage, output current, input voltage, input current, and the losses in the transformer.
- The output power of a transformer is given by Pout = Vout x Iout, where Vout is the output voltage and Iout is the output current.
- The input power of a transformer is given by Pin = Vin x Iin, where Vin is the input voltage and Iin is the input current.
- The losses in a transformer consist of two types: core losses and copper losses.
- Core losses are due to the hysteresis and eddy currents in the magnetic core of the transformer, and they are constant for a given frequency and flux density.
- Copper losses are due to the resistance of the windings, and they vary with the load current.
- The core losses can be measured by performing an open-circuit test, where the secondary winding is left open and the primary winding is connected to a variable voltage source. The input power in this case is equal to the core losses.
- The copper losses can be measured by performing a short-circuit test, where the secondary winding is shorted and the primary winding is connected to a variable voltage source. The input power in this case is equal to the copper losses.
- The efficiency of a transformer can be calculated by using the formula:

  Efficiency = (Pout / Pin) x 100%

  where Pin = Pout + core losses + copper losses

- To calculate the efficiency of a DC machine, we need to know the output power, input power, and the losses in the machine.
- The output power of a DC machine is given by Pout = V x I, where V is the terminal voltage and I is the load current.
- The input power of a DC machine is given by Pin = E x Ia, where E is the induced emf and Ia is the armature current.
- The losses in a DC machine consist of three types: copper losses, iron losses, and mechanical losses.
- Copper losses are due to the resistance of the armature and the field windings, and they vary with the load current.
- Iron losses are due to the hysteresis and eddy currents in the magnetic core of the machine, and they are constant for a given speed and flux.
- Mechanical losses are due to the friction and windage in the bearings and the air gap, and they are constant for a given speed.
- The copper losses can be calculated by using the formula:

  Copper losses = Ia^2 x Ra + If^2 x Rf

  where Ra is the armature resistance and Rf is the field resistance.

- The iron losses can be measured by performing a no-load test, where the machine is run at rated speed and voltage with no load. The input power in this case is equal to the iron losses plus the mechanical losses.
- The mechanical losses can be measured by performing a blocked-rotor test, where the machine is run at rated voltage with the rotor locked. The input power in this case is equal to the copper losses plus the mechanical losses.
- The efficiency of a DC machine can be calculated by using the formula:

  Efficiency = (Pout / Pin) x 100%

  where Pin = Pout + copper losses + iron losses + mechanical losses



##### CO 5 Perform experiments on speed measurement and reversal of direction of three phase induction motor and Identify the type of DC and AC machines based on their construction. K4

- To perform experiments on speed measurement and reversal of direction of three phase induction motor, the following steps are required:

  - Connect the three phase induction motor to a three phase supply and a tachometer to measure the speed of the motor.
  - Start the motor and observe the speed and direction of rotation of the motor.
  - To reverse the direction of rotation of the motor, interchange any two of the supply lines and restart the motor. Observe the change in the speed and direction of rotation of the motor.
  - To vary the speed of the motor, connect a variable frequency drive (VFD) to the supply and adjust the frequency of the supply. Observe the change in the speed of the motor.

- To identify the type of DC and AC machines based on their construction, the following features are to be noted:

  - DC machines have a commutator and brushes, while AC machines do not have them.
  - DC machines have a constant magnetic field produced by permanent magnets or field coils, while AC machines have a rotating magnetic field produced by stator windings.
  - DC machines have armature windings on the rotor, while AC machines have armature windings on the stator or the rotor depending on the type of the machine.
  - DC machines can be classified into shunt, series, and compound types based on the connection of the field and armature windings, while AC machines can be classified into synchronous and asynchronous types based on the speed of the rotor relative to the stator.



#### K1 – Remember, K2 – Understand, K3 – Apply, K4 – Analyze, K5 – Evaluate, K6 – Create

- These are the six levels of cognitive learning according to Bloom's taxonomy, a framework for classifying educational objectives and outcomes.
- K1 – Remember: This level involves recalling facts, terms, definitions, concepts, or procedures from memory. Examples of verbs used at this level are: define, list, name, identify, label, recognize, etc.
- K2 – Understand: This level involves explaining the meaning, interpretation, or summary of information in one's own words. Examples of verbs used at this level are: describe, explain, paraphrase, summarize, illustrate, classify, etc.
- K3 – Apply: This level involves using learned information to solve problems or perform tasks in new situations. Examples of verbs used at this level are: apply, demonstrate, use, calculate, solve, implement, etc.
- K4 – Analyze: This level involves breaking down information into parts, examining the relationships, causes, effects, or implications of each part, and identifying patterns or trends. Examples of verbs used at this level are: analyze, compare, contrast, differentiate, distinguish, examine, etc.
- K5 – Evaluate: This level involves making judgments, assessments, or critiques of information based on criteria, standards, or evidence. Examples of verbs used at this level are: evaluate, judge, critique, appraise, argue, justify, etc.
- K6 – Create: This level involves generating, producing, or designing new or original ideas, products, or solutions based on information or knowledge. Examples of verbs used at this level are: create, design, invent, compose, construct, synthesize, etc.

