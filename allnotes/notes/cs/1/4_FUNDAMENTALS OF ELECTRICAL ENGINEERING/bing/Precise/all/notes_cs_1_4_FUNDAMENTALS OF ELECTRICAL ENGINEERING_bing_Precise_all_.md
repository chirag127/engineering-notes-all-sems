

# FUNDAMENTALS OF ELECTRICAL ENGINEERING

1. Electrical engineering is a branch of engineering that deals with the study and application of electricity, electronics, and electromagnetism.
2. The basic concepts of electrical engineering include electric charge, electric current, electric potential, and electric power.
3. Electric charge is a fundamental property of matter that results from the presence or absence of electrons. It is measured in coulombs (C).
4. Electric current is the flow of electric charge through a conductor. It is measured in amperes (A).
5. Electric potential is the amount of work required to move a unit of electric charge from one point to another. It is measured in volts (V).
6. Electric power is the rate at which electric energy is transferred by an electric circuit. It is measured in watts (W).
7. Electrical engineering also involves the study of circuits, which are networks of interconnected components that carry electric current.
8. Electrical engineers design, develop, and test electrical equipment and systems, including power generation and distribution systems, communication systems, and electronic devices.
9. Electrical engineering is a broad field that encompasses many sub-disciplines, including electronics, power engineering, control systems, and telecommunications.
10. To become an electrical engineer, one typically needs to earn a bachelor's degree in electrical engineering or a related field. Many electrical engineers also pursue advanced degrees to specialize in a particular area of the field.



## Unit 1 - DC Circuits

1. **Introduction to DC Circuits:** A direct current (DC) circuit is an electrical circuit that consists of any combination of constant voltage sources, constant current sources, and resistors. In a DC circuit, the direction of the flow of electrons is constant, flowing from the negative pole of the power source to the positive pole.

2. **Ohm's Law:** Ohm's Law states that the current flowing through a conductor between two points is directly proportional to the voltage across the two points. Mathematically, Ohm's Law is represented as `V = IR`, where `V` is the voltage, `I` is the current, and `R` is the resistance.

3. **Series and Parallel Circuits:** In a series circuit, the components are connected end-to-end, such that the current flows through each component in turn. In a parallel circuit, the components are connected across common points, such that the voltage is the same across each component.

4. **Kirchhoff's Laws:** Kirchhoff's Current Law (KCL) states that the algebraic sum of currents entering a node (or a closed boundary) is zero. Kirchhoff's Voltage Law (KVL) states that the algebraic sum of the voltage drops around any closed loop is zero.

5. **Power in DC Circuits:** The power dissipated in a resistor is given by the formula `P = IV`, where `P` is the power, `I` is the current, and `V` is the voltage. Alternatively, the power can be calculated using the formula `P = I^2R` or `P = V^2/R`.

6. **Capacitors and Inductors:** Capacitors and inductors are passive components that store energy in an electric field and a magnetic field, respectively. In a DC circuit, capacitors act as open circuits, while inductors act as short circuits.

7. **DC Circuit Analysis:** DC circuit analysis involves calculating the voltage, current, and power in each component of a DC circuit. This can be done using techniques such as nodal analysis, mesh analysis, and Thevenin's theorem.



# Electrical Circuit Elements (R, L and C)

## Unit 1 - DC Circuits

### Fundamentals of Electrical Engineering

1. **Resistor (R)**: A resistor is a passive two-terminal electrical component that implements electrical resistance as a circuit element. In electronic circuits, resistors are used to reduce current flow, adjust signal levels, to divide voltages, bias active elements, and terminate transmission lines, among other uses.

2. **Inductor (L)**: An inductor, also known as a coil, choke, or reactor, is a passive two-terminal electrical component that stores energy in a magnetic field when electric current flows through it. Inductors are used in analog circuits and signal processing, and are commonly used in electronic filters to separate signals of different frequencies, and in combination with capacitors to make tuned circuits, used to tune radio and TV receivers.

3. **Capacitor (C)**: A capacitor is a passive two-terminal electrical component that stores electrical energy in an electric field. The effect of a capacitor is known as capacitance. Capacitors are widely used in electronic circuits for blocking direct current while allowing alternating current to pass, in filter networks, for smoothing the output of power supplies, in the resonant circuits that tune radios to particular frequencies, and for many other purposes.

These are the basic definitions and uses of the three main electrical circuit elements: Resistor (R), Inductor (L), and Capacitor (C). They are commonly used in DC circuits and are fundamental to the study of electrical engineering.



# Concept of Active and Passive Elements

In the study of electrical engineering, it is important to understand the concept of active and passive elements in DC circuits. These elements are classified based on their ability to generate or consume energy.

## Active Elements
Active elements are capable of generating energy or converting one form of energy into another. They can provide power to a circuit and are typically used to amplify or control signals. Examples of active elements include batteries, generators, and operational amplifiers.

## Passive Elements
Passive elements, on the other hand, are incapable of generating energy. They can only consume, store, or dissipate energy. Passive elements are used to control the flow of current or voltage in a circuit. Examples of passive elements include resistors, capacitors, and inductors.

In summary, active elements generate or convert energy, while passive elements consume, store, or dissipate energy. Understanding the difference between these two types of elements is crucial in the design and analysis of DC circuits.



### Voltage and Current Sources

Voltage and current sources are fundamental components of electrical circuits. They are used to provide power to the circuit and to control the flow of current.

#### Voltage Sources

A voltage source is a device that provides a constant voltage to a circuit. The voltage provided by the source is independent of the current flowing through it. Examples of voltage sources include batteries and power supplies.

#### Current Sources

A current source is a device that provides a constant current to a circuit. The current provided by the source is independent of the voltage across it. Examples of current sources include photovoltaic cells and constant current power supplies.

#### Ideal and Real Sources

In an ideal voltage source, the voltage provided is constant regardless of the load connected to it. In a real voltage source, the voltage may vary slightly depending on the load.

Similarly, in an ideal current source, the current provided is constant regardless of the load connected to it. In a real current source, the current may vary slightly depending on the load.

#### Dependent and Independent Sources

Voltage and current sources can be either dependent or independent. An independent source provides a constant voltage or current regardless of other circuit elements. A dependent source, on the other hand, provides a voltage or current that is dependent on another circuit element.

#### Summary

- Voltage and current sources are fundamental components of electrical circuits.
- A voltage source provides a constant voltage to a circuit.
- A current source provides a constant current to a circuit.
- Voltage and current sources can be either ideal or real, and either dependent or independent.




### Concept of Linearity

Linearity is a mathematical property that is used to describe the behavior of a system or a component. In the context of DC circuits, linearity refers to the relationship between the voltage and current in a circuit element.

A circuit element is said to be linear if its voltage-current relationship follows Ohm's Law, which states that the current through a conductor between two points is directly proportional to the voltage across the two points. This means that if the voltage across a linear circuit element is doubled, the current through it will also double.

In a linear circuit, the output is directly proportional to the input. This means that if the input voltage or current is increased, the output voltage or current will also increase by the same factor. Similarly, if the input is decreased, the output will also decrease by the same factor.

Linear circuit elements include resistors, capacitors, and inductors. These elements obey Ohm's Law and their behavior can be easily predicted using mathematical equations.

