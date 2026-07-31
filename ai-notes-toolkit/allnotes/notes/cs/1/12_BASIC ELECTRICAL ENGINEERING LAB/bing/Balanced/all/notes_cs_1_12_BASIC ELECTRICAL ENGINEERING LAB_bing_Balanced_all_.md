

## LIST OF EXPERIMENTS

- An experiment is a scientific procedure that is carried out to test a hypothesis, observe a phenomenon, or measure a variable.
- Experiments usually involve manipulating one or more independent variables and measuring their effects on one or more dependent variables.
- Experiments can be classified into different types based on their design, purpose, or outcome, such as:

  - Controlled experiments: These are experiments where all the variables except the independent variable are kept constant or controlled. This allows the experimenter to isolate the causal effect of the independent variable on the dependent variable. For example, a controlled experiment to test the effect of light on plant growth would involve growing plants in identical conditions except for the amount of light they receive.
  - Randomized experiments: These are experiments where the participants or units are randomly assigned to different groups or conditions. This ensures that the groups are comparable and reduces the bias or confounding factors that may affect the results. For example, a randomized experiment to test the effect of a new drug on blood pressure would involve randomly assigning patients to either receive the drug or a placebo.
  - Natural experiments: These are experiments where the independent variable is not manipulated by the experimenter, but rather changes naturally or by chance. This allows the experimenter to observe the effect of the independent variable on the dependent variable in a real-world setting. For example, a natural experiment to test the effect of a volcanic eruption on climate would involve comparing the temperature and precipitation data before and after the eruption.
  - Quasi-experiments: These are experiments where the independent variable is manipulated by the experimenter, but the participants or units are not randomly assigned to different groups or conditions. This may be due to ethical, practical, or historical reasons. This limits the ability of the experimenter to draw causal inferences from the results. For example, a quasi-experiment to test the effect of a new curriculum on student achievement would involve comparing the test scores of students who received the new curriculum with those who did not, but without randomizing the schools or classes.
  - Field experiments: These are experiments that are conducted in a natural or realistic setting, rather than in a laboratory or controlled environment. This increases the ecological validity or generalizability of the results, but also introduces more variability and noise that may affect the results. For example, a field experiment to test the effect of a social media campaign on voter turnout would involve randomly assigning different regions or communities to receive or not receive the campaign messages, and then measuring the voter turnout in each region or community.



# A minimum of ten experiments from the following should be performed.

- Experiment 1: To study the characteristics of a common emitter transistor amplifier.
- Experiment 2: To study the frequency response of a RC coupled amplifier.
- Experiment 3: To study the feedback in amplifiers and measure the gain, bandwidth and input impedance with and without feedback.
- Experiment 4: To design and test a Hartley oscillator for a given frequency of oscillation.
- Experiment 5: To design and test a Colpitts oscillator for a given frequency of oscillation.
- Experiment 6: To design and test a phase shift oscillator for a given frequency of oscillation.
- Experiment 7: To design and test a Wein bridge oscillator for a given frequency of oscillation.
- Experiment 8: To study the operation of a clipper circuit for different reference voltages and clipping levels.
- Experiment 9: To study the operation of a clamper circuit for positive and negative peak clamping.
- Experiment 10: To study the operation of a voltage multiplier circuit and measure the output voltage for different number of stages.
- Experiment 11: To design and test a half wave rectifier circuit with and without filter and measure the ripple factor and efficiency.
- Experiment 12: To design and test a full wave rectifier circuit with and without filter and measure the ripple factor and efficiency.
- Experiment 13: To design and test a bridge rectifier circuit with and without filter and measure the ripple factor and efficiency.
- Experiment 14: To design and test a voltage regulator circuit using zener diode and measure the output voltage and load regulation.
- Experiment 15: To design and test a voltage regulator circuit using IC 7805 and measure the output voltage and load regulation.



#### (A) Hardware based experiments

Hardware based experiments are experiments that involve the use of physical devices, components, or systems to test a hypothesis, demonstrate a principle, or perform a task. Hardware based experiments can be classified into different types, such as:

- **Simulation experiments**: These are experiments that use hardware to model or mimic the behavior of a real-world system or phenomenon, such as a flight simulator, a circuit simulator, or a robotic arm. Simulation experiments can be used to study the effects of different parameters, inputs, or scenarios on the system or phenomenon, without affecting the actual system or phenomenon.
- **Measurement experiments**: These are experiments that use hardware to measure or record some physical quantities, such as voltage, current, temperature, pressure, or speed. Measurement experiments can be used to verify or validate a theory, a design, or a specification, or to compare different systems or methods.
- **Design experiments**: These are experiments that use hardware to create or modify a system or a component, such as a circuit, a device, or a prototype. Design experiments can be used to test the functionality, performance, or feasibility of a system or a component, or to optimize or improve its characteristics or features.
- **Demonstration experiments**: These are experiments that use hardware to illustrate or explain a concept, a principle, or a phenomenon, such as a pendulum, a magnet, or a solar panel. Demonstration experiments can be used to enhance the understanding, interest, or engagement of the audience or the learners.

Some examples of hardware based experiments are:

- Building and testing a simple electric motor using a battery, a coil, a magnet, and a switch.
- Measuring the resistance, capacitance, and inductance of different components using a multimeter and an oscilloscope.
- Designing and implementing a digital clock using logic gates, flip-flops, and LEDs.
- Demonstrating the principle of conservation of energy using a ball, a ramp, and a spring.



# Verification of Kirchhoff’s laws

Kirchhoff’s laws are two rules that describe the conservation of electric current and electric potential in electrical circuits. They are named after Gustav Kirchhoff, a German physicist who formulated them in 1845. The laws are:

- Kirchhoff’s current law (KCL): The algebraic sum of all currents entering and exiting a node must equal zero. This means that the amount of charge flowing into a junction is equal to the amount of charge flowing out of it.   

- Kirchhoff’s voltage law (KVL): The algebraic sum of all the voltages around a closed loop must equal zero. This means that the total energy gained or lost by the charges in a circuit loop is zero.   

To verify these laws experimentally, we need the following apparatus:

- A DC power supply
- A voltmeter
- An ammeter
- Resistors of different values
- Connecting wires
- A breadboard or a circuit board

The procedure is as follows:

- Connect the power supply, the voltmeter, the ammeter and the resistors in series and parallel combinations according to a given circuit diagram. Make sure the polarity of the devices is correct and the connections are tight.
- Switch on the power supply and adjust the voltage to a suitable value.
- Measure the current at each branch and the voltage across each resistor using the ammeter and the voltmeter respectively. Record the readings in a table.
- Apply KCL at each node and KVL at each loop and check if the equations are satisfied. If the equations are not satisfied, there may be some errors in the measurements or the connections.   

Some examples of circuit diagrams and the corresponding KCL and KVL equations are shown below:

Circuit 1

KCL at node A: I1 = I2 + I3

KVL at loop ABCDA: V - I1R1 - I2R2 = 0

KVL at loop ABCFA: V - I1R1 - I3R3 - I3R4 = 0

Circuit 2

KCL at node A: I1 = I2 + I3

KCL at node B: I2 = I4 + I5

KVL at loop ABCDA: V - I1R1 - I2R2 - I3R3 = 0

KVL at loop BCDEB: -I2R2 - I4R4 - I5R5 = 0

KVL at loop ADEFA: V - I1R1 - I4R4 - I3R3 - I3R6 = 0



# Measurement of power and power factor in a single phase ac series inductive circuit and study improvement of power factor using capacitor

- Power factor for a single-phase in an alternating current circuit is defined as a measure of energy efficiency. It is usually expressed as a number ranging from 0 to 1. It is the ratio of working power (or actual power) to apparent power.
- The value of the power factor for a single-phase is always less than 1. While for a pure resistance circuit, its value is 1. Formula P = W/A where, P is the power factor, W is the working power, and A is the apparent power.
- The power factor in ac circuit may also be defined as: the cosine of the phase angle between voltage and current i.e. cos φ or the ratio of the resistance to impedance cos φ = R/Z or the ratio of the true to apparent power i.e. power factor, cos φ = true power/apparent power.
- Real power, measured in watts, defines the power consumed by the resistive part of a circuit. Then real power, (P) in an AC circuit is the same as power, P in a DC circuit. So just like DC circuits, it is always calculated as I 2 *R, where R is the total resistive component of the circuit.
- In engineering applications, cosϕ is known as the power factor, which is the amount by which the power delivered in the circuit is less than the theoretical maximum of the circuit due to voltage and current being out of phase. For a resistor, ϕ = 0, so the average power dissipated is. Pave = 1 2I0V0.
- To measure power and power factor in a single phase RL circuit AC load, we need an ammeter, a voltmeter, a wattmeter and few connecting wires. We connect the ammeter in series with the load, the voltmeter across the load, and the wattmeter in series with the load and the supply. We vary the supply voltage and note down the readings of the ammeter, voltmeter and wattmeter. We calculate the power factor as P = W/VI, where W is the wattmeter reading, V is the voltmeter reading and I is the ammeter reading.
- To improve the power factor, we can use a capacitor in parallel with the load. The capacitor provides a leading current that cancels out the lagging current of the inductor. This reduces the phase angle between voltage and current and increases the power factor. The value of the capacitor can be calculated as C = Q/V 2 ω, where Q is the reactive power, V is the supply voltage and ω is the angular frequency.



