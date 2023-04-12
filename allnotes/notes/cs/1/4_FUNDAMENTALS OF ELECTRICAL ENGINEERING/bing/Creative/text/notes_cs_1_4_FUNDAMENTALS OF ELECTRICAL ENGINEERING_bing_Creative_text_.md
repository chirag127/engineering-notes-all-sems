

Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss.

Some possible topics are:

- History
- Science
- Mathematics
- Literature
- Art
- Music
- Sports
- Politics
- Philosophy
- Psychology

Please choose a topic or type your own.



# FUNDAMENTALS OF ELECTRICAL ENGINEERING

- Electrical engineering is the branch of engineering that deals with the study, design, and application of electrical and electronic systems, devices, and circuits.
- Electrical engineering covers a wide range of topics, such as electric circuits, power systems, control systems, signal processing, communication systems, and microelectronics.
- Some of the fundamental concepts of electrical engineering are:

  - Voltage, current, power, and energy: Voltage is the potential difference between two points in an electric circuit, current is the rate of flow of electric charge, power is the rate of doing work or transferring energy, and energy is the capacity to do work or transfer heat.
  - Ohm's law, Kirchhoff's laws, and Thevenin's theorem: Ohm's law states that the voltage across a resistor is proportional to the current through it, Kirchhoff's laws state that the sum of currents entering a node is equal to the sum of currents leaving it, and the sum of voltages around a loop is zero, and Thevenin's theorem states that any linear circuit can be replaced by an equivalent circuit consisting of a voltage source and a resistor.
  - Resistors, capacitors, inductors, and diodes: Resistors are passive components that oppose the flow of current, capacitors are passive components that store electric charge, inductors are passive components that store magnetic energy, and diodes are active components that allow current to flow in one direction only.
  - AC and DC circuits: AC stands for alternating current, which is a current that changes its direction and magnitude periodically, and DC stands for direct current, which is a current that flows in one direction only. AC circuits are more common in power generation and transmission, while DC circuits are more common in electronic devices and batteries.
  - Transformers, motors, and generators: Transformers are devices that change the voltage and current of an AC source, motors are devices that convert electrical energy into mechanical energy, and generators are devices that convert mechanical energy into electrical energy.
  - Frequency, phase, and impedance: Frequency is the number of cycles of an AC signal per second, phase is the angle of an AC signal relative to a reference signal, and impedance is the ratio of voltage to current for an AC circuit element. Frequency, phase, and impedance are important for analyzing the behavior and performance of AC circuits and systems.



## Unit 1 - DC Circuits

- A DC circuit is a circuit that consists of direct current (DC) sources, such as batteries, and resistors, capacitors, inductors, switches, and other components that obey Ohm's law and Kirchhoff's laws.
- Ohm's law states that the voltage across a resistor is proportional to the current through it, and the constant of proportionality is the resistance: V = IR.
- Kirchhoff's current law (KCL) states that the algebraic sum of the currents entering and leaving a node (a point where two or more branches meet) is zero: ∑I = 0.
- Kirchhoff's voltage law (KVL) states that the algebraic sum of the voltages around any closed loop (a path that starts and ends at the same node) is zero: ∑V = 0.
- A series circuit is a circuit where the components are connected end to end, so that there is only one path for the current to flow. The current is the same in every component, and the total voltage is the sum of the voltages across each component: V<sub>total</sub> = V<sub>1</sub> + V<sub>2</sub> + ... + V<sub>n</sub>.
- A parallel circuit is a circuit where the components are connected across the same pair of nodes, so that there are multiple paths for the current to flow. The voltage is the same across every component, and the total current is the sum of the currents through each component: I<sub>total</sub> = I<sub>1</sub> + I<sub>2</sub> + ... + I<sub>n</sub>.
- A series-parallel circuit is a circuit that combines both series and parallel connections of components. To analyze such a circuit, one can use the methods of simplification, such as combining resistors in series or parallel, or applying the voltage divider or current divider rules.
- A voltage divider is a series circuit that divides the input voltage into fractions across the resistors. The voltage across any resistor is given by the formula: V<sub>R</sub> = V<sub>in</sub> * (R / R<sub>total</sub>), where R<sub>total</sub> is the total resistance of the series circuit.
- A current divider is a parallel circuit that divides the input current into fractions through the resistors. The current through any resistor is given by the formula: I<sub>R</sub> = I<sub>in</sub> * (R<sub>total</sub> / R), where R<sub>total</sub> is the equivalent resistance of the parallel circuit.



### Electrical circuit elements (R, L and C)