In contrast, non-linear circuit elements, such as diodes and transistors, do not obey Ohm's Law. Their voltage-current relationship is not a straight line and their behavior is more complex.

Linearity is an important concept in the analysis of DC circuits because it allows us to use simple mathematical techniques, such as superposition and Thevenin's theorem, to analyze and solve complex circuits.

In summary, linearity is a property of a circuit element that describes its voltage-current relationship. Linear circuit elements obey Ohm's Law and their behavior can be easily predicted using mathematical equations. Linearity is an important concept in the analysis of DC circuits because it allows us to use simple mathematical techniques to analyze and solve complex circuits.



# Unilateral and Bilateral Elements

Unilateral and bilateral elements are terms used to describe the behavior of electrical components in a circuit. These terms are important to understand when studying DC circuits in the subject of Fundamentals of Electrical Engineering.

## Unilateral Elements

- Unilateral elements are electrical components that allow current to flow in only one direction.
- Examples of unilateral elements include diodes, which allow current to flow in the forward direction but block current in the reverse direction.
- Unilateral elements are important in circuits where the direction of current flow needs to be controlled, such as in rectifier circuits.

## Bilateral Elements

- Bilateral elements are electrical components that allow current to flow in both directions.
- Examples of bilateral elements include resistors, capacitors, and inductors, which allow current to flow in both directions.
- Bilateral elements are important in circuits where the direction of current flow is not important, such as in filter circuits.

In summary, unilateral and bilateral elements are important concepts to understand when studying DC circuits in the subject of Fundamentals of Electrical Engineering. Unilateral elements allow current to flow in only one direction, while bilateral elements allow current to flow in both directions. These elements are used in different types of circuits depending on the desired behavior of the circuit.



# Kirchhoff's Laws

Kirchhoff's laws, also known as Kirchhoff's rules, are two laws that deal with the current and voltage in electrical circuits. They are widely used in electrical engineering and form the basis for network analysis .

1. **Kirchhoff's Current Law (KCL)**: Also known as Kirchhoff's junction rule, Kirchhoff's first law, Kirchhoff's point rule, and Kirchhoff's nodal rule, this law is an application of the principle of conservation of electric charge. It states that the sum of all currents entering and exiting a node must sum to zero  .

2. **Kirchhoff's Voltage Law (KVL)**: This law states that the sum of the voltage drops around any closed loop in a circuit must be zero. It is based on the principle of conservation of energy.

These laws can be applied in both time and frequency domains and are the foundation of advanced circuit analysis  . They build upon the foundation outlined in Ohm's Law and have helped pave the way for the complex circuit analysis that we rely on today .



# Mesh and Nodal Methods of Analysis

Mesh and nodal methods of analysis are two common techniques used to analyze DC circuits. These methods are used to determine the current and voltage values in a circuit.

## Mesh Analysis

Mesh analysis is a technique used to solve circuits with multiple loops. It involves writing equations based on Kirchhoff's Voltage Law (KVL) for each loop in the circuit. The equations are then solved simultaneously to determine the current flowing in each loop.

The steps for performing mesh analysis are as follows:

1. Identify all the loops in the circuit.
2. Assign a current to each loop.
3. Write KVL equations for each loop.
4. Solve the equations simultaneously to determine the current in each loop.

## Nodal Analysis

Nodal analysis is a technique used to solve circuits with multiple nodes. It involves writing equations based on Kirchhoff's Current Law (KCL) for each node in the circuit. The equations are then solved simultaneously to determine the voltage at each node.

The steps for performing nodal analysis are as follows:

1. Identify all the nodes in the circuit.
2. Assign a voltage to each node.
3. Write KCL equations for each node.
4. Solve the equations simultaneously to determine the voltage at each node.

Both mesh and nodal analysis are powerful techniques for analyzing DC circuits. They can be used to solve complex circuits with multiple loops and nodes. It is important to understand these methods and be able to apply them when analyzing DC circuits.



## Unit 2 - Steady State Analysis of Single Phase AC Circuits

1. **Introduction:** Steady state analysis of single phase AC circuits involves the calculation of current, voltage, and power in circuits that are powered by a single phase AC source.

2. **Single Phase AC Source:** A single phase AC source is an electrical power source that delivers a sinusoidal voltage waveform. The voltage varies periodically with time, and the frequency of the variation is typically 50 or 60 Hz.

3. **Steady State:** Steady state refers to the condition where all the circuit variables such as current, voltage, and power have reached their final values and are no longer changing with time.

4. **Impedance:** Impedance is a measure of the opposition to the flow of current in an AC circuit. It is a complex quantity, with both magnitude and phase angle.

5. **Ohm's Law:** Ohm's law states that the current flowing through a conductor is directly proportional to the voltage applied across it, and inversely proportional to the resistance of the conductor. In an AC circuit, Ohm's law can be extended to include impedance.

6. **Power Factor:** Power factor is the ratio of the real power consumed by a load to the apparent power supplied to it. It is a measure of how effectively the load is using the supplied power.

7. **Power Calculations:** In an AC circuit, power calculations involve the determination of real, reactive, and apparent power. Real power is the power consumed by the resistive elements of the circuit, while reactive power is the power consumed by the reactive elements. Apparent power is the product of the RMS values of voltage and current.

8. **Series and Parallel Circuits:** In a series circuit, all the components are connected end-to-end, and the same current flows through all the components. In a parallel circuit, the components are connected across common points, and the voltage across each component is the same.

9. **Resonance:** Resonance occurs in an AC circuit when the inductive reactance and the capacitive reactance are equal in magnitude. At resonance, the circuit exhibits maximum or minimum impedance, depending on the type of circuit.

10. **Conclusion:** Steady state analysis of single phase AC circuits involves the use of various concepts such as impedance, Ohm's law, power factor, and resonance. Understanding these concepts is essential for the analysis and design of AC circuits.



# Representation of Sinusoidal waveforms – Average and effective values

## Unit 2 - Steady State Analysis of Single Phase AC Circuits

### FUNDAMENTALS OF ELECTRICAL ENGINEERING

- A sinusoidal waveform is a mathematical curve that describes a smooth, repetitive oscillation.
- It is named after the function sine, which it resembles.
- The average value of a sinusoidal waveform is the arithmetic mean of the waveform over one period.
- The effective value, also known as the root mean square (RMS) value, is the square root of the mean of the squares of the waveform over one period.
- The RMS value is used to represent the equivalent steady-state value of a sinusoidal waveform for the purposes of power calculations.
- The RMS value of a sinusoidal waveform is equal to its peak value divided by the square root of two.
- The average and effective values are important for the analysis of single-phase AC circuits in steady state.




### Form and Peak Factors

Form factor and peak factor are two important concepts in the steady state analysis of single phase AC circuits. These factors are used to describe the shape of an AC waveform.

1. **Form Factor**: The form factor is defined as the ratio of the RMS (root mean square) value of an AC waveform to its average value. It is a measure of the "flatness" of the waveform. A waveform with a high form factor has a more peaked shape, while a waveform with a low form factor is flatter.

2. **Peak Factor**: The peak factor is defined as the ratio of the peak value of an AC waveform to its RMS value. It is a measure of the "sharpness" of the waveform. A waveform with a high peak factor has a sharper peak, while a waveform with a low peak factor has a more rounded peak.