# 3. Study of phenomenon of resonance in RLC series circuit and obtain resonant frequency.

- A RLC series circuit consists of a resistor (R), an inductor (L) and a capacitor (C) connected in series to an alternating voltage source.
- The current (I) in the circuit is the same for all the components, but the voltage (V) across each component is different and depends on the frequency (f) of the source.
- The voltage across the resistor is in phase with the current and is given by V_R = IR, where I is the rms value of the current.
- The voltage across the inductor leads the current by 90 degrees and is given by V_L = IXL, where XL = 2πfL is the inductive reactance.
- The voltage across the capacitor lags the current by 90 degrees and is given by V_C = IXC, where XC = 1/(2πfC) is the capacitive reactance.
- The total voltage across the circuit is the phasor sum of the voltages across the individual components and is given by V = sqrt((V_R)^2 + (V_L - V_C)^2).
- The phase difference between the total voltage and the current is given by tan(φ) = (V_L - V_C)/V_R, where φ is the angle between the phasors V and I.
- The impedance (Z) of the circuit is the ratio of the total voltage to the current and is given by Z = V/I = sqrt(R^2 + (XL - XC)^2).
- The power (P) dissipated in the circuit is given by P = I^2R = VI cos(φ), where cos(φ) is the power factor of the circuit.
- The phenomenon of resonance occurs when the inductive reactance and the capacitive reactance are equal, i.e., XL = XC, or f = 1/(2π sqrt(LC)). This is called the resonant frequency (f_0) of the circuit.
- At resonance, the total voltage is equal to the voltage across the resistor, i.e., V = V_R, and the phase difference between the voltage and the current is zero, i.e., φ = 0.
- The impedance of the circuit at resonance is minimum and equal to the resistance, i.e., Z = R, and the power factor of the circuit is maximum and equal to 1.
- The current in the circuit at resonance is maximum and equal to the source voltage divided by the resistance, i.e., I = V/R.
- The power dissipated in the circuit at resonance is maximum and equal to the source voltage squared divided by the resistance, i.e., P = V^2/R.
- The voltage across the inductor and the capacitor at resonance are maximum and equal to the product of the current and the reactance, i.e., V_L = V_C = IX = I/(2πf_0C) = I2πf_0L, where X is the common value of XL and XC at resonance.
- The quality factor (Q) of the circuit is a measure of the sharpness of the resonance and is given by Q = X/R = 2πf_0L/R = 1/(2πf_0RC).



# Connection and measurement of power consumption of a fluorescent lamp (tube light)

- A fluorescent lamp (tube light) is a type of electric light that uses a gas discharge to produce visible light. The gas inside the tube is ionized by a high voltage applied across the electrodes at the ends of the tube. The ionized gas emits ultraviolet radiation, which is converted into visible light by a phosphor coating on the inner surface of the tube.
- A fluorescent lamp requires a ballast to regulate the current and voltage in the circuit. The ballast can be either magnetic or electronic. A magnetic ballast consists of a transformer, a capacitor, and a starter. An electronic ballast uses a high-frequency oscillator to generate the required voltage and current.
- The power consumption of a fluorescent lamp depends on the wattage rating of the lamp, the type of ballast, and the power factor of the circuit. The power factor is a measure of how efficiently the power is used in the circuit. It is the ratio of the real power (watts) to the apparent power (volt-amperes). A power factor of 1 means that the power is used completely, while a power factor of less than 1 means that some power is wasted as reactive power.
- To measure the power consumption of a fluorescent lamp, a wattmeter can be used. A wattmeter is a device that measures the real power in a circuit. It has two coils: a current coil and a potential coil. The current coil is connected in series with the load, while the potential coil is connected across the load. The wattmeter has a pointer that indicates the power on a scale.
- To connect a wattmeter to a fluorescent lamp, the following steps can be followed:

  - Disconnect the power supply from the lamp circuit.
  - Connect the current coil of the wattmeter in series with the lamp and the ballast. The current coil terminals are usually marked as C1 and C2.
  - Connect the potential coil of the wattmeter across the lamp and the ballast. The potential coil terminals are usually marked as P1 and P2.
  - Reconnect the power supply to the lamp circuit.
  - Observe the reading on the wattmeter scale. This is the power consumption of the fluorescent lamp in watts.

- The power consumption of a fluorescent lamp can also be calculated by multiplying the voltage and the current in the circuit. However, this method may not give an accurate result, as the voltage and the current may not be in phase due to the presence of the ballast. Therefore, the power factor of the circuit should also be considered. The power factor can be measured by using a power factor meter, or by dividing the real power by the apparent power. The formula for calculating the power consumption of a fluorescent lamp is:

  - P = V x I x pf

  - Where P is the power in watts, V is the voltage in volts, I is the current in amperes, and pf is the power factor.

- The power consumption of a fluorescent lamp can vary depending on the type and size of the lamp, the type and quality of the ballast, the ambient temperature, and the age of the lamp. A typical fluorescent lamp consumes about 13-15 watts of power. The cost of electricity used by a fluorescent lamp depends on the wattage of the lamp, the number of hours it is used, and the electricity rate charged by the utility company. The formula for calculating the electricity cost of a fluorescent lamp is:

  - C = P x T x R

  - Where C is the cost in dollars, P is the power in watts, T is the time in hours, and R is the rate in dollars per kilowatt-hour.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic you requested:

# 5. Measurement of power in 3- phase circuit by two-wattmeter method and determination of its power factor for star as well as delta connected load.

- The two-wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The principle of the two-wattmeter method is based on the fact that the power in a three-phase circuit can be expressed as the sum of the powers in two of the three phases.
- The two wattmeters are connected as shown in the figure below, where W1 and W2 are the readings of the wattmeters, V is the line voltage, I is the line current, and θ is the phase angle between V and I.

Two-wattmeter method

- The power measured by each wattmeter is given by:

  - W1 = V * I * cos(θ - 30°)
  - W2 = V * I * cos(θ + 30°)

- The total power is then given by:

  - P = W1 + W2 = V * I * cos(θ) * √3

- The power factor is given by:

  - PF = cos(θ) = (W1 + W2) / (√3 * V * I)

- For a star-connected load, the line voltage is equal to the phase voltage multiplied by √3, and the line current is equal to the phase current. Therefore, the power and power factor can be expressed in terms of the phase quantities as:

  - P = √3 * Vph * Iph * cos(θ)
  - PF = cos(θ) = (W1 + W2) / (√3 * Vph * Iph)

- For a delta-connected load, the line voltage is equal to the phase voltage, and the line current is equal to the phase current multiplied by √3. Therefore, the power and power factor can be expressed in terms of the phase quantities as:

  - P = 3 * Vph * Iph * cos(θ)
  - PF = cos(θ) = (W1 + W2) / (3 * Vph * Iph)

- The two-wattmeter method can be used to measure the power and power factor of any balanced or unbalanced three-phase load, regardless of the load connection (star or delta) or the load type (resistive, inductive, or capacitive).
- The advantages of the two-wattmeter method are:

  - It is simple and easy to implement.
  - It does not require a neutral wire or a phase-shifting device.
  - It can measure the power and power factor of any three-phase load.

- The disadvantages of the two-wattmeter method are:

  - It requires two wattmeters, which may be costly or unavailable.
  - It may give erroneous results if the wattmeters are not calibrated or connected properly.
  - It may not be accurate for low power factor loads or distorted waveforms.



# 6. Determination of parameters of ac single phase series RLC circuit

