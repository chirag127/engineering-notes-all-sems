

# SENSORS, ACTUATORS AND SIGNAL PROCESSING

- Sensors are devices that convert a physical event or phenomenon into an electrical signal that can be measured, processed, or transmitted .
- Actuators are devices that convert an electrical signal into a physical event or phenomenon, such as movement, force, or sound .
- Sensors and actuators often work together to monitor and control physical systems, such as machines, robots, vehicles, or environments.
- Signal processing is the manipulation, analysis, or transformation of signals, such as sensor data, images, sounds, or texts.
- Signal processing techniques can be used to enhance, filter, compress, encode, decode, classify, or interpret signals for various applications, such as security, communication, entertainment, or health.
- Signal processing can be performed in analog or digital domains, using hardware or software components, or a combination of both.
- Some examples of sensors are temperature sensors, pressure sensors, light sensors, motion sensors, or chemical sensors .
- Some examples of actuators are motors, solenoids, speakers, valves, or heaters .
- Some examples of signal processing techniques are Fourier transform, wavelet transform, convolution, correlation, filtering, modulation, demodulation, or machine learning .



# KCS

KCS stands for Knowledge-Centered Service, a methodology that aims to improve service delivery and knowledge management in service organizations. Some of the main points about KCS are:

- KCS is based on the principle that knowledge is a by-product of solving problems and that the knowledge should be captured, structured, and reused as part of the service process.
- KCS involves creating and maintaining knowledge articles that document the issues, solutions, and context of service interactions. These articles are stored in a knowledge base that can be accessed and updated by service agents and customers.
- KCS has four main practices: capture, structure, reuse, and improve. Capture means creating knowledge articles as a natural part of solving problems. Structure means following a consistent format and style for the articles. Reuse means finding and using existing articles to solve problems and avoid duplication. Improve means reviewing and updating the articles based on feedback and usage.
- KCS has many benefits for service organizations, such as: increasing customer satisfaction, reducing resolution time, enhancing agent productivity, decreasing costs, and improving service quality.
- KCS is not a one-size-fits-all solution, but a flexible and adaptable framework that can be customized to fit different service contexts and goals. KCS also requires a cultural change and a commitment from the service organization to adopt and sustain the methodology.



# Unit 1 - Sensors / Transducers: Principles, Classification, Parameters, Characteristics, Environmental Parameters (EP), Characterization

## Principles

- A sensor is an element that senses a variation in input energy to produce a variation in another or same form of energy.
- A transducer is an element that converts one form of energy to another form. The process of conversion of energy from one form to another is called transduction.
- The principle of transduction is the physical phenomenon or property that is used to convert the input energy to the output energy. For example, a thermocouple uses the Seebeck effect to convert heat to electricity, and a piezoelectric crystal uses the piezoelectric effect to convert mechanical stress to electric charge.

## Classification

- Sensors and transducers can be classified based on different criteria, such as:
  - The input and output energy forms, such as mechanical, electrical, thermal, optical, chemical, etc. For example, a strain gauge is a mechanical-electrical transducer, and a photodiode is an optical-electrical transducer.
  - The principle of transduction, such as resistive, inductive, capacitive, piezoelectric, thermoelectric, etc. For example, a potentiometer is a resistive transducer, and a transformer is an inductive transducer.
  - The mode of operation, such as active or passive. Active sensors require an external source of power (excitation voltage) that provides the majority of the output power of the signal, while passive sensors produce the output power almost entirely from the measured signal without an excitation voltage. For example, a thermocouple is a passive sensor, and a strain gauge is an active sensor.
  - The type of output signal, such as analog or digital. Analog sensors produce a continuous output signal that varies proportionally to the input quantity, while digital sensors produce a discrete output signal that is encoded in binary form. For example, a thermistor is an analog sensor, and a digital thermometer is a digital sensor.

## Parameters

- Parameters are the specifications or characteristics that describe the performance and behavior of sensors and transducers. Some of the common parameters are:
  - Sensitivity: The ratio of the change in output signal to the change in input quantity. It indicates how responsive the sensor is to the input variation.
  - Range: The minimum and maximum values of the input quantity that the sensor can measure or respond to.
  - Resolution: The smallest change in input quantity that the sensor can detect or measure.
  - Accuracy: The degree of closeness of the output signal to the true value of the input quantity. It indicates how correct the sensor measurement is.
  - Precision: The degree of repeatability of the output signal for the same input quantity. It indicates how consistent the sensor measurement is.
  - Linearity: The extent to which the output signal follows a straight line relationship with the input quantity. It indicates how proportional the sensor response is.
  - Hysteresis: The difference in output signal for the same input quantity when the input is increasing or decreasing. It indicates how dependent the sensor response is on the previous input values.
  - Drift: The change in output signal over time due to aging, wear, or environmental factors. It indicates how stable the sensor performance is.

## Characteristics

- Characteristics are the graphical representations of the parameters or the relationships between the input and output quantities of sensors and transducers. Some of the common characteristics are:
  - Input-output characteristic: The curve that shows the variation of output signal with respect to input quantity. It can be linear or nonlinear, depending on the sensor principle and design.
  - Transfer function: The mathematical equation that relates the output signal to the input quantity. It can be derived from the input-output characteristic or from the sensor model.
  - Frequency response: The curve that shows the variation of output signal amplitude and phase with respect to input frequency. It indicates how the sensor responds to different frequency components of the input signal.
  - Dynamic response: The curve that shows the variation of output signal with respect to time when the input quantity changes abruptly. It indicates how fast the sensor responds to the input change.