These factors are important in the analysis of AC circuits because they affect the behavior of the circuit components. For example, the form factor and peak factor of the voltage waveform can affect the heating of a resistor in an AC circuit.



# Analysis of single phase AC Circuits consisting R-L-C combination (Series and Parallel)

## Introduction
- Single phase AC circuits are electrical circuits that are powered by a single phase alternating current (AC) source.
- These circuits can consist of various combinations of resistors (R), inductors (L), and capacitors (C) connected in series or parallel.
- The analysis of these circuits involves calculating the current, voltage, and power in each component.

## Series R-L-C Circuit
- In a series R-L-C circuit, the components are connected end-to-end, forming a single path for the current to flow.
- The total impedance of the circuit is the sum of the individual impedances of the components.
- The current in the circuit is the same for all components and is calculated using Ohm's Law: I = V/Z, where V is the voltage of the AC source and Z is the total impedance of the circuit.
- The voltage across each component can be calculated using the voltage divider rule: Vx = Zx/Z * V, where Vx is the voltage across component x, Zx is the impedance of component x, and Z is the total impedance of the circuit.

## Parallel R-L-C Circuit
- In a parallel R-L-C circuit, the components are connected side-by-side, forming multiple paths for the current to flow.
- The total impedance of the circuit is calculated using the formula for parallel impedances: 1/Z = 1/Z1 + 1/Z2 + ... + 1/Zn, where Z1, Z2, ... Zn are the individual impedances of the components.
- The current in each component can be calculated using Ohm's Law: Ix = V/Zx, where Ix is the current in component x, V is the voltage of the AC source, and Zx is the impedance of component x.
- The voltage across each component is the same and is equal to the voltage of the AC source.

## Conclusion
- The analysis of single phase AC circuits consisting of R-L-C combinations in series or parallel involves calculating the total impedance of the circuit and using Ohm's Law and the voltage divider rule to determine the current and voltage in each component.
- Understanding these concepts is essential for the steady state analysis of single phase AC circuits in the subject of Fundamentals of Electrical Engineering.



### Apparent, Active & Reactive Power

In the study of AC circuits, power is an important concept. There are three types of power in an AC circuit: apparent power, active power, and reactive power.

1. **Apparent Power** is the product of the RMS values of voltage and current. It is measured in volt-amperes (VA) and is represented by the letter 'S'. Apparent power is the total power supplied to the circuit, and is the sum of the active and reactive power.

2. **Active Power** is the power that is actually consumed by the load in the circuit. It is measured in watts (W) and is represented by the letter 'P'. Active power is the power that is converted into useful work, such as heat, light, or motion.

3. **Reactive Power** is the power that is stored in the circuit and then returned to the source. It is measured in volt-amperes reactive (VAR) and is represented by the letter 'Q'. Reactive power is the power that is used to establish the magnetic and electric fields in inductive and capacitive loads.

In a purely resistive circuit, the apparent power is equal to the active power, and there is no reactive power. In a circuit with inductive or capacitive loads, the apparent power is greater than the active power, and there is reactive power present.

It is important to understand the relationship between these three types of power when analyzing AC circuits, as it can affect the efficiency and performance of the circuit. Understanding these concepts is essential for the steady state analysis of single phase AC circuits, which is covered in Unit 2 of the subject Fundamentals of Electrical Engineering.



# Power Factor

Power factor is a term used in the analysis of AC circuits. It is defined as the ratio of the real power absorbed by the load to the apparent power flowing in the circuit . Real power is the average of the instantaneous product of voltage and current and represents the capacity of the electricity for performing work .

Power factor can also be defined as the cosine of the phase angle between voltage and current, or the ratio of the resistance to impedance . It can also be expressed as the ratio of the true power to the apparent power .

In engineering applications, the power factor is the amount by which the power delivered in the circuit is less than the theoretical maximum of the circuit due to voltage and current being out of phase . For a resistor, the phase angle is 0, so the average power dissipated is the product of the RMS values of the current and voltage .



### Concept of Resonance in Series & Parallel Circuits

Resonance is a phenomenon that occurs in both series and parallel AC circuits. It is a condition where the circuit's impedance is purely resistive, resulting in maximum power transfer from the source to the load.

#### Series Resonance

In a series RLC circuit, resonance occurs when the inductive reactance (XL) equals the capacitive reactance (XC). At this point, the circuit's impedance is purely resistive, and the current is at its maximum value.

The resonant frequency of a series RLC circuit is given by the formula:

f = 1 / (2π * √(LC))

At resonance, the voltage across the inductor and capacitor are equal in magnitude but opposite in phase, resulting in a net voltage of zero across the two components.

#### Parallel Resonance

In a parallel RLC circuit, resonance occurs when the admittance of the circuit is purely conductive. This happens when the conductance (G) equals the susceptance (B).

The resonant frequency of a parallel RLC circuit is given by the formula:

f = 1 / (2π * √(LC))

At resonance, the current through the inductor and capacitor are equal in magnitude but opposite in phase, resulting in a net current of zero through the two components.

#### Applications of Resonance

Resonance has many practical applications in electrical engineering. It is used in the design of filters, oscillators, and tuned circuits. In power systems, resonance can cause overvoltage and overcurrent conditions, which can damage equipment. Therefore, it is important to understand the concept of resonance and its effects on AC circuits.




# Bandwidth and Quality Factor

## Bandwidth
- Bandwidth is defined as the range of frequencies in which the amplitude of the current is equal to or greater than (1 / 2 = 2 / 2) times its maximum amplitude.
- Bandwidth is measured between the 0.707 current amplitude points. The 0.707 current points correspond to the half power points since P = I^2 R, (0.707)^2 = (0.5).
- The bandwidth of the series circuit is given by the formula B = !2-!1= R/L.

## Quality Factor
- Quality factor is a dimensionless parameter that characterizes the resonance of a circuit.
- A high Q resonant circuit has a narrow bandwidth as compared to a low Q.
- The formula for the quality factor is given by Q = fc/BW, where fc is the resonant frequency and BW is the bandwidth.

## Relationship between Bandwidth and Quality Factor
- The bandwidth and quality factor of a circuit are inversely proportional. As the quality factor increases, the bandwidth decreases and vice versa.
- The formula for the relationship between bandwidth and quality factor is given by BW = fc/Q, where fc is the resonant frequency and Q is the quality factor.



### Three phase balanced circuits

Three phase balanced circuits are an important topic in the study of steady state analysis of single phase AC circuits, which is covered in Unit 2 of the subject Fundamentals of Electrical Engineering.

1. The electrical system is of two types: the single-phase system and the three-phase system. The single-phase system has only one phase wire and one return wire, thus it is used for low power transmission .
2. It is always better to solve the balanced three-phase circuits on the basis of each phase. When the three-phase supply voltage is given without reference to the line or phase value, then it is the line voltage which is taken into consideration .
3. In a balanced system, the neutral current and neutral power is zero. You can think of a balanced three-phase system as three single-phase systems connected to a neutral line .




### Voltage and Current Relations in Star and Delta Connections

#### Star Connection
- In a star connection, the phase voltage is equal to the line voltage divided by the square root of 3.
- The phase current is equal to the line current.
- The power in a star connection is equal to the square root of 3 multiplied by the line voltage, line current, and power factor.