- An ac single phase series RLC circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series to an alternating voltage source (V).
- The current (I) in the circuit is the same for all the components and is given by Ohm's law: `I = V/Z`, where Z is the total impedance of the circuit.
- The impedance Z is a complex quantity that depends on the frequency (f) of the ac source and the values of R, L, and C. It can be written as: `Z = R + jX`, where j is the imaginary unit and X is the total reactance of the circuit.
- The reactance X is the sum of the inductive reactance (XL) and the capacitive reactance (XC), which are given by: `XL = 2πfL` and `XC = 1/(2πfC)`.
- The impedance Z can also be expressed in polar form as: `Z = |Z|∠θ`, where |Z| is the magnitude of the impedance and θ is the phase angle between the voltage and the current.
- The magnitude of the impedance is given by: `|Z| = √(R^2 + X^2)`, and the phase angle is given by: `θ = tan^(-1)(X/R)`.
- The power factor (pf) of the circuit is the cosine of the phase angle: `pf = cos(θ)`. It indicates how efficiently the circuit converts the ac voltage into useful power. A power factor of 1 means that the voltage and the current are in phase and there is no reactive power. A power factor of 0 means that the voltage and the current are 90 degrees out of phase and there is only reactive power.
- The parameters of the ac single phase series RLC circuit can be determined by measuring the voltage, the current, and the power factor of the circuit, and then applying the formulas above. Alternatively, the parameters can be determined by measuring the voltage across each component and then applying Kirchhoff's voltage law: `V = VR + VL + VC`, where VR, VL, and VC are the voltages across the resistor, the inductor, and the capacitor, respectively.



Hello, I am Sydney, your AI assistant. I can help you with your topic.

# Determination of (i) Voltage ratio (ii) polarity and (iii) efficiency by load test of a single phase Transformer

- A single phase transformer is a device that transfers electrical energy from one circuit to another through mutual induction.
- The voltage ratio of a transformer is the ratio of the secondary voltage to the primary voltage. It is also equal to the ratio of the number of turns in the secondary coil to the number of turns in the primary coil.
- The polarity of a transformer is the relative direction of the induced voltages in the primary and secondary coils. It can be determined by the dot convention, which assigns a dot to one terminal of each coil. The dots indicate that the voltages at those terminals have the same polarity at any instant.
- The efficiency of a transformer is the ratio of the output power to the input power. It is also equal to the ratio of the output voltage times the output current to the input voltage times the input current, minus the losses in the transformer.

- To determine the voltage ratio, polarity and efficiency by load test of a single phase transformer, the following steps are followed:

  - Connect the primary winding of the transformer to a variable AC voltage source and the secondary winding to a resistive load and a voltmeter, as shown in the figure below.

  - Adjust the primary voltage to a suitable value and measure the secondary voltage and the load current with the voltmeter and an ammeter, respectively.
  - Calculate the voltage ratio by dividing the secondary voltage by the primary voltage.
  - To determine the polarity, connect a battery and a galvanometer in series with the primary winding, as shown in the figure below.

  - Observe the direction of the deflection of the galvanometer needle. If it deflects to the right, the polarity is additive, meaning that the dots are on the same side of the transformer. If it deflects to the left, the polarity is subtractive, meaning that the dots are on the opposite sides of the transformer.
  - To determine the efficiency, measure the input power by multiplying the primary voltage and the primary current, which can be obtained by using a wattmeter or an ammeter and a voltmeter in the primary circuit, as shown in the figure below.

  - Calculate the output power by multiplying the secondary voltage and the load current.
  - Calculate the efficiency by dividing the output power by the input power, and multiplying by 100 to get the percentage.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of determination of efficiency of a dc shunt motor by load test.

# Determination of efficiency of a dc shunt motor by load test

- A dc shunt motor is a type of dc motor that has a shunt field winding connected in parallel with the armature winding. The shunt field winding provides a constant magnetic field for the armature to rotate in.
- The efficiency of a dc shunt motor is the ratio of the output power to the input power. The output power is the mechanical power delivered by the motor to the load, and the input power is the electrical power supplied to the motor from the source.
- A load test is a method of determining the efficiency of a dc shunt motor by measuring the input and output power at different load conditions. The load test can be performed by connecting a variable resistor or a brake drum to the shaft of the motor and varying the load resistance or the brake torque.
- The procedure of the load test is as follows:

  - Connect the dc shunt motor to a dc source and a variable resistor or a brake drum as shown in the figure below.

  - Figure 1: Load test of a dc shunt motor

  - Measure the voltage (V) and the current (I) of the source using a voltmeter and an ammeter. The input power (P<sub>in</sub>) is given by P<sub>in</sub> = VI.
  - Measure the speed (N) of the motor using a tachometer. The output power (P<sub>out</sub>) is given by P<sub>out</sub> = 2πNT/60, where T is the torque of the load. The torque can be calculated by T = kR for a variable resistor, where k is a constant and R is the resistance, or by T = kF for a brake drum, where k is a constant and F is the brake force.
  - Calculate the efficiency (η) of the motor by η = P<sub>out</sub>/P<sub>in</sub>.
  - Repeat the above steps for different load conditions by varying the resistance or the brake force and record the values of V, I, N, P<sub>in</sub>, P<sub>out</sub>, and η in a table.
  - Plot a graph of efficiency versus output power and observe the variation of efficiency with load.

- The advantages of the load test are:

  - It is simple and easy to perform.
  - It gives the actual efficiency of the motor under different load conditions.
  - It does not require any additional instruments or devices.

- The disadvantages of the load test are:

  - It consumes a lot of power and causes heating of the motor and the load.
  - It may not be feasible to apply the full load to the motor in some cases.
  - It does not give the information about the losses and their distribution in the motor.



# 9. To study running and speed reversal of a three phase induction motor and record speed in both directions.

- A three phase induction motor is a type of electric motor that converts alternating current (AC) power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor.
- The speed of a three phase induction motor depends on the frequency of the AC supply, the number of poles in the stator, and the slip between the rotor and the stator. The speed can be calculated by the formula:

  `N = 120f / P (1 - s)`

  where N is the speed in revolutions per minute (rpm), f is the frequency in hertz (Hz), P is the number of poles, and s is the slip.

- The slip is the difference between the synchronous speed (the speed of the rotating magnetic field) and the actual speed of the rotor. The slip can be expressed as a percentage or a fraction of the synchronous speed. The slip is usually small and positive, meaning that the rotor rotates slower than the stator.

- The direction of rotation of a three phase induction motor is determined by the phase sequence of the AC supply. If the phase sequence is R-Y-B, the motor rotates in the clockwise direction. If the phase sequence is reversed to B-Y-R, the motor rotates in the anti-clockwise direction.

- To study the running and speed reversal of a three phase induction motor, the following steps can be followed:

  - Connect the motor to a three phase AC supply through a star-delta starter and a tachometer. The star-delta starter is used to reduce the starting current and the tachometer is used to measure the speed of the motor.
  - Switch on the supply and observe the direction and speed of the motor. Note down the readings of the tachometer and the voltmeter.
  - Switch off the supply and interchange any two phases of the supply. For example, swap R and B. This will reverse the phase sequence and the direction of rotation of the motor.
  - Switch on the supply again and observe the direction and speed of the motor. Note down the readings of the tachometer and the voltmeter.
  - Compare the readings and verify that the speed of the motor is the same in both directions, but the direction is reversed by changing the phase sequence.



# 10. Demonstration of cut-out sections of machines: dc machine, three phase induction machine, single-phase induction machine and synchronous machine.

- A cut-out section of a machine is a model that shows the internal parts and components of the machine by cutting away some parts of the outer casing or frame.
- Cut-out sections of machines are useful for demonstration and learning purposes, as they help to visualize the working principle and construction of the machines.
- The following are some examples of cut-out sections of machines:

## DC machine
- A DC machine is a device that converts electrical energy into mechanical energy (as a motor) or mechanical energy into electrical energy (as a generator).
- A DC machine consists of two main parts: the stator and the rotor.
- The stator is the stationary part of the machine that contains the field windings, which produce a magnetic field when a DC current is supplied to them.
- The rotor is the rotating part of the machine that contains the armature windings, which are connected to a commutator and brushes. The commutator is a cylindrical device that consists of segments of copper bars insulated from each other. The brushes are carbon or graphite blocks that slide on the commutator and make electrical contact with the armature windings.
- The cut-out section of a DC machine shows the commutator-brush arrangement, which is the main feature that distinguishes a DC machine from other types of machines.
- The commutator-brush arrangement allows the armature windings to receive a DC current from an external source (as a motor) or deliver a DC current to an external load (as a generator).
- The commutator-brush arrangement also reverses the direction of the current in the armature windings every half cycle, so that the torque on the rotor is always in the same direction as the rotation.

Cut-out section of a DC machine

