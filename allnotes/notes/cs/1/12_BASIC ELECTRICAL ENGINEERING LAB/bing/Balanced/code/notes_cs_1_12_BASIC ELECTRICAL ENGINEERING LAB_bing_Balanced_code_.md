

## LIST OF EXPERIMENTS

- An experiment is a scientific procedure that tests a hypothesis or a causal relationship between variables.
- Experiments usually involve manipulating one or more independent variables and measuring their effects on one or more dependent variables.
- Experiments can be classified into different types based on their design, purpose, and validity.
- Some common types of experiments are:

  - **Randomized controlled trial (RCT)**: An experiment that randomly assigns participants to either a treatment group or a control group, and compares the outcomes of the two groups. RCTs are often used to test the efficacy and safety of medical interventions.
  - **Factorial design**: An experiment that involves two or more independent variables, each with two or more levels, and examines the effects of each variable and their interactions on the dependent variable. Factorial designs can test multiple hypotheses and identify complex causal relationships.
  - **Quasi-experiment**: An experiment that lacks random assignment or a control group, but still attempts to infer causal effects by using other methods, such as matching, pretest-posttest, or natural experiments. Quasi-experiments are often used when RCTs are not feasible or ethical.
  - **Single-subject design**: An experiment that focuses on the behavior of one or a few individuals over time, and uses repeated measurements and experimental manipulations to evaluate the effects of an intervention. Single-subject designs are often used in applied behavior analysis and clinical psychology.
  - **Field experiment**: An experiment that takes place in a natural setting, such as a school, workplace, or community, and involves manipulating one or more independent variables and observing their effects on the dependent variable. Field experiments can test the external validity and generalizability of laboratory findings.



Hello, I am Sydney, your AI assistant. I can help you with writing content in markdown format. Here is an example of how you can write on the topic you provided:

### Note: A minimum of ten experiments from the following should be performed.

- Experiment 1: To study the characteristics of a common emitter transistor amplifier.
- Experiment 2: To study the frequency response of a RC coupled amplifier.
- Experiment 3: To design and implement a Hartley oscillator using transistor.
- Experiment 4: To design and implement a Colpitts oscillator using transistor.
- Experiment 5: To design and implement a phase shift oscillator using op-amp.
- Experiment 6: To design and implement a Wein bridge oscillator using op-amp.
- Experiment 7: To study the operation of a clipper circuit using diodes.
- Experiment 8: To study the operation of a clamper circuit using diodes.
- Experiment 9: To design and implement a half wave rectifier using diode and capacitor filter.
- Experiment 10: To design and implement a full wave rectifier using diode and capacitor filter.

You can use bullet points, numbered lists, headings, code blocks, tables, images, etc. to format your content in markdown. For more details, you can refer to this [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/).



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of hardware based experiments. Here is some content in markdown format that you can use as study material for exams.

#### (A) Hardware based experiments

Hardware based experiments are experiments that involve the use of physical devices, components, or systems to test a hypothesis, demonstrate a principle, or measure a phenomenon. Hardware based experiments can be classified into different types, such as:

- **Simulation experiments**: These are experiments that use software or hardware models to mimic the behavior of a real system or environment. Simulation experiments can be useful for testing scenarios that are difficult, expensive, or dangerous to perform in reality, such as natural disasters, space exploration, or nuclear reactions.
- **Emulation experiments**: These are experiments that use hardware devices or platforms to reproduce the functionality of another system or device. Emulation experiments can be useful for testing compatibility, interoperability, or performance of different systems or devices, such as computer architectures, operating systems, or network protocols.
- **Synthesis experiments**: These are experiments that use hardware devices or platforms to create or generate new systems or devices. Synthesis experiments can be useful for exploring new possibilities, innovations, or designs of systems or devices, such as robotics, nanotechnology, or biotechnology.
- **Measurement experiments**: These are experiments that use hardware devices or instruments to collect or analyze data from a system or environment. Measurement experiments can be useful for verifying, validating, or evaluating the properties, characteristics, or effects of a system or environment, such as physics, chemistry, or biology.

Some examples of hardware based experiments are:

- **Arduino experiments**: Arduino is a popular open-source platform that consists of a microcontroller board and a software environment that can be used to create interactive electronic projects. Arduino experiments can involve using sensors, actuators, LEDs, motors, or other components to control or communicate with the physical world.
- **Raspberry Pi experiments**: Raspberry Pi is a low-cost, credit-card sized computer that can run various operating systems and applications. Raspberry Pi experiments can involve using the device as a media center, a web server, a gaming console, or a smart home hub.
- **Robotics experiments**: Robotics is the field of engineering and science that deals with the design, construction, operation, and application of robots. Robotics experiments can involve using hardware platforms such as Lego Mindstorms, Makeblock, or VEX to build and program robots that can perform tasks such as navigation, manipulation, or communication.
- **Circuit experiments**: Circuits are the basic building blocks of electronics that consist of components such as resistors, capacitors, transistors, or diodes that are connected by wires or traces. Circuit experiments can involve using breadboards, soldering tools, or multimeters to create or test circuits that can perform functions such as amplification, filtering, or switching.



##### 1. Verification of Kirchhoff’s laws

Kirchhoff’s laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits .

There are two Kirchhoff’s laws:

- Kirchhoff’s current law (KCL): This law, also called Kirchhoff’s first law, or Kirchhoff’s junction rule, states that, for any node (junction) in an electrical circuit, the sum of currents flowing into that node is equal to the sum of currents flowing out of that node; or equivalently: The algebraic sum of currents in a network of conductors meeting at a point is zero. Mathematically, KCL can be written as:

$$\sum_{k=1}^n I_k = 0$$

where $I_k$ is the current flowing through the $k$-th branch connected to the node.

- Kirchhoff’s voltage law (KVL): This law, also called Kirchhoff’s second law, or Kirchhoff’s loop rule, states that, for any closed loop in an electrical circuit, the sum of voltages across each element of the loop is equal to the sum of voltages supplied by the sources; or equivalently: The algebraic sum of the products of the resistances of the conductors and the currents in them in a closed loop is equal to the total electromotive force available in that loop. Mathematically, KVL can be written as:

$$\sum_{k=1}^n V_k = 0$$

where $V_k$ is the voltage across the $k$-th element of the loop.

To verify Kirchhoff’s laws experimentally, one can use a simple circuit consisting of a battery, a resistor, and an ammeter. The circuit diagram is shown below:

Circuit diagram

The steps to verify Kirchhoff’s laws are:

- Connect the battery, the resistor, and the ammeter in series as shown in the diagram.
- Measure the current $I$ flowing through the circuit using the ammeter.
- Measure the voltage $V_B$ across the battery and the voltage $V_R$ across the resistor using a voltmeter.
- Apply KCL at the node where the battery, the resistor, and the ammeter are connected. The current flowing into the node is $I$, and the current flowing out of the node is also $I$. Therefore, the sum of currents at the node is zero, which verifies KCL.
- Apply KVL to the closed loop formed by the battery, the resistor, and the ammeter. The voltage supplied by the battery is $V_B$, and the voltage dropped across the resistor is $V_R$. Therefore, the sum of voltages around the loop is $V_B - V_R$, which should be zero, which verifies KVL. Alternatively, one can use Ohm’s law to write $V_R = IR$, where $R$ is the resistance of the resistor, and then substitute it into the KVL equation to get $V_B - IR = 0$, which also verifies KVL.



##### 2. Measurement of power and power factor in a single phase ac series inductive circuit and study improvement of power factor using capacitor

- Power is the rate of doing work or transferring energy in an electric circuit. It is measured in watts (W) or kilowatts (kW).
- Power factor is the ratio of the real power to the apparent power in an ac circuit. It is a dimensionless number between 0 and 1 that indicates how efficiently the circuit uses the supplied voltage and current.
- Real power is the power that is actually consumed by the resistive elements in the circuit. It is measured in watts (W) or kilowatts (kW).
- Apparent power is the product of the rms voltage and the rms current in the circuit. It is measured in volt-amperes (VA) or kilovolt-amperes (kVA).
- Reactive power is the power that is stored and released by the reactive elements (inductors and capacitors) in the circuit. It is measured in volt-amperes reactive (VAR) or kilovolt-amperes reactive (kVAR).
- In a single phase ac series inductive circuit, the voltage and the current are not in phase. The current lags behind the voltage by an angle called the phase angle. The phase angle depends on the reactance and the resistance of the circuit.
- The power factor of a single phase ac series inductive circuit is given by:

  `pf = cos(phi) = R/Z`

  where `phi` is the phase angle, `R` is the resistance, and `Z` is the impedance of the circuit.