#### Delta Connection
- In a delta connection, the phase voltage is equal to the line voltage.
- The phase current is equal to the line current divided by the square root of 3.
- The power in a delta connection is equal to 3 multiplied by the phase voltage, phase current, and power factor.




## Unit 3 - Transformers

Transformers are electrical devices that transfer electrical energy between two or more circuits through electromagnetic induction. They are used to increase or decrease the voltage of an alternating current (AC) power supply.

1. **Principle of operation:** A transformer operates on the principle of electromagnetic induction, which states that a changing magnetic field can induce an electromotive force (EMF) in a conductor.
2. **Construction:** A transformer consists of two or more coils of wire wrapped around a magnetic core, usually made of iron. The coil connected to the power source is called the primary coil, and the coil connected to the load is called the secondary coil.
3. **Types of transformers:** There are several types of transformers, including step-up transformers, step-down transformers, isolation transformers, and autotransformers. Each type serves a specific purpose and is used in different applications.
4. **Efficiency:** The efficiency of a transformer is the ratio of the power delivered to the load to the power supplied to the primary coil. Factors that affect the efficiency of a transformer include the resistance of the coils, the core losses, and the leakage flux.
5. **Applications:** Transformers are used in a wide range of applications, including power generation, transmission, and distribution, as well as in electronic devices such as radios, televisions, and computers.




### Magnetic Circuits

Magnetic circuits are used to analyze the behavior of magnetic fields in transformers. They are similar to electric circuits, but instead of electric current, they deal with magnetic flux.

Here are some key points to remember about magnetic circuits:

1. Magnetic circuits are used to analyze the behavior of magnetic fields in transformers.
2. Magnetic circuits are similar to electric circuits, but instead of electric current, they deal with magnetic flux.
3. Magnetic flux is the measure of the total magnetic field that passes through a given area.
4. The unit of magnetic flux is the Weber (Wb).
5. Magnetic circuits are made up of magnetic materials, such as iron or steel, that have the ability to conduct magnetic flux.
6. The magnetic field strength, or magnetomotive force (MMF), is the force that drives the magnetic flux through the magnetic circuit.
7. The magnetic field strength is measured in ampere-turns (At).
8. The reluctance of a magnetic circuit is the opposition to the flow of magnetic flux. It is analogous to the resistance in an electric circuit.
9. The unit of reluctance is the ampere-turn per Weber (At/Wb).
10. The total magnetic flux in a magnetic circuit is equal to the MMF divided by the reluctance.




# Unit 3 - Transformers

### Ideal and Practical Transformer

An ideal transformer is an imaginary transformer that has no losses, meaning that the power input is equal to the power output. In an ideal transformer, the primary and secondary windings have no resistance, and there is no leakage of magnetic flux. The core of an ideal transformer has infinite permeability, meaning that all the magnetic flux is confined to the core.

A practical transformer, on the other hand, is a real transformer that has losses. These losses can be divided into two categories: copper losses and iron losses. Copper losses are caused by the resistance of the windings, while iron losses are caused by the core's magnetic properties.

In a practical transformer, the primary and secondary windings have resistance, and there is leakage of magnetic flux. The core of a practical transformer has finite permeability, meaning that some of the magnetic flux leaks out of the core.

Despite these losses, practical transformers can still be very efficient, with efficiencies of over 90% being common. The efficiency of a transformer can be improved by using better materials, such as high-grade copper for the windings and high-permeability steel for the core.

In summary, an ideal transformer is an imaginary transformer with no losses, while a practical transformer is a real transformer that has losses. Despite these losses, practical transformers can still be very efficient.



### Equivalent Circuit of Transformers

An equivalent circuit of a transformer is a graphical representation of a transformer circuit in which the resistance and leakage reactance are imagined to be external to the winding. The exact equivalent circuit of a transformer can be referred to as the primary or secondary side.

In fact, an equivalent circuit of any electric instrument is important for the analysis of its performance and to discover any scope of further modification of modeling. The equivalent circuit of transformer includes a setup of inductance, resistance, voltage, capacitance, etc.

The equivalent circuit diagram of a transformer is a simplified circuit in which the impedance, resistance and leakage reactance of the transformer can be more easily calculated. The equivalent impedance of transformer is an important parameter to be calculated.



### Losses in Transformers

Transformers are used to transfer electrical energy from one circuit to another through electromagnetic induction. However, during this process, some energy is lost in the form of heat. These losses are known as transformer losses. There are two main types of losses in transformers: core losses and copper losses.

1. **Core losses:** Core losses, also known as iron losses, occur in the magnetic core of the transformer. These losses are caused by two main factors: hysteresis and eddy currents. Hysteresis losses occur due to the repeated magnetization and demagnetization of the core, while eddy current losses occur due to the circulation of currents within the core. Core losses are constant and do not vary with the load on the transformer.

2. **Copper losses:** Copper losses, also known as winding losses, occur in the windings of the transformer. These losses are caused by the resistance of the windings and vary with the load on the transformer. Copper losses increase as the load on the transformer increases.

In addition to these two main types of losses, there are also other minor losses such as stray losses and dielectric losses. Stray losses occur due to leakage of magnetic flux, while dielectric losses occur due to the insulation of the windings.

To minimize transformer losses, the design of the transformer must be optimized. This can be done by using high-quality materials for the core and windings, and by carefully designing the transformer to minimize leakage of magnetic flux.




# Regulation and Efficiency

Regulation and efficiency are two important parameters for transformers in the subject of Fundamentals of Electrical Engineering.

## Regulation

- Regulation is the measure of the change in the secondary voltage of a transformer when the load is varied from no-load to full-load.
- It is expressed as a percentage of the no-load voltage.
- The regulation of a transformer is given by the formula: %Regulation = (No-load voltage - Full-load voltage) / Full-load voltage * 100
- A transformer with good regulation will have a small change in secondary voltage when the load is varied.
- The regulation of a transformer depends on its design and the power factor of the load.

## Efficiency

- Efficiency is the measure of how well a transformer converts the input power to output power.
- It is expressed as a percentage of the input power that is delivered to the load.
- The efficiency of a transformer is given by the formula: %Efficiency = (Output power / Input power) * 100
- A transformer with high efficiency will deliver more power to the load for a given input power.
- The efficiency of a transformer depends on its design, the power factor of the load, and the losses in the transformer.




## Unit 4 - Electrical machines

1. Electrical machines are devices that convert electrical energy into mechanical energy or vice versa.
2. There are two main types of electrical machines: motors and generators.
3. Motors convert electrical energy into mechanical energy, while generators convert mechanical energy into electrical energy.
4. Electrical machines operate on the principle of electromagnetic induction.
5. The efficiency of an electrical machine is the ratio of its output power to its input power.
6. The performance of an electrical machine is affected by factors such as its design, construction, and operating conditions.
7. Electrical machines are used in a wide range of applications, including transportation, industrial processes, and power generation.
8. Maintenance and proper operation of electrical machines are important to ensure their safe and efficient operation.



### DC Machines

DC machines are electro-mechanical energy conversion devices. There are two types of DC machines: DC generators and DC motors. A DC generator converts mechanical power into DC electrical power, while a DC motor converts DC electrical power into mechanical power .