- Electrical circuit elements are components that can store, dissipate, or transfer electrical energy in a circuit.
- The most common circuit elements are resistors (R), inductors (L), and capacitors (C).
- Resistors are devices that oppose the flow of electric current and convert electrical energy into heat. The resistance of a resistor is measured in ohms (Ω) and depends on its material, shape, and temperature. The voltage across a resistor is proportional to the current through it, according to Ohm's law: V = IR, where V is the voltage, I is the current, and R is the resistance.
- Inductors are devices that store electrical energy in a magnetic field when current flows through them. The inductance of an inductor is measured in henries (H) and depends on its shape, size, and number of turns of wire. The voltage across an inductor is proportional to the rate of change of current through it, according to Faraday's law: V = L(dI/dt), where V is the voltage, L is the inductance, and dI/dt is the derivative of current with respect to time.
- Capacitors are devices that store electrical energy in an electric field when voltage is applied across them. The capacitance of a capacitor is measured in farads (F) and depends on its shape, size, and type of dielectric material. The charge on a capacitor is proportional to the voltage across it, according to the definition of capacitance: Q = CV, where Q is the charge, C is the capacitance, and V is the voltage. The current through a capacitor is proportional to the rate of change of voltage across it, according to the definition of current: I = C(dV/dt), where I is the current, C is the capacitance, and dV/dt is the derivative of voltage with respect to time.
- The behavior of circuit elements can be analyzed using Kirchhoff's laws, which state that the sum of currents entering a node is equal to the sum of currents leaving it (Kirchhoff's current law or KCL), and that the sum of voltages around a closed loop is equal to zero (Kirchhoff's voltage law or KVL).
- The response of circuit elements to different types of input signals, such as direct current (DC), alternating current (AC), or transient signals, can be determined using various methods, such as mesh analysis, nodal analysis, superposition, Thevenin's theorem, Norton's theorem, or phasor analysis.



### Concept of active and passive elements

- Active and passive elements are two types of electronic circuit elements that have different roles and characteristics.
- Active elements are capable of supplying energy to the circuit or providing amplification of the signal. They can control the direction and magnitude of the current or voltage in the circuit. They usually require an external power source to operate. Examples of active elements are transistors, diodes, operational amplifiers, generators, etc.
- Passive elements are incapable of supplying energy to the circuit or providing amplification of the signal. They can only receive, store, or dissipate energy in the circuit. They do not require an external power source to operate. Examples of passive elements are resistors, capacitors, inductors, transformers, etc.
- The main difference between active and passive elements is that active elements can increase the power of the signal, while passive elements can only decrease or maintain the power of the signal.
- Active and passive elements are used for different purposes in electronic circuits. Active elements are used for current and voltage control, signal processing, switching, amplification, etc. Passive elements are used for energy storage, filtering, impedance matching, oscillation, etc.



### Voltage and Current Sources

- A voltage source is a device that provides a constant voltage across its terminals, regardless of the current drawn by the load .
- A current source is a device that provides a constant current through its terminals, regardless of the voltage across the load .
- Both voltage and current sources are idealized models that do not exist in reality, but are useful for circuit analysis and design .
- A practical voltage source has some internal resistance, which causes the output voltage to drop as the load current increases.
- A practical current source has some internal resistance, which causes the output current to decrease as the load voltage increases.
- Voltage and current sources can be either independent or dependent .
- An independent source is a device that provides a fixed voltage or current, regardless of any other variable in the circuit .
- A dependent source is a device that provides a voltage or current that is proportional to some other variable in the circuit, such as voltage, current, power, or resistance .
- Voltage and current sources are used to model various types of energy conversion devices, such as batteries, generators, solar cells, transistors, etc  .
- Voltage and current sources are also used to apply external stimuli to a circuit, such as input signals, test signals, bias voltages, etc  .



### Concept of Linearity

- Linearity is a property of an element or a system that describes a linear relationship between cause and effect.
- A linear element or system obeys the principles of homogeneity and additivity.
- Homogeneity means that if the input is scaled by a factor, the output is also scaled by the same factor.
- Additivity means that if the input is the sum of two or more signals, the output is also the sum of the corresponding outputs.
- In electrical engineering, linearity is often applied to the current-voltage characteristics of a component or a circuit.
- A linear component or circuit has a current-voltage curve that is a straight line, meaning that the current is proportional to the voltage.
- Examples of linear components are resistors, capacitors, and inductors.
- A linear circuit is a circuit that consists of only linear components and independent sources.
- A linear system is a system that can be modeled by a linear equation or a set of linear equations.
- Examples of linear systems are amplifiers, filters, and oscillators.
- Linearity is a useful property because it simplifies the analysis and design of electrical circuits and systems.
- One of the benefits of linearity is that it allows the use of superposition, which is a technique to find the response of a linear circuit or system to multiple inputs by adding the individual responses to each input.
- Another benefit of linearity is that it enables the use of frequency domain methods, such as Fourier and Laplace transforms, to solve linear differential equations that describe the behavior of electrical circuits and systems.



### Unilateral and Bilateral Elements

- Unilateral and bilateral elements are the two different types of electrical / electronic circuit elements on the basis of their V-I characteristics on reversal of voltage polarity.
- Unilateral elements are those that allow the current in only one direction and offer different impedance in different directions of current flow. Examples: Diodes, Transistors  .
- Bilateral elements are those that allow the current in both directions and offer the same impedance in either direction of current flow. Examples: Resistors, Inductors, Capacitors  .
- Unilateral and bilateral circuits are the circuits that contain only unilateral or only bilateral elements, or a combination of both.
- Unilateral and bilateral circuits can be used for various applications such as amplifiers, oscillators, power supplies and more.



### Kirchhoff's laws for DC circuits

Kirchhoff's laws are two principles that govern the analysis of electric circuits. They are named after Gustav Kirchhoff, a German physicist who formulated them in 1845. They are:

- Kirchhoff's current law (KCL): This law states that the algebraic sum of the currents entering and leaving any node (or junction) in a circuit is zero. In other words, the total current entering a node is equal to the total current leaving the node. This is based on the conservation of electric charge. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current of the k-th branch connected to the node.

- Kirchhoff's voltage law (KVL): This law states that the algebraic sum of the voltages around any closed loop (or mesh) in a circuit is zero. In other words, the total voltage rise in a loop is equal to the total voltage drop in the loop. This is based on the conservation of energy. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage of the k-th element in the loop.

Kirchhoff's laws are used to find the values of current, voltage, and resistance in DC circuits. They can also be used to find the unknown resistance in a circuit using a Wheatstone bridge. They are the basis of mesh and node analysis, which are systematic methods to solve complex circuits. They are applicable to any circuit configuration, as long as the circuit is linear and time-invariant.

Some limitations of Kirchhoff's laws are:

- They do not account for the effects of electromagnetic induction, which can cause voltage and current to vary with time in a circuit.
- They do not account for the effects of radiation, which can cause energy loss or gain in a circuit.
- They do not account for the effects of quantum mechanics, which can cause discrete changes in voltage and current in a circuit.

Some examples of applying Kirchhoff's laws to DC circuits are:

- Example 1: Find the current through each resistor in the following circuit.

  Circuit 1

  Solution: Applying KCL to node A, we get:

  $$I_1 + I_2 = I_3$$

  Applying KVL to loop ABCDA, we get:

  $$10 - 2I_1 - 3I_2 = 0$$

  Solving these two equations, we get:

  $$I_1 = 2.5 A$$
  $$I_2 = 1.67 A$$
  $$I_3 = 4.17 A$$

- Example 2: Find the voltage across each resistor in the following circuit.

  Circuit 2

  Solution: Applying KVL to loop ABFEDCBA, we get:

  $$V_1 + V_2 + V_3 - 12 = 0$$

  Applying Ohm's law to each resistor, we get:

  $$V_1 = 2I_1$$
  $$V_2 = 4I_2$$
  $$V_3 = 6I_3$$

  Applying KCL to node B, we get:

  $$I_1 = I_2 + I_3$$

  Substituting these expressions into the KVL equation, we get:

  $$2I_1 + 4I_2 + 6I_3 - 12 = 0$$

  Solving this equation, we get:

  $$I_1 = 1.5 A$$
  $$I_2 = 0.5 A$$
  $$I_3 = 1 A$$

  Therefore, the voltages across the resistors are:

  $$V_1 = 3 V$$
  $$V_2 = 2 V$$
  $$V_3 = 6 V$$



### Mesh and Nodal Methods of Analysis

- Mesh and nodal methods of analysis are two systematic techniques for solving linear circuits.
- Both methods are based on applying Kirchhoff's laws and Ohm's law to the circuit elements.
- Mesh analysis is a method that uses loop currents as the circuit variables.
- Nodal analysis is a method that uses node voltages as the circuit variables.
- The steps for applying mesh analysis are:
  - Identify all the meshes (loops that do not contain any other loop) in the circuit and assign a current to each mesh in a clockwise direction.
  - Write Kirchhoff's voltage law (KVL) equations for each mesh, expressing the voltage drops across each element in terms of the mesh currents.
  - Solve the system of linear equations for the mesh currents using any method such as substitution, elimination, or matrix inversion.
  - Find the voltages across any element or the currents through any branch by using Ohm's law and the mesh currents.
- The steps for applying nodal analysis are:
  - Identify all the nodes (points where two or more elements are connected) in the circuit and assign a voltage to each node with respect to a reference node (usually the ground).
  - Write Kirchhoff's current law (KCL) equations for each node, expressing the currents entering and leaving the node in terms of the node voltages and the element parameters.
  - Solve the system of linear equations for the node voltages using any method such as substitution, elimination, or matrix inversion.
  - Find the currents through any element or the voltages across any branch by using Ohm's law and the node voltages.
- The advantages of mesh analysis are:
  - It reduces the number of equations to be solved compared to nodal analysis, especially for planar circuits (circuits that can be drawn on a plane without any crossing branches).
  - It is easier to handle voltage sources and dependent sources in mesh analysis than in nodal analysis.
- The advantages of nodal analysis are:
  - It reduces the number of variables to be solved compared to mesh analysis, especially for non-planar circuits (circuits that cannot be drawn on a plane without any crossing branches).
  - It is easier to handle current sources and parallel branches in nodal analysis than in mesh analysis.



## Unit 2 - Steady State Analysis of Single Phase AC Circuits

- In this unit, we will learn how to analyze single phase AC circuits using phasors, complex numbers, and impedance.
- AC circuits are circuits that are powered by alternating current (AC) sources, such as sinusoidal voltage or current sources.
- AC sources have a frequency (f), which is the number of cycles per second, and an angular frequency (ω), which is 2πf radians per second.
- AC sources also have a peak value (Vp or Ip), which is the maximum value of the voltage or current, and a root mean square (RMS) value (Vrms or Irms), which is the effective value of the voltage or current.
- The RMS value of a sinusoidal voltage or current is equal to the peak value divided by the square root of 2, or Vrms = Vp/√2 and Irms = Ip/√2.
- AC sources can also have a phase angle (φ), which is the angle by which the voltage or current leads or lags the reference waveform, usually taken as the cosine wave.
- The phase angle can be positive or negative, depending on whether the voltage or current is leading or lagging the reference.
- The phase angle can be expressed in degrees or radians, and it can be converted from one to another using the formula φ(rad) = φ(deg) × π/180.

- To analyze AC circuits, we use phasors, which are rotating vectors that represent sinusoidal voltages or currents in the complex plane.
- Phasors have a magnitude, which is the peak value of the voltage or current, and an angle, which is the phase angle of the voltage or current.
- Phasors can be written in rectangular form, using real and imaginary parts, or in polar form, using magnitude and angle.
- For example, a sinusoidal voltage of V(t) = Vp cos(ωt + φ) can be represented by a phasor of V = Vp ∠ φ in polar form, or V = Vp cos φ + jVp sin φ in rectangular form, where j is the imaginary unit.
- Phasors can be added, subtracted, multiplied, and divided using the rules of complex numbers.
- Phasors can also be converted from one form to another using the formulas:

  - Rectangular to polar: |V| = √(Re(V)^2 + Im(V)^2) and ∠V = tan^(-1)(Im(V)/Re(V))
  - Polar to rectangular: Re(V) = |V| cos ∠V and Im(V) = |V| sin ∠V

- To analyze AC circuits, we also use impedance, which is the ratio of phasor voltage to phasor current in an AC circuit element.
- Impedance is a complex quantity that has a magnitude and an angle, and it can be written in rectangular or polar form, similar to phasors.
- Impedance can be calculated for different circuit elements, such as resistors, capacitors, and inductors, using the formulas:

  - Resistor: ZR = R ∠ 0°
  - Capacitor: ZC = 1/jωC = -j/ωC ∠ -90°
  - Inductor: ZL = jωL ∠ 90°

- Impedance can also be combined for series and parallel connections of circuit elements, using the rules of series and parallel resistances, but with complex numbers instead of real numbers.
- For example, the equivalent impedance of two series impedances Z1 and Z2 is Zeq = Z1 + Z2, and the equivalent impedance of two parallel impedances Z1 and Z2 is Zeq = (Z1Z2)/(Z1 + Z2).

- To analyze AC circuits, we can use the following steps:

  1. Identify the AC source and its frequency, peak value, and phase angle.
  2. Convert the AC source to a phasor voltage or current, using rectangular or polar form.
  3. Identify the circuit elements and their values, such as resistance, capacitance, and inductance.
  4. Convert the circuit elements to impedances, using rectangular or polar form.
  5. Simplify the circuit by combining series and parallel impedances, using the rules of complex numbers.
  6. Apply Kirchhoff's voltage law (KVL) and Kirchhoff's current law (KCL) to the simplified circuit, using the rules of phasor algebra.
  7. Solve for the unknown phas



### Representation of Sinusoidal waveforms – Average and effective values

- A sinusoidal waveform is a periodic function that oscillates between positive and negative peak values with a constant frequency.
- The peak value (Vp) of a sinusoidal waveform is the maximum or minimum amplitude of the waveform.
- The average value (Vav) of a sinusoidal waveform is the arithmetic mean of the waveform over one complete cycle. It is calculated by multiplying the peak value by 0.637.
- The effective value (Vrms) of a sinusoidal waveform is the equivalent DC value that would produce the same heating effect in a resistor as the AC waveform. It is calculated by multiplying the peak value by 0.707.
- The form factor (FF) of a sinusoidal waveform is the ratio of the effective value to the average value. It is always equal to 1.11 for a pure sinusoidal waveform.
- The peak factor (PF) of a sinusoidal waveform is the ratio of the peak value to the effective value. It is always equal to 1.414 for a pure sinusoidal waveform.
- A sinusoidal waveform can be represented by a phasor, which is a rotating vector with a constant magnitude and angular frequency. The phasor can be used to analyze the phase difference and impedance of AC circuits.



### Form and peak factors for the notes of the Unit 2 - Steady State Analysis of Single Phase AC Circuits in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

- Form factor is a parameter used in describing AC waveforms and is given by the ratio between the RMS value of the alternating quantity and the average value.
- RMS value is the effective value of an AC waveform that produces the same heating effect as a DC voltage of the same magnitude.
- Average value is the arithmetic mean of the positive half cycle of an AC waveform.
- Form factor can be expressed as:

$$
F_f = \frac{V_{rms}}{V_{avg}}
$$

- Where $V_{rms}$ is the RMS value and $V_{avg}$ is the average value of the AC waveform.
- Peak factor is also called as crest factor and is defined as the ratio of the peak value of an AC waveform to the RMS value.
- Peak value is the maximum value attained by an AC waveform during a half cycle.
- Peak factor can be expressed as:

$$
F_p = \frac{V_{peak}}{V_{rms}}
$$

- Where $V_{peak}$ is the peak value and $V_{rms}$ is the RMS value of the AC waveform.
- The form factor and peak factor values for different types of AC waveforms are given in the table below :

| Waveform | Form factor | Peak factor |
|----------|-------------|-------------|
| Sinusoidal | 1.11 | 1.41 |
| Half-wave rectified | 1.57 | 2 |
| Full-wave rectified | 1.11 | 1.41 |
| Triangular | 1.15 | 1.73 |
| Square | 1 | 1 |

- Form factor and peak factor are useful in analyzing the shape and quality of AC waveforms and their effects on electrical circuits and devices.



### Analysis of single phase AC Circuits consisting R-L-C combination (Series and Parallel)

- A single phase AC circuit is a circuit that is powered by a single alternating voltage or current source.
- A R-L-C circuit is a circuit that contains a resistor (R), an inductor (L) and a capacitor (C) as its elements.
- A R-L-C circuit can be connected in series or parallel, depending on how the elements are arranged with respect to the voltage or current source.
- In a series R-L-C circuit, the elements are connected one after another, forming a single loop. The same current flows through all the elements, but the voltage across each element may differ.
- In a parallel R-L-C circuit, the elements are connected across the same two terminals, forming multiple branches. The same voltage is applied across all the elements, but the current through each element may differ.
- The analysis of R-L-C circuits involves finding the voltage, current, power, impedance, admittance, phase angle and resonance frequency of the circuit or its elements, using various methods such as Kirchhoff's laws, phasor diagrams, complex algebra, etc.
- The impedance (Z) of a series R-L-C circuit is the total opposition to the current flow, and it is given by the vector sum of the resistance (R), the inductive reactance (X_L) and the capacitive reactance (X_C). The impedance can be expressed as a complex number Z = R + j(X_L - X_C), where j is the imaginary unit.
- The admittance (Y) of a parallel R-L-C circuit is the total ease of the current flow, and it is given by the vector sum of the conductance (G), the inductive susceptance (B_L) and the capacitive susceptance (B_C). The admittance can be expressed as a complex number Y = G + j(B_C - B_L), where j is the imaginary unit.
- The phase angle (phi) of a R-L-C circuit is the angle between the voltage and the current phasors, and it indicates the degree of phase shift between them. The phase angle can be positive, negative or zero, depending on the relative values of R, L and C. The phase angle can be calculated using the formula tan(phi) = X/R for series circuits, and tan(phi) = B/G for parallel circuits, where X and B are the net reactance and susceptance, respectively.
- The resonance frequency (f_0) of a R-L-C circuit is the frequency at which the circuit exhibits maximum or minimum impedance or admittance, depending on whether it is series or parallel. The resonance frequency can be found by equating the net reactance or susceptance to zero, and solving for f. The resonance frequency can be expressed as f_0 = 1/(2*pi*sqrt(LC)) for both series and parallel circuits, where L and C are the inductance and capacitance, respectively.



### Apparent, active and reactive power

- Apparent power is the product of the RMS voltage and current in an AC circuit, without reference to the phase angle between them. It is measured in volt-amperes (VA) and is symbolized by S.
- Active power is the component of apparent power that does real work in the circuit, such as heating, lighting, or motion. It is in phase with the voltage and is measured in watts (W) and is symbolized by P.
- Reactive power is the component of apparent power that does not do any work, but is needed to maintain the voltage levels in the circuit. It is out of phase with the voltage and is measured in volt-amperes reactive (VAR) and is symbolized by Q.
- The relationship between apparent, active and reactive power can be represented by a right-angled triangle called the power triangle, where the hypotenuse is the apparent power, the base is the active power, and the height is the reactive power  .
- The angle between the apparent power and the active power is called the power factor angle, and it indicates how much of the apparent power is converted into active power. The power factor is the cosine of this angle, and it ranges from 0 to 1. A power factor of 1 means that all the apparent power is active power, and a power factor of 0 means that all the apparent power is reactive power  .
- The apparent, active and reactive power can be calculated using the following formulas :

  - S = Vrms * Irms
  - P = Vrms * Irms * cos(θ)
  - Q = Vrms * Irms * sin(θ)
  - S^2 = P^2 + Q^2
  - cos(θ) = P / S
  - sin(θ) = Q / S
  - tan(θ) = Q / P



### Power factor

- Power factor is a dimensionless quantity that measures how effectively an AC circuit uses the supplied power.
- Power factor is defined as the ratio of the real power (P) absorbed by the load to the apparent power (S) flowing in the circuit. Real power is the average of the instantaneous product of voltage and current and represents the capacity of the electricity for performing work. Apparent power is the product of the root mean square (RMS) values of voltage and current and represents the amount of power that the circuit draws from the source.  
- Power factor can also be expressed as the cosine of the angle (θ) by which the current waveform lags or leads the voltage waveform. This angle is called the phase angle and it depends on the type of load in the circuit. 
- Power factor can range from 0 to 1. A power factor of 1 means that the current and voltage are in phase and the circuit is purely resistive. A power factor of 0 means that the current and voltage are out of phase by 90 degrees and the circuit is purely reactive. A power factor between 0 and 1 means that the circuit has both resistive and reactive components and the current and voltage are out of phase by some angle less than 90 degrees. 
- Power factor is important because it affects the efficiency and reliability of the power system. A low power factor means that the circuit draws more current than necessary to deliver the same amount of real power. This increases the losses in the transmission lines and the voltage drop across them. It also reduces the available capacity of the power source and the circuit breakers. A high power factor means that the circuit draws less current and operates more efficiently. 
- Power factor can be improved by adding power factor correction devices such as capacitors or inductors to the circuit. These devices can cancel out the reactive power and bring the current and voltage closer to being in phase. This reduces the apparent power and increases the power factor.



### Concept of Resonance in series & parallel circuits

- Resonance is a condition that occurs in AC circuits when the reactive power of the capacitors and of the inductors become equal.
- Resonance can happen in circuits where capacitors and inductors are connected in series or in parallel.
- In series resonance, the circuit impedance is minimum and the current is maximum at the resonant frequency. The series resonance circuit is also known as the acceptor circuit because it accepts the maximum power from the source at the resonant frequency.
- In parallel resonance, the circuit impedance is maximum and the current is minimum at the resonant frequency. The parallel resonance circuit is also known as the rejector circuit because it rejects the maximum power from the source at the resonant frequency.
- The resonant frequency of a series or parallel circuit is given by the formula: f0 = 1 / (2π√LC), where L is the inductance and C is the capacitance.
- The quality factor or Q factor of a series or parallel circuit is a measure of how sharp the resonance is. It is defined as the ratio of the reactive power to the resistive power at the resonant frequency.
- The Q factor of a series circuit is given by the formula: Qseries = XL / R, where XL is the inductive reactance and R is the resistance.
- The Q factor of a parallel circuit is given by the formula: Qparallel = RT / XL, where RT is the total parallel resistance and XL is the inductive reactance.
- The Q factor of a series or parallel circuit determines the bandwidth or the range of frequencies around the resonant frequency where the circuit behaves as a resonant circuit.
- The bandwidth of a series or parallel circuit is given by the formula: B = f0 / Q, where f0 is the resonant frequency and Q is the quality factor.
- The bandwidth of a series or parallel circuit is inversely proportional to the Q factor. A higher Q factor means a narrower bandwidth and a sharper resonance, and vice versa.
- The presence of resistance in a series or parallel circuit can affect the resonant frequency and the Q factor. Resistance can cause the resonant frequency to shift from the calculated value and the Q factor to decrease .
- The effect of resistance on the resonant frequency and the Q factor is called antiresonance. Antiresonance can be minimized by choosing components with low resistance or by using tuning methods .



### Bandwidth and Quality Factor for the Notes of the Unit 2 - Steady State Analysis of Single Phase AC Circuits in the Subject of Fundamentals of Electrical Engineering

- Bandwidth of a resonant circuit is the range of frequencies over which the current or voltage amplitude is equal to or greater than 70.7% of its maximum value at the resonant frequency  .
- Quality factor of a resonant circuit is a dimensionless quantity that measures how underdamped the circuit is, or equivalently, how narrow the bandwidth of the circuit is    .
- The quality factor is inversely proportional to the bandwidth, meaning that a high quality factor implies a low bandwidth and vice versa    .
- The quality factor can be calculated from the resonant frequency and the bandwidth using the following formula    :

Q = f_r / BW

where f_r is the resonant frequency and BW is the bandwidth.

- The quality factor can also be calculated from the resistance, inductance and capacitance of the circuit using the following formulas    :

For a series resonant circuit:

Q = X_L / R = X_C / R = 1 / (R * sqrt(C / L))

where X_L is the inductive reactance, X_C is the capacitive reactance, R is the resistance, C is the capacitance and L is the inductance.

For a parallel resonant circuit:

Q = R / X_L = R / X_C = R * sqrt(C / L)

where X_L, X_C, R, C and L have the same meanings as above.

- The bandwidth can be calculated from the quality factor and the resonant frequency using the following formula    :

BW = f_r / Q

where f_r and Q have the same meanings as above.

- The bandwidth can also be calculated from the half-power frequencies, which are the frequencies at which the current or voltage amplitude is 50% of its maximum value at the resonant frequency  . The half-power frequencies are also called the 3 dB frequencies or the cutoff frequencies  . The bandwidth is the difference between the upper and lower half-power frequencies  :

BW = f_h - f_l

where f_h is the upper half-power frequency and f_l is the lower half-power frequency.



### Three phase balanced circuits

- A three phase balanced circuit is a type of alternating current circuit that consists of three voltage sources and three loads connected in either star or delta configuration.
- The three voltage sources have equal magnitudes and frequencies, but are phase shifted by 120 degrees with respect to each other. The three loads have equal impedances and power factors.
- In a three phase balanced circuit, the total power delivered by the sources is equal to the total power consumed by the loads, and the neutral current is zero.
- The advantages of using three phase balanced circuits are higher efficiency, lower cost, and smoother operation of electrical machines and devices.
- The analysis of a three phase balanced circuit can be simplified by using the following steps:
  - Choose a reference phase, usually phase a, and assign the positive direction of the current and voltage in that phase.
  - Draw the phasor diagram of the voltages and currents in the reference phase, using the phase sequence abc or acb depending on the polarity of the sources.
  - Apply Kirchhoff's voltage law and Kirchhoff's current law to the reference phase, and solve for the unknown variables.
  - Use the phase shift of 120 degrees to find the voltages and currents in the other two phases, b and c.
  - Calculate the power and power factor of each phase and the total power and power factor of the circuit.



Hello, I am Sydney, your AI assistant. I can help you with your topic of voltage and current relations in star and delta connections for the notes of the Unit 2 - Steady State Analysis of Single Phase AC Circuits in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING. Here is a summary of the main points:

- A star connection is a three-phase system where one end of each phase winding is connected to a common point called the neutral point, and the other end is connected to the line terminal. A delta connection is a three-phase system where each phase winding is connected in a loop, and the line terminals are connected at the junctions of the windings.
- In a star connection, the line voltage (the voltage between any two line terminals) is equal to the square root of three times the phase voltage (the voltage between the neutral point and any line terminal). In a delta connection, the line voltage is equal to the phase voltage (the voltage across any phase winding).
- In a star connection, the line current (the current flowing in any line terminal) is equal to the phase current (the current flowing in the corresponding phase winding). In a delta connection, the line current is equal to the square root of three times the phase current (the current flowing in any phase winding).
- The power transmitted by both the star and delta connections is the same, and is equal to three times the product of the line voltage and the line current. However, the power factor (the ratio of the real power to the apparent power) may differ depending on the load impedance and the connection type.
- Both star and delta connections can be used for three-phase four-wire systems, where a neutral wire is also provided along with the three line wires. However, only star connections can be used for three-phase three-wire systems, where no neutral wire is available. The choice of the connection type depends on the load characteristics, the voltage level, and the cost and availability of the transformers.



## Unit 3 - Transformers

- A transformer is a device that converts alternating current (AC) from one voltage level to another voltage level by using the principle of electromagnetic induction.
- A transformer consists of two or more coils of wire, called the primary and secondary windings, that are wound around a common core, usually made of iron or steel.
- The primary winding is connected to the AC source, and the secondary winding is connected to the load. When an AC voltage is applied to the primary winding, it creates a changing magnetic flux in the core, which induces an AC voltage in the secondary winding.
- The ratio of the number of turns in the primary and secondary windings determines the voltage transformation. If the secondary winding has more turns than the primary winding, the output voltage is higher than the input voltage, and the transformer is called a step-up transformer. If the secondary winding has fewer turns than the primary winding, the output voltage is lower than the input voltage, and the transformer is called a step-down transformer.
- The power transferred from the primary to the secondary winding is equal to the product of the voltage and current in each winding, assuming no losses. Therefore, the current transformation is inversely proportional to the voltage transformation. If the output voltage is higher than the input voltage, the output current is lower than the input current, and vice versa.
- Transformers are used for various purposes, such as to increase or decrease the voltage of AC circuits, to isolate different parts of a circuit, to match the impedance of a source and a load, to transmit electrical energy over long distances, and to control the frequency and phase of AC signals .
- Transformers can be classified into different types based on their construction, operation, and application. Some common types of transformers are: single-phase and three-phase transformers, shell-type and core-type transformers, auto-transformers, isolation transformers, current transformers, potential transformers, audio transformers, power transformers, distribution transformers, and instrument transformers .



### Magnetic circuits

- A magnetic circuit is a closed path to which a magnetic field, represented as lines of magnetic flux, is confined .
- A magnetic circuit is analogous to an electric circuit, but instead of electric charge flowing, the magnetic flux is the quantity of interest.
- A magnetic circuit consists of a structure composed for the most part of high permeability magnetic material, such as iron, which guides the magnetic flux.
- The presence of high permeability material causes the magnetic flux to be confined to the paths defined by the structure, much as currents are confined to the conductors of an electric circuit.
- A magnetic circuit may have air gaps or other materials in the path, which increase the reluctance of the circuit and reduce the flux.
- Some examples of magnetic circuits are: horseshoe magnet with iron keeper (low-reluctance circuit), horseshoe magnet with no keeper (high-reluctance circuit), electric motor (variable-reluctance circuit), and transformer (magnetic circuit with two or more windings).
- The analysis of magnetic circuits is based on the following principles:
  - The total magnetic flux in a closed magnetic circuit is zero, according to Gauss's law for magnetism.
  - The magnetic flux in a magnetic circuit is proportional to the magnetomotive force (MMF) and inversely proportional to the reluctance, according to Ohm's law for magnetic circuits.
  - The MMF in a series magnetic circuit is equal to the sum of the MMFs of the individual components, according to Kirchhoff's voltage law for magnetic circuits.
  - The magnetic flux in a parallel magnetic circuit is equal to the sum of the fluxes of the individual branches, according to Kirchhoff's current law for magnetic circuits.



### Ideal and Practical Transformer

- An ideal transformer is a hypothetical device that has no energy losses and perfect coupling between the primary and secondary windings. A practical transformer is a real device that has some energy losses and imperfect coupling between the windings.
- The main differences between an ideal and practical transformer are:

  - Efficiency: An ideal transformer has 100% efficiency, meaning that the input power is equal to the output power. A practical transformer has less than 100% efficiency, meaning that some power is lost as heat, core losses, and leakage flux. The efficiency of a practical transformer depends on the power factor and loading of the transformer .
  - Winding resistance: An ideal transformer has zero resistance in both windings, meaning that there is no voltage drop across the windings. A practical transformer has some resistance in both windings, meaning that there is some voltage drop across the windings. The voltage drop reduces the output voltage and increases the copper losses .
  - Leakage flux: An ideal transformer has no leakage flux, meaning that all the flux produced by the primary winding links with the secondary winding. A practical transformer has some leakage flux, meaning that some flux produced by the primary winding does not link with the secondary winding. The leakage flux reduces the mutual inductance and the output voltage of the transformer .
  - Core losses: An ideal transformer has zero core losses, meaning that there is no hysteresis or eddy current loss in the core. A practical transformer has some core losses, meaning that there is some hysteresis and eddy current loss in the core. The core losses reduce the output power and increase the temperature of the transformer .
  - Magnetizing current: An ideal transformer has zero magnetizing current, meaning that the primary winding draws no current from the source when the secondary winding is open. A practical transformer has some magnetizing current, meaning that the primary winding draws some current from the source even when the secondary winding is open. The magnetizing current creates a no-load loss and reduces the power factor of the transformer .

- The ideal transformer is a useful model for analyzing the basic principles and performance of a practical transformer. However, the ideal transformer does not account for the energy losses and imperfections that are present in a real transformer. Therefore, the practical transformer is a more realistic model for designing and operating a transformer in the real world.



### Equivalent Circuit of a Transformer

- An equivalent circuit of a transformer is a simplified representation of a real transformer that shows its electrical parameters such as winding resistance, leakage reactance, magnetizing admittance, and core losses.
- An equivalent circuit of a transformer helps to analyze its performance under different operating conditions and to design efficient and reliable transformers.
- There are two types of equivalent circuits of a transformer: the no-load equivalent circuit and the exact equivalent circuit.

#### No-Load Equivalent Circuit of a Transformer

- The no-load equivalent circuit of a transformer is obtained by neglecting the primary winding resistance and leakage reactance, and assuming that the secondary winding is open-circuited.
- The no-load equivalent circuit of a transformer consists of a voltage source E1 that represents the induced emf in the primary winding, and a parallel branch of a resistance R0 and a reactance X0 that represent the core losses and the magnetizing current respectively.
- The no-load equivalent circuit of a transformer is shown below:

No-Load Equivalent Circuit of a Transformer

- The no-load equivalent circuit of a transformer can be used to calculate the no-load current I0, the no-load power factor cosφ0, the iron losses Pi, and the magnetizing reactance Xm.

#### Exact Equivalent Circuit of a Transformer

- The exact equivalent circuit of a transformer is obtained by considering the primary winding resistance R1 and leakage reactance X1, and the secondary winding resistance R2 and leakage reactance X2, and assuming that the secondary winding is loaded with a load impedance ZL.
- The exact equivalent circuit of a transformer consists of a voltage source E1 that represents the induced emf in the primary winding, a series branch of a resistance R1 and a reactance X1 that represent the primary winding impedance, a parallel branch of a resistance R0 and a reactance X0 that represent the core losses and the magnetizing current respectively, and a series branch of a resistance R2' and a reactance X2' that represent the secondary winding impedance referred to the primary side, and a load impedance ZL' that represents the load impedance referred to the primary side.
- The exact equivalent circuit of a transformer is shown below:

Exact Equivalent Circuit of a Transformer

- The exact equivalent circuit of a transformer can be used to calculate the primary and secondary voltages V1 and V2, the primary and secondary currents I1 and I2, the primary and secondary power factors cosφ1 and cosφ2, the copper losses Pc, the iron losses Pi, the efficiency η, and the voltage regulation VR.



### Losses in Transformers

A transformer is a device that transfers electrical energy from one circuit to another by electromagnetic induction. It consists of two or more coils of wire that are wound around a magnetic core. The primary coil is connected to the input voltage source, and the secondary coil is connected to the output load. The transformer works on the principle of mutual induction, which means that a changing current in one coil induces a voltage in the other coil.

However, a transformer is not a perfect device, and some energy is lost during the process of energy transfer. These losses reduce the efficiency and performance of the transformer. The losses in a transformer can be classified into four main types     :

- **Copper loss**: This is the power loss due to the resistance of the transformer windings. The current flowing through the windings causes heat dissipation, which reduces the output power. The copper loss depends on the current and the resistance of the windings, and it can be calculated by the formula:

  `P_c = I_1^2 R_1 + I_2^2 R_2`

  where `P_c` is the copper loss, `I_1` and `I_2` are the currents in the primary and secondary windings, and `R_1` and `R_2` are the resistances of the primary and secondary windings.

- **Core loss**: This is the power loss due to the magnetic properties of the transformer core. The core loss consists of two components: hysteresis loss and eddy current loss. The hysteresis loss is caused by the repeated magnetization and demagnetization of the core material, which results in energy dissipation. The eddy current loss is caused by the currents induced in the core by the changing magnetic flux, which also causes heat dissipation. The core loss depends on the frequency and the flux density of the magnetic field, and it can be calculated by the formula:

  `P_i = P_h + P_e`

  where `P_i` is the core loss, `P_h` is the hysteresis loss, and `P_e` is the eddy current loss.

- **Stray loss**: This is the power loss due to the leakage of the magnetic flux from the transformer. The leakage flux is the part of the magnetic flux that does not link the primary and secondary windings, and it causes unwanted currents and voltages in the surrounding parts of the transformer. The stray loss depends on the design and construction of the transformer, and it can be reduced by using proper insulation and shielding.

- **Dielectric loss**: This is the power loss due to the insulation material of the transformer. The insulation material acts as a capacitor, which stores and releases electric energy when the voltage across it changes. The dielectric loss is caused by the dissipation of this electric energy as heat. The dielectric loss depends on the frequency and the quality of the insulation material, and it can be reduced by using low-loss materials.

The total loss in a transformer is the sum of all the above losses, and it can be calculated by the formula:

`P_t = P_c + P_i + P_s + P_d`

where `P_t` is the total loss, `P_c` is the copper loss, `P_i` is the core loss, `P_s` is the stray loss, and `P_d` is the dielectric loss.

The efficiency of a transformer is the ratio of the output power to the input power, and it can be calculated by the formula:

`η = P_o / P_i`

where `η` is the efficiency, `P_o` is the output power, and `P_i` is the input power.

The efficiency of a transformer can also be expressed in terms of the losses, as follows:

`η = 1 - (P_t / P_i)`

where `η` is the efficiency, `P_t` is the total loss, and `P_i` is the input power.

The losses in a transformer can be minimized by using proper materials, design, and construction. The losses in a transformer affect its performance, reliability, and lifespan. Therefore, it is important to understand and measure the losses in a transformer for its optimal operation and maintenance.



### Regulation and Efficiency of Transformers

- Regulation of a transformer is the measure of how well the output voltage of the transformer remains constant under varying load conditions. It is defined as the percentage change in the secondary voltage from no-load to full-load at a constant primary voltage and frequency.
- Regulation of a transformer can be calculated by the formula:

    `Regulation (%) = [(VNL - VFL) / VFL] x 100`

    where VNL is the no-load secondary voltage and VFL is the full-load secondary voltage.

- A transformer with low regulation has a more stable output voltage and is more desirable for most applications. The regulation of a transformer depends on its design, construction, and operating conditions.

- Efficiency of a transformer is the ratio of the output power to the input power. It is expressed as a percentage and indicates how well the transformer converts electrical energy from one circuit to another. It is defined as:

    `Efficiency (%) = [(Pout / Pin) x 100]`

    where Pout is the output power and Pin is the input power.

- Efficiency of a transformer can be improved by reducing the losses in the transformer. There are two types of losses in a transformer: core losses and copper losses.

- Core losses are the losses due to the hysteresis and eddy currents in the magnetic core of the transformer. They depend on the frequency, flux density, and quality of the core material. They are constant for a given transformer and can be minimized by using high-grade steel or laminated cores.

- Copper losses are the losses due to the resistance of the windings of the transformer. They depend on the current, resistance, and temperature of the windings. They vary with the load and can be minimized by using thick wires or low-resistance materials.

- The efficiency of a transformer is maximum when the core losses are equal to the copper losses. This is called the condition of maximum efficiency.

- The efficiency of a transformer is also affected by the power factor of the load. The power factor is the ratio of the true power to the apparent power of the load. It is a measure of how well the load utilizes the electrical energy supplied by the transformer. A high power factor means a more efficient load and a higher transformer efficiency.

- The efficiency of a transformer is regulated by the Department of Energy (DOE) in the United States. The DOE sets minimum efficiency standards for different types of transformers to reduce the energy consumption and greenhouse gas emissions of the power grid  .

- The DOE 2016 efficiency standards are the latest and most stringent standards for transformers sold in the United States. They require transformers to have efficiency ratings ranging from 98.70% to 99.55%, depending on the size and type of the transformer. These standards are expected to save consumers and businesses billions of dollars in energy costs and reduce CO2 emissions by millions of tons over the lifetime of the transformers.



## Unit 4 - Electrical machines

- Electrical machines are devices that convert electrical energy into mechanical energy or vice versa.
- Electrical machines can be classified into three main categories: generators, motors and transformers.
- Generators are machines that convert mechanical energy into electrical energy. They use the principle of electromagnetic induction to produce voltage and current in a coil of wire that rotates in a magnetic field.
- Motors are machines that convert electrical energy into mechanical energy. They use the principle of electromagnetic force to create torque and rotation in a coil of wire that interacts with a magnetic field.
- Transformers are machines that transfer electrical energy from one circuit to another without changing the frequency. They use the principle of mutual induction to induce voltage and current in a secondary coil of wire that is linked to a primary coil of wire by a magnetic core.
- Electrical machines can be further classified based on the type of current they use: direct current (DC) or alternating current (AC).
- DC machines are machines that operate with a constant polarity of voltage and current. They have commutators and brushes to switch the direction of current in the coil of wire as it rotates in the magnetic field. DC machines can be either shunt, series or compound wound depending on the connection of the field winding and the armature winding.
- AC machines are machines that operate with a sinusoidal or alternating polarity of voltage and current. They have slip rings and brushes to transfer the current from the stationary part to the rotating part of the machine. AC machines can be either synchronous or asynchronous depending on the speed of the rotor relative to the stator. Synchronous machines have a constant speed that is equal to the frequency of the supply voltage. Asynchronous machines have a variable speed that is lower than the frequency of the supply voltage. Asynchronous machines are also called induction machines because they induce current in the rotor by the rotating magnetic field of the stator.



### DC Machines

- A DC machine is an electromechanical device that is used to convert electrical energy into mechanical energy or vice versa.
- The working principle of a DC machine is based on an effect when a current carrying conductor is placed in a magnetic field, and then the magnetic force generates a torque that rotates the DC machine.
- The construction of a DC machine consists of the following main parts :
  - Yoke: It is the outer frame of the machine that supports and protects the other parts. It is usually made of cast iron or steel.
  - Poles and pole shoes: They are the projections on the inner side of the yoke that carry the field windings. The pole shoes are used to spread the flux uniformly over the armature.
  - Field windings: They are the coils of wire wound on the poles that produce the magnetic field when energized by a DC source.
  - Armature: It is the rotating part of the machine that carries the armature windings. It is usually made of laminated iron core with slots on its surface.
  - Armature windings: They are the coils of wire wound in the slots of the armature that carry the current induced by the magnetic field or the current supplied to the motor.
  - Commutator: It is a cylindrical structure made of copper segments insulated from each other and attached to the armature. It acts as a mechanical rectifier that converts the alternating voltage induced in the armature into direct voltage or vice versa.
  - Brushes: They are the sliding contacts that connect the commutator to the external circuit. They are usually made of carbon or graphite.
- The types of DC machines are classified based on the connection of the field windings to the armature windings:
  - Separately excited DC machine: The field windings are energized by a separate DC source independent of the armature.
  - Shunt-wound DC machine: The field windings are connected in parallel with the armature windings and share the same DC source.
  - Series-wound DC machine: The field windings are connected in series with the armature windings and carry the same current as the armature.
  - Compound-wound DC machine: The field windings are a combination of shunt and series windings. There are two types of compound-wound DC machines: cumulative compound and differential compound.
- The applications of DC machines are based on their characteristics and performance :
  - DC generators are used to supply DC power to various devices and systems, such as batteries, electroplating, welding, lighting, traction, etc.
  - DC motors are used to convert DC power into mechanical power for various purposes, such as fans, pumps, cranes, elevators, electric vehicles, etc.



### Principle and Construction of Electrical Machines

- Electrical machines are devices that convert mechanical energy to electrical energy and vice versa.
- The principle of operation of electrical machines is based on the interaction of magnetic fields and electric currents.
- The main types of electrical machines are DC machines, AC machines, and special purpose machines.
- DC machines are those that operate on direct current (DC) and have a commutator to change the direction of current in the armature coils .
- AC machines are those that operate on alternating current (AC) and have no commutator. They are further classified into synchronous machines and induction machines.
- Special purpose machines are those that are designed for specific applications or functions, such as stepper motors, servo motors, brushless DC motors, etc.

#### Construction of DC Machines

- The main parts of a DC machine are yoke, poles, field coils, armature, commutator, and brushes .
- Yoke is the outer frame of the machine that supports and protects the other parts. It is usually made of cast iron or steel .
- Poles are the projections on the inner side of the yoke that carry the field coils. They are usually made of laminated steel to reduce eddy current losses .
- Field coils are the windings that produce the magnetic field when current flows through them. They are connected in series or parallel to the DC supply .
- Armature is the rotating part of the machine that carries the armature coils. It is usually made of laminated steel to reduce eddy current losses and has slots on its surface to accommodate the coils .
- Armature coils are the windings that generate the output voltage or torque when they cut the magnetic flux. They are connected in series to form a closed loop and are connected to the commutator segments .
- Commutator is a cylindrical structure that consists of insulated copper segments. It is mounted on the armature shaft and rotates with it. It acts as a mechanical rectifier that reverses the direction of current in the armature coils every half rotation .
- Brushes are the stationary contacts that press against the commutator segments and transfer the current to or from the external circuit. They are usually made of carbon or graphite .

#### Working of DC Machines

- The working of a DC machine is based on the principle of electromagnetic induction, which states that when a conductor moves in a magnetic field, an emf is induced in it.
- In a DC generator, the armature coils are driven by a prime mover, such as a turbine or an engine, and rotate in the magnetic field produced by the field coils. As the coils cut the flux, an emf is induced in them, which is collected by the commutator and brushes and delivered to the external load.
- In a DC motor, the armature coils are connected to a DC supply through the commutator and brushes, and current flows through them. As the current-carrying coils interact with the magnetic field, a torque is produced on them, which makes them rotate. The rotation of the armature is transferred to the load through a shaft.



### Types of Electrical Machines

Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. They can be broadly classified into two types: static and dynamic.

- Static electrical machines are stationary devices that do not have any moving parts. They transfer electrical energy from one circuit to another without changing its frequency. The most common example of a static electrical machine is a transformer, which can step up or step down the voltage and current of an alternating current (AC) source. Transformers are used for power transmission, distribution, and conversion applications.   

- Dynamic electrical machines are rotating devices that have a rotor and a stator. They can either generate electrical energy from mechanical energy or use electrical energy to produce mechanical energy. The most common examples of dynamic electrical machines are generators and motors. Generators convert mechanical energy into electrical energy by inducing an electromotive force (EMF) in the coils of the stator. Motors convert electrical energy into mechanical energy by creating a torque on the rotor.   

Dynamic electrical machines can be further classified into different types based on the nature of the current, the magnetic field, and the commutation. Some of the main types are:

- DC machines: These are machines that use direct current (DC) as the input or output. They have a commutator and brushes that switch the direction of the current in the rotor coils. They can be further divided into permanent magnet DC machines, which have permanent magnets in the rotor, and wound DC machines, which have electromagnets in the rotor. DC machines are used for applications that require variable speed and torque control, such as electric vehicles, cranes, and elevators.   

- Synchronous machines: These are machines that use alternating current (AC) as the input or output. They have a constant speed and frequency that is synchronized with the supply. They can be further divided into salient pole machines, which have projecting poles on the rotor, and cylindrical rotor machines, which have a smooth rotor. Synchronous machines are used for applications that require high power and efficiency, such as power generation, power factor correction, and frequency conversion.  

- Induction machines: These are machines that use alternating current (AC) as the input or output. They have a variable speed and frequency that depends on the load. They do not have any commutator or brushes, but rely on the induction of an EMF in the rotor by the stator. They can be further divided into squirrel cage machines, which have a simple and rugged rotor, and wound rotor machines, which have slip rings and external resistors. Induction machines are used for applications that require low cost and maintenance, such as fans, pumps, and compressors.  

- Brushless machines: These are machines that use alternating current (AC) as the input or output. They do not have any commutator or brushes, but use electronic devices to switch the current in the coils. They can be further divided into permanent magnet synchronous machines, which have permanent magnets in the rotor, and reluctance machines, which have variable reluctance in the rotor. Brushless machines are used for applications that require high speed and reliability, such as aerospace, robotics, and medical equipment.



### EMF equation of generator and torque equation of motor

- A generator is a device that converts mechanical energy into electrical energy by inducing a voltage in a coil that rotates in a magnetic field.
- A motor is a device that converts electrical energy into mechanical energy by applying a torque to a coil that rotates in a magnetic field.
- The EMF equation of a generator relates the generated voltage (Eg) to the number of turns (N), the magnetic flux (Φ), the speed of rotation (Z), the number of poles (P), and the number of parallel paths (A) in the coil. The equation is:

  Eg = ΦZN / 60A

- The EMF equation of a motor relates the back EMF (Eb) to the same parameters as the generator. The back EMF is the voltage that opposes the applied voltage and reduces the current in the coil. The equation is:

  Eb = ΦZN / 60A

- The torque equation of a motor relates the torque (T) to the current (I), the magnetic flux (Φ), the number of turns (N), and the number of parallel paths (A) in the coil. The equation is:

  T = IΦN / A

- The torque equation of a generator is the same as the motor, except that the current is the output current of the generator, not the input current of the motor.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on the applications of DC motors:

### Applications of DC motors

- DC motors are electric motors that are powered by direct current (DC), such as from a battery or DC power supply.
- DC motors can be classified into four main types based on their connection and commutation: permanent magnet, series, shunt, and compound.
- Each type of DC motor has different features and applications, as summarized below:

| Type | Features | Applications |
| --- | --- | --- |
| Permanent magnet | - Has a permanent magnet to create a field flux.<br>- Does not have a field winding or commutator.<br>- Has a simple and compact design.<br>- Has a high efficiency and low noise.<br>- Has a constant speed and torque. | - Computer equipment, such as CPU cooling fans and drive motors for HDDs and CD-ROM drives.<br>- Audio and video equipment, such as audio CD, DVD, and Blu-ray players.<br>- Home appliances, such as electric toothbrushes and hair dryers.<br>- Automobiles, such as fuel pumps and power steering motors.<br>- Industrial machinery and medical equipment, such as servo motors in robots and fan motors in respirators . |
| Series | - Has a field winding connected in series with the armature winding.<br>- Has a commutator and brushes.<br>- Has a high starting torque and low starting current.<br>- Has a variable speed and torque depending on the load.<br>- Has a poor speed regulation and efficiency. | - Traction systems, such as trains and electric vehicles  .<br>- Cranes and hoists, such as lifting and lowering loads  .<br>- Air compressors and vacuum cleaners, such as creating suction and pressure  .<br>- Sewing machines and drills, such as varying the speed and power  . |
| Shunt | - Has a field winding connected in parallel with the armature winding.<br>- Has a commutator and brushes.<br>- Has a low starting torque and high starting current.<br>- Has a constant speed and torque regardless of the load.<br>- Has a good speed regulation and efficiency. | - Lathes and milling machines, such as cutting and shaping materials .<br>- Fans and blowers, such as circulating air and cooling systems .<br>- Centrifugal pumps and conveyors, such as moving fluids and materials .<br>- Printing presses and textile machines, such as producing and processing fabrics . |
| Compound | - Has a combination of series and shunt field windings.<br>- Has a commutator and brushes.<br>- Has a moderate starting torque and current.<br>- Has a variable speed and torque depending on the load and the type of connection.<br>- Has a better speed regulation and efficiency than series motors. | - Elevators and escalators, such as moving people and goods vertically .<br>- Electric locomotives and trolleys, such as transporting passengers and cargo .<br>- Presses and shears, such as cutting and bending metals .<br>- Generators and dynamos, such as converting mechanical energy into electrical energy . |

- Simple numerical problems on the applications of DC motors can be solved by using the following formulas:

- For permanent magnet motors, the torque (T) is proportional to the current (I) and the flux (φ), and the speed (N) is proportional to the voltage (V) and inversely proportional



### Three Phase Induction Motor

- A three phase induction motor is a type of AC motor that uses three alternating currents (AC) to generate a rotating magnetic field   .
- The rotating magnetic field induces an electromotive force (EMF) in the stator, which causes the rotor to rotate and produce mechanical power  .
- The stator is the stationary part of the motor that consists of three sets of windings that are connected to the three phase supply .
- The rotor is the rotating part of the motor that can be either a squirrel-cage type or a slip-ring type .
- The squirrel-cage rotor is made of copper or aluminum bars that are short-circuited by end rings at both ends .
- The slip-ring rotor is made of wound coils that are connected to external resistors or rheostats through slip rings and brushes .
- The speed of the rotor depends on the frequency of the supply voltage, the number of poles in the stator, and the slip .
- The slip is the difference between the synchronous speed and the actual speed of the rotor, expressed as a percentage of the synchronous speed .
- The three phase induction motor has many advantages, such as simple construction, high efficiency, low cost, easy maintenance, and self-starting capability  .
- The three phase induction motor has many applications, such as pumps, fans, compressors, conveyors, elevators, cranes, and electric vehicles  .



### Principle & Construction for the notes of the Unit 4 - Electrical machines in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

- Electrical machines are devices that convert mechanical energy to electrical energy and vice versa.
- The principle of operation of electrical machines is based on the interaction of magnetic fields and electric currents.
- The basic elements of an electrical machine are:
  - A magnetic field, which can be produced by permanent magnets or electromagnets.
  - A conductor, which can be a wire or a coil, that carries an electric current.
  - A force or torque, which is generated by the interaction of the magnetic field and the electric current.
- There are two main types of electrical machines: generators and motors.
  - Generators convert mechanical energy to electrical energy by inducing an electric current in the conductor when it moves in the magnetic field.
  - Motors convert electrical energy to mechanical energy by applying a force or torque on the conductor when an electric current flows through it in the magnetic field.
- The construction of electrical machines depends on the type, size, and application of the machine.
  - The common components of electrical machines are:
    - Yoke, which is the outer frame that supports and protects the machine.
    - Poles, which are the parts that produce the magnetic field. They can be fixed or rotating, depending on the type of machine.
    - Coils, which are the windings of conductors that carry the electric current. They can be field coils or armature coils, depending on their function.
    - Commutator, which is a device that reverses the direction of the current in the armature coils of a DC machine.
    - Brushes, which are the contacts that connect the external circuit to the commutator or the slip rings of the machine.
    - Bearings, which are the parts that support and reduce the friction of the rotating shaft of the machine.
- The construction of DC machines and AC machines differs in some aspects, such as the type of magnetic field, the type of current, and the type of commutation.
  - DC machines have a constant or a variable DC magnetic field, a DC current, and a mechanical commutation using a commutator and brushes.
  - AC machines have an alternating or a rotating AC magnetic field, an AC current, and an electrical commutation using slip rings or electronic devices.



### Types of Electrical Machines

Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. They can be classified into two main categories: static and rotating machines  .

- Static machines are machines that do not have any moving parts. They are used to transfer electrical energy from one circuit to another without changing its frequency. The most common example of a static machine is a transformer  .
- Rotating machines are machines that have a rotating part called a rotor. They are used to convert mechanical energy into electrical energy or electrical energy into mechanical energy. The most common examples of rotating machines are generators and motors   .

Rotating machines can be further classified into different types based on the type of current they use, the type of magnetic field they produce, and the type of rotor they have  .

- DC machines are machines that use direct current (DC) as the input or output. They have a commutator and brushes to switch the direction of the current in the rotor coil. They can be divided into permanent magnet DC machines, which have permanent magnets in the rotor, and wound DC machines, which have electromagnets in the rotor  .
- AC machines are machines that use alternating current (AC) as the input or output. They do not have a commutator or brushes, but rely on the changing magnetic field of the stator to induce a current in the rotor. They can be divided into synchronous machines, which have a constant speed and a fixed magnetic field in the rotor, and induction machines, which have a variable speed and an induced magnetic field in the rotor  .

Some of the main characteristics and applications of different types of electrical machines are summarized in the table below.

| Type of machine | Current | Magnetic field | Rotor | Characteristics | Applications |
| --- | --- | --- | --- | --- | --- |
| Transformer | AC | AC | None | Can step up or step down voltage and current | Power transmission and distribution, isolation, impedance matching |
| Permanent magnet DC machine | DC | DC | Permanent magnet | High efficiency, low maintenance, simple control | Toys, fans, pumps, electric vehicles |
| Wound DC machine | DC | DC | Electromagnet | High torque, variable speed, easy reversal | Cranes, elevators, traction, electric vehicles |
| Synchronous machine | AC | AC | Electromagnet or permanent magnet | Constant speed, power factor control, high efficiency | Generators, motors, power factor correction |
| Induction machine | AC | AC | Short-circuited coil or squirrel cage | Simple, rugged, low cost, self-starting | Fans, pumps, compressors, mixers, conveyors |



### Slip-torque characteristics of induction motor

- The slip-torque characteristic of an induction motor is the relationship between the torque produced by the motor and the slip of the rotor relative to the synchronous speed.
- The slip of the rotor is defined as the difference between the synchronous speed and the actual speed of the rotor, expressed as a fraction of the synchronous speed.
- The slip-torque characteristic can be derived from the equivalent circuit of the induction motor, where the torque is proportional to the power transferred from the stator to the rotor, and the slip is related to the rotor resistance and reactance.
- The slip-torque characteristic can be divided into three regions, as shown in the figure below:

Slip-torque characteristic

- Low slip region: In this region, the slip is very small and the rotor speed is near the synchronous speed. The torque is proportional to the slip and increases linearly with the slip. The rotor resistance is much larger than the slip times the rotor reactance, so the power factor of the rotor is high and the rotor current is low. This region corresponds to the normal operating range of the motor under light load conditions.
- Medium slip region: In this region, the slip is moderate and the rotor speed is lower than the synchronous speed. The torque increases nonlinearly with the slip and reaches a maximum value at a certain slip, called the pull-out slip or the critical slip. The rotor resistance is comparable to the slip times the rotor reactance, so the power factor of the rotor is lower and the rotor current is higher. This region corresponds to the normal operating range of the motor under heavy load conditions.
- High slip region: In this region, the slip is large and the rotor speed is much lower than the synchronous speed. The torque decreases with the slip and becomes zero at the maximum slip, called the breakdown slip or the stalling slip. The rotor resistance is much smaller than the slip times the rotor reactance, so the power factor of the rotor is very low and the rotor current is very high. This region corresponds to the abnormal operating range of the motor under excessive load conditions or starting conditions.

- The shape of the slip-torque characteristic depends on the design parameters of the motor, such as the number of poles, the stator and rotor resistances and reactances, and the mutual inductance between the stator and the rotor. The slip-torque characteristic can be modified by changing the rotor resistance, either by inserting external resistors in the rotor circuit or by using a wound rotor with slip rings and brushes. By increasing the rotor resistance, the maximum torque can be increased and the pull-out slip can be shifted to a higher value, which can improve the starting performance and the speed control of the motor. However, increasing the rotor resistance also increases the rotor losses and reduces the efficiency of the motor.



Hello, I am Sydney, your AI assistant. I can help you with your topic of applications of slip in electrical machines. Here are some notes and examples for you.

### Applications (Numerical problems related to slip only)

- Slip is the difference between the synchronous speed and the actual speed of an induction motor, expressed as a fraction or percentage of the synchronous speed.
- Slip can be calculated by the formula: `s = (Ns - N)/Ns`, where `s` is the slip, `Ns` is the synchronous speed, and `N` is the actual speed of the motor.
- Slip is an important parameter that affects the performance and efficiency of an induction motor. It determines the torque, power, current, and power factor of the motor.
- Some numerical problems related to slip are:

  - Example 1: A three-phase induction motor has a synchronous speed of 1200 rpm and runs at 1140 rpm. Find the slip of the motor.
    - Solution: Using the formula, `s = (Ns - N)/Ns`, we get `s = (1200 - 1140)/1200 = 0.05`. Therefore, the slip of the motor is 0.05 or 5%.
  - Example 2: A four-pole, 50 Hz induction motor has a full-load slip of 4%. Find the full-load speed of the motor.
    - Solution: The synchronous speed of the motor is given by `Ns = 120f/p`, where `f` is the frequency and `p` is the number of poles. Substituting the values, we get `Ns = 120*50/4 = 1500 rpm`. The full-load speed of the motor is given by `N = Ns(1 - s)`, where `s` is the slip. Substituting the values, we get `N = 1500(1 - 0.04) = 1440 rpm`. Therefore, the full-load speed of the motor is 1440 rpm.
  - Example 3: A six-pole, 60 Hz induction motor has a no-load speed of 1170 rpm and a full-load speed of 1125 rpm. Find the no-load and full-load slip of the motor.
    - Solution: The synchronous speed of the motor is given by `Ns = 120f/p`, where `f` is the frequency and `p` is the number of poles. Substituting the values, we get `Ns = 120*60/6 = 1200 rpm`. The no-load slip of the motor is given by `s = (Ns - N)/Ns`, where `N` is the no-load speed. Substituting the values, we get `s = (1200 - 1170)/1200 = 0.025`. Therefore, the no-load slip of the motor is 0.025 or 2.5%. The full-load slip of the motor is given by `s = (Ns - N)/Ns`, where `N` is the full-load speed. Substituting the values, we get `s = (1200 - 1125)/1200 = 0.0625`. Therefore, the full-load slip of the motor is 0.0625 or 6.25%.



### Single Phase Induction Motor

- A single phase induction motor is a type of AC motor that operates on single phase power supply .
- It has a stator with distributed single phase winding and a rotor with a cage winding .
- The stator produces a pulsating magnetic field that does not rotate, and the rotor is not electrically connected to the stator .
- The single phase induction motor has no starting torque, as there is no net torque acting on the rotor when it is stationary .
- To make the single phase induction motor self-starting, various methods are used to create a rotating magnetic field at least at starting, such as:
  - Split-phase method: The stator has two windings, a main winding and an auxiliary winding, with different resistances and inductances. The auxiliary winding is connected in series with a capacitor and a switch. The capacitor creates a phase difference between the currents in the two windings, resulting in a rotating magnetic field. The switch disconnects the auxiliary winding after the motor reaches a certain speed.
  - Permanent-split capacitor method: The stator has two windings, a main winding and an auxiliary winding, with different resistances and inductances. The auxiliary winding is permanently connected in series with a capacitor. The capacitor creates a phase difference between the currents in the two windings, resulting in a rotating magnetic field. This method eliminates the need for a switch, but has lower starting torque than the split-phase method.
  - Capacitor-start capacitor-run method: The stator has two windings, a main winding and an auxiliary winding, with different resistances and inductances. The auxiliary winding is connected in series with two capacitors, one for starting and one for running. The starting capacitor creates a large phase difference between the currents in the two windings, resulting in a high starting torque. The running capacitor creates a smaller phase difference, resulting in a higher efficiency and power factor. The starting capacitor is disconnected by a switch after the motor reaches a certain speed.
  - Shaded-pole method: The stator has a single winding with salient poles. Each pole has a copper ring or band around a part of it, called the shaded pole. The shaded pole creates a phase difference between the fluxes in the shaded and unshaded parts of the pole, resulting in a rotating magnetic field. This method has low starting torque and efficiency, but is simple and cheap.
- The single phase induction motor has the following advantages and disadvantages:
  - Advantages:
    - Simple and cheap construction
    - Easy to maintain and repair
    - High reliability and durability
    - Suitable for low power and variable load applications
  - Disadvantages:
    - Low starting torque and power factor
    - Low efficiency and speed regulation
    - Requires additional devices for starting
    - Generates more noise and vibration



### Principle of operation and introduction to methods of starting for the notes of the Unit 4 - Electrical machines in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

- Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. They can be classified into two main categories: direct current (DC) machines and alternating current (AC) machines.
- DC machines operate on the principle of Lorentz force, which states that a current carrying conductor placed in a magnetic field experiences a force that is perpendicular to both the current and the field. The direction of the force can be determined by Fleming's left hand rule. The magnitude of the force is given by F = BIL, where B is the magnetic flux density, I is the current and L is the length of the conductor.
- DC machines can be further divided into DC generators and DC motors. DC generators convert mechanical energy into electrical energy by rotating a coil of conductors in a magnetic field. The induced voltage in the coil is given by Faraday's law of electromagnetic induction, which states that the rate of change of magnetic flux linkage through a coil is equal to the induced electromotive force (emf) in the coil. The direction of the induced emf can be determined by Fleming's right hand rule. The output voltage of a DC generator can be controlled by varying the field current or the speed of rotation.
- DC motors convert electrical energy into mechanical energy by applying a voltage to a coil of conductors placed in a magnetic field. The coil experiences a torque that causes it to rotate. The direction of the torque can be determined by Fleming's left hand rule. The magnitude of the torque is given by T = BIL sin θ, where θ is the angle between the coil and the field. The speed of rotation of a DC motor can be controlled by varying the armature voltage or the field current.
- DC machines can be classified into four types based on the connection of the field winding: DC shunt machines, DC series machines, DC compound machines and DC permanent magnet machines. DC shunt machines have the field winding connected in parallel with the armature winding. DC series machines have the field winding connected in series with the armature winding. DC compound machines have both shunt and series field windings. DC permanent magnet machines have permanent magnets instead of field windings.
- The methods of starting a DC motor depend on the type of the motor. For DC shunt and compound motors, the most common method is to use a three-point starter, which consists of a variable resistance, a no-volt coil and an overload coil. The variable resistance limits the initial armature current and reduces the starting torque. The no-volt coil prevents the motor from running away if the supply voltage is interrupted. The overload coil protects the motor from excessive current due to overload or short circuit. For DC series motors, the most common method is to use a four-point starter, which has an additional holding coil that bypasses the no-volt coil and maintains the contact even if the supply voltage is interrupted. For DC permanent magnet motors, the most common method is to use a rheostat or a chopper circuit to vary the armature voltage and control the speed.
- AC machines operate on the principle of rotating magnetic field, which states that a set of stationary coils carrying alternating currents can produce a magnetic field that rotates at a constant speed. The speed of rotation of the magnetic field is given by N = 120f/P, where f is the frequency of the currents and P is the number of poles. The direction of rotation of the magnetic field can be determined by Lenz's law, which states that the induced current in a coil opposes the change in magnetic flux that causes it.
- AC machines can be further divided into AC generators and AC motors. AC generators convert mechanical energy into electrical energy by rotating a set of coils in a magnetic field. The induced voltage in the coils is given by Faraday's law of electromagnetic induction. The output voltage of an AC generator can be controlled by varying the field current or the speed of rotation. AC generators can be classified into two types based on the type of the magnetic field: synchronous generators and induction generators. Synchronous generators have a constant speed of rotation that is equal to the speed of the magnetic field. Induction generators have a variable speed of rotation that is slightly higher than the speed of the magnetic field.
- AC motors convert electrical energy into mechanical energy by applying a voltage to a set of coils placed in a magnetic field. The coils experience a torque that causes them to rotate. The direction of the torque can be determined by Lenz's law. The



### Applications of Electrical Machines

Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. They are widely used in various fields of engineering, industry, and everyday life. Some of the common applications of electrical machines are:

- **Electric motors**: Electric motors are used to drive various machines and devices that require mechanical power, such as fans, pumps, compressors, conveyors, elevators, cranes, robots, electric vehicles, etc. Electric motors can be classified into two main types: AC motors and DC motors. AC motors operate on alternating current and can be further divided into synchronous motors and induction motors. DC motors operate on direct current and can be further divided into brushed motors and brushless motors. Electric motors can also be classified based on their speed, torque, power, efficiency, and control methods .
- **Electric generators**: Electric generators are used to produce electrical energy from mechanical energy, such as from wind turbines, hydro turbines, steam turbines, gas turbines, etc. Electric generators can also be classified into two main types: AC generators and DC generators. AC generators produce alternating current and can be further divided into synchronous generators and induction generators. DC generators produce direct current and can be further divided into separately excited generators and self-excited generators. Electric generators can also be classified based on their voltage, frequency, power, efficiency, and regulation methods .
- **Electric transformers**: Electric transformers are used to change the voltage and current levels of an alternating current without changing its frequency or power. They are used for various purposes, such as transmission, distribution, isolation, impedance matching, voltage regulation, etc. Electric transformers can be classified into two main types: power transformers and instrument transformers. Power transformers are used to transfer large amounts of power between different voltage levels. Instrument transformers are used to measure or protect the electrical circuits. Electric transformers can also be classified based on their construction, winding arrangement, cooling method, and insulation type.
- **Electric actuators**: Electric actuators are used to convert electrical energy into linear or rotary motion for various applications, such as valves, switches, relays, solenoids, etc. Electric actuators can be classified into two main types: electromagnetic actuators and electrostatic actuators. Electromagnetic actuators use magnetic fields to generate force and motion, such as linear motors, stepper motors, servo motors, etc. Electrostatic actuators use electric fields to generate force and motion, such as piezoelectric actuators, electrostatic motors, etc. Electric actuators can also be classified based on their speed, force, displacement, accuracy, and control methods.



### Three Phase Synchronous Machines

- A three phase synchronous machine is a type of electric machine that can operate as either a generator or a motor, depending on the direction of power flow.
- A three phase synchronous machine consists of two main parts: a stator and a rotor.
- The stator is the stationary part of the machine that contains a three phase winding, which is connected to the AC supply or the load. The stator winding produces a rotating magnetic field when energized by AC current.
- The rotor is the rotating part of the machine that contains a DC field winding, which is excited by a DC source or an exciter. The rotor field interacts with the stator field to produce torque and power.
- The rotor can be either cylindrical (round rotor) or salient pole (projected pole), depending on the shape and distribution of the field poles. Round rotor machines are used for high speed and high power applications, such as steam turbines and gas turbines. Salient pole machines are used for low speed and low power applications, such as hydro generators and single phase motors.
- The speed of the rotor is equal to the speed of the stator field, which is determined by the frequency of the AC supply and the number of poles of the machine. This speed is called the synchronous speed, and it is given by the formula:

  $$n_s = \frac{120f}{p}$$

  where $n_s$ is the synchronous speed in revolutions per minute (rpm), $f$ is the frequency of the AC supply in hertz (Hz), and $p$ is the number of poles of the machine.
- A three phase synchronous machine can operate in two modes: synchronous mode and asynchronous mode. In synchronous mode, the rotor speed is equal to the synchronous speed, and the machine is said to be in synchronism. In asynchronous mode, the rotor speed is different from the synchronous speed, and the machine is said to be out of synchronism.
- A three phase synchronous generator converts mechanical energy into electrical energy by rotating the rotor in the same direction as the stator field. The output voltage and frequency of the generator depend on the speed and excitation of the rotor. The generator can supply power to a balanced or an unbalanced load, depending on the connection of the stator winding (star or delta).
- A three phase synchronous motor converts electrical energy into mechanical energy by rotating the rotor in the opposite direction of the stator field. The input voltage and frequency of the motor determine the synchronous speed of the stator field. The motor can be started by various methods, such as damper winding, induction motor, or external prime mover. The motor can operate at constant speed or variable speed, depending on the control of the rotor excitation. The motor can also operate at leading or lagging power factor, depending on the load torque and the rotor excitation.



### Principle of operation of alternator and synchronous motor

- An **alternator** or **synchronous generator** is a device that converts mechanical energy into electrical energy by producing alternating current (AC).
- A **synchronous motor** is a device that converts electrical energy into mechanical energy by rotating at a constant speed that is synchronized with the frequency of the AC supply.
- Both devices work on the **principle of electromagnetic induction**, i.e., when the flux linking a conductor changes, an EMF is induced in the conductor.
- In an alternator, the armature winding is fixed on the stator and the field winding is rotated by a prime mover (such as a turbine or an engine). The rotating field winding creates a rotating magnetic field that induces an AC voltage in the armature winding.
- In a synchronous motor, the field winding is fixed on the rotor and the armature winding is connected to a three-phase AC supply. The AC supply creates a rotating magnetic field that interacts with the field winding and causes the rotor to rotate at the same speed as the magnetic field.
- The speed of rotation of both devices depends on the number of poles (p) and the frequency of the AC supply (f). The speed (N) is given by the formula: N = 120f/p revolutions per minute (rpm).
- The advantages of alternators are that they can produce high voltages and currents, they can be easily paralleled, and they have good voltage regulation. The disadvantages are that they require a separate DC source for excitation, they have high initial cost and maintenance, and they have low efficiency at low loads.
- The advantages of synchronous motors are that they have high efficiency, power factor, and torque, they can operate at constant speed and can be used for power factor correction. The disadvantages are that they require a separate DC source for excitation, they have high initial cost and maintenance, and they have difficulty in starting and synchronizing.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 4 - Electrical machines in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING. Here are some notes on the topic of their applications:

### Their applications

- Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. They are widely used in various sectors such as industry, transportation, power generation, and domestic appliances.
- Some of the common applications of electrical machines are:

  - **DC motors**: These are used for variable speed control, such as in electric vehicles, cranes, elevators, robots, and industrial drives. They can also be used as generators, such as in wind turbines, hydroelectric plants, and diesel generators.
  - **AC motors**: These are used for constant speed applications, such as in fans, pumps, compressors, conveyors, and air conditioners. They can also be used as generators, such as in synchronous generators for power grids, induction generators for wind farms, and alternators for automobiles.
  - **Transformers**: These are used for changing the voltage level of alternating current, such as in power transmission, distribution, and conversion. They can also be used for isolation, impedance matching, and signal processing, such as in audio amplifiers, radio receivers, and medical equipment.
  - **DC generators**: These are used for producing direct current, such as in batteries, solar panels, and thermoelectric devices. They can also be used for charging, welding, and electroplating, such as in battery chargers, arc welders, and electroplating machines.
  - **AC generators**: These are used for producing alternating current, such as in power plants, aircraft, and ships. They can also be used for frequency conversion, such as in frequency changers, inverters, and cycloconverters.



## Unit 5 - Electrical Installations

- Electrical installations are the construction or installation of electrical wiring and the permanent attachment or installation of electrical products in or on any structure that is not itself an electrical product.
- Electrical installations can be done by professional independent installers who are licensed, insured and background checked, such as those offered by Lowe's installation service.
- Electrical installations must comply with the International Electrotechnical Commission (IEC) standards, which provide guidelines for the design, installation, inspection and maintenance of low to medium-voltage electrical installations.
- Electrical installations involve the following steps:
  - Planning the layout and design of the electrical system, including the location of outlets, switches, lighting fixtures, appliances, circuit breakers, etc.
  - Obtaining the necessary permits and approvals from the local authorities and utility companies.
  - Installing the electrical wiring and conduits, following the color codes and wiring diagrams.
  - Connecting the electrical products and devices, such as sockets, lamps, fans, heaters, etc.
  - Testing the electrical system for safety and functionality, using tools such as multimeters, voltage testers, etc.
  - Troubleshooting and repairing any faults or defects in the electrical system, such as loose connections, short circuits, overloads, etc.



### Introduction of Switch Fuse Unit (SFU)

- A switch fuse unit (SFU) is a device that combines the functions of a switch and a fuse in one unit.
- A switch is used to manually open or close an electrical circuit, while a fuse is used to protect the circuit from overcurrent or short circuit by melting and breaking the circuit when the current exceeds a certain value.
- A switch fuse unit is typically used to isolate and protect a sub-circuit or a branch circuit from the main circuit.
- A switch fuse unit consists of three main components: a switch, a fuse carrier, and a fuse link.
- The switch is a mechanical device that can be operated by a handle or a lever. It has two positions: ON and OFF. When the switch is ON, the circuit is closed and the current can flow. When the switch is OFF, the circuit is open and the current is interrupted.
- The fuse carrier is a metal or plastic enclosure that holds the fuse link. It is attached to the switch and can be removed or inserted into the switch. The fuse carrier has terminals that connect to the circuit wires.
- The fuse link is a metal strip or wire that has a low melting point. It is inserted into the fuse carrier and forms part of the circuit. The fuse link has a rated current value that indicates the maximum current that it can carry without melting. If the current in the circuit exceeds the rated current of the fuse link, the fuse link will melt and break the circuit, thus protecting the circuit from damage.
- A switch fuse unit can be classified into two types: open type and enclosed type.
- An open type switch fuse unit is one that is not enclosed in a metal or plastic box. It is usually mounted on a wooden or metal board and exposed to the environment. It is suitable for indoor use where there is no risk of moisture, dust, or corrosion.
- An enclosed type switch fuse unit is one that is enclosed in a metal or plastic box. It is usually mounted on a wall or a pole and protected from the environment. It is suitable for outdoor use where there is a risk of moisture, dust, or corrosion.



### MCB for the notes of the Unit 5 - Electrical Installations in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

- MCB stands for **Miniature Circuit Breaker**, which is an automatically operated electrical switch that protects an electrical circuit from damage caused by excess current from an overload or short circuit.
- MCBs are designed to trip and interrupt the current flow in case of a fault condition, and can be reset manually or automatically to resume normal operation.
- MCBs are commonly used in low-voltage electrical networks, such as residential, commercial and industrial applications, where they provide reliable and safe protection for electrical equipment and wiring.
- MCBs have several advantages over fuses, such as faster response, higher breaking capacity, easier identification of faulty circuits, and reusability.
- MCBs are classified into different types based on their tripping characteristics, such as Type B, Type C, and Type D, which indicate the amount of current that will cause the MCB to trip.
- MCBs are also rated by their current carrying capacity, voltage rating, and breaking capacity, which indicate the maximum current, voltage, and fault current that the MCB can safely handle.
- MCBs are installed in electrical panels or distribution boards, where they are arranged in rows and columns, and connected to the incoming and outgoing wires of the circuits they protect.
- To install an MCB, the following steps are required :
  - Step 1: Identify the spot to install the MCB. Turn off the power supply to the electric panel and remove the cover over it. Use a test light or meter to verify that the power is off. Look for an unused location to accommodate the MCB. If the location has a knockout plate, remove it before the installation.
  - Step 2: Place the MCB in the panel. Select the correct MCB that is allowed to be installed in the panel. Place the new MCB next to an existing MCB. Align the clips on the back of the MCB with the slots on the panel. Push the MCB firmly into the panel until it snaps into place.
  - Step 3: Connect the wires to the MCB. Strip the insulation from the incoming and outgoing wires of the circuit. Connect the incoming wire to the terminal marked as "line" or "L" on the MCB. Connect the outgoing wire to the terminal marked as "load" or "N" on the MCB. Tighten the screws on the terminals to secure the wires.
  - Step 4: Test the MCB and restore the power. Turn on the MCB by flipping the switch to the "on" position. Replace the cover over the electric panel and turn on the power supply. Use a test light or meter to check that the MCB and the circuit are working properly. If the MCB trips, identify and fix the fault before resetting the MCB.



### ELCB

- ELCB stands for Earth Leakage Circuit Breaker   .
- It is a safety device used in electrical installations with high Earth impedance to prevent shock  .
- It detects small stray voltages on the metal enclosures of electrical equipment, and interrupts the circuit if a dangerous voltage is detected  .
- It is a specialised type of latching relay that has a building's incoming mains power connected through its switching contacts so that the ELCB disconnects the power when earth leakage is detected .
- It detects fault currents from live to the Earth (ground) wire within the installation it protects .

#### Advantages of ELCB

- It provides protection against electrical shock and fire hazards caused by earth leakage .
- It is sensitive to very low currents and can operate in milliseconds .
- It can be used to protect individual circuits or the whole installation .
- It can be reset manually or automatically after clearing the fault .

#### Disadvantages of ELCB

- It may not detect some types of earth faults, such as balanced faults or high-impedance faults .
- It may be affected by external factors, such as lightning, moisture, or noise .
- It may cause nuisance tripping due to transient voltages or capacitive leakage currents .
- It may not work properly if the earth wire is broken or disconnected .

#### Applications of ELCB

- ELCB is mainly used for protection against electrical shock in domestic, commercial, and industrial installations .
- ELCB is also used for protection of equipment and appliances from earth leakage currents .
- ELCB is suitable for use in circuits with high earth impedance, such as underground cables, metal pipes, or metal frames .
- ELCB is compatible with other types of circuit breakers, such as MCBs, MCCBs, or RCDs .



### MCCB

- MCCB stands for **Moulded Case Circuit Breaker** , which is a type of electrical protection device used to protect the electrical circuit from excessive current, which can cause overload, short circuit, instantaneous over current and earth fault   .
- MCCB is an advanced version of MCB (Miniature Circuit Breaker), as it can handle higher current ratings, up to 2500A  , and has adjustable trip settings  .
- MCCB consists of three main components: the **moulded case**, the **operating mechanism**, and the **trip unit**  .
  - The moulded case is made of insulating material, such as plastic or resin, and provides mechanical support and insulation for the internal parts  .
  - The operating mechanism is the part that opens and closes the contacts of the MCCB, either manually or automatically  .
  - The trip unit is the part that senses the current and triggers the opening of the contacts when a fault occurs  .
- MCCB can have different types of trip units, such as **thermal**, **magnetic**, **thermal-magnetic**, or **electronic**  .
  - Thermal trip units use a bimetallic strip that bends when heated by the current, and releases a latch that opens the contacts  . They provide overload protection, as they respond to the temperature rise caused by the current  .
  - Magnetic trip units use an electromagnet that attracts a plunger when the current exceeds a certain level, and pushes a lever that opens the contacts  . They provide short circuit protection, as they respond to the magnetic field generated by the current  .
  - Thermal-magnetic trip units combine both thermal and magnetic elements, and provide both overload and short circuit protection  .
  - Electronic trip units use a microprocessor that measures the current and compares it with the preset values, and sends a signal to the operating mechanism to open the contacts when a fault occurs  . They provide more accurate and adjustable protection, as they can be programmed for different current levels, time delays, and trip curves  .
- MCCB can have different ratings, such as **current rating**, **voltage rating**, **frequency rating**, **interrupting rating**, and **service conditions**   .
  - Current rating is the maximum current that the MCCB can carry continuously without tripping   . It is expressed in amperes (A) and depends on the size and type of the MCCB   .
  - Voltage rating is the maximum voltage that the MCCB can withstand without breaking down   . It is expressed in volts (V) and depends on the insulation and clearance of the MCCB   .
  - Frequency rating is the frequency of the alternating current (AC) that the MCCB can operate with   . It is expressed in hertz (Hz) and depends on the design and calibration of the MCCB   .
  - Interrupting rating is the maximum current that the MCCB can interrupt safely without causing damage to itself or the circuit   . It is expressed in kil



### ACB

- ACB stands for Air Circuit Breaker, which is an electrical device used to provide overcurrent and short-circuit protection for electric circuits over 800 Amps to 10kA   .
- ACB operates at atmospheric pressure in air, where air-blast as an arc quenching medium .
- ACB is used in the switching mechanism and protection of the electrical system, especially in low voltage applications below 450V .
- ACB has three main components: the contacts, the arc chute, and the operating mechanism .
- The contacts are the conductive parts that carry the current and make or break the circuit. They consist of a fixed contact and a moving contact .
- The arc chute is the device that extinguishes the arc when the contacts separate. It consists of a series of metal plates that create a low resistance path for the arc and split it into smaller arcs that are easier to quench .
- The operating mechanism is the device that controls the opening and closing of the contacts. It can be manual, spring, or magnetic .
- ACB can be classified into two types: plain air circuit breaker and air blast circuit breaker .
- Plain air circuit breaker uses the natural process of air to quench the arc. It has a simple construction and low maintenance cost, but it has a slow speed of operation and a large size .
- Air blast circuit breaker uses a high-pressure air blast to quench the arc. It has a high speed of operation and a small size, but it has a high maintenance cost and a high noise level .
- ACB has several advantages over other types of circuit breakers, such as oil circuit breaker and vacuum circuit breaker. Some of the advantages are  :
  - ACB does not require any insulating medium other than air, which is cheap and readily available.
  - ACB does not produce any harmful gases or fire hazards during operation, unlike oil circuit breaker.
  - ACB does not have any contact erosion or metal deposition problems, unlike vacuum circuit breaker.
  - ACB has a high breaking capacity and a long service life.
  - ACB can be easily integrated with other protection devices and control systems.
- ACB has some disadvantages as well, such as  :
  - ACB requires a large space for installation and a high voltage rating for the contacts.
  - ACB has a high initial cost and a high power consumption for the air compressor.
  - ACB has a high arc voltage and a high arc resistance, which may affect the current interruption and the voltage recovery.
  - ACB may cause electromagnetic interference and acoustic noise due to the air blast.
- ACB has various applications in the electrical industry, such as  :
  - ACB is used in distribution panels, switchboards, and substations for low voltage systems.
  - ACB is used in industrial plants, power stations, and transmission lines for medium voltage systems.
  - ACB is used in special applications, such as railways, ships, and aircrafts, where high speed and reliability are required.



### Types of Wires for the notes of the Unit 5 - Electrical Installations in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

- A wire is a single, flexible strand or rod of metal that can carry electric current when connected to a power source.
- Wires are used to connect electrical devices, such as switches, outlets, lights, appliances, and machines, to the electrical system of a building or a vehicle.
- Wires can be classified by their material, size, shape, insulation, and function.

#### Material
- The most common materials for wires are copper and aluminum, which have high electrical conductivity and low resistance.
- Copper wires are more ductile, have higher tensile strength, and can be soldered easily. They are also more expensive and heavier than aluminum wires.
- Aluminum wires are cheaper, lighter, and more resistant to corrosion than copper wires. They are also more prone to oxidation, expansion, and loosening of connections. They require special connectors and terminals to prevent overheating and fire hazards.

#### Size
- The size of a wire is measured by its cross-sectional area or diameter, which determines its current-carrying capacity and resistance.
- The unit of wire size is the American Wire Gauge (AWG), which ranges from 0000 (the largest) to 40 (the smallest).
- The larger the AWG number, the smaller the wire diameter, and the lower the current-carrying capacity and the higher the resistance.
- For example, a 14 AWG wire has a diameter of 1.63 mm and can carry up to 15 amps of current, while a 10 AWG wire has a diameter of 2.59 mm and can carry up to 30 amps of current.

#### Shape
- Wires can be either solid or stranded, depending on the number of strands or filaments that make up the wire.
- Solid wires are made of a single, solid metal rod. They are stiffer, stronger, and more durable than stranded wires. They are also more difficult to bend and route, and more susceptible to breakage and fatigue.
- Stranded wires are made of several thin metal strands twisted together. They are more flexible, pliable, and resistant to vibration and fatigue than solid wires. They are also more difficult to terminate and splice, and more prone to corrosion and oxidation.

#### Insulation
- Insulation is the material that covers the wire to protect it from physical damage, moisture, heat, and electric shock.
- Insulation can be made of various materials, such as rubber, plastic, PVC, Teflon, or fiberglass, depending on the voltage, temperature, and environment of the wire.
- Insulation can be either thermoplastic or thermoset, depending on the behavior of the material when heated.
- Thermoplastic insulation softens when heated and hardens when cooled. It is easier to manufacture and recycle, but less resistant to heat, chemicals, and abrasion than thermoset insulation.
- Thermoset insulation does not soften when heated, but cures and becomes rigid. It is more resistant to heat, chemicals, and abrasion, but more difficult to manufacture and recycle than thermoplastic insulation.

#### Function
- Wires can be classified by their function, such as hot, neutral, or ground wires, depending on the role they play in the electrical circuit.
- Hot wires are the wires that carry electric current from the power source to the load. They are usually black or red in color, and have a positive or alternating voltage.
- Neutral wires are the wires that complete the circuit by returning the electric current from the load to the power source. They are usually white or light gray in color, and have a zero or near-zero voltage.
- Ground wires are the wires that provide a path for excess or fault current to flow to the earth in case of a short circuit or a ground fault. They are usually bare copper or green insulated wires, and have a zero or near-zero voltage. They help reduce the risk of electric shock and fire.



### Cables and Bus-bars

- Cables and bus-bars are two methods of transporting electrical energy in distribution systems.
- Cables are insulated conductors that are usually made of copper or aluminum and can be run in trays or conduit. Cables can carry different voltages and currents depending on their size and insulation. Cables are flexible and can be routed around obstacles, but they also have some disadvantages, such as:
  - Cables have high resistance and voltage drop, which reduces the efficiency and power quality of the system.
  - Cables generate heat and electromagnetic fields, which can affect nearby equipment and personnel.
  - Cables are prone to damage and corrosion, which can cause short circuits and fire hazards.
  - Cables are difficult to change or modify once installed, which limits the flexibility and scalability of the system.
- Bus-bars are metal bars that are usually made of copper or aluminum and are enclosed in a metal casing. Bus-bars can carry large amounts of current and have low resistance and voltage drop. Bus-bars are rigid and can be mounted on walls or ceilings, but they also have some advantages, such as:
  - Bus-bars have high efficiency and power quality, which improves the performance and reliability of the system.
  - Bus-bars have low heat and electromagnetic fields, which reduces the interference and risk to nearby equipment and personnel.
  - Bus-bars are resistant to damage and corrosion, which increases the safety and durability of the system.
  - Bus-bars are easy to change or modify, which enhances the flexibility and scalability of the system.



### Fundamentals of earthing and lightning protection

- Earthing and lightning protection are important for everyone that uses electrical equipment and that includes the large majority of the world.
- Earthing is the process of connecting the metallic parts of an electrical system or appliance to the earth. It provides a low-resistance path for fault currents and protects the system and the users from electric shock.
- Lightning protection is the process of intercepting or diverting lightning and providing a certain path for conducting the surges safely to the ground by adequate down conductors to grounding electrodes. It helps prevent disastrous events like fires, injuries, and deaths.
- The basic principles of earthing and lightning protection are:
  - Providing an alternative path for the lightning current to flow to ground and ensure that:
    - Lightning current flowing in the lightning protection system (LPS) does not induce dangerous currents in any parallel metallic systems near the LPS, and
    - The potential difference between the LPS and the earth is kept to a minimum.
  - Providing a low-impedance connection between the LPS and the earth by using suitable earthing electrodes and conductors.
  - Providing adequate bonding between the LPS and other metallic systems to avoid potential differences and flashovers.
  - Providing surge protection devices (SPDs) to limit the overvoltages and protect the sensitive equipment from damage.
- The types and components of earthing and lightning protection systems are:
  - Earthing systems: They can be classified into three types based on the connection of the neutral point of the supply system to the earth. They are:
    - TN system: The neutral point is directly connected to the earth and the exposed conductive parts of the equipment are connected to the neutral point.
    - TT system: The neutral point is directly connected to the earth and the exposed conductive parts of the equipment are connected to a separate earthing electrode.
    - IT system: The neutral point is either isolated from the earth or connected through a high impedance and the exposed conductive parts of the equipment are connected to a separate earthing electrode.
  - Lightning protection systems: They can be classified into two types based on the method of interception of the lightning strike. They are:
    - Conventional system: It uses air terminals (rods or masts) to capture the lightning and down conductors to carry the current to the earth electrodes. It also uses equipotential bonding and SPDs to reduce the risk of side flashes and overvoltages.
    - Non-conventional system: It uses devices that claim to prevent or reduce the probability of a direct strike by modifying the electric field around the protected structure. Examples are early streamer emission (ESE) terminals and charge transfer system (CTS).
- The latest industry standards and procedures for earthing and lightning protection are:
  - IEC 60364 series: It covers the electrical installations of buildings and specifies the requirements for earthing systems, protective conductors, equipotential bonding, and SPDs.
  - IEC 62305 series: It covers the protection against lightning and specifies the general principles, risk assessment, physical damage to structures and life hazard, and electrical and electronic systems within structures.
  - IEEE Std 80: It covers the safety in AC substation grounding and specifies the methods for calculating the ground resistance, touch and step voltages, and ground potential rise.
  - IEEE Std 142: It covers the grounding of industrial and commercial power systems and specifies the methods for designing, installing, and testing the grounding systems.



### Types of Batteries

Batteries are devices that store electrical energy in the form of chemical energy and convert it into electrical current when needed. Batteries are widely used in electrical engineering for various applications, such as portable devices, electric vehicles, power backup, etc.

There are mainly two categories of batteries: primary batteries and secondary batteries. A primary battery is a disposable kind of battery. Once used, it cannot be recharged. A secondary battery is a rechargeable battery. Once empty, it can be recharged again and again.

There are also other types of batteries, such as reserve cells, fuel cells, and flow batteries, that have different characteristics and applications.

Some of the common types of batteries and their applications are:

- **Lead-acid batteries**: These are the oldest type of rechargeable batteries, invented in 1859. They consist of lead plates immersed in sulfuric acid solution. They have a low energy density, but a high power density and a low cost. They are used for automobile starter motors, emergency lighting, and uninterruptible power supplies (UPS).
- **Nickel-cadmium batteries (Ni-Cd)**: These are rechargeable batteries that use nickel oxide hydroxide and metallic cadmium as electrodes. They have a high energy density, but suffer from memory effect and environmental issues. They are used for portable devices, such as cameras, toys, and cordless tools.
- **Nickel-metal hydride batteries (Ni-MH)**: These are rechargeable batteries that use nickel oxide hydroxide and a hydrogen-absorbing alloy as electrodes. They have a higher energy density and a lower memory effect than Ni-Cd batteries, but a lower power density and a higher self-discharge rate. They are used for portable devices, such as laptops, mobile phones, and hybrid electric vehicles (HEV).
- **Lithium-ion batteries (Li-ion)**: These are rechargeable batteries that use lithium compounds as electrodes. They have a very high energy density, a high power density, and a low self-discharge rate. They are used for portable devices, such as smartphones, tablets, and laptops, as well as electric vehicles and aerospace applications.
- **Alkaline batteries**: These are primary batteries that use zinc and manganese dioxide as electrodes. They have a high energy density, a long shelf life, and a low cost. They are used for common household devices, such as flashlights, clocks, and remote controls.
- **Zinc-carbon batteries**: These are primary batteries that use zinc and carbon as electrodes. They have a low energy density, a short shelf life, and a low cost. They are used for low-power devices, such as radios, toys, and calculators.
- **Coin cell batteries**: These are small primary batteries that use various combinations of metals and chemicals as electrodes. They have a high energy density, a long shelf life, and a low cost. They are used for small devices, such as watches, hearing aids, and key fobs.
- **Zinc-air batteries**: These are primary batteries that use zinc and oxygen as electrodes. They have a high energy density, but a low power density and a short shelf life. They are used for hearing aids, medical devices, and electric vehicles.
- **Sealed lead-acid batteries**: These are rechargeable batteries that use lead and sulfuric acid as electrodes. They have a low energy density, but a high power density and a low maintenance. They are used for emergency lighting, security systems, and solar power systems.