## Environmental Parameters (EP)

- Environmental parameters are the external factors that affect the performance and behavior of sensors and transducers. Some of the common environmental parameters are:
  - Temperature: The measure of heat or coldness of the surroundings. It can cause thermal expansion, contraction, or stress in



# Mechanical and Electromechanical Sensors

## Introduction

- Mechanical sensors are devices that convert mechanical stimuli, such as force, pressure, displacement, strain, or vibration, into electrical signals.
- Electromechanical sensors are a subclass of mechanical sensors that use electromechanical phenomena, such as piezoelectricity, magnetism, or induction, to generate electrical signals.
- Mechanical and electromechanical sensors have various applications in fields such as robotics, aerospace, automotive, biomedical, industrial, and wearable technologies .
- Mechanical and electromechanical sensors can be classified based on their sensing principle, such as resistive, inductive, capacitive, electrostatic, piezoelectric, or ultrasonic .

## Resistive Potentiometer

- A resistive potentiometer is a type of mechanical sensor that measures the displacement or rotation of a movable contact along a resistive element.
- The output voltage of a resistive potentiometer is proportional to the position of the contact relative to the terminals of the resistive element.
- A resistive potentiometer can be linear or rotary, depending on the shape and arrangement of the resistive element and the contact.
- A resistive potentiometer is simple, inexpensive, and easy to use, but it has drawbacks such as wear, friction, noise, and limited resolution.

## Strain Gauge

- A strain gauge is a type of mechanical sensor that measures the strain or deformation of a material or structure due to an applied force or stress .
- A strain gauge consists of a thin metallic wire or foil that is attached to the surface of the material or structure to be measured .
- The electrical resistance of a strain gauge changes as the wire or foil is stretched or compressed due to the strain .
- The change in resistance of a strain gauge is proportional to the strain, according to the gauge factor, which is a constant that depends on the material and geometry of the strain gauge .
- A strain gauge can be used to measure various physical quantities, such as force, pressure, torque, acceleration, or temperature, by converting them into strain .

## Resistance Strain Gauge

- A resistance strain gauge is a type of strain gauge that uses a resistive wire or foil as the sensing element .
- A resistance strain gauge can be uniaxial, biaxial, or rosette, depending on the orientation and arrangement of the wire or foil relative to the direction of the strain .
- A resistance strain gauge can be connected in a Wheatstone bridge circuit to measure the change in resistance due to the strain .
- A resistance strain gauge is widely used and versatile, but it has limitations such as low sensitivity, temperature dependence, hysteresis, and drift .

## Semiconductor Strain Gauges

- A semiconductor strain gauge is a type of strain gauge that uses a semiconductor material, such as silicon or germanium, as the sensing element .
- A semiconductor strain gauge has a much higher gauge factor than a resistance strain gauge, which means it has a higher sensitivity and resolution .
- A semiconductor strain gauge can be integrated with microelectronic circuits and microelectromechanical systems (MEMS) to form miniaturized and multifunctional sensors .
- A semiconductor strain gauge is more expensive, fragile, and temperature sensitive than a resistance strain gauge, and it requires special fabrication and packaging techniques .

## Inductive Sensors

- An inductive sensor is a type of electromechanical sensor that measures the change in inductance of a coil due to the displacement or movement of a magnetic core or target .
- The output voltage or frequency of an inductive sensor is proportional to the position or velocity of the core or target relative to the coil .
- An inductive sensor can be linear or rotary, depending on the shape and arrangement of the coil and the core or target .
- An inductive sensor is robust, reliable, and immune



# Unit 2 - Thermal Sensors

## Introduction

- Thermal sensors are devices that measure temperature or heat flux using various physical principles and properties.
- Temperature is a measure of the average kinetic energy of the molecules in a system, while heat flux is the rate of heat transfer per unit area.
- Thermal sensors can be classified into two main categories: contact and non-contact sensors.
- Contact sensors require physical contact with the object or medium whose temperature is to be measured, while non-contact sensors measure temperature remotely using radiation or other means.
- Thermal sensors can also be classified based on the physical property or principle that changes with temperature, such as gas pressure, thermal expansion, acoustic velocity, dielectric constant, refractive index, electrical resistance, thermoelectric voltage, semiconductor junction voltage, thermal radiation, quartz crystal frequency, nuclear magnetic resonance, spectroscopy, or noise.

## Gas Thermometric Sensors

- Gas thermometric sensors are contact sensors that use the pressure or volume of a gas as a function of temperature to measure temperature.
- The gas can be enclosed in a sealed container or a flexible membrane, and the pressure or volume can be measured using a manometer, a bourdon tube, a bellows, or a strain gauge.
- Gas thermometric sensors can measure a wide range of temperatures, from cryogenic to very high temperatures, depending on the type and amount of gas used.
- Gas thermometric sensors are accurate, stable, and insensitive to environmental factors, but they are slow, bulky, and require calibration.

## Thermal Expansion Type Thermometric Sensors

- Thermal expansion type thermometric sensors are contact sensors that use the change in length, volume, or shape of a solid or liquid material as a function of temperature to measure temperature.
- The material can be a metal, a liquid, a bimetal, or a shape memory alloy, and the change in length, volume, or shape can be measured using a dial, a pointer, a lever, a spring, or an electrical transducer.
- Thermal expansion type thermometric sensors can measure a moderate range of temperatures, from low to high temperatures, depending on the type and amount of material used.
- Thermal expansion type thermometric sensors are simple, inexpensive, and easy to use, but they are slow, have low resolution, and are affected by mechanical stress and hysteresis.