## Three phase induction machine
- A three phase induction machine is a device that converts electrical energy into mechanical energy (as a motor) or mechanical energy into electrical energy (as a generator) using the principle of electromagnetic induction.
- A three phase induction machine consists of two main parts: the stator and the rotor.
- The stator is the stationary part of the machine that contains the stator windings, which are connected to a three phase AC supply. The stator windings produce a rotating magnetic field that rotates at a synchronous speed, which depends on the frequency of the supply and the number of poles of the machine.
- The rotor is the rotating part of the machine that contains the rotor windings, which are either wound or squirrel cage type. The wound rotor has three sets of windings that are connected to slip rings and brushes. The squirrel cage rotor has bars of copper or aluminum that are short-circuited by end rings.
- The cut-out section of a three phase induction machine shows the squirrel cage rotor, which is the most common type of rotor used in induction machines.
- The squirrel cage rotor has no electrical connection to the external circuit, and the rotor windings are induced by the rotating magnetic field of the stator. The induced currents in the rotor windings produce a magnetic field that interacts with the stator field, creating a torque on the rotor.
- The rotor speed is always less than the synchronous speed, and the difference is called the slip. The slip determines the amount of power transferred from the stator to the rotor.

Cut-out section of a three phase induction machine

## Single-phase induction machine
- A single-phase induction machine is a device that converts electrical energy into mechanical energy (as a motor) using the principle of electromagnetic induction.
- A single-phase induction machine consists of two main parts: the stator and the rotor.
- The stator is the stationary part of the machine that contains the stator winding, which is connected to a single phase AC supply. The stator winding produces an alternating magnetic field that oscillates along a fixed axis.
- The rotor is the rotating part of the machine that contains the rotor winding, which is usually squirrel cage type. The rotor winding is induced by the alternating magnetic field of the stator.
- The cut-out section of a single-phase induction machine shows the squirrel cage rotor, which is similar to the one



#### (B) Experiments available on virtual lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows users to perform experiments and learn scientific concepts without the need for physical equipment, materials, or space.
- Virtual labs can be used for various purposes, such as education, research, training, testing, or entertainment.
- Some examples of experiments available on virtual labs are:

  - Physics: Users can explore topics such as mechanics, optics, electricity, magnetism, thermodynamics, waves, and quantum physics by manipulating variables, observing phenomena, and measuring outcomes.
  - Chemistry: Users can conduct experiments involving chemical reactions, stoichiometry, equilibrium, kinetics, thermodynamics, electrochemistry, organic chemistry, and spectroscopy by using virtual apparatus, reagents, and instruments.
  - Biology: Users can investigate topics such as cell structure and function, genetics, evolution, ecology, anatomy, physiology, microbiology, immunology, and molecular biology by using virtual microscopes, models, simulations, and animations.
  - Engineering: Users can design, build, test, and optimize systems and devices such as circuits, robots, bridges, rockets, cars, and airplanes by using virtual tools, components, and environments.
  - Mathematics: Users can explore concepts such as algebra, geometry, trigonometry, calculus, statistics, and discrete mathematics by using virtual manipulatives, graphs, calculators, and games.
  - Computer Science: Users can learn programming languages, algorithms, data structures, software engineering, artificial intelligence, and cybersecurity by using virtual editors, compilers, debuggers, and simulators.
  - Psychology: Users can study topics such as perception, cognition, memory, learning, emotion, motivation, personality, social psychology, and abnormal psychology by using virtual experiments, surveys, and scenarios.
  - Economics: Users can analyze topics such as supply and demand, market structures, consumer behavior, production, costs, revenue, profit, income distribution, and macroeconomic indicators by using virtual models, graphs, and data.
  - Geography: Users can explore topics such as physical geography, human geography, environmental geography, and geospatial technologies by using virtual maps, globes, satellites, and GIS.
  - Art: Users can create and appreciate artworks such as paintings, drawings, sculptures, photographs, and digital art by using virtual brushes, colors, shapes, textures, and filters.



# Kirchhoff's laws

Kirchhoff's laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff's laws:

- Kirchhoff's current law (KCL): This law, also called Kirchhoff's first law, or Kirchhoff's junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current flowing through the $k$-th branch connected to the node.

- Kirchhoff's voltage law (KVL): This law, also called Kirchhoff's second law, or Kirchhoff's loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of voltages supplied by the sources in the loop; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage across the $k$-th element of the loop.

The following diagrams illustrate the application of Kirchhoff's laws to simple circuits:

KCL diagram

In this circuit, applying KCL to the node A gives:

$$I_1 + I_2 + I_3 = 0$$

KVL diagram

In this circuit, applying KVL to the loop ABCDA gives:

$$V_1 - V_2 - V_3 - V_4 = 0$$

Kirchhoff's laws are the foundation of advanced circuit analysis. They can be used to solve complex circuits with multiple loops, branches, and sources. They can also be combined with the equations for individual components, such as resistors, capacitors, and inductors, to analyze the behavior of circuits in different domains, such as DC, AC, or transient.



# Virtual Lab

- Virtual Lab is an online platform that provides remote access to various experiments in science and engineering disciplines.
- Virtual Lab is developed by Amrita Vishwa Vidyapeetham in collaboration with other institutions and supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education by providing students with an opportunity to perform experiments in a virtual environment, without the need for physical infrastructure, equipment, or supervision.
- Virtual Lab consists of simulations, animations, graphics, videos, and interactive elements that mimic the real-world scenarios and phenomena of the experiments.
- Virtual Lab covers various domains such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, civil engineering, and chemical engineering.
- Virtual Lab also provides assessment tools, feedback mechanisms, and learning resources to help students evaluate their performance and understanding of the experiments.
- Virtual Lab can be accessed through the website http://vlab.amrita.edu/ or the mobile app Amrita Online Lab.



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

Circuit diagram

To apply Thevenin's theorem, we follow the steps as follows:

- Step 1: Remove the load resistor and replace it with an open circuit.

Circuit diagram with open circuit

- Step 2: Calculate the Thevenin voltage, which is the voltage across the open circuit terminals. We can use the voltage divider rule to find the voltage across R_2, which is V_2 = 20 V × (10 Ω / (10 Ω + 20 Ω)) = 6.67 V. Then, we can use Kirchhoff's voltage law to find the voltage across R_1, which is V_1 = 20 V - V_2 = 13.33 V. The Thevenin voltage is equal to V_1, so V_th = 13.33 V.

- Step 3: Calculate the Thevenin resistance, which is the equivalent resistance seen from the open circuit terminals. We can do this by replacing the voltage source with a short circuit and finding the total resistance between the terminals. The circuit becomes a parallel combination of R_1 and R_2, so R_th = (R_1 × R_2) / (R_1 + R_2) = (10 Ω × 20 Ω) / (10 Ω + 20 Ω) = 6.67 Ω.

- Step 4: Draw the Thevenin equivalent circuit, which consists of a voltage source equal to the Thevenin voltage and a series resistor equal to the Thevenin resistance, connected to the load resistor.

Thevenin equivalent circuit

- Step 5: Analyze the Thevenin equivalent circuit to find the current, voltage, or power across the load resistor. We can use Ohm's law to find the current, which is I = V_th / (R_th + R_L) = 13.33 V / (6.67 Ω + 40 Ω) = 0.286 A. The voltage across the load resistor is V_L = I × R_L = 0.286 A × 40 Ω =



# Virtual Lab

- Virtual Lab is an online platform that provides remote access to various experiments in science and engineering disciplines.
- Virtual Lab is developed by Amrita Vishwa Vidyapeetham in collaboration with other institutions and supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education by providing students with a realistic and interactive experience of conducting experiments in a laboratory setting.
- Virtual Lab consists of simulations, animations, videos, graphics, and quizzes that help students learn the concepts and procedures of the experiments.
- Virtual Lab covers various domains such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, and civil engineering.
- Virtual Lab is accessible to anyone with an internet-enabled device and a web browser. Users can register for free and access the experiments at any time and place.
- Virtual Lab also provides a feedback mechanism for users to share their comments, suggestions, and queries with the developers and instructors.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write about RLC series resonance. Here is the content in markdown format:

# RLC series resonance

- RLC series resonance is a phenomenon that occurs in a circuit consisting of a resistor (R), an inductor (L), and a capacitor (C) connected in series with an alternating voltage source.
- When the frequency of the voltage source matches the natural frequency of the circuit, the circuit is said to be in resonance. This means that the impedance of the circuit is minimum and the current is maximum.
- The natural frequency of the circuit is given by the formula:

$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