The construction of a DC machine is the same for both a DC motor and a DC generator. The main components of a DC machine include the yoke (or frame), poles and pole shoes, armature core, field winding, armature winding, commutator, brushes, shaft, and bearings .

The yoke, also known as the frame, covers the internal parts of the machine. The poles and pole shoes are responsible for producing the magnetic field. The armature core is the rotating part of the machine, and the armature winding is the winding on the armature core. The field winding is the winding on the poles, and the commutator is responsible for converting the AC generated in the armature winding into DC. The brushes are responsible for conducting current between the commutator and the external circuit. The shaft is the rotating part of the machine, and the bearings support the shaft .

DC machines have many applications, including in electric vehicles, industrial motors, and generators. They are versatile machines that can be used for a wide range of purposes.



# Principle & Construction of Electrical Machines

Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. They operate on the principles of electromagnetism, which states that an electric current flowing through a conductor produces a magnetic field around it.

There are two main types of electrical machines: generators and motors.

## Generators
Generators convert mechanical energy into electrical energy. They operate on the principle of electromagnetic induction, which states that a changing magnetic field induces an electric current in a conductor.

The construction of a generator consists of two main parts: the rotor and the stator. The rotor is the rotating part of the machine and contains the magnetic field. The stator is the stationary part of the machine and contains the conductors where the electric current is induced.

## Motors
Motors convert electrical energy into mechanical energy. They operate on the principle of electromagnetic force, which states that a current-carrying conductor placed in a magnetic field experiences a force.

The construction of a motor is similar to that of a generator, with a rotor and a stator. The rotor contains the conductors where the electric current flows, and the stator contains the magnetic field.

In summary, electrical machines operate on the principles of electromagnetism, and their construction consists of a rotor and a stator. Generators convert mechanical energy into electrical energy, while motors convert electrical energy into mechanical energy.



# Types of Electrical Machines

Electrical machines are devices that convert electrical energy into mechanical energy or vice versa. There are several types of electrical machines, including:

1. **DC Machines**: These machines convert direct current (DC) electrical energy into mechanical energy or vice versa. They include DC motors and DC generators.

2. **AC Machines**: These machines convert alternating current (AC) electrical energy into mechanical energy or vice versa. They include AC motors and AC generators, also known as alternators.

3. **Transformers**: These machines transfer electrical energy from one circuit to another through electromagnetic induction. They are used to change the voltage level of an AC power supply.

4. **Special Machines**: These machines have specific applications and include machines such as stepper motors, servo motors, and linear motors.

Each type of electrical machine has its own unique characteristics and is used in different applications. It is important to understand the differences between these machines in order to select the appropriate machine for a specific application.



# EMF Equation of Generator and Torque Equation of Motor

## Unit 4: Electrical Machines

### Fundamentals of Electrical Engineering

#### EMF Equation of Generator

The EMF equation of a generator is used to determine the generated EMF in a generator. It is given by the formula:

EMF = (Φ * Z * N * P) / (60 * A)

Where:
- Φ is the flux per pole in Weber
- Z is the total number of armature conductors
- N is the speed of the armature in RPM
- P is the number of poles
- A is the number of parallel paths in the armature

#### Torque Equation of Motor

The torque equation of a motor is used to determine the torque produced by a motor. It is given by the formula:

T = (Φ * Ia * Z * P) / (2π * A)

Where:
- Φ is the flux per pole in Weber
- Ia is the armature current in Amperes
- Z is the total number of armature conductors
- P is the number of poles
- A is the number of parallel paths in the armature

These equations are important for understanding the operation of electrical machines and are commonly used in the study of the fundamentals of electrical engineering. It is important to note that the values of the variables in these equations can vary depending on the specific design and construction of the machine in question. Therefore, it is important to use the appropriate values for the specific machine being analyzed.



# Applications of DC Motors (Simple Numerical Problems)

DC motors are widely used in various applications due to their versatility and performance. Some of the common applications of DC motors include:

1. **Electric vehicles:** DC motors are used in electric vehicles to provide propulsion. The high torque and speed control capabilities of DC motors make them ideal for this application.

2. **Industrial machinery:** DC motors are used in various industrial machinery such as lathes, drills, and milling machines. The speed control and high starting torque of DC motors make them suitable for these applications.

3. **Home appliances:** DC motors are used in various home appliances such as vacuum cleaners, washing machines, and kitchen appliances. The compact size and efficiency of DC motors make them ideal for these applications.

4. **Robotics:** DC motors are used in robotics to provide motion control. The precise speed and position control capabilities of DC motors make them ideal for this application.

Here is a simple numerical problem to illustrate the use of DC motors in an application:

**Problem:** A DC motor is used to lift a load of 100 kg to a height of 10 meters. The motor has an efficiency of 80% and operates at a voltage of 220V. Calculate the power required by the motor and the time taken to lift the load.

**Solution:**
- The work done in lifting the load is given by the formula: Work = Force x Distance
- The force required to lift the load is equal to the weight of the load, which is given by the formula: Weight = Mass x Acceleration due to gravity
- Substituting the values, we get: Force = 100 kg x 9.8 m/s^2 = 980 N
- The work done in lifting the load is: Work = 980 N x 10 m = 9800 J
- The power required by the motor is given by the formula: Power = Work / Time
- Since the motor has an efficiency of 80%, the actual power required by the motor is: Power = 9800 J / (Time x 0.8)
- The electrical power supplied to the motor is given by the formula: Power = Voltage x Current
- Substituting the values, we get: Current = 9800 J / (Time x 0.8 x 220V)
- Let's assume that the time taken to lift the load is 10 seconds. Substituting this value, we get: Current = 9800 J / (10 s x 0.8 x 220V) = 5.57 A
- The power required by the motor is: Power = 220V x 5.57 A = 1225.4 W
- The time taken to lift the load is: Time = 9800 J / (0.8 x 1225.4 W) = 10 s




# Three Phase Induction Motor

A three-phase induction motor is a type of AC induction motor that operates on a three-phase supply, as compared to a single-phase induction motor, which requires a single-phase supply to operate.

## Working Principle

An electrical motor is an electromechanical device that converts electrical energy into mechanical energy. In the case of three-phase AC operation, the most widely used motor is a three-phase induction motor, as this type of motor does not require an additional starting device.

## Construction

A three-phase induction motor consists of two major parts: a stator and a rotor.

### Stator

The stator of a three-phase induction motor is made up of a number of slots to construct a three-phase winding circuit, which is connected to a three-phase AC source.

## Applications

Three-phase alternating current (AC) machines represent the most important family of electric machines for industrial drives and other heavy-duty applications. Induction machines can be divided into two categories: squirrel-cage machines and wound rotor machines with slip rings.



### Principle & Construction

Unit 4 - Electrical Machines in the subject of Fundamentals of Electrical Engineering