# Magnetic Sensors: Introduction, Sensors and the Principles Behind, Magneto-resistive Sensors, Anisotropic Magneto-resistive Sensing, Semiconductor Magneto-resistors, Hall Effect and Sensors, Inductance and Eddy Current Sensors, Angular/Rotary Movement Transducers, Synchronous, Synchronousresolvers, Eddy Current Sensors, Electromagnetic Flow meter, Switching Magnetic Sensors, SQUID Sensors

## Introduction
- Magnetic sensors are devices that measure the presence or variation of magnetic fields or magnetic materials.
- Magnetic sensors can be used for various applications, such as position, speed, direction, rotation, proximity, level, flow, and current sensing.
- Magnetic sensors can operate without physical contact, which reduces wear and tear, and can work in harsh environments, such as high temperature, pressure, humidity, and vibration.
- Magnetic sensors can have different operating principles, such as electromagnetic induction, magneto-resistance, Hall effect, inductance, eddy currents, and superconducting quantum interference devices (SQUID) .

## Sensors and the Principles Behind
- Electromagnetic induction sensors use the principle that a changing magnetic field induces an electric current in a conductor. The induced current is proportional to the rate of change of the magnetic field and the area of the conductor. Electromagnetic induction sensors can be used to measure linear or angular displacement, speed, or direction.
- Magneto-resistive sensors use the principle that the electrical resistance of some materials changes when they are subjected to a magnetic field. The resistance change is proportional to the magnitude and direction of the magnetic field. Magneto-resistive sensors can be used to measure magnetic field strength, angle, or position .
- Hall effect sensors use the principle that a voltage difference is generated across a conductor when it carries a current in a magnetic field. The voltage difference is proportional to the product of the current and the magnetic field. Hall effect sensors can be used to measure magnetic field strength, current, or position.
- Inductance sensors use the principle that the inductance of a coil changes when it is placed near a magnetic material or a magnet. The inductance change is proportional to the permeability and the geometry of the magnetic material or the magnet. Inductance sensors can be used to measure displacement, proximity, or level.
- Eddy current sensors use the principle that a changing magnetic field induces eddy currents in a conductive material. The eddy currents generate a secondary magnetic field that opposes the primary magnetic field. The eddy current effect depends on the conductivity, permeability, and geometry of the material, as well as the frequency and amplitude of the primary magnetic field. Eddy current sensors can be used to measure displacement, speed, or conductivity.
- SQUID sensors use the principle that a superconducting loop can act as a very sensitive detector of magnetic flux. A SQUID consists of two Josephson junctions, which are weak links between superconductors that allow a small current to flow without resistance. The voltage across a SQUID depends on the magnetic flux through the loop and the bias current applied to the junctions. SQUID sensors can be used to measure very weak magnetic fields, such as those generated by the brain or the heart .

## Magneto-resistive Sensors
- Magneto-resistive sensors are based on the property of some materials to change their electrical resistance when exposed to a magnetic field.
- There are different types of magneto-resistive sensors, such as anisotropic magneto-resistive (AMR), giant magneto-resistive (GMR), tunnel magneto-resistive (TMR), and colossal magneto-resistive (CMR) sensors.
- The main advantages of magneto-resistive sensors are their high sensitivity, low power consumption, small size, and compatibility with integrated circuits .
- The main disadvantages of magneto-resistive sensors are their nonlinearity, hysteresis, temperature dependence, and interference from external magnetic fields .

## Anisotropic Magneto-resistive Sensing
- Anisotropic magneto-resistive (AMR) sensing is a type of magneto-resistive sensing that uses the property of some ferromagnetic materials, such as permalloy, to have different resist



# Unit 3 - Radiation Sensors

## Introduction

- Radiation sensors or radiation detectors are devices that can sense and measure radiation emissions or levels of radiation produced by a source  .
- Radiation sensors are mostly based on the photoelectric effect, which is the emission of electrons from a material when electromagnetic radiation, such as a photon of visible light, falls on them.
- Radiation sensors are used for various applications, such as medical imaging, nuclear power, security, environmental monitoring, and scientific research .

## Basic Characteristics

- Some basic characteristics of radiation sensors are:

  - Sensitivity: the ability to detect low levels of radiation or small changes in radiation intensity.
  - Resolution: the ability to distinguish between different types or energies of radiation or different sources of radiation.
  - Efficiency: the ratio of the number of radiation events detected to the number of radiation events incident on the sensor.
  - Linearity: the proportionality between the output signal and the input radiation intensity.
  - Stability: the ability to maintain consistent performance over time and under varying environmental conditions.
  - Response time: the time required for the sensor to produce an output signal after receiving an input radiation.
  - Dynamic range: the range of radiation intensities that the sensor can measure without saturation or distortion.

## Types of Photosensistors/Photo detectors

- Photosensistors or photo detectors are devices that convert light into electric current or voltage.
- Some common types of photosensistors or photo detectors are:

  - Photodiodes: semiconductor devices that generate a current proportional to the light intensity. They have fast response time, high sensitivity, and low noise, but require external bias voltage and amplification.
  - Phototransistors: semiconductor devices that amplify the current generated by a photodiode. They have higher sensitivity and gain than photodiodes, but slower response time and higher noise.
  - Photovoltaic cells: semiconductor devices that generate a voltage proportional to the light intensity. They do not require external bias voltage or amplification, but have lower sensitivity and efficiency than photodiodes.
  - Photoresistors: resistors whose resistance changes with the light intensity. They have high sensitivity and dynamic range, but slow response time and non-linear output.
  - Photomultiplier tubes: vacuum tubes that multiply the current generated by a photocathode by using a series of dynodes. They have very high sensitivity and resolution, but require high voltage and are bulky and expensive.