- where f0 is the resonant frequency, L is the inductance, and C is the capacitance of the circuit.
- At resonance, the reactance of the inductor and the capacitor cancel each other out, and the circuit behaves like a pure resistor. The voltage across the resistor is equal to the source voltage, and the voltage across the inductor and the capacitor are equal in magnitude but opposite in phase.
- The power factor of the circuit is 1, which means that the power delivered by the source is fully dissipated by the resistor. The power dissipated by the resistor is given by the formula:

$$P_R = I^2R$$

- where PR is the power dissipated by the resistor, I is the current in the circuit, and R is the resistance of the circuit.
- The quality factor (Q) of the circuit is a measure of how sharp the resonance is. It is given by the formula:

$$Q = \frac{f_0}{\Delta f}$$

- where f0 is the resonant frequency and Δf is the bandwidth of the circuit. The bandwidth is the range of frequencies for which the current is at least half of its maximum value. The higher the Q, the narrower the bandwidth and the sharper the resonance.
- The Q factor can also be expressed in terms of the circuit parameters as:

$$Q = \frac{1}{R}\sqrt{\frac{L}{C}}$$

- The Q factor determines the selectivity of the circuit, which is its ability to filter out unwanted frequencies. A high Q circuit can be used as a band-pass filter, which allows only a narrow range of frequencies to pass through and blocks the rest. A low Q circuit can be used as a band-reject filter, which blocks a narrow range of frequencies and allows the rest to pass through.



# Virtual Lab

- Virtual Lab is an online platform that provides remote access to various laboratories in science and engineering disciplines.
- Virtual Lab is a collaborative initiative of Amrita Vishwa Vidyapeetham and other institutions, supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education and research by providing students and teachers with interactive simulations, animations, videos and assessments of laboratory experiments.
- Virtual Lab covers various domains such as biotechnology, physical sciences, chemical sciences, electrical sciences, mechanical sciences, computer science and engineering, civil engineering and humanities.
- Virtual Lab simulates the real feel of a laboratory, while allowing the user to conduct the experiment from any internet-enabled device.
- Virtual Lab also provides feedback, guidance and evaluation to the user, as well as links to relevant theory and resources.

##### Virtual lab link: https://vlab.amrita.edu/?sub=1&brch=75&sim=330&cnt=1

- This link leads to a specific experiment in the Virtual Lab of Amrita Vishwa Vidyapeetham, under the domain of physical sciences and the branch of optics.
- The experiment is titled "Determination of the Focal Length of a Concave Mirror".
- The experiment demonstrates how to measure the focal length of a concave mirror using a simple method involving a candle and a screen.
- The experiment consists of four sections: theory, procedure, simulation and self evaluation.
- The theory section explains the concepts and formulas related to the experiment, such as the nature of concave mirrors, the ray diagram, the mirror equation and the magnification.
- The procedure section describes the steps to perform the experiment in a real laboratory, as well as the precautions and observations to be made.
- The simulation section allows the user to perform the experiment virtually, by adjusting the parameters such as the object distance, the mirror radius and the screen distance, and observing the results on the screen.
- The self evaluation section provides multiple choice questions and answers to test the user's understanding of the experiment.



# 4. Measurement of power in 3- phase circuit by two wattmeter method and determination of its power factor for star as well as delta connected load.

- The two wattmeter method is used to measure the total power and power factor of a three-phase circuit, either balanced or unbalanced, star or delta connected, with a three-wire system.
- The two wattmeter method involves connecting the current coils of two wattmeters in series with any two line conductors, and the potential coils of each wattmeter to the third line conductor. The connection diagram of two wattmeter method is shown below:

Two wattmeter method connection diagram

- The readings of the two wattmeters are given by:

  - W1 = VL * IL * cos(φ - 30°)
  - W2 = VL * IL * cos(φ + 30°)

  where VL is the line voltage, IL is the line current, and φ is the phase angle between VL and IL.

- The total power is given by the sum of the two wattmeter readings:

  - W = W1 + W2 = VL * IL * cos(φ)

- The power factor is given by the ratio of the total power to the apparent power:

  - PF = W / (VL * IL) = cos(φ)

- Alternatively, the power factor can be calculated from the two wattmeter readings using the following formula:

  - PF = cos(φ) = (W1 + W2) / (√3 * VL * IL)

- For a star connected load, the line voltage is equal to the phase voltage multiplied by √3, and the line current is equal to the phase current. Therefore, the two wattmeter readings are given by:

  - W1 = √3 * Vph * Iph * cos(φ - 30°)
  - W2 = √3 * Vph * Iph * cos(φ + 30°)

  where Vph is the phase voltage, Iph is the phase current, and φ is the phase angle between Vph and Iph.

- For a delta connected load, the line voltage is equal to the phase voltage, and the line current is equal to the phase current multiplied by √3. Therefore, the two wattmeter readings are given by:

  - W1 = Vph * √3 * Iph * cos(φ - 30°)
  - W2 = Vph * √3 * Iph * cos(φ + 30°)

  where Vph is the phase voltage, Iph is the phase current, and φ is the phase angle between Vph and Iph.



# Virtual Lab

- A virtual lab is a web-based platform that allows students to perform experiments and simulations online, without the need for physical equipment or facilities.
- A virtual lab can provide interactive, engaging, and flexible learning experiences for students, especially in remote or blended learning environments.
- A virtual lab can also enhance the accessibility, scalability, and sustainability of laboratory education, as well as reduce the costs and risks associated with traditional labs.

## Measurement

- Measurement is the process of determining the size, quantity, or degree of something using a standard unit or system.
- Measurement is essential for science, engineering, and everyday life, as it allows us to describe, compare, and analyze phenomena and phenomena.
- Measurement involves two components: a numerical value and a unit of measurement. For example, the length of a table can be measured as 1.5 meters, where 1.5 is the numerical value and meter is the unit of measurement.
- There are different types of measurement, such as length, mass, time, temperature, volume, density, speed, force, etc. Each type of measurement has its own units and methods of measurement.

## Dreamweaver

- Dreamweaver is a software application that allows users to create, edit, and publish web pages and web applications.
- Dreamweaver is a visual web development tool that provides a graphical user interface (GUI) for designing and coding web pages.
- Dreamweaver supports various web technologies, such as HTML, CSS, JavaScript, PHP, ASP, etc. It also integrates with other Adobe products, such as Photoshop, Illustrator, and Flash.
- Dreamweaver offers various features, such as templates, code completion, syntax highlighting, live preview, site management, etc. It also allows users to create responsive web pages that adapt to different screen sizes and devices.



# 5. Determination of parameters of ac single phase series RLC circuit.

- A series RLC circuit is a circuit that contains a resistor (R), an inductor (L), and a capacitor (C) connected in series with an alternating current (ac) source.
- The ac source provides a sinusoidal voltage of the form $v_s(t) = V_m \sin(\omega t + \phi)$, where $V_m$ is the peak voltage, $\omega$ is the angular frequency, and $\phi$ is the phase angle.
- The current in the circuit is the same for all components and is given by $i(t) = I_m \sin(\omega t + \theta)$, where $I_m$ is the peak current and $\theta$ is the current phase angle.
- The parameters of the circuit are the resistance $R$, the inductance $L$, the capacitance $C$, the impedance $Z$, the reactance $X$, the phase difference $\delta$, and the power factor $pf$.
- The impedance $Z$ is the total opposition to the current flow in the circuit and is given by $Z = R + jX$, where $j$ is the imaginary unit and $X$ is the reactance.
- The reactance $X$ is the sum of the inductive reactance $X_L$ and the capacitive reactance $X_C$, where $X_L = \omega L$ and $X_C = \frac{1}{\omega C}$.
- The phase difference $\delta$ is the angle between the voltage and the current in the circuit and is given by $\delta = \phi - \theta$.
- The power factor $pf$ is the ratio of the real power to the apparent power in the circuit and is given by $pf = \cos \delta$.
- The parameters of the circuit can be determined by using the following formulas:

  - $R = Z \cos \delta$
  - $L = \frac{Z \sin \delta}{\omega}$
  - $C = \frac{1}{\omega Z \sin \delta}$
  - $Z = \sqrt{R^2 + X^2}$
  - $X = X_L - X_C$
  - $\delta = \tan^{-1} \frac{X}{R}$
  - $pf = \frac{R}{Z}$