1. Electrical machines are devices that convert electrical energy into mechanical energy or vice versa.
2. The principle of operation of electrical machines is based on the interaction between magnetic fields and electric currents.
3. The construction of electrical machines involves the use of magnetic materials, conductors, and insulators.
4. The main components of an electrical machine are the stator, rotor, and windings.
5. The stator is the stationary part of the machine and contains the magnetic field.
6. The rotor is the rotating part of the machine and interacts with the magnetic field to produce mechanical motion.
7. The windings are conductors that carry electric currents and are responsible for generating the magnetic field.
8. The design and construction of electrical machines must take into account factors such as efficiency, power output, and operating conditions.
9. Different types of electrical machines, such as motors, generators, and transformers, have different construction and operating principles.
10. Understanding the principles and construction of electrical machines is essential for their proper operation and maintenance.




# Types of Electrical Machines

In the subject of Fundamentals of Electrical Engineering, Unit 4 focuses on Electrical Machines. There are several types of electrical machines, including:

1. **DC Machines**: These machines convert electrical energy into mechanical energy or vice versa using direct current. They can be further classified into DC generators and DC motors.

2. **AC Machines**: These machines convert electrical energy into mechanical energy or vice versa using alternating current. They can be further classified into AC generators (alternators) and AC motors.

3. **Transformers**: These machines transfer electrical energy from one circuit to another through electromagnetic induction. They can be further classified into step-up and step-down transformers.

4. **Special Machines**: These machines have specific applications and include machines such as stepper motors, servo motors, and brushless DC motors.

Each type of electrical machine has its own unique characteristics and applications. It is important to understand the differences between them in order to select the appropriate machine for a given task.



# Slip-torque characteristics

Slip-torque characteristics are an important aspect of electrical machines, particularly in the study of induction motors. These characteristics describe the relationship between the slip and torque of an induction motor.

1. Slip is defined as the difference between the synchronous speed of the rotating magnetic field and the rotor speed, expressed as a percentage of the synchronous speed.
2. Torque is the rotational force produced by the motor.
3. The slip-torque characteristic curve shows how the torque produced by the motor varies with changes in slip.
4. At low slip values, the torque produced by the motor is low. As the slip increases, the torque also increases, reaching a maximum value at a certain slip value known as the pull-out or breakdown torque.
5. Beyond the pull-out torque, the torque decreases with increasing slip until the motor stalls.
6. The shape of the slip-torque characteristic curve is determined by the design of the motor, particularly the rotor resistance and reactance.
7. By varying the rotor resistance, the slip-torque characteristic curve can be modified to suit specific applications.

This information is part of Unit 4 - Electrical Machines in the subject of Fundamentals of Electrical Engineering. It is important to understand the slip-torque characteristics of induction motors in order to properly design and operate these machines.



# Applications (Numerical problems related to slip only)

Slip is an important concept in the study of electrical machines, particularly in the context of induction motors. It is defined as the difference between the synchronous speed of the rotor magnetic field and the actual speed of the rotor, expressed as a percentage of the synchronous speed.

Here are some numerical problems related to slip:

1. An induction motor has a synchronous speed of 1200 RPM and a rotor speed of 1140 RPM. Calculate the slip of the motor.

Solution: Slip = (Synchronous speed - Rotor speed) / Synchronous speed
Slip = (1200 - 1140) / 1200
Slip = 0.05 or 5%

2. An induction motor has a slip of 4% at full load. If the synchronous speed of the motor is 1500 RPM, calculate the rotor speed at full load.

Solution: Slip = (Synchronous speed - Rotor speed) / Synchronous speed
Rotor speed = Synchronous speed - (Slip * Synchronous speed)
Rotor speed = 1500 - (0.04 * 1500)
Rotor speed = 1440 RPM

3. An induction motor has a synchronous speed of 1800 RPM and a rotor speed of 1750 RPM. Calculate the slip of the motor.

Solution: Slip = (Synchronous speed - Rotor speed) / Synchronous speed
Slip = (1800 - 1750) / 1800
Slip = 0.0278 or 2.78%

These are some examples of numerical problems related to slip in the context of electrical machines. Understanding and solving these types of problems can help in gaining a better understanding of the concept of slip and its applications in electrical machines.



# Single Phase Induction Motor

- A single phase induction motor is similar to the three phase squirrel cage induction motor except there is single phase two windings (instead of one three phase winding in 3-phase motors) mounted on the stator and the cage winding rotor is placed inside the stator which freely rotates with the help of mounted bearings on the motor shaft .
- The electrical power factor of single phase induction motors is low as compared to three phase induction motors. For the same size, the single-phase induction motors develop about 50% of the output as that of three phase induction motors. The starting torque is also low for asynchronous motors/single phase induction motor .
- The rotor is a rotating part of an induction motor. The rotor connects the mechanical load through the shaft. The rotor in the single-phase induction motor is of squirrel cage rotor type. The construction of single phase induction motor is almost similar to the squirrel cage three-phase induction motor .
- Single-phase induction motors have a copper or aluminum squirrel cage embedded in a cylinder of steel laminations, typical of polyphase induction motors. Permanent-Split Capacitor Motor One way to solve the single phase problem is to build a 2-phase motor, deriving 2-phase power from single phase .




# Principle of Operation and Introduction to Methods of Starting

## Electrical Machines - Unit 4

### Fundamentals of Electrical Engineering

1. Electrical machines are devices that convert electrical energy into mechanical energy or vice versa.
2. The principle of operation of electrical machines is based on the interaction between magnetic fields and electric currents.
3. There are two main types of electrical machines: generators and motors.
4. Generators convert mechanical energy into electrical energy, while motors convert electrical energy into mechanical energy.
5. The starting methods of electrical machines vary depending on the type of machine and its application.
6. Common starting methods for motors include direct-on-line starting, star-delta starting, and soft starting.
7. Direct-on-line starting involves applying full voltage to the motor windings, resulting in high starting current and torque.
8. Star-delta starting reduces the starting current by connecting the motor windings in a star configuration during starting, and then switching to a delta configuration for normal operation.
9. Soft starting gradually increases the voltage applied to the motor windings, reducing the starting current and torque.
10. The choice of starting method depends on factors such as the size of the motor, the load characteristics, and the power supply conditions.




# Applications of Electrical Machines

Unit 4 of the subject Fundamentals of Electrical Engineering covers the topic of Electrical Machines. Here are some of the applications of electrical machines:

1. **Electric Motors**: Electric motors are used to convert electrical energy into mechanical energy. They are used in a wide range of applications, including household appliances, industrial machinery, and transportation vehicles.

2. **Generators**: Generators are used to convert mechanical energy into electrical energy. They are used in power plants to generate electricity for homes and businesses.

3. **Transformers**: Transformers are used to change the voltage of an electrical supply. They are used in power distribution systems to step up or step down the voltage of the electricity being transmitted.

4. **Alternators**: Alternators are used to generate alternating current (AC) electricity. They are commonly used in vehicles to charge the battery and power the electrical system.

5. **Synchronous Machines**: Synchronous machines are used in power plants to generate electricity. They are also used in large industrial applications to provide a constant speed for machinery.




# Three Phase Synchronous Machines

Three Phase Synchronous Machines are a type of electrical machine that can operate as either a motor or a generator. These machines are commonly used in power generation and industrial applications.

1. **Three-Phase Synchronous Generator**: A synchronous machine that converts mechanical energy into 3-phase electrical energy through the process of electromagnetic induction is known as a 3-phase synchronous generator or alternator. A 3-phase alternator consists of an armature winding and a field winding, where the EMF is induced in the armature.