## X-ray and Nuclear Radiation Sensors

- X-ray and nuclear radiation sensors are devices that can detect and measure X-rays and nuclear radiation, such as alpha, beta, gamma, and neutron radiation  .
- Some common types of X-ray and nuclear radiation sensors are:

  - Gas-filled detectors: devices that use the ionization effect that occurs when radiation passes through a gas-filled chamber. They produce a current or a pulse proportional to the radiation energy. They have high sensitivity and resolution, but require high voltage and are affected by pressure and temperature.
  - Scintillation detectors: devices that use the level of light energy produced when radiation strikes a scintillating material, such as a crystal or a plastic. They convert the light into an electrical signal using a photomultiplier tube or a photodiode. They have high efficiency and resolution, but require external power and are affected by background light.
  - Solid-state detectors: devices that use the creation of electron-hole pairs when radiation interacts with a semiconductor material, such as silicon or germanium. They produce a voltage or a pulse proportional to the radiation energy. They have high resolution and linearity, but require cooling and amplification.

## Fiber Optic Sensors

- Fiber optic sensors are devices that use optical fibers to transmit, modulate, or reflect light in response to physical or chemical changes, such as temperature, pressure, strain, or radiation.
- Some common types of fiber optic sensors are:

  - Intensity-based sensors: devices that measure the change in light intensity due to attenuation, scattering, or modulation by the sensing element. They have simple structure and low cost, but are affected by noise and power fluctuations.
  - Phase-based sensors: devices that measure the change in light phase due to interference, diffraction, or polarization by the sensing element. They have high sensitivity and resolution, but require coherent light sources and complex signal processing.
  - Wavelength-based sensors: devices that measure the change in light wavelength due to absorption, fluorescence



# Electro Analytical Sensors

- Electro analytical sensors are a class of chemical sensors that use electrodes as transducers to measure the presence or concentration of an analyte in a solution or a gas .
- Electro analytical sensors can detect various parameters such as pH, oxygen, carbon dioxide, glucose, ethanol, etc. by measuring the electrical signals that result from the electrochemical reactions between the analyte and the sensing surface .
- Electro analytical sensors can be based on different measurement principles such as amperometry, potentiometry, conductometry, voltammetry, etc. depending on the type of electrode and the applied potential or current.

## The Electrochemical Cell

- An electrochemical cell is a device that converts chemical energy into electrical energy or vice versa by using redox reactions.
- An electrochemical cell consists of two electrodes (anode and cathode) immersed in an electrolyte solution that allows the flow of ions between them.
- The electrodes are connected by an external circuit that allows the flow of electrons between them.
- The anode is the electrode where oxidation (loss of electrons) occurs and the cathode is the electrode where reduction (gain of electrons) occurs.
- The difference in the electrical potential between the two electrodes is called the cell potential or the electromotive force (EMF) of the cell.

## The Cell Potential

- The cell potential is the measure of the driving force of the redox reaction in an electrochemical cell.
- The cell potential depends on the nature and concentration of the reactants and products, the temperature, and the type of electrodes.
- The cell potential can be calculated by using the Nernst equation, which relates the cell potential to the standard cell potential and the reaction quotient.
- The standard cell potential is the cell potential when the reactants and products are in their standard states (usually 1 M for solutions and 1 atm for gases) and the temperature is 25°C.
- The reaction quotient is the ratio of the activities or concentrations of the products to the reactants at any given condition.
- The Nernst equation is given by:

E = E° - (RT/nF) ln Q

where E is the cell potential, E° is the standard cell potential, R is the gas constant, T is the temperature, n is the number of electrons transferred, F is the Faraday constant, and Q is the reaction quotient.

## Standard Hydrogen Electrode (SHE)

- The standard hydrogen electrode (SHE) is a reference electrode that is used to measure the standard cell potential of other electrodes.
- The SHE consists of a platinum wire coated with platinum black that is immersed in a 1 M HCl solution and is in contact with hydrogen gas at 1 atm and 25°C.
- The SHE is assigned a potential of 0 V by convention.
- The SHE is used to measure the standard reduction potential of other electrodes by connecting them to the SHE and measuring the cell potential.
- The standard reduction potential of an electrode is the potential when the electrode is reduced by the SHE.
- The standard reduction potential of an electrode is equal to the negative of the standard oxidation potential of the same electrode.

## Liquid Junction and Other Potentials

- Liquid junction potential is the potential difference that arises when two solutions of different concentrations or compositions are in contact with each other.
- Liquid junction potential is caused by the unequal diffusion rates of the ions in the solutions and the charge separation that occurs at the interface.
- Liquid junction potential can affect the accuracy of the cell potential measurement and should be minimized or eliminated by using a salt bridge or a porous plug that connects the two solutions.
- Other potentials that can affect the cell potential measurement are the electrode potential, the junction potential, the diffusion potential, and the concentration potential.
- Electrode potential is the potential difference between the electrode and the solution due to the charge transfer at the interface.
- Junction potential is the potential difference between two electrodes due to the different materials or coatings used.
- Diffusion potential is the potential difference that arises when a solution is not homogeneous and the concentration of the ions varies with distance.
- Concentration potential is the potential difference that arises when the concentration of the ions in the solution changes due to the