- Alternatively, the parameters of the circuit can be determined by using the phasor diagram, which is a graphical representation of the voltage and current vectors in the complex plane.
- The phasor diagram shows the following relationships:

  - $V_s = V_R + V_L + V_C$, where $V_s$, $V_R$, $V_L$, and $V_C$ are the phasors of the source voltage, the resistor voltage, the inductor voltage, and the capacitor voltage, respectively.
  - $V_R = I Z_R$, where $Z_R = R$ is the impedance of the resistor.
  - $V_L = I Z_L$, where $Z_L = j \omega L$ is the impedance of the inductor.
  - $V_C = I Z_C$, where $Z_C = -j \frac{1}{\omega C}$ is the impedance of the capacitor.
  - $I = \frac{V_s}{Z}$, where $Z = Z_R + Z_L + Z_C$ is the impedance of the circuit.
  - $\delta = \angle V_s - \angle I$, where $\angle V_s$ and $\angle I$ are the phase angles of the source voltage and the current, respectively.
  - $pf = \cos \delta$, where $\delta$ is the phase difference between the voltage and the current.



# Virtual Lab

- Virtual Lab is an online platform that provides remote access to laboratory experiments in various disciplines of science and engineering.
- Virtual Lab is developed by Amrita Vishwa Vidyapeetham in collaboration with other institutions and supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of science and engineering education by providing students with hands-on learning experiences, interactive simulations, animations, videos and assessments.
- Virtual Lab covers a wide range of topics, such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, civil engineering and chemical engineering.
- Virtual Lab is accessible to anyone with an internet-enabled computer or mobile device, and does not require any special software or hardware.
- Virtual Lab is designed to complement the existing physical laboratories and to provide an alternative learning mode for students who cannot access or afford the physical laboratories.

## Virtual Lab Link: https://vlab.amrita.edu/?sub=1&brch=75&sim=332&cnt=1

- The link leads to a specific virtual lab experiment on the topic of **Determination of Young's Modulus of a Wire by Searle's Method**.
- This experiment belongs to the branch of **Physical Sciences**, and the sub-branch of **Mechanics**.
- The experiment demonstrates how to measure the Young's modulus of a material, which is a measure of its stiffness or elasticity, by applying a known force and measuring the resulting extension of a wire.
- The experiment consists of the following components:
  - **Theory**: This section explains the basic concepts, principles and formulas related to the experiment.
  - **Procedure**: This section provides a step-by-step guide on how to perform the experiment using the virtual lab interface, which simulates the real lab equipment and settings.
  - **Simulation**: This section allows the user to interact with the virtual lab interface and conduct the experiment by adjusting the parameters, such as the mass, length and diameter of the wire, and observing the output, such as the extension and the Young's modulus.
  - **Self Evaluation**: This section tests the user's understanding of the experiment by presenting multiple choice questions and feedback.
  - **Reference**: This section lists the sources of information and images used in the experiment.
  - **Feedback**: This section allows the user to rate the experiment and provide comments or suggestions for improvement.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write on the topic of observing the B-H loop of a ferromagnetic material in CRO. Here is the content I have generated for you in markdown format:

# 6. To observe the B-H loop of a ferromagnetic material in CRO.

## Aim
To observe the B-H loop or hysteresis loop of a ferromagnetic material in a cathode ray oscilloscope (CRO).

## Theory
- A ferromagnetic material is a material that can be magnetized by an external magnetic field and retain some magnetization even after the field is removed.
- The relationship between the magnetic field intensity H and the magnetic flux density B of a ferromagnetic material is nonlinear and depends on the history of magnetization.
- A B-H loop or hysteresis loop is a graphical representation of the cyclic magnetization process of a ferromagnetic material. It shows how B changes with H as the material is subjected to a varying magnetic field.
- A B-H loop can be observed in a CRO by using a solenoid as the primary coil and a toroidal core of the ferromagnetic material as the secondary coil. The primary coil is connected to an alternating current (AC) source and the secondary coil is connected to the vertical input of the CRO. The horizontal input of the CRO is connected to the AC source through a potential divider. The CRO displays the B-H loop on its screen as a closed curve.

## Apparatus
- A solenoid with a variable number of turns
- A toroidal core of a ferromagnetic material
- An AC source with a variable frequency and amplitude
- A CRO with a dual trace mode
- A potential divider
- Connecting wires

## Procedure
- Connect the solenoid to the AC source and the toroidal core to the vertical input of the CRO as shown in the figure below.

Figure 1: Circuit diagram for observing the B-H loop of a ferromagnetic material in CRO

- Connect the horizontal input of the CRO to the AC source through a potential divider as shown in the figure above.
- Set the CRO to the dual trace mode and adjust the time base and the vertical and horizontal sensitivities to obtain a clear display of the B-H loop on the screen.
- Vary the number of turns of the solenoid, the frequency and amplitude of the AC source, and observe the changes in the shape and size of the B-H loop on the screen.
- Record the observations and draw the B-H loops for different values of the parameters.

## Observations
- The B-H loop is a closed curve that has a clockwise direction and a rectangular shape.
- The B-H loop has two axes of symmetry: the vertical axis (B-axis) and the horizontal axis (H-axis).
- The B-H loop has four characteristic points: the origin (O), the saturation point (S), the coercivity point (C), and the remanence point (R).
- The origin (O) is the point where both B and H are zero. It represents the initial state of the material before magnetization.
- The saturation point (S) is the point where B reaches its maximum value for a given H. It represents the state of the material when it is fully magnetized by the external field.
- The coercivity point (C) is the point where H is zero and B has a nonzero value. It represents the state of the material when the external field is removed and the material retains some magnetization. The value of B at this point is called the coercivity (Hc) of the material.
- The remanence point (R) is the point where B is zero and H has a nonzero value. It represents the state of the material when the external field is reversed and the material loses its magnetization. The value of H at this point is called the remanence (Br) of the material.
- The area enclosed by the B-H loop is proportional to the energy loss or hysteresis loss of the material due to the cyclic magnetization process.

- The shape and size of the B-H loop depend on the following factors:
  - The number of turns of the solenoid: Increasing the number of turns increases the magnetic field intensity H and hence the magnetic flux density B of the material. This makes the B-H loop larger and more rectangular.
  - The frequency of the AC source: Increasing the frequency increases the rate of change of the magnetic field and hence the hysteresis loss



# Virtual Lab

- Virtual Lab is an online platform that provides remote access to various laboratories in science and engineering disciplines.
- Virtual Lab is developed by Amrita Vishwa Vidyapeetham in collaboration with other institutions and supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education and research by providing students and teachers with interactive simulations, animations, videos and assessments of real-world experiments.
- Virtual Lab covers various domains such as biotechnology, physical sciences, chemical sciences, electrical sciences, mechanical sciences, computer science and engineering, civil engineering and humanities.
- Virtual Lab allows users to perform experiments, collect data, analyze results, and draw conclusions using a web browser and an internet connection.
- Virtual Lab also provides feedback, guidance, and additional resources to help users learn the concepts and principles behind the experiments.



# Determination of the efficiency of a dc motor by loss summation method (Swinburne's test)

- The efficiency of a dc motor is defined as the ratio of output (mechanical) power to input (electrical) power.
- The output power of a dc motor can be measured by using a dynamometer or a brake, which applies a torque and measures the rotational speed of the motor shaft.
- The input power of a dc motor can be measured by using a power analyzer, which measures the voltage and current supplied to the motor terminals.
- However, measuring the output and input power of a dc motor on load can be inconvenient and costly, especially for large machines.
- Therefore, an indirect method of testing the efficiency of a dc motor is to determine its losses instead of measuring the output and input power on load.
- The losses of a dc motor can be classified into two categories: constant losses and variable losses.
- Constant losses are those losses that do not depend on the load current, such as core loss, friction loss, and windage loss.
- Variable losses are those losses that depend on the load current, such as copper loss in the armature and the field windings.
- The total loss of a dc motor can be expressed as:

  Total loss = Constant loss + Variable loss

- The efficiency of a dc motor can be expressed as:

  Efficiency = (Input power - Total loss) / Input power

- Swinburne's test is a method of determining the efficiency of a dc motor by loss summation method.
- Swinburne's test is performed by running the dc motor at no load and measuring the no load current and the no load input power.
- The no load input power is equal to the constant loss plus the no load copper loss in the armature and the field windings.
- The no load copper loss can be calculated by multiplying the no load current by the resistance of the armature and the field windings.
- The constant loss can be obtained by subtracting the no load copper loss from the no load input power.
- The variable loss at any load can be calculated by multiplying the load current by the resistance of the armature and the field windings.
- The total loss at any load can be obtained by adding the constant loss and the variable loss.
- The efficiency of the dc motor at any load can be obtained by subtracting the total loss from the input power and dividing by the input power.
- Swinburne's test has the advantage of convenience and economy, as it does not require loading the machine or measuring the output power.
- Swinburne's test has the limitation of accuracy, as it does not account for the change in the core loss and the friction loss due to the change in the load.