2. **Three-Phase Synchronous Motor**: A synchronous machine that converts three-phase electricity into mechanical energy is known as three-phase synchronous motor. Like any other electric motor, a synchronous motor also consists of two major parts namely stator and rotor.

Large AC machines are three-phase type synchronous machines because for the same size of the frame, three-phase machines have nearly 1.5 times the output than that of the single-phase machine. Three-phase power is transmitted and distributed more economical than single-phase power.



# Principle of operation of alternator and synchronous motor

## Alternator
- An alternator or synchronous generator works on the principle of electromagnetic induction, i.e., when the flux linking a conductor changes, an EMF is induced in the conductor.
- When the armature winding of the alternator is subjected to the rotating magnetic field, the voltage will be generated in the armature winding.
- The rotor of an alternator or a synchronous generator is mechanically coupled to the shaft or the turbine blades, which is made to rotate at synchronous speed Ns under some mechanical force results in magnetic flux cutting of the stationary armature conductors housed on the stator.

## Synchronous Motor
- A synchronous motor is an AC motor, which is identical to the alternator or synchronous generator.
- Similar to the DC generator, the synchronous generator can be made to run as a synchronous motor when driven electrically.
- The synchronous motor converts the electrical energy input into mechanical energy.
- The principle of operation of a synchronous motor can be understood by considering the stator windings to be connected to a three-phase alternating-current supply.
- The effect of the stator current is to establish a magnetic field rotating at 120f/p revolutions per minute for a frequency of f hertz and for p poles.
- Synchronous motors are a doubly excited machine, i.e., two electrical inputs are provided to it.
- Its stator winding which consists of a We provide three-phase supply to three-phase stator winding, and DC to the rotor winding.




# Unit 4 - Electrical Machines: Applications

1. All electrical machines use applications of electro-magnetic principles where electric currents create magnetic fields, which either attract or repel each other. This is the basis of all electric motors, whether they operate on alternating current (AC), direct current (DC) or are universal motors that operate on both .
2. The use of DC machines, i.e., DC generators and motors are very limited. They are mainly used in supplying excitation of small and medium-range alternators. The Industrial Applications of DC Machines are in Electrolytic Processes, Welding processes and Variable speed motor drives .
3. Electric motors are found in applications as diverse as industrial fans, blowers and pumps, machine tools, household appliances, power tools, and disk drives. They may be powered by direct current or by alternating current which leads to the two main classifications: AC motors and DC motors .
4. Rotating electric machines include DC electric machines – DC motors and DC generators, Synchronous machines – Alternators and Synchronous motors, and Induction motors or Asynchronous machines .
5. Electric machines are essential systems in electric vehicles and are widely used in other applications. In particular, permanent magnet direct current (PMDC) motors have been extensively employed in industrial applications such as electric vehicles .



## Unit 5 - Electrical Installations

1. Electrical installations refer to the fixed electrical equipment that is supplied through the electrical wiring system of a building or structure.
2. These installations can include lighting, power outlets, heating and cooling systems, and other electrical equipment.
3. Electrical installations must be designed and installed in accordance with relevant standards and regulations to ensure safety and reliability.
4. The design of an electrical installation should take into account factors such as the intended use of the building or structure, the electrical load requirements, and the environmental conditions.
5. Electrical installations should be regularly inspected and maintained to ensure their continued safe and reliable operation.
6. Faulty or improperly installed electrical installations can pose a serious risk of electric shock or fire.
7. It is important to hire a qualified electrician to carry out any work on electrical installations.




### Introduction of Switch Fuse Unit (SFU)

A Switch Fuse Unit (SFU) is an electrical device that combines the functions of a switch and a fuse. It is used in electrical installations to provide protection against overcurrent and short circuits. The switch allows the user to manually turn the circuit on or off, while the fuse provides automatic protection by melting and breaking the circuit when the current exceeds a certain level.

Some key points to note about SFUs are:

1. SFUs are commonly used in low voltage electrical installations.
2. They provide both manual and automatic control and protection of electrical circuits.
3. The switch and fuse components of an SFU can be replaced separately if needed.
4. SFUs are available in different sizes and current ratings to suit different applications.
5. They are typically installed in a switchboard or distribution board.

In summary, a Switch Fuse Unit (SFU) is an important component in electrical installations, providing both manual control and automatic protection against overcurrent and short circuits. It is essential to select the appropriate size and current rating of SFU for the specific application to ensure safe and reliable operation of the electrical circuit.



# MCB

MCB stands for Miniature Circuit Breaker. It is an automatically operated electrical switch designed to protect an electrical circuit from damage caused by excess current from an overload or short circuit. Its basic function is to interrupt current flow after a fault is detected.

## Key Features of MCB
- MCBs are designed to protect against overcurrent and short circuit conditions.
- They are available in different current ratings and tripping characteristics to suit different applications.
- MCBs are resettable and can be easily turned back on after tripping, unlike fuses which need to be replaced.
- They are compact in size and can be easily installed in consumer units or distribution boards.

## Types of MCB
There are three main types of MCBs based on their tripping characteristics:
1. Type B: trips between 3 and 5 times the full load current and is used for light loads and domestic applications.
2. Type C: trips between 5 and 10 times the full load current and is used for commercial and industrial applications with moderate inrush currents.
3. Type D: trips between 10 and 20 times the full load current and is used for heavy-duty industrial applications with high inrush currents.

## Advantages of MCB
- MCBs provide reliable and fast protection against overcurrent and short circuit conditions.
- They are easy to install and operate, and do not require any special tools or skills.
- MCBs are resettable and can be easily turned back on after tripping, reducing downtime and maintenance costs.
- They are compact in size and can be easily integrated into existing electrical installations.

## Disadvantages of MCB
- MCBs may not provide protection against all types of faults, such as earth faults or residual current faults.
- They may not be suitable for all applications, and the correct type and rating of MCB must be selected for the specific application.
- MCBs may be more expensive than other types of circuit protection devices, such as fuses.




# ELCB

An Earth-leakage circuit breaker (ELCB) is a safety device used in electrical installations with high Earth impedance to prevent electric shocks. It detects small stray voltages on the metal enclosures of electrical equipment and interrupts the circuit if a dangerous voltage is detected .

- ELCB is capable of detecting the slight amount of current in a faulty metal electrical equipment. If any current flows to the ground wire, it is because of electrical faults, and the supply of current to that appliance must be stopped. ELCBs are used to protect the person who is in contact with the electrical device .

- The main function of an ELCB is to prevent shock while electrical installations through high Earth impedance because it is a safety device .

- ELCB is mainly used for protection against electrical shock. They do not offer protection against overloading or short circuit. Therefore, they must be used in series with an MCB (miniature circuit breaker) .

- There are two types of ELCBs: Voltage-Operated and Current-Operated .




### MCCB for the notes of the Unit 5 - Electrical Installations in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

MCCB stands for Molded Case Circuit Breaker. It is a type of electrical protection device that is used to protect the electrical circuit from excessive current, which can cause overload or short circuit. MCCB is used to protect the low voltage distribution system and is available in rating up to 2500 Amps and 1.1 kV.

The construction of an MCCB includes the following main parts:
- Arc chute
- Contacts
- Operating mechanism
- Terminal Connector
- Thermal Trip Unit
- Magnetic Trip Unit