# Smart Sensors: Introduction, Primary Sensors, Excitation, Amplification, Filters, Converters, Compensation, Information Coding/Processing, Data Communication, Standards for Smart Sensor Interface, the Automation.

## Introduction

- A smart sensor is an analog or digital transducer combined with sensing and computing abilities.
- It consists of a transduction component, signal conditioning electronics, and a processor that supports some intelligence in a single package.
- A smart sensor can sense physical phenomena, convert them into another form—usually in electronic signals—and process the data collected.
- A smart sensor can also communicate with other devices or networks using wired or wireless connections.
- A smart sensor can perform functions such as aggregation, error checking, calibration, compensation, self-diagnosis, self-identification, and self-adaptation .
- A smart sensor can improve the performance, reliability, accuracy, and efficiency of a system or application .

## Primary Sensors

- A primary sensor is the sensing element that senses the physical phenomenon, such as the temperature, humidity, pressure, level, flow, etc., and converts it into an electrical signal .
- A primary sensor can be classified into different types based on the principle of operation, such as resistive, capacitive, inductive, piezoelectric, optical, magnetic, etc .
- A primary sensor can be selected based on the requirements of the application, such as the range, resolution, sensitivity, linearity, accuracy, stability, response time, etc .

## Excitation

- Excitation is the process of providing an external energy source to the primary sensor to enable its operation.
- Excitation can be in the form of voltage, current, frequency, light, etc., depending on the type of the primary sensor.
- Excitation can be constant or variable, depending on the application.
- Excitation can affect the output signal of the primary sensor, such as its amplitude, phase, frequency, etc.
- Excitation can also cause errors or noise in the output signal, such as drift, hysteresis, nonlinearity, etc.
- Excitation can be controlled or regulated by the smart sensor to improve the quality and accuracy of the output signal.

## Amplification

- Amplification is the process of increasing the magnitude of the output signal of the primary sensor to make it suitable for further processing or transmission.
- Amplification can be done by using electronic circuits, such as operational amplifiers, transistors, etc.
- Amplification can be classified into different types based on the function, such as voltage amplification, current amplification, power amplification, etc.
- Amplification can also be classified into different types based on the frequency response, such as low-pass, high-pass, band-pass, band-stop, etc.
- Amplification can improve the signal-to-noise ratio, dynamic range, and resolution of the output signal.
- Amplification can also introduce errors or noise in the output signal, such as distortion, offset, drift, etc.
- Amplification can be adjusted or compensated by the smart sensor to optimize the performance and accuracy of the output signal.



# Sensors Applications

Sensors are devices that detect and measure physical quantities such as temperature, pressure, light, sound, motion, etc. and convert them into electrical signals. Sensors are widely used in various fields and industries for different purposes. Some of the applications of sensors are:

## Introduction

- Sensors can improve the world through diagnostics in medical applications; improved performance of energy sources like fuel cells, batteries and solar power; improved health, safety and security for people; sensors for exploring space and the known universe; and improved environmental monitoring.
- Sensors can also enable the Internet of Things (IoT) by collecting the data for smarter decisions. IoT is the network of physical objects that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the internet.

## On-board Automobile Sensors (Automotive Sensors)

- Sensors are central to automotive applications being used for braking and traction control, air bags, engine management, fuel injection, tire pressure monitoring, parking assistance, collision avoidance, etc.
- Some examples of automotive sensors are:

  - Antilock Braking System (ABS) Sensors: These sensors are connected to the wheel and measure the speed of the wheel rotation. They help to prevent the wheels from locking up and skidding during braking, thus improving the vehicle stability and safety.
  - Air Bags - Anti Cushion Restraint System (ACRS): These sensors include crush sensors and accelerometers that are placed in the vehicle body and detect the impact and severity of a collision. They trigger the deployment of air bags to protect the occupants from injuries.
  - Engine Management Sensors: These sensors monitor the engine performance and emissions by measuring parameters such as air flow, oxygen level, fuel pressure, engine temperature, etc. They help to optimize the fuel efficiency and reduce the environmental impact of the vehicle.

## Home Appliance Sensors

- Sensors are also used in various home appliances such as refrigerators, washing machines, air conditioners, microwaves, etc. to enhance their functionality and convenience.
- Some examples of home appliance sensors are:

  - Refrigerator Sensors: These sensors measure the temperature and humidity inside the refrigerator and adjust the cooling system accordingly. They also detect the opening and closing of the door and activate the interior light and alarm.
  - Washing Machine Sensors: These sensors detect the load size, fabric type, and dirt level of the clothes and adjust the water level, detergent amount, and washing cycle accordingly. They also monitor the water temperature, pressure, and flow and prevent overflow and leakage.
  - Air Conditioner Sensors: These sensors measure the room temperature and humidity and control the cooling and heating system accordingly. They also detect the presence and movement of people in the room and adjust the air flow and direction accordingly.

## Aerospace Sensors

- Sensors are essential for aerospace applications being used for navigation, guidance, control, communication, surveillance, etc. Sensors are also used for monitoring the health and performance of the aircraft and spacecraft components and systems.
- Some examples of aerospace sensors are:

  - Inertial Navigation System (INS) Sensors: These sensors include accelerometers and gyroscopes that measure the acceleration and angular velocity of the aircraft or spacecraft. They help to determine the position, velocity, and orientation of the vehicle without relying on external references such as GPS or stars.
  - Radar Sensors: These sensors emit and receive electromagnetic waves and measure the distance, speed, and direction of the objects in the surrounding space. They help to detect and avoid obstacles, track and identify targets, and map the terrain.
  - Structural Health Monitoring (SHM) Sensors: These sensors include strain gauges, piezoelectric sensors, fiber optic sensors, etc. that measure the stress, strain, vibration, temperature, etc. of the aircraft or spacecraft structures and components. They help to detect and locate any damage or degradation and alert the maintenance crew.