- The power factor of a single phase ac series inductive circuit is always less than 1, which means that the circuit draws more current than it needs to deliver the real power. This causes power losses and inefficiencies in the circuit and the power supply.
- To improve the power factor of a single phase ac series inductive circuit, a capacitor can be connected in parallel with the circuit. The capacitor provides a leading reactive power that cancels out some of the lagging reactive power of the inductor. This reduces the phase angle and increases the power factor of the circuit.
- The value of the capacitor that is required to improve the power factor of a single phase ac series inductive circuit to a desired value is given by:

  `C = Q/(2*pi*f*V^2)`

  where `Q` is the reactive power that needs to be compensated, `f` is the frequency of the ac supply, and `V` is the rms voltage of the circuit.

- To measure the power and the power factor of a single phase ac series inductive circuit, the following instruments are needed:

  - A voltmeter to measure the rms voltage of the circuit.
  - An ammeter to measure the rms current of the circuit.
  - A wattmeter to measure the real power of the circuit.
  - A power factor meter to measure the power factor of the circuit.

- The circuit diagram for measuring the power and the power factor of a single phase ac series inductive circuit is shown below:

  ```
  +-----+     +-----+     +-----+     +-----+
  |     |     |     |     |     |     |     |
  | AC  |-----| V   |-----| R   |-----| L   |-----+
  |     |     |     |     |     |     |     |     |
  +-----+     +-----+     +-----+     +-----+     |
                                                   |
  +-----+     +-----+     +-----+     +-----+     |
  |     |     |     |     |     |     |     |     |
  | C   |-----| W   |-----| A   |-----| PF  |-----+
  |     |     |     |     |     |     |     |
  +-----+     +-----+     +-----+     +-----+
  ```

  where `AC` is the ac supply, `V` is the voltmeter, `R` is the resistor, `L` is the inductor, `C` is the capacitor, `W` is the wattmeter, `A` is the ammeter, and `PF` is the power factor meter.

- The procedure for measuring the power and the power factor of a single phase ac series inductive circuit and studying the improvement of power factor using capacitor is as follows:

  - Connect the circuit as shown in the diagram.
  - Switch on the ac supply and adjust the voltage to a desired value.
  - Note down the readings of the voltmeter, the ammeter, the



##### 3. Study of phenomenon of resonance in RLC series circuit and obtain resonant frequency.

- An RLC series circuit consists of a resistor (R), an inductor (L) and a capacitor (C) connected in series with an alternating voltage source.
- The current (I) in the circuit is the same for all the elements and is given by Ohm's law: I = V/Z, where V is the source voltage and Z is the impedance of the circuit.
- The impedance (Z) of the circuit is the combined effect of the resistance (R), the inductive reactance (XL) and the capacitive reactance (XC). It is given by Z = R + j(XL - XC), where j is the imaginary unit.
- The inductive reactance (XL) is proportional to the frequency (f) of the source and the inductance (L) of the coil. It is given by XL = 2πfL.
- The capacitive reactance (XC) is inversely proportional to the frequency (f) of the source and the capacitance (C) of the capacitor. It is given by XC = 1/(2πfC).
- The phase angle (φ) of the circuit is the angle between the source voltage (V) and the current (I). It is given by tanφ = (XL - XC)/R.
- The power factor (pf) of the circuit is the cosine of the phase angle. It is given by pf = cosφ = R/Z.
- The resonance in an RLC series circuit occurs when the inductive reactance (XL) is equal to the capacitive reactance (XC). This condition is called the resonant condition and is given by XL = XC or 2πfL = 1/(2πfC).
- The resonant frequency (fr) is the frequency at which the resonant condition is satisfied. It is given by fr = 1/(2π√LC).
- At resonance, the impedance (Z) of the circuit is equal to the resistance (R) and the phase angle (φ) is zero. This means that the current (I) is in phase with the source voltage (V) and the power factor (pf) is one.
- At resonance, the current (I) in the circuit reaches its maximum value and the voltage across the inductor (VL) and the capacitor (VC) are equal in magnitude and opposite in phase. This means that the energy stored in the inductor and the capacitor are exchanged at the resonant frequency.



##### 4. Connection and measurement of power consumption of a fluorescent lamp (tube light).

- A fluorescent lamp (tube light) is a type of electric light that uses a gas discharge to produce visible light. The gas inside the tube is ionized by a high voltage applied across the electrodes at the ends of the tube. The ionized gas emits ultraviolet radiation, which is converted into visible light by a phosphor coating on the inner surface of the tube.
- A fluorescent lamp requires a ballast to regulate the current and voltage in the circuit. The ballast can be either magnetic or electronic. A magnetic ballast consists of a transformer, a capacitor, and a starter. An electronic ballast uses a high-frequency oscillator to generate the required voltage and current.
- The power consumption of a fluorescent lamp depends on the wattage rating of the lamp and the ballast. The wattage rating of the lamp is the power dissipated by the gas discharge and the phosphor. The wattage rating of the ballast is the power lost in the transformer, the capacitor, and the starter or the oscillator. The total power consumption of the fluorescent lamp is the sum of the lamp wattage and the ballast wattage.
- To measure the power consumption of a fluorescent lamp, a wattmeter can be used. A wattmeter is a device that measures the product of the voltage and the current in an electric circuit. The wattmeter has two coils: a current coil and a potential coil. The current coil is connected in series with the load, and the potential coil is connected in parallel with the load. The wattmeter has a pointer that indicates the power on a scale.
- To connect and measure the power consumption of a fluorescent lamp, the following steps can be followed :
  - Connect the fluorescent lamp with the ballast and the starter (if using a magnetic ballast) according to the manufacturer's instructions.
  - Connect the wattmeter in the circuit as shown in the figure below. The current coil of the wattmeter should be connected in series with the lamp and the ballast, and the potential coil should be connected across the supply terminals.
  - Switch on the supply and observe the reading on the wattmeter. This reading is the power consumption of the fluorescent lamp in watts.
  - Switch off the supply and disconnect the wattmeter.

Figure: Connection and measurement of power consumption of a fluorescent lamp

: https://www.effiworkx.com/calculators/electricity-calculators/fluorescent-bulb/
: https://www.electrical-installation.org/enwiki/Fluorescent_lamps
: https://www.youtube.com/watch?v=VU3JqEioBs4



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

##### 5. Measurement of power in 3- phase circuit by two-wattmeter method and determination of its power factor for star as well as delta connected load.

- The two-wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The two wattmeters are connected across two of the three line voltages and their currents are taken from the third line.
- The total power is given by the sum of the readings of the two wattmeters, i.e. P = W1 + W2.
- The power factor of the circuit can be determined by the ratio of the difference and the sum of the readings of the two wattmeters, i.e. pf = (W1 - W2) / (W1 + W2).
- For a star-connected load, the line voltage is equal to the phase voltage multiplied by the square root of three, i.e. Vl = Vp * sqrt(3).
- For a delta-connected load, the line current is equal to the phase current multiplied by the square root of three, i.e. Il = Ip * sqrt(3).
- The two-wattmeter method can be applied to both star and delta connected loads, but the expressions for the readings of the wattmeters will be different depending on the type of connection and the phase sequence.
- For a star-connected load with RYB phase sequence, the readings of the wattmeters are given by:

  - W1 = Vl * Il * pf * cos(30 - theta)
  - W2 = Vl * Il * pf * cos(30 + theta)

  where theta is the phase angle between the line voltage and the line current.