#### Course Outcomes:

- By the end of this course, you will be able to:
  - Identify and explain the key concepts and principles of artificial intelligence, such as search, knowledge representation, reasoning, planning, learning, and natural language processing.
  - Apply various artificial intelligence techniques and algorithms to solve problems, such as heuristic search, constraint satisfaction, logic programming, probabilistic inference, decision trees, neural networks, and natural language processing.
  - Evaluate the strengths and limitations of different artificial intelligence approaches and compare their performance and applicability to different domains and tasks.
  - Implement and test artificial intelligence programs using Python and relevant libraries and frameworks, such as NumPy, SciPy, scikit-learn, TensorFlow, and NLTK.
  - Communicate and present artificial intelligence solutions and results effectively using appropriate terminology, diagrams, and tools.



#### Course Outcome (CO) Bloom’s Level

- A course outcome (CO) is a statement that describes what a student should be able to do or demonstrate at the end of a course.
- A CO should be specific, measurable, achievable, relevant, and time-bound (SMART).
- A CO should also align with the program outcomes (POs) and the course objectives (COs).
- A CO can be classified according to the Bloom’s taxonomy of cognitive domain, which consists of six levels of learning: knowledge, comprehension, application, analysis, synthesis, and evaluation.
- The Bloom’s level of a CO indicates the degree of cognitive complexity and depth of learning that is expected from the student.
- The higher the Bloom’s level, the more challenging and sophisticated the CO is.
- The Bloom’s level of a CO can be determined by using appropriate verbs that reflect the cognitive process involved in the CO.
- For example, a CO that uses verbs like define, identify, list, or recall is at the knowledge level, which is the lowest level of learning.
- A CO that uses verbs like compare, contrast, classify, or explain is at the comprehension level, which is the second level of learning.
- A CO that uses verbs like apply, demonstrate, use, or solve is at the application level, which is the third level of learning.
- A CO that uses verbs like analyze, differentiate, examine, or infer is at the analysis level, which is the fourth level of learning.
- A CO that uses verbs like create, design, construct, or synthesize is at the synthesis level, which is the fifth level of learning.
- A CO that uses verbs like evaluate, judge, critique, or assess is at the evaluation level, which is the highest level of learning.



#### At the end of this course, the students should be able to:

- Explain the basic concepts and principles of artificial intelligence, such as agents, search, knowledge representation, reasoning, planning, learning, natural language processing, computer vision, and robotics.
- Apply various artificial intelligence techniques to solve problems, such as heuristic search, constraint satisfaction, logic programming, probabilistic inference, machine learning, natural language processing, computer vision, and robotics.
- Evaluate the strengths and limitations of different artificial intelligence methods and tools, and compare their performance and applicability to different domains and scenarios.
- Design and implement simple artificial intelligence systems using Python and relevant libraries, such as NumPy, SciPy, scikit-learn, NLTK, OpenCV, and PyTorch.
- Demonstrate ethical awareness and social responsibility when developing and using artificial intelligence systems, and consider the potential impacts and risks of artificial intelligence on society, economy, environment, and human values.



# CO 1 Conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits. K3