## Sensors for Manufacturing

- Sensors are vital for manufacturing applications being used for process control, quality inspection, automation, robotics, etc. Sensors are also used for improving the efficiency, productivity, and safety of the manufacturing operations and workers.
- Some examples of sensors for manufacturing are:

  - Temperature Sensors: These sensors measure the temperature of the materials, machines, and products during the manufacturing process. They help to ensure the optimal temperature for the process and prevent overheating, melting, or burning of the materials and products.
  - Vision Sensors: These sensors capture and process the images of the materials, machines, and



# Unit 4 - Actuators: Pneumatic and Hydraulic Actuation Systems

## Actuation systems
- An actuation system is a device or mechanism that converts energy into motion or force to perform a task.
- Actuation systems can be classified into three types: mechanical, electrical and fluid power.
- Mechanical actuation systems use gears, levers, springs, cams, etc. to transmit motion or force.
- Electrical actuation systems use electric motors, solenoids, relays, etc. to convert electrical energy into mechanical energy.
- Fluid power actuation systems use pressurized fluids (liquids or gases) to transmit power and control motion or force.

## Pneumatic and hydraulic systems
- Pneumatic and hydraulic systems are types of fluid power actuation systems that use compressed air and pressurized oil respectively as the working fluids.
- Pneumatic systems are suitable for low to medium force and speed applications, such as clamping, lifting, sorting, etc.
- Hydraulic systems are suitable for high force and speed applications, such as pressing, cutting, drilling, etc.
- Pneumatic and hydraulic systems consist of four main components: a power supply, a control unit, an actuator and a transmission line.
- The power supply provides the pressurized fluid to the system. It consists of a compressor or a pump, a reservoir, a filter and a pressure regulator.
- The control unit regulates the flow and direction of the fluid to the actuator. It consists of valves, switches, sensors and logic devices.
- The actuator converts the fluid power into mechanical motion or force. It can be linear or rotary, such as cylinders, motors, etc.
- The transmission line connects the power supply, the control unit and the actuator. It consists of pipes, hoses, fittings and seals.

## Directional control valves
- Directional control valves are devices that control the direction of fluid flow in a pneumatic or hydraulic system.
- Directional control valves can be classified into two types: discrete and continuous.
- Discrete directional control valves have a fixed number of positions, such as two-way, three-way or four-way valves. They are used to switch the fluid flow on or off, or to change the direction of flow between two or more paths.
- Continuous directional control valves have a variable number of positions, such as proportional or servo valves. They are used to modulate the fluid flow by varying the flow rate or pressure.
- Directional control valves can be operated by different methods, such as manual, mechanical, electrical, pneumatic or hydraulic.

## Pressure control valves
- Pressure control valves are devices that regulate the pressure of the fluid in a pneumatic or hydraulic system.
- Pressure control valves can be classified into three types: pressure relief valves, pressure reducing valves and pressure sequence valves.
- Pressure relief valves are used to limit the maximum pressure in a system by opening a bypass path when the pressure exceeds a preset value. They are used to protect the system from overpressure and damage.
- Pressure reducing valves are used to maintain a constant lower pressure in a part of the system by reducing the pressure from a higher source. They are used to provide different pressure levels for different actuators or circuits.
- Pressure sequence valves are used to control the order of operation of multiple actuators by opening or closing a flow path when the pressure reaches a preset value. They are used to perform sequential tasks or logic functions.

## Cylinders
- Cylinders are linear actuators that convert fluid power into linear motion or force.
- Cylinders can be classified into two types: single-acting and double-acting.
- Single-acting cylinders have one port and one piston. They can produce motion or force in one direction only, by extending or retracting the piston. The return stroke is achieved by a spring or an external load.
- Double-acting cylinders have two ports and one piston. They can produce motion or force in both directions, by extending or retracting the piston. The fluid enters and exits the cylinder through the two ports alternately.
- Cylinders can have different designs, such as rod, telescopic, diaphragm, etc.

## Servo and proportional control valves
- Servo and proportional control valves are types of continuous directional control valves that can modulate the fluid flow by varying the flow rate or pressure.
- Servo and proportional control valves can be classified into two types: electrohydraulic and electropneumatic.
- Electrohydraulic servo and proportional control valves use an electric signal to control a hydraulic valve. They are used to control the position, speed or force of a hydraulic actuator.
- Electropneumatic servo and proportional control valves use an electric signal to control a pneumatic valve. They are used to control the position



# Mechanical Actuation Systems

- Mechanical actuation systems are mechanisms that use a source of power to achieve physical movement.
- Mechanical actuation systems are used in countless applications where automated control is needed, such as manufacturing, automotive, robotics, aerospace and defense .
- The most common type of mechanical actuation is a linear actuator, which uses a motor to convert rotational motion into linear (back-and-forth) motion.
- Most mechanical actuation systems are controlled by some type of electronic controller, which activates the actuator when it receives a signal from an input device.

## Types of motion

- There are two main types of motion in mechanical actuation systems: linear and rotary.
- Linear motion is the movement of an object along a straight line, such as a piston or a slider.
- Rotary motion is the movement of an object around a fixed point, such as a wheel or a shaft.
- Linear and rotary motions can be combined to create complex motions, such as helical, elliptical, or circular.