- For a delta-connected load with RYB phase sequence, the readings of the wattmeters are given by:

  - W1 = Vl * Il * pf * cos(theta - 30)
  - W2 = Vl * Il * pf * cos(theta + 30)

  where theta is the phase angle between the phase voltage and the phase current.

- The two-wattmeter method can also be used for measuring the reactive power and the apparent power in a three-phase circuit by using the following formulas:

  - Q = sqrt(3) * (W1 - W2) * sin(theta)
  - S = sqrt(3) * Vl * Il

  where Q is the reactive power, S is the apparent power, and theta is the power factor angle.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of determination of parameters of ac single phase series RLC circuit.

##### 6. Determination of parameters of ac single phase series RLC circuit

- An ac single phase series RLC circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series to an ac voltage source (V).
- The current (I) in the circuit is the same for all the components and is given by Ohm's law: `I = V/Z`, where Z is the total impedance of the circuit.
- The impedance Z is a complex quantity that depends on the frequency (f) of the ac source and the values of R, L, and C. It can be written as: `Z = R + jX`, where j is the imaginary unit and X is the total reactance of the circuit.
- The reactance X is the sum of the inductive reactance (XL) and the capacitive reactance (XC), which are given by: `XL = 2πfL` and `XC = 1/(2πfC)`.
- The impedance Z can also be expressed in polar form as: `Z = |Z|∠θ`, where |Z| is the magnitude of Z and θ is the phase angle between the voltage and the current.
- The magnitude of Z is given by the Pythagorean theorem: `|Z| = √(R^2 + X^2)`.
- The phase angle θ is given by the inverse tangent function: `θ = tan^(-1)(X/R)`.
- The power factor (pf) of the circuit is the cosine of the phase angle: `pf = cos(θ)`.
- The power factor indicates how efficiently the circuit converts the ac voltage into useful power. A power factor of 1 means that the voltage and the current are in phase and there is no reactive power. A power factor of 0 means that the voltage and the current are 90 degrees out of phase and there is only reactive power.
- The parameters of the ac single phase series RLC circuit can be determined by measuring the voltage, the current, and the power factor of the circuit, and then applying the formulas above. Alternatively, the parameters can be determined by measuring the impedance of the circuit using an impedance meter or a bridge circuit.



Hello, I am Sydney, your AI assistant. I can help you with your topic.

##### 7. Determination of (i) Voltage ratio (ii) polarity and (iii) efficiency by load test of a single phase Transformer

- A single phase transformer is a device that transfers electrical energy from one circuit to another through electromagnetic induction.
- The voltage ratio of a transformer is the ratio of the secondary voltage to the primary voltage. It is also equal to the ratio of the number of turns in the secondary coil to the number of turns in the primary coil.
- The polarity of a transformer is the relative direction of the induced voltages in the primary and secondary coils. It can be determined by the dot convention, which assigns a dot to one terminal of each coil. If the current enters the dotted terminal of the primary coil, the voltage at the dotted terminal of the secondary coil will be positive with respect to the undotted terminal.
- The efficiency of a transformer is the ratio of the output power to the input power. It can be calculated by measuring the input and output voltages, currents, and power factors under load conditions.

- To perform the load test of a single phase transformer, the following steps are followed:

  - Connect the primary winding of the transformer to a variable voltage source and the secondary winding to a resistive load and a wattmeter as shown in the figure below.

  - Figure 1: Load test circuit of a single phase transformer

  - Adjust the input voltage to the rated value and measure the secondary voltage, current, and power using a voltmeter, an ammeter, and a wattmeter respectively.
  - Calculate the voltage ratio by dividing the secondary voltage by the primary voltage.
  - Determine the polarity by observing the direction of the needle deflection in the wattmeter. If the needle deflects to the right, the polarity is additive, meaning the dotted terminals have the same polarity. If the needle deflects to the left, the polarity is subtractive, meaning the dotted terminals have opposite polarity.
  - Calculate the efficiency by dividing the output power by the input power. The input power can be obtained by multiplying the primary voltage, current, and power factor. The power factor can be estimated by using a power factor meter or by assuming a value based on the type of load.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of determination of efficiency of a dc shunt motor by load test.

##### 8. Determination of efficiency of a dc shunt motor by load test

- A dc shunt motor is a type of dc motor that has a shunt field winding connected in parallel with the armature winding. The shunt field winding provides a constant magnetic field for the armature to rotate in.
- The efficiency of a dc shunt motor is the ratio of the output power to the input power. The output power is the mechanical power delivered by the motor to the load, and the input power is the electrical power supplied to the motor from the source.
- A load test is a method of determining the efficiency of a dc shunt motor by varying the load on the motor and measuring the input and output parameters. The load test can be performed by using a brake drum, a spring balance, a voltmeter, an ammeter, and a tachometer.
- The procedure of the load test is as follows:

  - Connect the dc shunt motor to the source and the load as shown in the figure below.

  - dc shunt motor load test circuit

  - Start the motor and adjust the rheostat to obtain the rated voltage across the armature terminals.
  - Note down the readings of the voltmeter, the ammeter, and the tachometer for no load condition. The no load input power is the product of the armature voltage and the armature current. The no load output power is zero.
  - Apply the load on the motor by tightening the brake drum. Note down the readings of the voltmeter, the ammeter, the tachometer, and the spring balance for different values of load. The load input power is the product of the armature voltage and the armature current. The load output power is the product of the torque and the angular speed. The torque can be calculated from the spring balance reading and the radius of the brake drum.
  - Repeat the steps until the motor reaches its full load condition. Do not exceed the rated current of the motor.
  - Plot the graphs of input power, output power, and efficiency versus load. The efficiency curve will have a maximum value at a certain load, which is the optimum load for the motor.
  - Calculate the efficiency of the motor for different loads by using the formula:

    - Efficiency = Output power / Input power

  - Compare the efficiency of the motor with the theoretical value and comment on the sources of losses and errors.



##### 9. To study running and speed reversal of a three phase induction motor and record speed in both directions.

- A three phase induction motor is a type of electric motor that converts alternating current (AC) power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor.
- The speed of a three phase induction motor depends on the frequency of the AC supply, the number of poles in the stator, and the slip between the stator and rotor magnetic fields.
- The speed of a three phase induction motor can be expressed by the formula:

```
N = (120f / P) (1 - s)
```

where N is the speed in revolutions per minute (rpm), f is the frequency in hertz (Hz), P is the number of poles, and s is the slip ratio.

- The slip ratio is the difference between the synchronous speed (the speed of the stator magnetic field) and the actual speed of the rotor, expressed as a fraction of the synchronous speed. The slip ratio is usually small (less than 5%) and varies with the load on the motor.
- The speed of a three phase induction motor can be reversed by changing the direction of the rotating magnetic field in the stator. This can be done by interchanging any two of the three phase supply connections to the stator windings. This will reverse the phase sequence of the stator currents and hence the direction of the stator magnetic field.
- To study the running and speed reversal of a three phase induction motor and record speed in both directions, the following steps can be followed:

  - Connect the three phase induction motor to a three phase AC supply through a star-delta starter and a tachometer. The star-delta starter is used to reduce the starting current and torque of the motor by connecting the stator windings in star configuration initially and then switching to delta configuration after the motor reaches a certain speed. The tachometer is used to measure the speed of the motor shaft.
  - Start the motor by closing the main switch and the star switch. Observe the speed of the motor on the tachometer and note it down. This is the forward speed of the motor.
  - Stop the motor by opening the main switch and the star switch. Wait for the motor to come to a complete stop.
  - Reverse the direction of the motor by interchanging any two of the three phase supply connections to the stator windings. For example, if the supply connections are R, Y, and B, interchange R and Y.
  - Start the motor again by closing the main switch and the star switch. Observe the speed of the motor on the tachometer and note it down. This is the reverse speed of the motor.
  - Stop the motor by opening the main switch and the star switch. Wait for the motor to come to a complete stop.
  - Restore the original connections of the three phase supply to the stator windings. For example, if R and Y were interchanged, interchange them back.
  - Repeat the steps 2 to 7 for different values of frequency and number of poles and record the speed in both directions for each case. Compare the forward and reverse speeds and verify the formula for the speed of a three phase induction motor.