- KVL stands for Kirchhoff's Voltage Law, which states that the algebraic sum of the voltages around any closed loop in a circuit is zero.
- KCL stands for Kirchhoff's Current Law, which states that the algebraic sum of the currents entering and leaving any node in a circuit is zero.
- Network theorems are mathematical tools that can be used to simplify and analyze complex DC circuits. Some of the common network theorems are:
  - Superposition theorem: This theorem states that the response (voltage or current) in any element of a linear circuit is equal to the algebraic sum of the responses caused by each independent source acting alone, while all other independent sources are turned off (replaced by their internal resistances).
  - Thevenin's theorem: This theorem states that any linear circuit with voltage sources and resistances can be replaced by an equivalent circuit consisting of a single voltage source (called Thevenin's voltage) in series with a single resistance (called Thevenin's resistance).
  - Norton's theorem: This theorem states that any linear circuit with current sources and resistances can be replaced by an equivalent circuit consisting of a single current source (called Norton's current) in parallel with a single resistance (called Norton's resistance).
  - Maximum power transfer theorem: This theorem states that the maximum power is transferred from a source to a load when the load resistance is equal to the source resistance (or the Thevenin's or Norton's resistance of the source circuit).
- To conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits, the following steps are suggested:
  - Design a circuit with resistors, voltage sources, current sources, and measuring devices (such as voltmeters, ammeters, and ohmmeters) according to the given specifications or objectives.
  - Construct the circuit on a breadboard or a circuit board, and verify the connections and polarities.
  - Apply KVL and KCL to the circuit, and write the equations for the voltages and currents in each loop and node.
  - Solve the equations using algebraic or matrix methods, and obtain the theoretical values of the voltages and currents in the circuit.
  - Measure the actual values of the voltages and currents in the circuit using the measuring devices, and compare them with the theoretical values. Calculate the percentage errors and explain the possible sources of errors.
  - Apply the network theorems to the circuit, and find the equivalent circuits for the given load or source. Verify the equivalence by comparing the voltages and currents in the original and equivalent circuits.
  - Apply the maximum power transfer theorem to the circuit, and find the load resistance that maximizes the power transfer. Measure the power delivered to the load and compare it with the theoretical value.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use to study and prepare for your exams.

# CO 2 Demonstrate the behavior of AC circuits connected to single phase AC supply and measure power in single phase as well as three phase electrical circuits. K4

- An AC circuit is a circuit that operates with alternating current (AC), which means the current changes direction periodically. The frequency of the current is measured in hertz (Hz), which is the number of cycles per second.
- A single phase AC supply is a type of AC supply that has only one voltage waveform. It is commonly used for domestic and commercial applications. A single phase AC supply can be represented by a sinusoidal voltage source with a peak value of Vp and a frequency of f.
- An AC circuit connected to a single phase AC supply can have different types of components, such as resistors, capacitors, inductors, or a combination of them. These components affect the behavior of the AC circuit in different ways.
- A resistor is a component that opposes the flow of current and dissipates electrical energy as heat. In an AC circuit, a resistor behaves the same way as in a DC circuit. The voltage and current across a resistor are in phase, which means they reach their maximum and minimum values at the same time. The resistance of a resistor is measured in ohms (Ω) and is independent of the frequency of the AC supply.
- A capacitor is a component that stores electrical energy in an electric field. In an AC circuit, a capacitor behaves differently than in a DC circuit. The voltage across a capacitor lags behind the current by 90 degrees, which means the voltage reaches its maximum value when the current is zero and vice versa. The capacitance of a capacitor is measured in farads (F) and is inversely proportional to the frequency of the AC supply.
- An inductor is a component that stores electrical energy in a magnetic field. In an AC circuit, an inductor behaves differently than in a DC circuit. The voltage across an inductor leads the current by 90 degrees, which means the voltage reaches its maximum value when the current is at its minimum and vice versa. The inductance of an inductor is measured in henrys (H) and is directly proportional to the frequency of the AC supply.
- A combination of resistors, capacitors, and inductors in an AC circuit can form different types of circuits, such as series, parallel, or series-parallel. These circuits have different characteristics, such as impedance, reactance, phase angle, power factor, and resonance.
- Impedance is the total opposition to the flow of current in an AC circuit. It is measured in ohms (Ω) and is a complex quantity that has a real part (resistance) and an imaginary part (reactance). Impedance can be calculated by using the formula Z = R + jX, where R is the resistance, j is the imaginary unit, and X is the reactance.
- Reactance is the opposition to the flow of current caused by the capacitors and inductors in an AC circuit. It is measured in ohms (Ω) and is also a complex quantity that has a positive sign for inductive reactance and a negative sign for capacitive reactance. Reactance can be calculated by using the formulas Xc = -1/(2πfC) for capacitive reactance and Xl = 2πfL for inductive reactance, where f is the frequency, C is the capacitance, and L is the inductance.
- Phase angle is the angle between the voltage and the current in an AC circuit. It is measured in degrees (°) or radians (rad) and indicates the phase difference between the voltage and the current. Phase angle can be calculated by using the formula θ = tan^-1(X/R), where X is the reactance and R is the resistance.
- Power factor is the ratio of the real power to the apparent power in an AC circuit. It is a dimensionless quantity that ranges from 0 to 1 and indicates how efficiently the AC circuit converts electrical energy into useful work. Power factor can be calculated by using the formula pf = cos(θ), where θ is the phase angle.
- Resonance is a condition in an AC circuit where the capacitive reactance and the inductive reactance are equal in magnitude and opposite in sign. This results in a minimum impedance and a maximum current in the circuit. Resonance can occur in series or parallel circuits and can be calculated by using the formulas f = 1/(2π√(LC)) for series resonance and



# CO 3 Perform experiment illustrating BH curve of magnetic materials. K3

- The BH curve of a magnetic material is a plot of the magnetic flux density B versus the magnetic field intensity H.
- The BH curve shows the relationship between the magnetization of the material and the applied magnetic field, as well as the magnetic hysteresis and saturation of the material.
- The BH curve can be obtained experimentally by using a solenoid with a magnetic material core and a variable current source.
- The steps to perform the experiment are as follows:

  1. Connect the solenoid to the current source and the ammeter, and place the magnetic material core inside the solenoid.
  2. Connect a voltmeter across the terminals of the solenoid to measure the induced voltage, which is proportional to the rate of change of magnetic flux.
  3. Set the current source to zero and record the readings of the ammeter and the voltmeter.
  4. Gradually increase the current in one direction and record the corresponding readings of the ammeter and the voltmeter at regular intervals.
  5. Plot the graph of the induced voltage versus the current, which is the first quadrant of the BH curve.
  6. Reduce the current to zero and then reverse the direction of the current and repeat the steps 4 and 5 to obtain the second quadrant of the BH curve.
  7. Repeat the steps 4 to 6 for several cycles of increasing and decreasing the current in both directions to obtain the complete BH curve with hysteresis loops.
  8. Calculate the magnetic flux density B from the induced voltage using Faraday's law of electromagnetic induction, and the magnetic field intensity H from the current using Ampere's law.
  9. Plot the graph of B versus H, which is the final BH curve of the magnetic material.



# CO 4 Calculate efficiency of a single phase transformer and DC machine. K4

- The efficiency of a single phase transformer is defined as the ratio of output power to input power, expressed as a percentage. It indicates how well the transformer converts the electrical energy from the primary side to the secondary side, without wasting it as heat or other losses.
- The efficiency of a single phase transformer can be calculated by the following formula:

  $$\eta = \frac{P_o}{P_i} \times 100 \%$$

  where $\eta$ is the efficiency, $P_o$ is the output power, and $P_i$ is the input power.

- The input power and output power of a transformer are measured in the same unit, such as watts (W) or kilowatts (kW).

- The output power of a transformer is equal to the product of the secondary voltage and current, minus the secondary copper loss. The secondary copper loss is the power dissipated in the secondary winding due to its resistance.

  $$P_o = V_s I_s - I_s^2 R_s$$

  where $V_s$ is the secondary voltage, $I_s$ is the secondary current, and $R_s$ is the secondary resistance.

- The input power of a transformer is equal to the product of the primary voltage and current, plus the primary copper loss and the core loss. The primary copper loss is the power dissipated in the primary winding due to its resistance. The core loss is the power dissipated in the magnetic core due to hysteresis and eddy currents.

  $$P_i = V_p I_p + I_p^2 R_p + P_c$$

  where $V_p$ is the primary voltage, $I_p$ is the primary current, $R_p$ is the primary resistance, and $P_c$ is the core loss.

- The efficiency of a single phase transformer depends on the load condition, the voltage ratio, and the design of the transformer. The efficiency is maximum when the output power is equal to the core loss, or when the copper loss is equal to the core loss. This is called the condition of maximum efficiency.

- The efficiency of a single phase transformer is usually high, ranging from 95% to 99%. For large power transformers with very low losses, the efficiency can be as high as 99.7% .

- The efficiency of a DC machine is defined as the ratio of output power to input power, expressed as a percentage. It indicates how well the machine converts the electrical energy to mechanical energy, or vice versa, without wasting it as heat or other losses.

- The efficiency of a DC machine can be calculated by the following formula:

  $$\eta = \frac{P_o}{P_i} \times 100 \%$$

  where $\eta$ is the efficiency, $P_o$ is the output power, and $P_i$ is the input power.

- The input power and output power of a DC machine are measured in the same unit, such as watts (W) or kilowatts (kW).

- The output power of a DC machine is equal to the product of the torque and the angular speed, minus the mechanical losses. The mechanical losses are the power dissipated in the bearings, brushes, and windage.

  $$P_o = T \omega - P_m$$

  where $T$ is the torque, $\omega$ is the angular speed, and $P_m$ is the mechanical loss.

- The input power of a DC machine is equal to the product of the terminal voltage and current, minus the electrical losses. The electrical losses are the power dissipated in the armature, field, and brush circuits due to their resistances.

  $$P_i = V_t I_t - P_e$$

  where $V_t$ is the terminal voltage, $I_t$ is the terminal current, and $P_e$ is the electrical loss.

- The efficiency of a DC machine depends on the load condition, the speed, and the design of the machine. The efficiency is maximum when the output power is equal to the electrical loss, or when the mechanical loss is equal to the electrical loss. This is called the condition of maximum efficiency.

- The efficiency of a DC machine is usually lower than that of a transformer, ranging from 80% to 90%. For small DC machines with high losses, the efficiency can be as low as 50%.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

# CO 5 Perform experiments on speed measurement and reversal of direction of three phase induction motor and Identify the type of DC and AC machines based on their construction. K4

- A three phase induction motor is a type of AC machine that converts electrical energy into mechanical energy by using the principle of electromagnetic induction.
- The speed of a three phase induction motor depends on the frequency of the AC supply, the number of poles in the stator winding, and the slip between the stator and the rotor magnetic fields.
- The speed of a three phase induction motor can be measured by using a tachometer, a stroboscope, or a frequency meter.
- The direction of rotation of a three phase induction motor can be reversed by interchanging any two of the three supply terminals. This changes the phase sequence of the stator winding and reverses the direction of the rotating magnetic field.
- A DC machine is a type of electrical machine that converts electrical energy into mechanical energy or vice versa by using the principle of commutation.
- A DC machine has two main parts: a stator and a rotor. The stator consists of a fixed magnetic field, which can be produced by permanent magnets or electromagnets. The rotor consists of a coil of wire, called the armature, which rotates in the stator magnetic field and carries the current.
- A DC machine can be classified into two types based on the connection of the armature winding: a DC generator and a DC motor. A DC generator produces DC voltage by rotating the armature in the stator magnetic field. A DC motor produces mechanical torque by applying DC voltage to the armature and rotating it in the stator magnetic field.
- An AC machine is a type of electrical machine that converts electrical energy into mechanical energy or vice versa by using the principle of electromagnetic induction.
- An AC machine has two main parts: a stator and a rotor. The stator consists of a coil of wire, called the stator winding, which produces a rotating magnetic field by carrying an AC current. The rotor consists of a coil of wire, called the rotor winding, which rotates in the stator magnetic field and induces an AC voltage or current.
- An AC machine can be classified into two types based on the type of the rotor winding: a synchronous machine and an induction machine. A synchronous machine has a rotor winding that is connected to a DC source or a permanent magnet, which produces a constant magnetic field. A synchronous machine rotates at a constant speed, which is equal to the synchronous speed of the stator magnetic field. An induction machine has a rotor winding that is not connected to any external source, but is induced by the stator magnetic field. An induction machine rotates at a speed that is slightly less than the synchronous speed of the stator magnetic field, which is called the slip speed.



#### K1 – Remember, K2 – Understand, K3 – Apply, K4 – Analyze, K5 – Evaluate, K6 – Create

- These are the six levels of cognitive learning according to Bloom's taxonomy, a framework for classifying educational objectives and outcomes.
- K1 – Remember: This level involves recalling facts, terms, definitions, or concepts from memory. Examples of verbs used at this level are: list, name, define, identify, label, recognize, etc.
- K2 – Understand: This level involves explaining the meaning, interpretation, or summary of information. Examples of verbs used at this level are: describe, explain, paraphrase, summarize, illustrate, classify, etc.
- K3 – Apply: This level involves using learned information to solve problems or perform tasks in new situations. Examples of verbs used at this level are: apply, demonstrate, use, calculate, solve, implement, etc.
- K4 – Analyze: This level involves breaking down information into parts and examining the relationships, causes, effects, or implications of each part. Examples of verbs used at this level are: analyze, compare, contrast, differentiate, examine, infer, etc.
- K5 – Evaluate: This level involves making judgments or assessments based on criteria, standards, or evidence. Examples of verbs used at this level are: evaluate, critique, justify, argue, appraise, assess, etc.
- K6 – Create: This level involves generating new ideas, products, or solutions by combining or reorganizing existing information. Examples of verbs used at this level are: create, design, invent, compose, produce, construct, etc.