## Kinematic chains

- A kinematic chain is a system of rigid bodies connected by joints that allow relative motion between them.
- A kinematic chain can be classified as open or closed, depending on whether the first and last bodies are connected or not.
- A kinematic chain can also be classified as serial or parallel, depending on whether the bodies are arranged in a single line or in multiple branches.
- A kinematic chain can be used to model the motion of a mechanical actuation system, such as a robot arm or a leg.

## Cams

- A cam is a rotating or sliding piece of metal that has a curved or irregular shape.
- A cam can be used to convert rotary motion into linear or oscillating motion, or vice versa, by interacting with a follower, such as a rod or a lever.
- A cam can also be used to control the timing or sequence of events in a mechanical actuation system, such as a valve or a switch.
- A cam can have different profiles, such as circular, elliptical, or sinusoidal, depending on the desired motion of the follower.

## Gears

- A gear is a toothed wheel that meshes with another toothed wheel to transmit or modify rotary motion.
- A gear can be used to change the speed, torque, or direction of rotation of a mechanical actuation system, such as a motor or a generator.
- A gear can have different types, such as spur, helical, bevel, or worm, depending on the orientation and shape of the teeth.
- A gear can also be part of a gear train, which is a combination of two or more gears that work together to achieve a desired output.

## Ratchet and pawl

- A ratchet and pawl is a mechanism that allows rotary motion in one direction only, and prevents it in the opposite direction.
- A ratchet and pawl consists of a toothed wheel (the ratchet) and a spring-loaded device (the pawl) that engages or disengages with the teeth of the ratchet.
- A ratchet and pawl can be used to maintain or increment the position of a mechanical actuation system, such as a jack or a winch.
- A ratchet and pawl can also be used to convert continuous rotary motion into intermittent linear motion, such as in a clock or a sewing machine.

## Belt and chain drives

- A belt and chain drive is a mechanism that uses a flexible loop (the belt or the chain) to transmit rotary motion between two or more pulleys or sprockets.
- A belt and chain drive can be used to transfer power or motion from one shaft to another, or to multiple shafts, in a mechanical actuation system, such as a conveyor or a bicycle.
- A belt and chain drive can also be used to change the speed, torque, or direction of rotation of a mechanical actuation system, by varying the size or arrangement of the pulleys or sprockets.
- A belt and chain drive can have different types, such as flat, V, or timing belts, or roller, silent, or toothed chains, depending on the material and shape of the loop.

## Bearings

- A bearing is a device that reduces friction and supports load between two moving parts, such as a shaft and a housing.
- A bearing can be used to improve the efficiency, performance, and lifespan of a mechanical actuation system, by reducing wear



# Unit 5 - Introduction of Signal Processing

## Classification of systems

- A system is a set of components that interact to perform a function or achieve a goal.
- A system can be classified according to different criteria, such as:

  - **Continuous or discrete**: A system is continuous if it operates on continuous signals, which are defined for all values of time. A system is discrete if it operates on discrete signals, which are defined only for discrete values of time.
  - **Linear or nonlinear**: A system is linear if it satisfies the principle of superposition, which means that the output of the system for a linear combination of inputs is equal to the same linear combination of the outputs for each input. A system is nonlinear if it does not satisfy this property.
  - **Causal or noncausal**: A system is causal if the output of the system at any time depends only on the input of the system up to that time. A system is noncausal if the output of the system at any time depends on the input of the system in the future.
  - **Stable or unstable**: A system is stable if the output of the system remains bounded for any bounded input. A system is unstable if the output of the system becomes unbounded for some bounded input.
  - **Dynamic or static**: A system is dynamic if the output of the system at any time depends on the input of the system and the state of the system at that time. A system is static if the output of the system at any time depends only on the input of the system at that time.
  - **Recursive or nonrecursive**: A system is recursive if the output of the system at any time depends on the input of the system and the output of the system at previous times. A system is nonrecursive if the output of the system at any time depends only on the input of the system at that time.
  - **Time-invariant or time-varying**: A system is time-invariant if the output of the system for a given input does not change when the input is shifted in time. A system is time-varying if the output of the system for a given input changes when the input is shifted in time.

## Classification of signals

- A signal is a function that conveys information about a phenomenon or a system.
- A signal can be classified according to different criteria, such as:

  - **Continuous or discrete**: A signal is continuous if it is defined for all values of time. A signal is discrete if it is defined only for discrete values of time.
  - **Energy or power**: A signal is energy if it has a finite amount of energy, which is the integral of the square of the signal over all time. A signal is power if it has a finite average power, which is the limit of the average of the square of the signal over a finite interval as the interval tends to infinity.
  - **Periodic or aperiodic**: A signal is periodic if it repeats itself after a fixed interval of time, called the period. A signal is aperiodic if it does not repeat itself after any interval of time.
  - **Even or odd**: A signal is even if it is symmetric about the origin, which means that the signal is equal to its mirror image. A signal is odd if it is antisymmetric about the origin, which means that the signal is equal to the negative of its mirror image.
  - **Deterministic or random**: A signal is deterministic if it can be predicted exactly for any time. A signal is random if it cannot be predicted exactly for any time, but it can be described by a probability distribution.

## Mathematical representation of signals