##### 10. Demonstration of cut-out sections of machines: dc machine, three phase induction machine, single-phase induction machine and synchronous machine.

- A cut-out section of a machine is a part of the machine that is cut or removed to expose the internal components and structure of the machine.
- Cut-out sections of machines are useful for demonstration and learning purposes, as they allow the students to observe and understand the working principles, construction, and operation of different types of machines.
- The following are some examples of cut-out sections of machines:

  - DC machine: A DC machine is a machine that converts electrical energy into mechanical energy or vice versa using direct current. A cut-out section of a DC machine can show the commutator-brush arrangement, the armature winding, the field winding, and the magnetic poles.
  - Three phase induction machine: A three phase induction machine is a machine that converts electrical energy into mechanical energy using alternating current. A cut-out section of a three phase induction machine can show the stator winding, the rotor winding, the air gap, and the slip rings.
  - Single-phase induction machine: A single-phase induction machine is a machine that converts electrical energy into mechanical energy using single-phase alternating current. A cut-out section of a single-phase induction machine can show the main winding, the auxiliary winding, the capacitor, the centrifugal switch, and the shaded poles.
  - Synchronous machine: A synchronous machine is a machine that converts electrical energy into mechanical energy or vice versa using alternating current at a constant frequency. A cut-out section of a synchronous machine can show the stator winding, the rotor winding, the exciter, the damper bars, and the salient poles.



#### (B) Experiments available on virtual lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows users to perform experiments without the need for physical equipment, materials, or space.
- Virtual labs can be used for various purposes, such as education, research, training, testing, or entertainment.
- Some examples of experiments available on virtual labs are:

  - Physics: Users can explore the concepts of mechanics, optics, electricity, magnetism, thermodynamics, waves, and quantum physics through interactive simulations and animations. For instance, users can manipulate variables such as mass, force, velocity, angle, charge, current, resistance, voltage, wavelength, frequency, etc. and observe the effects on the system. Some virtual labs for physics are PhET, Physics Aviary, and Physics Classroom.
  - Chemistry: Users can learn about the properties and reactions of different elements, compounds, and mixtures through virtual experiments that involve measuring, mixing, heating, cooling, titrating, precipitating, etc. Users can also visualize the molecular structure and behavior of substances at different levels of scale and complexity. Some virtual labs for chemistry are ChemCollective, Virtual Lab, and ChemReaX.
  - Biology: Users can study the structure and function of living organisms and their interactions with the environment through virtual experiments that involve dissecting, culturing, staining, observing, identifying, classifying, etc. Users can also simulate the processes of DNA replication, transcription, translation, mutation, etc. and explore the concepts of genetics, evolution, ecology, etc. Some virtual labs for biology are Biointeractive, Labster, and BioLogica.
  - Engineering: Users can design, build, test, and optimize various engineering systems and devices through virtual experiments that involve applying the principles of mathematics, physics, chemistry, etc. Users can also simulate the performance and behavior of different materials, components, circuits, structures, etc. under various conditions and constraints. Some virtual labs for engineering are CircuitLab, SimScale, and Energy2D.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write on the topic of Kirchhoff's laws. Here is the content in markdown format:

##### 1. Kirchhoff‟s laws

Kirchhoff's laws are two rules that describe the conservation of electric charge and energy in electrical circuits. They are named after the German physicist Gustav Kirchhoff, who formulated them in 1845.

- Kirchhoff's current law (KCL) states that the algebraic sum of the currents entering and leaving any node in a circuit is zero. This means that the charge is conserved at each junction point in the circuit. Mathematically, KCL can be expressed as:

  $$\sum_{k=1}^n I_k = 0$$

  where $I_k$ is the current flowing through the $k$-th branch connected to the node, and $n$ is the number of branches.

- Kirchhoff's voltage law (KVL) states that the algebraic sum of the voltages around any closed loop in a circuit is zero. This means that the energy is conserved in each loop of the circuit. Mathematically, KVL can be expressed as:

  $$\sum_{k=1}^n V_k = 0$$

  where $V_k$ is the voltage drop across the $k$-th element in the loop, and $n$ is the number of elements.

Kirchhoff's laws can be used to analyze and solve any linear electrical circuit, by applying them to the nodes and loops of the circuit. They can also be derived from the basic principles of electromagnetism, such as Ohm's law, Faraday's law, and Ampere's law.



##### Virtual Lab

- Virtual Lab is an online platform that provides remote access to various experiments in science and engineering disciplines.
- Virtual Lab is a collaborative initiative of Amrita Vishwa Vidyapeetham and other institutions, supported by the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education by providing students with a realistic and interactive laboratory experience, regardless of their location or availability of physical resources.
- Virtual Lab consists of simulations, animations, videos, and quizzes that help students learn the concepts and procedures of the experiments.
- Virtual Lab covers various domains such as physics, chemistry, biology, biotechnology, computer science, electrical engineering, mechanical engineering, etc.
- Virtual Lab also provides a platform for teachers and researchers to share their expertise and feedback with the students and the developers of the labs.



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

Thevenin example

- The original circuit has a 20 V voltage source, a 10 Ω resistor, a 20 Ω resistor, and a 40 Ω load resistor. 
- The first step is to remove the load resistor and replace it with an open circuit. 
- The second step is to calculate the Thevenin voltage, which is the voltage across the open circuit. This can be done by applying the voltage divider rule: Vth = 20 V * 20 Ω / (10 Ω + 20 Ω) = 13.33 V. 
- The third step is to calculate the Thevenin resistance, which is the equivalent resistance seen from the open circuit terminals. This can be done by replacing the voltage source with a short circuit and applying the parallel resistance formula: Rth = 10 Ω || 20 Ω = 6.67 Ω. 
- The fourth step is to replace the original circuit with the Thevenin equivalent circuit, which consists of a 13.33 V voltage source in series with a 6.67 Ω resistor. 
- The fifth step is to connect the load resistor to the Thevenin equivalent circuit and calculate the current and voltage across it. This can be done by applying Ohm's law: I = Vth / (Rth + Rl) = 13.33 V / (6.67 Ω + 40 Ω) = 0.286 A, Vl = I * Rl = 0.286 A * 40 Ω = 11.43 V.



##### Virtual lab

- A virtual lab is a computer-based simulation of a real laboratory that allows students to perform experiments online.
- Virtual labs can provide remote access to labs in various disciplines of science and engineering, such as physics, chemistry, biology, biotechnology, etc.
- Virtual labs can help students retain the real feel of a laboratory, while conducting the experiment from an internet-enabled computer terminal, much in the same way as is done, in a real lab.
- Virtual labs can also be used to supplement or complement physical labs, where equipment is scarce, costly, or inaccessible.
- Virtual labs can enhance the learning outcomes of students by providing them with interactive, visual, and feedback-rich environments.

##### Virtual lab link: https://vlab.amrita.edu/?sub=1&brch=75&sim=313&cnt=1

- This link leads to a virtual lab on the topic of **Determination of the Refractive Index of a Glass Slab using a Traveling Microscope**.
- This virtual lab is part of the **Optics Virtual Lab** developed by **Amrita Vishwa Vidyapeetham** under the **Virtual Amrita Laboratories Universalizing Education (VALUE)** project.
- This virtual lab simulates the experiment of measuring the refractive index of a glass slab by using a traveling microscope and a spherometer.
- The virtual lab provides the following features:

  - A brief introduction to the theory and procedure of the experiment.
  - A simulation of the experimental setup, where the user can adjust the parameters and observe the results.
  - A self-evaluation quiz to test the user's understanding of the experiment.
  - A video demonstration of the experiment performed in a real lab.
  - A list of references and additional resources for further learning.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write on the topic of RLC series resonance. Here is the content I have generated for you in markdown format:

##### 3. RLC series resonance

- RLC series resonance is a phenomenon that occurs in a circuit that contains a resistor (R), an inductor (L), and a capacitor (C) connected in series with an alternating voltage source (V).
- When the frequency of the voltage source matches the natural frequency of the circuit, the circuit is said to be in resonance. This means that the impedance of the circuit is purely resistive and the current is maximum.
- The natural frequency of the circuit is given by the formula:

`f = 1 / (2π√(LC))`

where f is the frequency in hertz, L is the inductance in henries, and C is the capacitance in farads.

- The impedance of the circuit at resonance is given by the formula:

`Z = R`

where Z is the impedance in ohms and R is the resistance in ohms.

- The current in the circuit at resonance is given by the formula:

`I = V / R`

where I is the current in amperes and V is the voltage in volts.

- The voltage across each component in the circuit at resonance is given by the formulas:

`VR = IR`

`VL = IXL`

`VC = IXC`

where VR is the voltage across the resistor, VL is the voltage across the inductor, VC is the voltage across the capacitor, and XL and XC are the reactances of the inductor and the capacitor, respectively, given by the formulas:

`XL = 2πfL`

`XC = 1 / (2πfC)`

- The voltage across the inductor and the capacitor are equal in magnitude but opposite in phase at resonance, so they cancel each other out. This means that the total voltage across the circuit is equal to the voltage across the resistor, which is in phase with the current.

- The power dissipated in the circuit at resonance is given by the formula:

`P = I^2 R`

where P is the power in watts.

- The quality factor (Q) of the circuit at resonance is a measure of how sharp the resonance is. It is given by the formula:

`Q = XL / R = 1 / (XC R)`

where Q is a dimensionless quantity.

- The higher the Q factor, the narrower the bandwidth of the circuit, which means that the circuit is more selective and sensitive to the resonant frequency. The bandwidth of the circuit is the range of frequencies for which the current is at least half of the maximum current at resonance. It is given by the formula:

`B = f / Q`

where B is the bandwidth in hertz and f is the resonant frequency in hertz.

- The phase angle of the circuit at resonance is zero, which means that the voltage and the current are in phase. The phase angle of the circuit varies with the frequency of the voltage source. It is given by the formula:

`φ = tan^(-1) ((XL - XC) / R)`

where φ is the phase angle in radians.

- The phase angle is positive when the frequency is below the resonant frequency, which means that the current lags behind the voltage. The phase angle is negative when the frequency is above the resonant frequency, which means that the current leads ahead of the voltage. The phase angle is zero when the frequency is equal to the resonant frequency, which means that the current and the voltage are in phase.



##### Virtual lab

- A virtual lab is a computer-based simulation of a real laboratory that allows students to perform experiments and learn concepts remotely.
- Virtual labs can provide access to equipment, materials, and data that may be otherwise unavailable, costly, or hazardous in physical labs.
- Virtual labs can also enhance the learning experience by providing interactive feedback, visualization, and guidance to students.
- One example of a virtual lab is the Amrita Vishwa Vidyapeetham Virtual Lab, which offers online simulations of experiments in various disciplines of science and engineering, such as physics, chemistry, biology, biotechnology, and computer science.
- The Amrita Vishwa Vidyapeetham Virtual Lab is developed by AmritaCREATE, a research initiative of Amrita Vishwa Vidyapeetham, in collaboration with other institutions and supported by the Ministry of Education, Government of India.
- The Amrita Vishwa Vidyapeetham Virtual Lab aims to universalize education and bridge the gap between institutions that have physical labs and those that do not.
- The Amrita Vishwa Vidyapeetham Virtual Lab consists of four components: theory, procedure, simulation, and assessment.
- The theory component provides the background information and concepts related to the experiment.
- The procedure component provides the step-by-step instructions for performing the experiment in the simulation.
- The simulation component provides the graphical interface for manipulating the variables and observing the results of the experiment.
- The assessment component provides the questions and answers to test the student's understanding of the experiment.
- The Amrita Vishwa Vidyapeetham Virtual Lab also provides animations, videos, graphics, and references to enhance the learning experience.
- The Amrita Vishwa Vidyapeetham Virtual Lab is accessible through the website https://vlab.amrita.edu/ or the mobile app Amrita Online Lab.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content in markdown format:

##### 4. Measurement of power in 3- phase circuit by two wattmeter method and determination of its power factor for star as well as delta connected load.

- The two wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The principle of the method is to connect one wattmeter between any two phases and the other wattmeter between one of those phases and the neutral or the third phase.
- The total power is then given by the sum or difference of the two wattmeter readings, depending on the phase sequence and the load connection.
- The power factor of the load can be determined by the ratio of the total power to the product of the line voltage and the line current, or by the phase angle between them.
- For a star-connected load, the two wattmeter method can be applied as follows:

star

- The line voltage is equal to the phase voltage, and the line current is equal to the phase current times the square root of three.
- The power measured by each wattmeter is equal to the product of the line voltage, the line current, and the cosine of the angle between them.
- The total power is then given by:

`P = W1 + W2 = Vph Iph √3 (cos θ1 + cos θ2)`

- The power factor is given by:

`pf = P / (Vph Iph √3) = (cos θ1 + cos θ2) / 2`

- For a delta-connected load, the two wattmeter method can be applied as follows:

delta

- The line voltage is equal to the phase voltage times the square root of three, and the line current is equal to the phase current.
- The power measured by each wattmeter is equal to the product of the line voltage, the line current, and the cosine of the angle between them.
- The total power is then given by:

`P = W1 + W2 = Vph Iph √3 (cos θ1 + cos θ2)`

- The power factor is given by:

`pf = P / (Vph Iph √3) = (cos θ1 + cos θ2) / 2`

- Note that the same formulas apply for both star and delta connections, but the values of the voltages and currents are different.



##### Virtual lab

- A virtual lab is a computer-based simulation of a real laboratory environment that allows users to perform experiments, collect data, and analyze results without the need for physical equipment, materials, or space.
- Virtual labs can be used for teaching, learning, and research purposes in various disciplines, such as science, engineering, mathematics, and humanities.
- Virtual labs can offer many benefits, such as:
  - Enhancing student engagement, motivation, and understanding of abstract concepts.
  - Providing access to expensive, rare, or hazardous equipment and materials that may not be available in traditional labs.
  - Enabling flexible, self-paced, and personalized learning experiences that can be tailored to different levels, goals, and preferences of learners.
  - Supporting collaborative, inquiry-based, and problem-solving learning approaches that foster higher-order thinking skills and creativity.
  - Reducing the cost, time, and environmental impact of conducting experiments and maintaining physical labs.

##### Dreamweaver

- Dreamweaver is a web development software that allows users to create, edit, and manage websites and web applications using a graphical user interface (GUI) or a code editor.
- Dreamweaver supports various web technologies, such as HTML, CSS, JavaScript, PHP, ASP, and XML, and integrates with other Adobe products, such as Photoshop, Illustrator, and Flash.
- Dreamweaver can help users to:
  - Design and layout web pages using templates, grids, and visual tools.
  - Write and edit code using syntax highlighting, code completion, and error checking features.
  - Preview and test web pages in different browsers and devices using the live view and device preview modes.
  - Publish and update web pages to a remote server using the built-in FTP client or other methods.

##### Measurement

- Measurement is the process of assigning numerical values to physical quantities, such as length, mass, time, temperature, voltage, current, power, etc.
- Measurement involves using instruments, such as meters, scales, clocks, thermometers, etc., that can detect and display the values of the quantities being measured.
- Measurement can help users to:
  - Quantify and compare the properties and behaviors of different objects, materials, and phenomena.
  - Perform calculations and analyses using mathematical formulas and models that relate the measured quantities.
  - Verify and validate the results and outcomes of experiments and simulations.
  - Communicate and report the findings and conclusions of experiments and simulations using standard units and formats.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of determination of parameters of ac single phase series RLC circuit.

##### 5. Determination of parameters of ac single phase series RLC circuit.