MCCBs can be used for a wide range of voltages and frequencies with adjustable trip settings. Selectivity between circuit breakers is important as it ensures that only the faulty part of the installation is isolated, while all the other switching and protective devices connected to the system remain operative. This reduces the duration of a fault and limits its possible damaging effect only to a part of the installation.



### ACB for the notes of the Unit 5 - Electrical Installations in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

- ACB stands for Air Circuit Breaker.
- It is a type of circuit breaker that operates in the air as an arc extinguishing medium, at a given atmospheric pressure.
- There are several types of air circuit breakers available in the market, and they are classified based on factors such as voltage level, installation location, external design, and breaking capacity.
- The main function of an ACB is to provide protection against overloads, short circuits, and earth faults.
- ACBs are commonly used in low voltage applications, such as in industrial and commercial power distribution systems.
- They are designed to handle large currents and are capable of interrupting high short-circuit currents.
- ACBs are typically installed in switchgear panels and are used to control and protect electrical equipment such as transformers, motors, and generators.
- They are also used in the main incoming section of an electrical distribution system to provide protection to the entire system.
- ACBs are reliable, easy to maintain, and have a long service life.
- They are available in different sizes and can be customized to meet specific requirements.




# Types of Wires for the notes of the Unit 5 - Electrical Installations in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING

1. **Solid Wire**: This type of wire is made of a single, solid conductor, usually copper or aluminum. It is commonly used in residential and commercial wiring for power and lighting circuits.

2. **Stranded Wire**: This type of wire is made of multiple, thin strands of conductor, usually copper, twisted together. It is more flexible than solid wire and is commonly used in applications where the wire needs to be moved or bent frequently.

3. **Braided Wire**: This type of wire is made of multiple, thin strands of conductor, usually copper, braided together. It is more flexible than solid wire and is commonly used in applications where the wire needs to be moved or bent frequently.

4. **Coaxial Cable**: This type of wire is made of a central conductor, surrounded by an insulating layer, a conductive shield, and an outer insulating layer. It is commonly used for transmitting high-frequency signals, such as television and radio signals.

5. **Twisted Pair Cable**: This type of wire is made of two insulated conductors twisted together. It is commonly used for transmitting data and voice signals in computer networks and telephone systems.

6. **Fiber Optic Cable**: This type of wire is made of thin strands of glass or plastic that transmit light signals. It is commonly used for transmitting high-speed data and voice signals over long distances.

7. **Ribbon Cable**: This type of wire is made of multiple, flat conductors arranged side by side in a flat, flexible ribbon. It is commonly used for connecting internal components in computers and other electronic devices.



# Cables and Bus-bars

Cables and bus-bars are used in electrical installations to distribute electrical power. They are essential components of any electrical system and are used to connect different electrical devices and equipment.

## Cables

Cables are insulated conductors that are used to transmit electrical power. They are available in different sizes and types, depending on the voltage level and current carrying capacity required.

- **Types of cables**: There are several types of cables, including single-core, multi-core, armored, and unarmored cables. The type of cable used depends on the application and the environment in which it will be installed.

- **Insulation**: The insulation of a cable is important to prevent electrical leakage and to protect against electric shock. Common insulation materials include PVC, XLPE, and EPR.

- **Sizing**: The size of a cable is determined by its current carrying capacity, which is dependent on the cross-sectional area of the conductor, the insulation material, and the ambient temperature.

## Bus-bars

Bus-bars are thick strips of copper or aluminum that are used to distribute electrical power. They are typically used in switchgear and distribution boards to connect different electrical devices.

- **Types of bus-bars**: Bus-bars are available in different shapes and sizes, including flat, tubular, and edge-wise. The shape and size of the bus-bar depends on the current carrying capacity required.

- **Insulation**: Bus-bars are often insulated to prevent accidental contact and to protect against electric shock. Common insulation materials include heat shrink tubing, epoxy, and PVC.

- **Sizing**: The size of a bus-bar is determined by its current carrying capacity, which is dependent on the cross-sectional area of the conductor, the material, and the ambient temperature.

In summary, cables and bus-bars are essential components of any electrical installation. They are used to distribute electrical power and are available in different types and sizes to meet the requirements of the application. Proper sizing and insulation are important to ensure safe and reliable operation.



# Fundamentals of Earthing and Lightning Protection

## Introduction
Earthing and lightning protection are important for everyone that uses electrical equipment. Earthing, Lighting Arrestors and Surge Protection Devices are the leading devices that protect devices against current shock.

## Lightning Protection System
A lightning protection system intercepts or diverts lightning and provides a certain path for conducting the surges safely to the ground by adequate down conductors to grounding electrodes. Thus, it helps prevent disastrous events like fires, injuries, and deaths. Lightning protection grounding helps protect structures and equipment from direct strikes. Overhead ground wires and surge arresters, connected to ground, can limit dangerous system overvoltages to safe values. Fundamentally, grounding an electronic system is the same as grounding any electrical system.

## Lightning Rod
In a lightning protection system, the lightning rod is a single component of the system. The lightning rod requires a connection to earth to give a building protection. Lightning rods come in many different forms, including hollow, solid, pointed or rounded. All lightning rods are made of conductive materials, such as copper and aluminum.

## Common Methods for Earthing and Lightning Protection
It’s a matter of providing an alternative path for the lightning current to flow to ground and ensure that:
1. Lightning current flowing in the lightning protection system (LPS) does not induce dangerous currents in any parallel metallic systems near the LPS.

## Conclusion
In conclusion, earthing and lightning protection are essential for the safety of electrical equipment and the prevention of disastrous events. It is important to have a fundamental knowledge about Earthing, Bonding, Lightning, and Surge Protection and to study the basic principles of earthing, types and components of earthing and surge protection systems. It is also important to stay up to date with the latest industry standards and procedures for earthing and lightning protection.



# Types of Batteries

Batteries can be broadly divided into two major types:

1. **Primary Cell / Primary battery**: These batteries are designed to be used once and then discarded. They cannot be recharged.

2. **Secondary Cell / Secondary battery**: These batteries are designed to be recharged and used multiple times.

Based on the application of the battery, they can be classified again. Some common types of batteries include:

- **Lead-acid batteries**: These batteries are commonly used in automobiles and for backup power supplies.

- **Nickel-cadmium batteries (Ni-Cd)**: These batteries are commonly used in portable electronic devices.

- **Nickel-metal hybrid batteries (Ni-MH)**: These batteries are commonly used in portable electronic devices and have a higher energy density than Ni-Cd batteries.

- **Lithium-ion batteries (Li-ion)**: These batteries are commonly used in portable electronic devices and have a higher energy density than Ni-MH batteries.

- **Alkaline batteries**: These batteries are commonly used in household devices and are designed to be used once and then discarded.

- **Zinc-carbon batteries**: These batteries are commonly used in household devices and are designed to be used once and then discarded.

- **Coin cell batteries**: These batteries are commonly used in small electronic devices such as watches and calculators.

- **Zinc-air cells**: These batteries are commonly used in hearing aids and other medical devices.

- **Sealed lead-acid batteries**: These batteries are commonly used in backup power supplies and other applications where maintenance-free operation is desired.