- A signal can be represented mathematically by different methods, such as:

  - **Time-domain representation**: A signal is represented by a function of time, which shows the variation of the signal with respect to time.
  - **Frequency-domain representation**: A signal is represented by a function of frequency, which shows the distribution of the signal energy or power over different frequencies.
  - **Spectral density**: A signal is represented by a function of frequency, which shows the density of the signal energy or power per unit frequency.
  - **Transform-domain representation**: A signal is represented by a function of a complex variable, which is obtained by applying a mathematical transform to the signal, such as the Fourier transform, the Laplace transform, or the Z-transform.

## Sampling techniques

- Sampling is the process of converting a continuous signal into a discrete signal by taking samples of the signal at regular intervals of time, called the sampling period or the sampling interval.
- Sampling techniques are methods of choosing the sampling period or the sampling interval to preserve the information of the signal as much as possible, such as:

  - **



# Digital signal representation

- A digital signal is a signal that represents data as a sequence of discrete values; at any given time it can only take on, at most, one of a finite number of values.
- A digital signal is an abstraction that is discrete in time and amplitude. The signal's value only exists at regular time intervals, since only the values of the corresponding physical signal at those sampled moments are significant for further digital processing.
- A digital signal is a sequence of codes drawn from a finite set of values. The codes can be binary digits (bits), decimal digits, or any other discrete symbols.
- Digital signals are represented by square waves. In digital signals 1 is represented by having a positive voltage and 0 is represented by having no voltage or zero voltage as shown in figure.

Figure: Digital signal representation

- Digital signals can be processed by digital signal processing (DSP), which is the use of digital processing, such as by computers or more specialized digital signal processors, to perform a wide variety of signal processing operations.
- Digital signals can be transmitted by digital circuits, such as logic gates, which use voltage signals measured in reference to a common circuit point called ground. The absence of voltage represents a binary “0” and the presence of full DC supply voltage represents a binary “1”.



# Digital Signal Processors: Introduction – Architecture – Features – Addressing Formats – Functional modes – Introduction to Commercial Processors

- **Introduction**: Digital Signal Processing (DSP) is the process of representing signals in a discrete mathematical sequence of numbers and analyzing, modifying, and extracting the information contained in the signal by carrying out algorithmic operations and processing on the signal. DSP involves the process of the real-world signals which are represented and converted by a sequence of numbers. Digital Signal Processors (DSP) are specialized microprocessors that are designed to perform DSP operations efficiently and quickly.
- **Architecture**: The architecture of a DSP is determined by the type of operations it needs to perform, the data types it supports, the memory organization, the instruction set, and the input/output interfaces. Some common features of DSP architectures are :
  - **Multiple functional units**: DSPs typically have multiple functional units that can operate in parallel, such as arithmetic logic units (ALUs), multipliers, shifters, accumulators, etc. These units can perform different types of operations on different types of data, such as fixed-point, floating-point, complex, etc.
  - **Pipelining**: DSPs use pipelining to increase the throughput of the functional units. Pipelining is the technique of dividing an operation into several stages and executing them in parallel on different data. For example, a multiplier can be divided into four stages: partial product generation, partial product alignment, partial product addition, and final result. Each stage can process a different data item in parallel, thus increasing the speed of the multiplier.
  - **Harvard architecture**: DSPs use a Harvard architecture, which means that they have separate memory spaces for instructions and data. This allows the DSP to fetch instructions and data simultaneously, thus reducing the memory access latency and increasing the performance. Additionally, DSPs may have multiple data buses and multiple data memories to support parallel data transfers and operations.
  - **Specialized addressing modes**: DSPs have specialized addressing modes that support efficient access to data in different memory locations and formats. For example, DSPs may have circular addressing, which allows the DSP to access data in a circular buffer without updating the address pointer; bit-reversed addressing, which allows the DSP to access data in a bit-reversed order for fast Fourier transform (FFT) operations; and modulo addressing, which allows the DSP to access data in a modulo arithmetic fashion for convolution and correlation operations.
  - **Very long instruction word (VLIW) or single instruction multiple data (SIMD) instruction set**: DSPs may use a VLIW or a SIMD instruction set to exploit the parallelism of the functional units and the data. A VLIW instruction is a long instruction that contains multiple operations that can be executed in parallel by different functional units. A SIMD instruction is a single instruction that operates on multiple data items in parallel by the same functional unit. Both VLIW and SIMD instructions increase the instruction-level parallelism and the performance of the DSP.
- **Features**: The features of DSPs include the following :
  - **High performance**: DSPs are mainly designed for supporting repetitive and numerically intensive tasks, such as filtering, convolution, FFT, etc. Most DSPs include a powerful data path and also the capacity to move large amounts of data to memory quickly. DSPs can also perform operations in a single cycle or a few cycles, thus achieving high performance.
  - **Low power consumption**: DSPs are often used in battery-powered or energy-constrained applications, such as mobile phones, audio/video devices, etc. Therefore, DSPs are designed to consume low power while maintaining high performance. DSPs may use techniques such as clock gating, dynamic voltage and frequency scaling, power management modes, etc. to reduce the power consumption.
  - **Programmability**: DSPs are programmable devices that can be configured to perform different types of DSP operations according to the application requirements. DSPs may have a general-purpose instruction set or a specialized instruction set that supports common DSP operations. DSPs may also have a software development environment that provides tools such as compilers, debuggers, simulators, etc. to facilitate the programming of the DSP.
  - **Flexibility**: DSPs are flexible devices that can adapt to changing application requirements and standards. DSPs can be reprogrammed or updated with new software or firmware to support new features or functions. DSPs can also be integrated with other devices or components, such as analog-to-digital converters (ADCs), digital-to-analog converters (