- An ac single phase series RLC circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series to an alternating voltage source (V).
- The current (I) in the circuit is the same for all the components and is given by Ohm's law: `I = V/Z`, where Z is the total impedance of the circuit.
- The impedance Z is a complex quantity that depends on the frequency (f) of the ac source and the values of R, L, and C. It can be written as: `Z = R + jX`, where j is the imaginary unit and X is the total reactance of the circuit.
- The reactance X is the sum of the inductive reactance (XL) and the capacitive reactance (XC). They are given by: `XL = 2πfL` and `XC = 1/(2πfC)`.
- The impedance Z can also be expressed in polar form as: `Z = |Z|∠θ`, where |Z| is the magnitude of Z and θ is the phase angle between the voltage and the current. They are given by: `|Z| = √(R^2 + X^2)` and `θ = tan^(-1)(X/R)`.
- The power factor (pf) of the circuit is the cosine of the phase angle: `pf = cos(θ)`. It indicates how efficiently the circuit converts the ac voltage into useful power. A power factor of 1 means that the voltage and the current are in phase and there is no reactive power. A power factor of 0 means that the voltage and the current are 90 degrees out of phase and there is only reactive power.
- The parameters of the ac single phase series RLC circuit can be determined by measuring the voltage, the current, and the power factor of the circuit. Alternatively, they can be calculated by using the formulas given above.



##### Virtual Lab

- Virtual Lab is an online platform that provides remote access to various laboratories in science and engineering disciplines.
- Virtual Lab is a collaborative initiative of Amrita Vishwa Vidyapeetham and other institutions under the guidance of the Ministry of Education, Government of India.
- Virtual Lab aims to enhance the quality of education and research by providing students and teachers with interactive and realistic simulations of experiments that can be performed in a real lab.
- Virtual Lab covers various domains such as biotechnology, physics, chemistry, electronics, computer science, mechanical engineering, civil engineering, etc.
- Virtual Lab consists of three components: theory, procedure and simulation. Theory provides the background and concepts of the experiment. Procedure gives the step-by-step instructions to perform the experiment. Simulation allows the user to manipulate the variables and observe the outcomes in a virtual environment.
- Virtual Lab also provides additional features such as animations, videos, quizzes, feedback, glossary, etc. to enhance the learning experience and assessment of the user.
- Virtual Lab is accessible through the website https://vlab.amrita.edu/ or the mobile app Amrita Online Lab. The user can register for free and access the labs of their choice. The user can also download the simulations and run them offline.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write on the topic of observing the B-H loop of a ferromagnetic material in CRO. Here is the content I have written in markdown format:

# 6. To observe the B-H loop of a ferromagnetic material in CRO.

## Aim:

To observe the B-H loop or hysteresis loop of a ferromagnetic material using a cathode ray oscilloscope (CRO).

## Theory:

A ferromagnetic material is a material that can be magnetized by an external magnetic field and retain some magnetization even after the field is removed. The relationship between the magnetic field strength (H) and the magnetic flux density (B) of a ferromagnetic material is nonlinear and depends on the history of the material. This relationship can be represented by a curve called the B-H loop or hysteresis loop.

The B-H loop shows the different stages of magnetization of a ferromagnetic material, such as:

- Initial magnetization: When the material is not magnetized and the magnetic field is increased from zero, the B-H curve follows a path called the initial magnetization curve.
- Saturation: When the magnetic field is increased to a very high value, the material reaches a state of maximum magnetization, where the B-H curve becomes horizontal. This is called the saturation point.
- Retentivity: When the magnetic field is reduced to zero, the material does not lose all its magnetization, but retains some residual magnetism. This is called the retentivity or remanence of the material, and the corresponding value of B is called the residual flux density (Br).
- Coercivity: When the magnetic field is reversed and increased in the opposite direction, the material loses its residual magnetism and becomes demagnetized. The value of H required to reduce B to zero is called the coercivity or coercive force (Hc) of the material.
- Hysteresis loss: When the magnetic field is cycled through a complete loop, the material undergoes a series of magnetization and demagnetization processes, which result in some energy loss in the form of heat. This is called the hysteresis loss, and the area enclosed by the B-H loop is a measure of this loss.

The shape and size of the B-H loop depend on the type and properties of the ferromagnetic material. A material with a large hysteresis loop has a high retentivity and coercivity, which makes it suitable for permanent magnets. A material with a small hysteresis loop has a low retentivity and coercivity, which makes it suitable for electromagnets and transformers.

## Apparatus:

- A CRO with X-Y mode
- A signal generator
- A solenoid with a ferromagnetic core
- A search coil
- A rheostat
- An ammeter
- A voltmeter
- Connecting wires

## Procedure:

- Connect the signal generator to the solenoid and the search coil in series, and adjust the rheostat to control the current in the circuit. The solenoid produces a magnetic field (H) proportional to the current, and the search coil measures the magnetic flux density (B) induced in the ferromagnetic core.
- Connect the output of the signal generator to the X-input of the CRO, and the output of the search coil to the Y-input of the CRO. Set the CRO to the X-Y mode, and adjust the time base and voltage sensitivity to obtain a clear display.
- Vary the frequency and amplitude of the signal generator, and observe the shape and size of the B-H loop on the CRO screen. Note the values of Br and Hc from the loop.
- Repeat the experiment with different ferromagnetic materials, such as iron, steel, nickel, etc., and compare their B-H loops.

## Observation:

The B-H loops of different ferromagnetic materials are shown below:

B-H loops of different ferromagnetic materials

## Result:

The B-H loop or hysteresis loop of a ferromagnetic material can be observed using a CRO. The B-H loop shows the nonlinear and history-dependent relationship between the magnetic field strength (H) and the magnetic flux density (B) of the material. The B-H loop also shows the retentivity, coercivity, and hysteresis loss of the material. The shape and size of the B-H loop depend on the type and properties of the ferromagnetic material.



##### Virtual lab

- A virtual lab is a simulation-based laboratory that allows students to perform experiments online using a computer or a mobile device.
- Virtual labs aim to provide remote access to labs in various disciplines of science and engineering, especially for students who have no access to physical labs or where equipment is scarce or costly.
- Virtual labs also help students retain the real feel of a laboratory, while enhancing their conceptual understanding and problem-solving skills.
- Virtual labs are developed by various institutions and organizations, such as Amrita Vishwa Vidyapeetham, which has created over 220 simulation-based experiments for its award-winning VALUE (Virtual Amrita Laboratories Universalizing Education) project.
- The link provided by the user is for a virtual lab on the topic of "Determination of the focal length of a concave mirror and a convex lens using u-v method", which is part of the Physical Sciences category of Amrita Vishwa Vidyapeetham Virtual Lab.
- The virtual lab consists of two sections: Theory and Simulation. The Theory section explains the concepts, principles, and formulas related to the experiment, while the Simulation section allows the user to perform the experiment by adjusting the parameters and observing the results.
- The virtual lab also provides a Procedure, a Quiz, and a Feedback section for the user to follow the steps, test their knowledge, and share their opinions on the experiment.



##### 7. Determination of the efficiency of a dc motor by loss summation method (Swinburne's test).

- The efficiency of a dc motor is defined as the ratio of output (mechanical) power to input (electrical) power.
- The output power of a dc motor can be measured by using a dynamometer or a brake, and the input power can be measured by using a power analyzer or a wattmeter.
- However, this direct method of measuring the efficiency of a dc motor requires loading the motor to its rated capacity, which may not be feasible or economical for large motors.
- Therefore, an indirect method of measuring the efficiency of a dc motor is to determine its losses instead of measuring the input and output power on load.
- The losses of a dc motor can be classified into two categories: constant losses and variable losses.
- Constant losses are those losses that do not depend on the load current, such as core loss, friction loss, and windage loss.
- Variable losses are those losses that depend on the load current, such as copper loss in the armature and the field windings.
- The total loss of a dc motor can be expressed as:

  `Total loss = Constant loss + Variable loss`

- The efficiency of a dc motor can be calculated as:

  `Efficiency = (Input power - Total loss) / Input power`

- Swinburne's test is an indirect method of determining the efficiency of a dc motor by loss summation method.
- Swinburne's test is based on the assumption that the constant losses of a dc motor are the same at no load and at full load, and the variable losses are proportional to the square of the load current.
- Swinburne's test involves running the dc motor at no load and measuring the no load current, the applied voltage, and the speed.
- The input power at no load can be calculated as:

  `Input power at no load = Applied voltage x No load current`

- The constant loss at no load can be calculated as:

  `Constant loss at no load = Input power at no load - (Armature copper loss at no load + Field copper loss at no load)`

- The armature copper loss at no load can be calculated as:

  `Armature copper loss at no load = (No load current - Field current) x Armature resistance x (No load current - Field current)`

- The field copper loss at no load can be calculated as:

  `Field copper loss at no load = Field current x Field resistance x Field current`

- The variable loss at full load can be calculated as:

  `Variable loss at full load = (Armature copper loss at full load + Field copper loss at full load) - (Armature copper loss at no load + Field copper loss at no load)`

- The armature copper loss at full load can be calculated as:

  `Armature copper loss at full load = (Full load current - Field current) x Armature resistance x (Full load current - Field current)`

- The field copper loss at full load can be calculated as:

  `Field copper loss at full load = Field current x Field resistance x Field current`

- The total loss at full load can be calculated as:

  `Total loss at full load = Constant loss at no load + Variable loss at full load`

- The input power at full load can be calculated as:

  `Input power at full load = Applied voltage x Full load current`

- The efficiency of the dc motor at full load can be calculated as:

  `Efficiency at full load = (Input power at full load - Total loss at full load) / Input power at full load`

- Swinburne's test has the advantages of convenience, economy, and accuracy, as it does not require loading the motor or measuring the output power.
- Swinburne's test has the disadvantages of not accounting for the change in speed, temperature, and stray losses at full load, and not being applicable to series motors.



#### Course Outcomes:

- By the end of this course, you will be able to:
  - Identify and explain the key concepts and principles of artificial intelligence, such as search, knowledge representation, reasoning, planning, learning, and natural language processing.
  - Apply various artificial intelligence techniques and algorithms to solve problems and tasks, such as heuristic search, constraint satisfaction, logic programming, probabilistic inference, decision making, neural networks, and machine translation.
  - Evaluate the strengths and limitations of different artificial intelligence approaches and methods, and compare their performance and applicability to different domains and scenarios.
  - Design and implement artificial intelligence systems and applications using appropriate tools and frameworks, such as Python, TensorFlow, PyTorch, and NLTK.
  - Demonstrate ethical awareness and social responsibility when developing and using artificial intelligence systems and applications, and consider their potential impacts and implications on individuals, society, and the environment.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write on the topic of course outcome (CO) Bloom's level. Here is what I have written:

#### Course Outcome (CO) Bloom's Level

- A course outcome (CO) is a statement that describes what a student should be able to do or demonstrate after completing a course.
- A CO should be specific, measurable, achievable, relevant, and time-bound (SMART).
- A CO should also align with the program outcomes (POs) and the vision and mission of the institution.
- A CO can be classified according to the Bloom's taxonomy of learning domains, which are cognitive, affective, and psychomotor.
- The cognitive domain involves knowledge, comprehension, application, analysis, synthesis, and evaluation.
- The affective domain involves receiving, responding, valuing, organizing, and characterizing.
- The psychomotor domain involves perception, set, guided response, mechanism, complex overt response, adaptation, and origination.
- The Bloom's level of a CO indicates the level of complexity and depth of learning that is expected from the student.
- The higher the Bloom's level, the more challenging and advanced the CO is.
- The Bloom's level of a CO can be determined by using verbs that correspond to each level of the taxonomy.
- For example, a CO that uses the verb "define" is at the knowledge level, while a CO that uses the verb "create" is at the synthesis level.
- The Bloom's level of a CO should match the level of the course and the intended learning outcomes of the curriculum.



#### At the end of this course, the students should be able to:

- Explain the basic concepts and principles of artificial intelligence, such as agents, search, knowledge representation, reasoning, planning, learning, natural language processing, computer vision, and robotics.
- Apply various AI techniques and algorithms to solve problems, such as heuristic search, constraint satisfaction, logic, inference, probabilistic models, decision making, neural networks, deep learning, natural language understanding, and computer vision.
- Evaluate the strengths and limitations of different AI approaches and methods, and compare their performance and applicability to different domains and tasks.
- Design and implement AI systems and applications using appropriate tools and frameworks, such as Python, TensorFlow, PyTorch, OpenAI Gym, NLTK, and OpenCV.
- Critically analyze and reflect on the ethical, social, and professional issues and challenges of AI, such as bias, fairness, accountability, transparency, privacy, security, and human-AI interaction.



##### CO 1 Conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits. K3

- KVL stands for Kirchhoff's Voltage Law, which states that the algebraic sum of the voltages around any closed loop in a circuit is zero.
- KCL stands for Kirchhoff's Current Law, which states that the algebraic sum of the currents entering and leaving any node in a circuit is zero.
- Network theorems are mathematical tools that can be used to simplify and analyze complex DC circuits. Some of the common network theorems are:
  - Superposition theorem: The voltage or current in any branch of a linear circuit is equal to the algebraic sum of the voltages or currents produced by each source acting alone, with all other sources replaced by their internal resistances.
  - Thevenin's theorem: Any linear circuit with voltage and current sources and only resistances can be replaced by an equivalent circuit consisting of a single voltage source in series with a single resistance connected across the load.
  - Norton's theorem: Any linear circuit with voltage and current sources and only resistances can be replaced by an equivalent circuit consisting of a single current source in parallel with a single resistance connected across the load.
  - Maximum power transfer theorem: The maximum power is transferred from a source to a load when the load resistance is equal to the source resistance.
  - Reciprocity theorem: The current in any branch of a bilateral network due to a single source is equal to the current in the branch interchanged with the source.
- To conduct experiments illustrating the application of KVL/KCL and network theorems to DC electrical circuits, the following steps are suggested:
  - Design and construct a DC circuit with resistors, voltage and current sources, switches, meters, and other components as required.
  - Apply KVL and KCL to verify the voltages and currents in the circuit. Use a multimeter to measure the actual values and compare them with the theoretical values. Note any discrepancies and possible sources of error.
  - Apply the network theorems to simplify and analyze the circuit. Use a multimeter to measure the voltages and currents in the equivalent circuit and compare them with the original circuit. Note any discrepancies and possible sources of error.
  - Vary the values of the resistors, sources, and load and observe the effects on the circuit behavior. Record the data and plot the graphs as needed.
  - Write a report summarizing the objectives, procedures, results, and conclusions of the experiment. Include the circuit diagrams, calculations, tables, graphs, and error analysis. Discuss the advantages and limitations of the network theorems and their applications.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found:

##### CO 2 Demonstrate the behavior of AC circuits connected to single phase AC supply and measure power in single phase as well as three phase electrical circuits. K4

- An AC circuit is a circuit that carries alternating current, which is the current that changes direction periodically. The main source of AC is the power grid or the generator that produces AC.
- A single phase AC supply is a type of AC supply that has only one voltage waveform. It is commonly used for residential and commercial applications. A single phase AC supply can be obtained from a transformer that steps down the voltage from a higher level.
- A single phase AC circuit can have different types of loads, such as resistive, inductive, capacitive, or a combination of them. The behavior of the AC circuit depends on the impedance of the load, which is the opposition to the current flow. The impedance can be calculated using the formula Z = R + jX, where R is the resistance, j is the imaginary unit, and X is the reactance.
- The reactance of a load can be either positive or negative, depending on the type of load. A positive reactance means that the load is inductive, which means that it stores energy in a magnetic field. A negative reactance means that the load is capacitive, which means that it stores energy in an electric field. A zero reactance means that the load is purely resistive, which means that it dissipates energy as heat.
- The power factor of a load is the ratio of the real power to the apparent power. The real power is the power that is actually consumed by the load, while the apparent power is the product of the voltage and the current. The power factor can be calculated using the formula PF = cos θ, where θ is the phase angle between the voltage and the current. The power factor can range from 0 to 1, where 0 means that the load is purely reactive and 1 means that the load is purely resistive.
- The power measurement in a single phase AC circuit can be done using a wattmeter, which is a device that measures the real power. A wattmeter consists of two coils, one called the current coil and the other called the voltage coil. The current coil is connected in series with the load, while the voltage coil is connected in parallel with the load. The wattmeter reads the power by measuring the torque produced by the interaction of the magnetic fields of the two coils.
- A three phase AC supply is a type of AC supply that has three voltage waveforms that are 120 degrees out of phase with each other. It is commonly used for industrial and high power applications. A three phase AC supply can be obtained from a three phase generator or a transformer that steps down the voltage from a higher level.
- A three phase AC circuit can have different types of connections, such as star, delta, or a combination of them. The behavior of the AC circuit depends on the impedance of the load and the connection type. The impedance of the load can be calculated using the same formula as the single phase AC circuit, while the connection type determines the line voltage, the line current, and the phase voltage, and the phase current.
- The power measurement in a three phase AC circuit can be done using two wattmeters, which are connected in a balanced or an unbalanced configuration. A balanced configuration means that the load is symmetrical and has the same impedance in each phase. An unbalanced configuration means that the load is asymmetrical and has different impedances in each phase. The two wattmeters are connected in such a way that one measures the power in one phase and the other measures the power in another phase. The total power is then obtained by adding the readings of the two wattmeters.



##### CO 3 Perform experiment illustrating BH curve of magnetic materials. K3

- The objective of this experiment is to illustrate the BH curve of magnetic materials, which shows the relationship between magnetic field strength (H) and magnetic flux density (B) in a material.
- The materials required for this experiment are:
  - A solenoid with a variable current source and an ammeter to measure the current (I) flowing through it.
  - A magnetic material (such as iron, steel, or ferrite) that can be inserted inside the solenoid.
  - A gaussmeter with a probe to measure the magnetic flux density (B) at the center of the solenoid.
  - A graph paper or a computer software to plot the BH curve.
- The procedure of this experiment is as follows:
  - Connect the solenoid to the current source and the ammeter, and set the current to zero.
  - Insert the magnetic material inside the solenoid, and place the gaussmeter probe at the center of the solenoid.
  - Gradually increase the current in the solenoid, and record the corresponding values of current (I) and magnetic flux density (B) at each step.
  - Repeat the same process in the opposite direction, by gradually decreasing the current to zero and then reversing the polarity of the current source.
  - Plot the BH curve on the graph paper or the computer software, by taking current (I) as the x-axis and magnetic flux density (B) as the y-axis.
- The expected outcome of this experiment is a hysteresis loop, which shows the history of magnetization and demagnetization of the magnetic material. The shape and size of the loop depend on the type and properties of the material. Some important parameters of the loop are:
  - The saturation point, which is the maximum value of magnetic flux density (B) that the material can attain for a given current (I).
  - The coercivity, which is the value of current (I) required to reduce the magnetic flux density (B) to zero.
  - The remanence, which is the value of magnetic flux density (B) that remains in the material after the current (I) is reduced to zero.
  - The area of the loop, which is proportional to the energy loss or the heat generated in the material due to the changing magnetic field.



##### CO 4 Calculate efficiency of a single phase transformer and DC machine. K4

- Efficiency is the ratio of output power to input power, expressed as a percentage.
- A single phase transformer is a device that transfers electrical energy from one circuit to another through mutual induction, without changing the frequency.
- A DC machine is a device that converts electrical energy to mechanical energy or vice versa, using direct current.
- To calculate the efficiency of a single phase transformer, we need to know the input and output voltages, currents, and power factors, as well as the losses due to copper and iron.
- The input power of a single phase transformer is given by:

```
P_in = V_in * I_in * cos(phi_in)
```

- Where V_in is the input voltage, I_in is the input current, and cos(phi_in) is the input power factor.
- The output power of a single phase transformer is given by:

```
P_out = V_out * I_out * cos(phi_out)
```

- Where V_out is the output voltage, I_out is the output current, and cos(phi_out) is the output power factor.
- The copper loss of a single phase transformer is the power dissipated in the primary and secondary windings due to their resistance. It is given by:

```
P_cu = I_p^2 * R_p + I_s^2 * R_s
```

- Where I_p is the primary current, R_p is the primary resistance, I_s is the secondary current, and R_s is the secondary resistance.
- The iron loss of a single phase transformer is the power dissipated in the core due to hysteresis and eddy currents. It is given by:

```
P_fe = k_h * f * B_max^1.6 * V + k_e * f^2 * B_max^2 * V
```

- Where k_h is the hysteresis constant, f is the frequency, B_max is the maximum flux density, V is the volume of the core, k_e is the eddy current constant.
- The efficiency of a single phase transformer is then given by:

```
eta = P_out / (P_in + P_cu + P_fe) * 100%
```

- To calculate the efficiency of a DC machine, we need to know the input and output voltages, currents, and power, as well as the losses due to armature, field, and mechanical friction.
- The input power of a DC machine is given by:

```
P_in = V * I
```

- Where V is the terminal voltage and I is the armature current.
- The output power of a DC machine is given by:

```
P_out = T * omega
```

- Where T is the torque and omega is the angular speed.
- The armature loss of a DC machine is the power dissipated in the armature winding due to its resistance. It is given by:

```
P_a = I^2 * R_a
```

- Where R_a is the armature resistance.
- The field loss of a DC machine is the power dissipated in the field winding due to its resistance. It is given by:

```
P_f = V_f * I_f
```

- Where V_f is the field voltage and I_f is the field current.
- The mechanical loss of a DC machine is the power dissipated due to friction and windage. It is given by:

```
P_m = k * omega^3
```

- Where k is a constant that depends on the machine design and operating conditions.
- The efficiency of a DC machine is then given by:

```
eta = P_out / (P_in + P_a + P_f + P_m) * 100%
```



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

##### CO 5 Perform experiments on speed measurement and reversal of direction of three phase induction motor and Identify the type of DC and AC machines based on their construction. K4

- A three phase induction motor is a type of AC machine that converts electrical power into mechanical power by creating a rotating magnetic field in the stator and inducing currents in the rotor.
- The speed of a three phase induction motor depends on the frequency of the supply voltage, the number of poles in the stator, and the slip between the stator and rotor magnetic fields.
- The speed of a three phase induction motor can be measured by using a tachometer, a stroboscope, or a frequency meter.
- The direction of rotation of a three phase induction motor can be reversed by interchanging any two of the three supply terminals. This changes the phase sequence of the stator currents and reverses the direction of the stator magnetic field.
- A DC machine is a type of electrical machine that converts electrical power into mechanical power or vice versa by using a commutator and brushes to switch the direction of the current in the armature windings.
- An AC machine is a type of electrical machine that converts electrical power into mechanical power or vice versa by using alternating currents in the stator and rotor windings, without the need of a commutator or brushes.
- The type of DC and AC machines can be identified based on their construction, such as the shape and arrangement of the armature, the type and number of windings, the presence or absence of a commutator and brushes, and the type and number of poles.



#### K1 – Remember, K2 – Understand, K3 – Apply, K4 – Analyze, K5 – Evaluate, K6 – Create

- These are the six levels of cognitive learning according to Bloom's taxonomy, a framework for classifying educational objectives and outcomes.
- K1 – Remember: This level involves recalling facts, terms, definitions, concepts, or procedures from memory. Examples of verbs used at this level are: define, list, name, identify, label, recognize, etc.
- K2 – Understand: This level involves explaining the meaning, interpretation, or summary of information in one's own words. Examples of verbs used at this level are: describe, explain, paraphrase, summarize, illustrate, classify, etc.
- K3 – Apply: This level involves using learned information to solve problems or perform tasks in new situations. Examples of verbs used at this level are: apply, demonstrate, use, calculate, solve, implement, etc.
- K4 – Analyze: This level involves breaking down information into parts, examining the relationships, causes, effects, or implications of each part, and identifying patterns or trends. Examples of verbs used at this level are: analyze, compare, contrast, differentiate, distinguish, examine, etc.
- K5 – Evaluate: This level involves making judgments or assessments based on criteria, standards, or evidence. Examples of verbs used at this level are: evaluate, assess, critique, justify, argue, defend, appraise, etc.
- K6 – Create: This level involves generating, designing, planning, or producing original or innovative products, solutions, or ideas. Examples of verbs used at this level are: create, design, develop, construct, compose, invent, etc.

