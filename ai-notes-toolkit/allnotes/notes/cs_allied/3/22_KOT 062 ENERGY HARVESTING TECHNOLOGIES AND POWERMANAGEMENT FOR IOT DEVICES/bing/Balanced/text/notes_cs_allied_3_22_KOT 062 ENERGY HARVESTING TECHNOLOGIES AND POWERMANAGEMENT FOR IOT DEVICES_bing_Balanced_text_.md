

# KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES

- Energy harvesting is a promising solution to power IoT devices especially when they are installed in inaccessible areas and regular battery maintenance is not possible.
- Energy harvesting captures energy from ambient sources such as RF waves, light, thermal gradients, or mechanical motion to power IoT devices.
- Energy harvesting based on a renewable source enables IoT devices to generate electrical energy by absorbing energy from the environment.
- Energy harvesting can extend the life cycle of the device and eliminate the constraint of fixed charge batteries as an energy source.
- Energy harvesting can also reduce the environmental impact of battery disposal and enhance the sustainability of the IoT.
- Energy harvesting and power management techniques at the circuit, device, and system levels are crucial for the IoT devices in the 5G era.
- Energy harvesting and power management techniques include:
  - Designing low-power circuits and devices that can operate with low voltage and current.
  - Developing efficient energy conversion and storage mechanisms that can match the harvested energy with the device power consumption.
  - Implementing adaptive and intelligent algorithms that can optimize the energy usage and performance of the IoT devices.
  - Integrating multiple energy harvesting sources and hybrid energy storage systems to increase the reliability and availability of the IoT devices.
  - Exploring novel energy harvesting materials and methods that can harvest energy from new sources such as body heat, sound, or vibration.
- Energy harvesting techniques for IoT face some challenges such as:
  - The variability and unpredictability of the ambient energy sources.
  - The trade-off between the size, cost, and efficiency of the energy harvesting and storage components.
  - The compatibility and interoperability of the energy harvesting and power management solutions with the existing IoT standards and protocols.
  - The security and privacy issues related to the energy harvesting and power management data and algorithms.



# KCS

- KCS stands for Knowledge-Centered Service, a methodology for creating and maintaining knowledge as a key asset of an organization.
- KCS is based on four basic principles: 
  - Integrate the creation and maintenance of knowledge into the problem-solving process.
  - Evolve content based on demand and usage.
  - Develop a knowledge base of collective experience.
  - Reward learning, collaboration, sharing, and improvement.
- KCS has two main processes: the Solve Loop and the Evolve Loop.
  - The Solve Loop focuses on capturing, structuring, and reusing knowledge at the point of interaction with customers or users.
  - The Evolve Loop focuses on analyzing, improving, and governing the knowledge base and the KCS practices.
- KCS has six core practices that support the principles and processes: 
  - Capture: create knowledge as a by-product of solving issues, using the customer's context and words.
  - Structure: use a standard template and metadata to make knowledge easy to find and use.
  - Reuse: search the knowledge base before solving an issue, and reuse existing knowledge whenever possible.
  - Improve: flag, fix, or flag and fix any errors or gaps in the knowledge base, and provide feedback to the authors.
  - Publish: make knowledge available to the intended audience, with the appropriate level of access and quality.
  - Measure: monitor and evaluate the performance and value of the knowledge base and the KCS practices, using both activity and outcome metrics.



## Unit 1 - ENERGY HARVESTING SYSTEMS

- Energy harvesting systems are devices or systems that are used to convert ambient energy, which is derived from external sources existing in the atmosphere, into electrical energy.
- Energy harvesting systems are attractive alternatives to battery-operated systems, especially for long-term, low-power, and self-sustaining electronic systems.
- Energy harvesting systems can scavenge and convert various sources of energy, such as mechanical load, vibrations, temperature gradients, light, etc., into small levels of power in the nW-mW range .
- Energy harvesting systems require interface circuits to control and regulate the flows of energy between the energy source, the energy storage, and the load.
- Energy harvesting systems have various applications, such as body sensor networks, inaccessible remote systems, oceanographic monitoring sensors, wireless sensor networks, etc .
- Energy harvesting systems can be classified into different types based on the energy source, such as solar, thermal, piezoelectric, electromagnetic, electrostatic, etc .
- Energy harvesting systems can also be classified into different types based on the energy conversion mechanism, such as levitation based, resonant based, nonlinear based, etc.



### Introduction

- Energy harvesting (EH) is the process of capturing and converting ambient energy from various sources such as light, heat, vibration, and radio frequency into usable electrical energy.
- Energy harvesting systems (EHS) are devices or circuits that utilize EH techniques to power low-power electronic systems such as sensors, actuators, microcontrollers, and wireless communication modules.
- EHS can provide a sustainable and maintenance-free alternative to batteries, especially for applications where battery replacement is impractical, costly, or hazardous, such as in remote, inaccessible, or implanted devices.
- EHS can also extend the lifetime and functionality of battery-powered devices by supplementing or recharging the batteries with harvested energy.
- EHS typically consist of four main components: an energy transducer, an energy storage element, a power management unit, and a load.
- An energy transducer is a device that converts one form of energy into another, such as a photovoltaic cell that converts light into electricity, a thermoelectric generator that converts heat into electricity, or a piezoelectric element that converts mechanical stress or strain into electricity.
- An energy storage element is a device that stores electrical energy for later use, such as a capacitor, a battery, or a supercapacitor.
- A power management unit is a circuit that regulates and controls the flow of energy between the transducer, the storage element, and the load, such as a DC-DC converter, a maximum power point tracker, or a battery charger.
- A load is the device or system that consumes the electrical energy provided by the EHS, such as a sensor, an actuator, a microcontroller, or a wireless communication module.



### Energy sources for the notes of the Unit 1 - ENERGY HARVESTING SYSTEMS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting is the process by which energy is derived from external sources (e.g., solar power, thermal energy, wind energy, salinity gradients, and kinetic energy, also known as ambient energy), and then stored for use by small, wireless autonomous devices, like sensors, microcontrollers, and actuators.
- Energy sources for energy harvesting include:
  - **Motion/mechanical energy** — Motion or mechanical energy is the energy associated with the movement or deformation of objects or materials. It can be harvested from sources such as body movements, animal movements, vehicle vibrations, wind turbines, ocean waves, and piezoelectric materials .
  - **Light energy** — Light energy is the energy carried by electromagnetic radiation, such as visible light, infrared, ultraviolet, and radio waves. It can be harvested from sources such as natural or artificial light, using photovoltaic (PV) cells, which are made of materials that convert light into an electrical current .
  - **Thermal energy** — Thermal energy is the energy related to the temperature difference between two objects or systems. It can be harvested from sources such as waste heat, body heat, geothermal heat, solar radiation, and thermoelectric materials, which are made of materials that generate an electrical voltage when exposed to a temperature gradient .
  - **RF energy** — RF energy is the energy carried by radio frequency (RF) signals, such as Wi-Fi, Bluetooth, cellular, and TV signals. It can be harvested from sources such as wireless transmitters, antennas, and RF energy harvesters, which are devices that can transform RF energy into electrical energy .
  - **Chemical energy** — Chemical energy is the energy stored in the bonds of chemical compounds, such as batteries, fuels, and biomolecules. It can be harvested from sources such as batteries, fuel cells, biofuel cells, and enzymatic fuel cells, which are devices that can convert chemical energy into electrical energy .



### Energy Harvesting Based Sensor Networks

- Energy harvesting based sensor networks are wireless sensor networks that use ambient energy sources such as solar, wind, thermal, vibration, etc. to power the sensor nodes and extend their lifetime .
- Energy harvesting based sensor networks have several advantages over battery-powered sensor networks, such as:
  - Reduced maintenance cost and environmental impact of replacing batteries.
  - Increased reliability and scalability of the network.
  - Enhanced flexibility and adaptability of the network to different environments and applications.
- Energy harvesting based sensor networks have several challenges, such as:
  - Intermittent and unpredictable nature of the energy sources.
  - Trade-off between energy consumption and quality of service (QoS) of the network.
  - Need for efficient energy management and routing protocols to optimize the network performance.
- Energy harvesting based sensor networks can be classified into two types based on the energy storage unit of the sensor nodes:
  - Battery-less sensor nodes: These nodes do not have any energy storage unit and operate only when the energy source is available. They have low cost and high efficiency, but also low reliability and QoS.
  - Battery-assisted sensor nodes: These nodes have a rechargeable battery or a supercapacitor as an energy storage unit and can operate even when the energy source is not available. They have high reliability and QoS, but also high cost and low efficiency.
- Energy harvesting based sensor networks can be applied to various domains, such as:
  - Environmental monitoring: These networks can monitor parameters such as temperature, humidity, air quality, water quality, etc. in different ecosystems and provide real-time data for analysis and decision making.
  - Industrial automation: These networks can monitor and control the processes and machines in factories and plants and improve the productivity and safety of the operations.
  - Healthcare: These networks can monitor the vital signs and activities of patients and provide remote diagnosis and treatment. They can also use alternative energy sources such as body heat, motion, and sweat to power the sensor nodes.



### Photovoltaic Cell Technologies

- Photovoltaic (PV) technologies are devices that absorb energy from sunlight and convert it into electrical energy through semiconducting materials.
- PV devices are also called solar cells, and they are based on the photovoltaic effect, which is the process of converting light (photons) to electricity (voltage).
- A single PV cell is usually small, producing about 1 or 2 watts of power, and is made of different semiconductor materials, such as silicon, cadmium telluride, copper indium gallium selenide, or perovskites .
- PV cells are connected together in chains to form larger units known as modules or panels, which can be mounted on rooftops, ground, or other structures to generate electricity for various applications.
- PV technologies can be classified into three main categories based on the type and arrangement of the semiconductor materials: crystalline silicon (c-Si), thin-film, and emerging PV.
- Crystalline silicon PV is the most widely used and mature technology, accounting for about 90% of the global PV market. It uses wafers of high-purity silicon that are either monocrystalline (single crystal) or polycrystalline (multiple crystals) in structure.
- Thin-film PV is a newer and cheaper technology that uses thin layers of semiconductor materials deposited on a substrate, such as glass, metal, or plastic. It has lower efficiency and durability than c-Si, but it can be flexible, lightweight, and adaptable to different surfaces and shapes. Some examples of thin-film PV materials are cadmium telluride (CdTe), copper indium gallium selenide (CIGS), and amorphous silicon (a-Si).
- Emerging PV is a category that includes novel and experimental PV materials and devices that have the potential to achieve higher efficiency, lower cost, or new functionalities. Some examples of emerging PV technologies are perovskites, organic PV, quantum dots, dye-sensitized solar cells, and multijunction solar cells.



### Generation of electric power in semiconductor PV cells

- PV cells or photovoltaic cells are devices that convert solar energy into electricity directly using the photovoltaic effect .
- The photovoltaic effect is the phenomenon of generating electric voltage or current in a material when it is exposed to light .
- The PV cell is composed of semiconductor material, such as silicon, which can conduct electricity better than an insulator but not as well as a metal .
- The semiconductor material is usually doped with impurities to create two layers: a p-type layer with excess positive charge carriers (holes) and an n-type layer with excess negative charge carriers (electrons) .
- The junction between the p-type and n-type layers is called the p-n junction, which forms an electric field that prevents the charge carriers from crossing over .
- When the semiconductor is exposed to sunlight, it absorbs the light, transferring the energy to the electrons in the n-type layer .
- Some of the electrons gain enough energy to overcome the electric field and cross the p-n junction to the p-type layer, creating a flow of electric current .
- The current can be extracted by connecting metal contacts to the p-type and n-type layers, forming a circuit .
- The voltage generated by the PV cell depends on the material and the intensity of the light, while the current depends on the area of the cell and the efficiency of the conversion .
- The power generated by a single PV cell is typically only about two watts, so multiple cells are connected in series or parallel to form a PV module or panel, which can produce more power .
- The PV modules or panels can be further connected to form a PV array or system, which can provide electricity for various applications, such as homes, buildings, or grids .



### Types of Energy Harvesting Systems

- Energy harvesting systems are devices or systems that convert ambient energy from external sources into electrical energy.
- The sources of ambient energy can be mechanical, thermal, electromagnetic, or chemical, depending on the environment and application.
- The types of energy harvesting systems can be classified based on the following criteria:

  - The type of energy source: vibration, solar, thermal, wind, RF, etc.
  - The type of energy conversion: piezoelectric, photovoltaic, thermoelectric, electromagnetic, electrostatic, etc.
  - The type of energy storage: capacitor, battery, supercapacitor, etc.
  - The type of energy management: power conditioning, power management, power conversion, etc.
  - The type of energy consumption: sensor, actuator, communication, computation, etc.

- Some examples of energy harvesting systems are:

  - Vibration energy harvesting system: a system that converts mechanical vibrations into electrical energy using piezoelectric, electromagnetic, or electrostatic transducers. The system can be used to power wireless sensors, wearable devices, or structural health monitoring systems.
  - Solar energy harvesting system: a system that converts solar radiation into electrical energy using photovoltaic cells. The system can be used to power remote devices, smart buildings, or environmental monitoring systems.
  - Thermal energy harvesting system: a system that converts temperature gradients or waste heat into electrical energy using thermoelectric generators. The system can be used to power biomedical implants, industrial sensors, or automotive systems.
  - Wind energy harvesting system: a system that converts wind flow into electrical energy using micro-turbines, piezoelectric beams, or flapping wings. The system can be used to power wireless sensor networks, weather stations, or small-scale applications.
  - RF energy harvesting system: a system that converts radio frequency signals into electrical energy using antennas, rectifiers, or resonators. The system can be used to power RFID tags, wireless sensors, or low-power devices.



## Unit 2 - Piezoelectric Energy Harvesting and Electromechanical Modeling

- Piezoelectric energy harvesting is the process of converting mechanical energy into electrical energy using piezoelectric materials, which are materials that generate electric charge when subjected to mechanical stress or strain.
- Piezoelectric energy harvesters are devices that utilize piezoelectric materials to scavenge energy from ambient vibrations, such as wind, traffic, human motion, etc.
- Piezoelectric energy harvesters can be used to power low-power electronic devices, such as wireless sensors, microcontrollers, LED lights, etc., without the need for batteries or external power sources.
- Electromechanical modeling of piezoelectric energy harvesters is the mathematical description of the coupled dynamics of the mechanical and electrical domains of the system, which can be used to analyze, design, and optimize the performance of the device.
- Electromechanical modeling of piezoelectric energy harvesters can be classified into two main approaches: lumped-parameter modeling and distributed-parameter modeling.
- Lumped-parameter modeling assumes that the piezoelectric energy harvester can be represented by a finite number of discrete elements, such as masses, springs, dampers, capacitors, etc., connected by ideal nodes. This approach is simple and convenient, but may not capture the effects of higher modes, geometric nonlinearities, or complex boundary conditions.
- Distributed-parameter modeling considers the piezoelectric energy harvester as a continuous system, such as a beam, plate, or shell, with spatially varying properties and fields. This approach is more accurate and general, but may require more computational effort and mathematical complexity.
- Depending on the type and configuration of the piezoelectric energy harvester, different distributed-parameter models can be used, such as Euler-Bernoulli beam theory, Timoshenko beam theory, Kirchhoff plate theory, Mindlin plate theory, etc.
- Distributed-parameter models can be derived using various methods, such as Hamilton's principle, Lagrange's equation, variational methods, finite element methods, etc.
- Distributed-parameter models can be solved using various techniques, such as modal analysis, Galerkin's method, Rayleigh-Ritz method, etc.
- Distributed-parameter models can be validated using experimental data, such as natural frequencies, mode shapes, voltage output, power output, etc.



### Piezoelectric materials

- Piezoelectric materials are materials that can convert mechanical stress into electrical charge or vice versa. This phenomenon is called the piezoelectric effect .
- Piezoelectric materials can be broadly classified into the following categories:
  - Crystalline materials, such as quartz, SiO2, which is the best known natural piezoelectric material.
  - Ceramic materials, such as lead zirconate titanate (PZT), barium titanate, and lead titanate, which are the most commonly produced and widely used synthetic piezoelectric materials . They have high piezoelectric coefficients and can be easily shaped and polarized.
  - Polymeric materials, such as polyvinylidene fluoride (PVDF), which have low piezoelectric coefficients but high flexibility and sensitivity.
  - Semiconductor materials, such as zinc oxide (ZnO) and gallium nitride (GaN), which have relatively wide band gaps and can be used as piezoelectric sensors and actuators.
  - Composite materials, which are combinations of different piezoelectric materials or piezoelectric materials and non-piezoelectric materials, such as epoxy or metal. They can have improved properties and performance compared to single-phase piezoelectric materials.
  - Glass-ceramic materials, such as lithium disilicate (Li2Si2O5) and barium titanate silicate (Ba2TiSiO6), which are formed by controlled crystallization of glass. They have high mechanical strength and thermal stability.
- Piezoelectric materials have useful applications in many industries, such as energy harvesting, sensing, actuation, power monitoring, microbalances, strain gauges, and medical treatment  .



### Transducers for Piezoelectric Energy Harvesting

- A transducer is a device that converts one form of energy into another. In the context of piezoelectric energy harvesting, a transducer converts mechanical energy (such as vibration, pressure, or strain) into electrical energy (such as voltage or current).
- The principle of piezoelectric energy harvesting is based on the direct piezoelectric effect, which is the property of some materials to generate an electric field when a mechanical force is applied .
- Piezoelectric transducers can be made of different shapes and materials, depending on the application and the desired performance. Some common shapes are cantilever beams, cylindrical rods, plates, and rings. Some common materials are ceramics, polymers, and composites  .
- The performance of a piezoelectric energy harvester depends on several factors, such as the frequency and amplitude of the mechanical input, the impedance matching between the transducer and the load, the electrical circuit configuration, and the environmental conditions .
- The advantages of piezoelectric energy harvesting are that it can scavenge energy from ambient sources, such as traffic, wind, or human motion, and that it can power low-power devices, such as sensors, wireless transmitters, or microelectromechanical systems (MEMS)  .
- The challenges of piezoelectric energy harvesting are that it requires a high mechanical input to generate a significant electrical output, that it suffers from low conversion efficiency and power density, and that it may degrade over time due to fatigue, aging, or environmental factors  .



### Harvesters

- Harvesters are devices that convert ambient energy sources, such as mechanical vibrations, into electrical energy.
- Piezoelectric harvesters are a type of harvester that use piezoelectric materials, which generate electric charge when subjected to mechanical stress or strain.
- Piezoelectric harvesters can be used to power low-power electronic devices, such as wireless sensors, without the need for batteries or external power sources.
- Piezoelectric harvesters can be designed in various shapes and configurations, such as cantilevers, beams, plates, or shells, depending on the application and the type of excitation.
- Piezoelectric harvesters can be excited by different forms of mechanical energy, such as base vibrations, fluid flow, acoustic waves, or human motion.

### Electromechanical Modeling

- Electromechanical modeling is the process of developing mathematical models that describe the coupled mechanical and electrical behavior of piezoelectric harvesters.
- Electromechanical modeling can help to understand the performance, optimize the design, and predict the output of piezoelectric harvesters under various operating conditions.
- Electromechanical modeling can be done at different levels of complexity and accuracy, depending on the assumptions and simplifications made.
- Electromechanical modeling can be classified into two main approaches: lumped-parameter modeling and distributed-parameter modeling.

#### Lumped-parameter modeling

- Lumped-parameter modeling is an approach that treats the piezoelectric harvester as a system of discrete masses, springs, and dampers, connected by ideal electrical elements, such as capacitors and resistors.
- Lumped-parameter modeling is based on the assumption that the harvester has one or a few dominant modes of vibration, and that the piezoelectric effect is uniform across the material.
- Lumped-parameter modeling is simpler and faster than distributed-parameter modeling, but it may not capture the effects of higher modes, geometric nonlinearities, or non-uniform piezoelectricity.

#### Distributed-parameter modeling

- Distributed-parameter modeling is an approach that treats the piezoelectric harvester as a continuous medium, with spatially varying mechanical and electrical properties.
- Distributed-parameter modeling is based on the application of partial differential equations, such as the Euler-Bernoulli beam equation or the Kirchhoff plate equation, coupled with the piezoelectric constitutive equations.
- Distributed-parameter modeling is more accurate and general than lumped-parameter modeling, but it may require numerical methods, such as finite element analysis or finite difference methods, to solve the equations.



### Microgenerators for Piezoelectric Energy Harvesting

- Piezoelectric energy harvesting is a technique that converts mechanical vibrations into electrical energy using piezoelectric materials.
- Piezoelectric materials are materials that generate an electric charge when they are subjected to mechanical stress or strain.
- Piezoelectric energy harvesting devices can be classified into two types: MEMS generators and nanogenerators.
- MEMS generators are micro-scale devices that use thin-film piezoelectric materials to harvest energy from ambient vibrations .
- Nanogenerators are nano-scale devices that use nanostructures of piezoelectric materials to harvest energy from various sources, such as body movements, wind, water, and sound .
- Piezoelectric energy harvesting devices can be used as an alternative or complementary energy source for powering wireless sensor devices, such as those used in aerospace, automotive, biomedical, and environmental applications .
- Piezoelectric energy harvesting devices have several advantages, such as high power density, wide frequency range, simple structure, and compatibility with MEMS and nanotechnology .
- Piezoelectric energy harvesting devices also have some challenges, such as low output voltage, nonlinear behavior, impedance mismatch, and environmental effects .
- Piezoelectric energy harvesting devices can be improved by using hybrid piezo-triboelectric nanogenerators, which combine the piezoelectric and triboelectric effects to enhance the energy conversion efficiency and output performance.
- Piezoelectric energy harvesting devices can also be integrated with multifunctional composites, such as carbon fiber reinforced polymers, to optimize the layup design and mechanical properties for energy harvesting applications.



### Strategies for enhancing the performance of energy harvesters

- Energy harvesters are devices that convert ambient energy sources, such as vibration, wind, or light, into electrical energy for powering low-power consumption devices, such as sensors, wireless transmitters, or wearable electronics.
- Energy harvesters can be classified into different types based on the energy conversion mechanism, such as piezoelectric, electromagnetic, electrostatic, thermoelectric, or triboelectric.
- Piezoelectric energy harvesters (PEHs) are one of the most widely studied and applied types of energy harvesters, as they can convert mechanical strain into electrical charge and vice versa, using piezoelectric materials, such as PZT, PVDF, or ZnO.
- PEHs can be designed in various configurations, such as cantilever, bridge, or bimorph, depending on the vibration mode, frequency range, and output power requirement.
- However, PEHs also face some challenges and limitations, such as low power density, narrow bandwidth, and frequency mismatch with ambient vibrations, which affect their performance and efficiency.
- Therefore, various strategies have been proposed and investigated to enhance the performance of PEHs, such as:

  - Adopting new materials or composites with higher piezoelectric coefficients, such as relaxor ferroelectrics, lead-free piezoceramics, or piezoelectric nanowires.
  - Optimizing the geometry, size, or shape of the piezoelectric element, such as using tapered, curved, or spiral structures, to increase the strain distribution and output voltage.
  - Introducing nonlinear elements, such as magnets, springs, or bistable mechanisms, to induce nonlinear behaviors, such as snap-through, chaos, or frequency up-conversion, which can widen the bandwidth and enhance the power output of PEHs.
  - Applying power-amplifying strategies, such as using elastic foundations, mechanical amplifiers, or synchronized switching techniques, to increase the effective displacement and force of the piezoelectric element and improve the power conversion efficiency.
  - Integrating multiple PEHs in series or parallel, or hybridizing PEHs with other energy harvesting technologies, such as electromagnetic, electrostatic, or triboelectric, to harvest energy from multiple vibration modes, directions, or sources, and increase the total power output and reliability of the energy harvesting system.



### Electromechanical modeling of Lumped parameter model and coupled distributed parameter models and closed-form solutions

- Electromechanical modeling is the process of describing the dynamic behavior of systems that involve both electrical and mechanical components, such as piezoelectric devices.
- Lumped parameter model is a simplified representation of a system that assumes that the system parameters (such as resistance, capacitance, inductance, etc.) are constant and uniform throughout the system, and that the system can be divided into discrete elements connected by nodes with zero electrical length and capacitance to ground.
- Coupled distributed parameter model is a more realistic representation of a system that takes into account the spatial variation of the system parameters, the finite electrical length and capacitance to ground of the nodes, and the interaction between different parts of the system.
- Closed-form solution is an analytical expression that can be obtained for the system response without using numerical methods, such as differential equations, integrals, etc.
- An example of a system that can be modeled by both lumped parameter and coupled distributed parameter models is a cantilevered piezoelectric energy harvester, which is a device that converts mechanical vibrations into electrical energy using the piezoelectric effect.
- A lumped parameter model of a piezoelectric energy harvester can be derived by applying Kirchhoff's laws and Newton's second law to the equivalent circuit of the device, which consists of a resistor, an inductor, a capacitor, and a voltage source representing the piezoelectric effect.
- A coupled distributed parameter model of a piezoelectric energy harvester can be derived by applying the Euler-Bernoulli beam theory and the constitutive equations of the piezoelectric material to the differential equations of motion and charge of the device, which account for the bending, stretching, and coupling effects of the piezoelectric beam.
- A closed-form solution for the lumped parameter model of a piezoelectric energy harvester can be obtained by solving the characteristic equation of the system, which is a second-order polynomial equation that relates the natural frequency and the damping ratio of the system to the system parameters.
- A closed-form solution for the coupled distributed parameter model of a piezoelectric energy harvester can be obtained by applying the Galerkin method, which is a technique that reduces the partial differential equations of the system to a set of ordinary differential equations by using a set of basis functions that satisfy the boundary conditions of the system.



## Unit 3 - ELECTROMAGNETIC ENERGY HARVESTING AND NON-LINEAR TECHNIQUES

- Electromagnetic energy harvesting is the process of converting ambient electromagnetic radiation into electrical energy for powering low-power devices.
- Non-linear techniques are methods that exploit the non-linear behavior of some components or systems to enhance the performance of energy harvesting devices.
- Some of the advantages of non-linear techniques are:
  - They can increase the bandwidth of the energy harvesting device by allowing it to operate over a wider range of frequencies or amplitudes.
  - They can improve the efficiency of the energy harvesting device by optimizing the impedance matching between the source and the load.
  - They can reduce the sensitivity of the energy harvesting device to environmental variations or disturbances.
- Some of the challenges of non-linear techniques are:
  - They can introduce complexity and instability in the design and analysis of the energy harvesting device.
  - They can require additional components or circuits that may increase the cost and size of the energy harvesting device.
  - They can generate unwanted harmonics or noise that may interfere with the signal quality or the functionality of the device.
- Some of the examples of non-linear techniques are:
  - Non-linear electromagnetic energy harvesters that use magnets, springs, or bistable mechanisms to create non-linear oscillations or vibrations in a coil or a magnet that induce an alternating current in a load  .
  - Non-linear interface circuits that use diodes, switches, or capacitors to rectify, regulate, or store the output voltage or current of the energy harvesting device.
  - Non-linear power management circuits that use DC-DC converters, charge pumps, or batteries to adjust, boost, or store the output power of the energy harvesting device.
  - Non-linear load circuits that use LEDs, sensors, or wireless transmitters to modulate, consume, or transmit the output power of the energy harvesting device.
  - Magnetic levitation-based electromagnetic energy harvesters that use permanent magnets, electromagnets, or superconductors to levitate a magnet or a coil that oscillates or rotates in a magnetic field and generates an electric power .
  - Hybrid energy harvesters that combine different energy transduction methods, such as thermoelectric, piezoelectric, electromagnetic, electrostatic, or triboelectric, to harvest multiple types of energy sources, such as heat, vibration, light, or friction.



### Basic principles for the notes of the Unit 3 - ELECTROMAGNETIC ENERGY HARVESTING AND NON-LINEAR TECHNIQUES in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Electromagnetic energy harvesting (EMEH) is a process of converting ambient mechanical vibrations into electrical energy using electromagnetic transducers .
- EMEH devices typically consist of a coil and a magnet, which induce a voltage across the coil when they move relative to each other due to external vibrations .
- EMEH devices can be classified into linear and nonlinear types, depending on the restoring force of the system.
- Linear EMEH devices have a constant restoring force and a fixed natural frequency, which limits their bandwidth and power output.
- Nonlinear EMEH devices have a variable restoring force and a frequency-dependent natural frequency, which enables them to adapt to different vibration frequencies and enhance their power output.
- Nonlinear EMEH devices can be realized by using magnetic levitation, bistable mechanisms, snap-through buckling, or other nonlinear elements  .
- Nonlinear EMEH devices require suitable interface circuits and power management circuits to optimize the power transfer and storage.
- EMEH devices can be used for self-powered wireless sensor nodes, wearable electronics, biomedical implants, and other applications that require low power and long lifetime .



### Micro fabricated coils and magnetic materials

- Micro fabricated coils are miniature coils that are made using micro fabrication techniques such as lithography, electroplating, etching, etc.  
- Micro fabricated coils can be used for various applications such as magnetooptical data storage, electromagnetic energy harvesting, magnetic neurostimulation, etc.   
- Micro fabricated coils can be classified into two types: planar and three-dimensional. Planar coils are fabricated on a single layer of substrate, while three-dimensional coils are fabricated on multiple layers of substrate or in a vertical direction. 
- Micro fabricated coils can have different shapes such as spiral, square, circular, rectangular, etc. The shape of the coil affects its inductance, resistance, and magnetic field distribution. 
- Micro fabricated coils can be integrated with magnetic materials to form magnetic circuits that enhance the performance of the coils. Magnetic materials can be either soft or hard, depending on their coercivity and remanence. Soft magnetic materials have low coercivity and high permeability, while hard magnetic materials have high coercivity and low permeability.  
- Micro fabricated coils and magnetic materials have some advantages and disadvantages compared to conventional wound coils and bulk magnets. Some of the advantages are: smaller size, lower weight, higher integration, lower cost, and higher reliability. Some of the disadvantages are: lower power density, lower efficiency, higher heat generation, and higher fabrication complexity.



### Scaling for the notes of the Unit 3 - ELECTROMAGNETIC ENERGY HARVESTING AND NON-LINEAR TECHNIQUES

- Scaling is the study of how the performance of an energy harvesting device changes with its size, frequency, and input acceleration.
- Scaling laws can help to compare different devices, optimize the design parameters, and identify the limitations and challenges of miniaturization.
- Electromagnetic energy harvesting devices (EMEH) are based on the principle of electromagnetic induction, where a coil of wire moves relative to a magnet and generates an electric current.
- The power output of an EMEH device depends on the coil resistance, the number of turns, the magnetic flux density, the velocity of the coil, and the load resistance.
- The power density of an EMEH device is defined as the power output per unit volume or mass of the device.
- The power density of an EMEH device can be expressed as a function of the scaling length, which is a characteristic dimension of the device, such as the coil diameter or the magnet length.
- The power density of an EMEH device can also be expressed as a function of the scaling mass, which is the total mass of the device, including the coil, the magnet, and the supporting structure.
- The power density of an EMEH device can also be expressed as a function of the scaling frequency, which is the natural frequency of the device or the frequency of the input vibration.
- The power density of an EMEH device can also be expressed as a function of the scaling acceleration, which is the amplitude of the input vibration.
- The scaling laws of EMEH devices can be derived from the equations of motion, the electromagnetic coupling, and the power balance of the device.
- The scaling laws of EMEH devices can be verified by experimental data from the literature, where different devices with different sizes, frequencies, and accelerations are compared.
- The scaling laws of EMEH devices can reveal some important insights, such as:
  - The power density increases with the scaling length, but decreases with the scaling mass, frequency, and acceleration.
  - The optimal load resistance decreases with the scaling length, mass, frequency, and acceleration.
  - The electromagnetic damping decreases with the scaling length, mass, frequency, and acceleration.
  - The mechanical quality factor increases with the scaling length, mass, frequency, and acceleration.
  - The efficiency of the device decreases with the scaling length, mass, frequency, and acceleration.
- The scaling laws of EMEH devices can also indicate some challenges and limitations of miniaturization, such as:
  - The power output of the device becomes very small when the size, frequency, or acceleration is reduced.
  - The coil resistance becomes very high when the size or frequency is reduced, which reduces the power output and the efficiency.
  - The magnetic flux density becomes very low when the size is reduced, which reduces the power output and the efficiency.
  - The fabrication and assembly of the device becomes more difficult when the size is reduced, which increases the cost and the variability.
  - The device becomes more sensitive to environmental factors, such as temperature, humidity, and noise, when the size, frequency, or acceleration is reduced.



### Power Maximization Techniques for Electromagnetic Energy Harvesting

- Electromagnetic energy harvesting is the process of converting ambient mechanical vibrations into electrical energy using electromagnetic induction.
- The basic principle of electromagnetic energy harvesting is that a coil of wire moves relative to a permanent magnet, generating an induced voltage across the coil terminals.
- The amount of harvested energy depends on several factors, such as the vibration frequency, the coil size, the magnet strength, the coil resistance, and the load impedance.
- To maximize the harvested energy, the following techniques can be applied:

  - Matching the natural frequency of the harvester to the vibration frequency of the source. This can be achieved by tuning the mass or the stiffness of the harvester, or by using a frequency up-conversion mechanism, such as a bistable or a nonlinear spring.
  - Optimizing the damping factor of the harvester. The damping factor determines the bandwidth and the peak power of the harvester. A low damping factor results in a narrow bandwidth and a high peak power, while a high damping factor results in a wide bandwidth and a low peak power. The optimal damping factor depends on the vibration spectrum and the load impedance of the harvester.
  - Maximizing the magnetic flux density in the coil. This can be achieved by using a strong magnet, a large coil area, a small air gap, and a high permeability core. The magnetic flux density can also be enhanced by using a resonant magnetic circuit, such as a Halbach array or a flux concentrator.
  - Minimizing the coil resistance and the parasitic capacitance. The coil resistance and the parasitic capacitance reduce the output voltage and the power factor of the harvester. The coil resistance can be minimized by using a thick wire, a short wire length, and a low resistivity material. The parasitic capacitance can be minimized by using a thin wire, a large wire spacing, and a low permittivity material.
  - Rectifying and regulating the output voltage. The output voltage of the harvester is an alternating current (AC) signal, which needs to be converted to a direct current (DC) signal to power the load. This can be done by using a rectifier, which is a circuit that allows the current to flow in one direction only. The rectifier can be a diode, a bridge, or a synchronous switch. The rectified voltage can then be regulated by using a DC-DC converter, which is a circuit that adjusts the voltage level to match the load requirements. The DC-DC converter can be a linear regulator, a buck converter, a boost converter, or a buck-boost converter. The rectifier and the DC-DC converter should have a high efficiency and a low power consumption to avoid wasting the harvested energy.



### Micro and Macro Scale Implementations for the Notes of the Unit 3 - Electromagnetic Energy Harvesting and Non-Linear Techniques

- Electromagnetic energy harvesting (EMEH) is a technique that converts ambient mechanical vibrations into electrical energy using electromagnetic induction.
- EMEH can be applied at both micro and macro scales, depending on the size and power requirements of the devices or systems.
- Micro-scale EMEH can be used for powering wireless sensor nodes, biomedical implants, wearable electronics, and other low-power applications.
- Macro-scale EMEH can be used for harvesting energy from large-scale structures, such as bridges, buildings, railways, and wind turbines.
- Non-linear techniques are methods that enhance the performance of EMEH by exploiting the non-linear dynamics of the system, such as bistability, chaos, and magnetic levitation.
- Non-linear techniques can increase the bandwidth, efficiency, and power density of EMEH, as well as enable operation at low frequencies and irregular vibrations.
- Some examples of non-linear techniques are:

  - Non-linear springs, which can create bistable or multi-stable configurations that allow large-amplitude vibrations over a wide frequency range .
  - Non-linear interface circuits, which can optimize the power transfer between the harvester and the load by adjusting the load resistance according to the input voltage.
  - Magnetic levitation, which can reduce the mechanical damping and friction of the system by suspending the moving magnet in the air using repulsive or attractive forces .

- The advantages and disadvantages of micro and macro scale EMEH and non-linear techniques are summarized in the following table:

| Scale/Technique | Advantages | Disadvantages |
| --- | --- | --- |
| Micro-scale EMEH | - Can power small and portable devices without batteries or wires. <br> - Can harvest energy from various sources, such as human motion, acoustic noise, and vibrations. | - Has low power output and efficiency. <br> - Requires complex fabrication and integration processes. <br> - May suffer from environmental and thermal effects. |
| Macro-scale EMEH | - Can harvest large amounts of energy from structural vibrations and wind. <br> - Can improve the reliability and safety of the structures by monitoring their health and condition. | - Has high cost and maintenance requirements. <br> - May cause unwanted interference or resonance with the structures. <br> - May face regulatory and ethical issues. |
| Non-linear techniques | - Can enhance the performance of EMEH by increasing the bandwidth, efficiency, and power density. <br> - Can enable EMEH to operate at low frequencies and irregular vibrations. | - May introduce complexity and instability to the system. <br> - May require additional components or tuning mechanisms. <br> - May have limited applicability or scalability. |



### Non-linear techniques for electromagnetic energy harvesting

- Electromagnetic energy harvesting (EMEH) is a technique that converts ambient mechanical vibrations into electrical energy using electromagnetic induction.
- Non-linear techniques are used to optimize the harvested energy from EMEH by exploiting the non-linear dynamics of the system, such as bistability, snap-through, magnetic levitation, etc.
- Non-linear techniques can enhance the bandwidth, output voltage, and power density of EMEH, as well as reduce the dependency on the resonance frequency and the input amplitude.
- Some examples of non-linear techniques for EMEH are:

  - Non-linear interface circuit: A circuit that uses a diode bridge rectifier and a capacitor to store the harvested energy and provide a non-linear load to the EMEH. This circuit can increase the output power by matching the load resistance to the optimal value .
  - Non-linear magnetic spring: A spring that consists of a small magnet moving in a tube surrounded by a coil and two fixed magnets at the ends. This spring can exhibit bistability and snap-through behavior, which can increase the output voltage and power by creating large relative motion between the magnet and the coil .
  - Non-linear multi-stable EMEH: An EMEH that has multiple stable equilibrium positions due to the interaction of magnetic forces and mechanical springs. This EMEH can harvest energy from low-frequency and random vibrations by switching between different stable states.



### Vibration Control and Steady State Cases

- Vibration control is the process of reducing or eliminating unwanted vibrations in a mechanical system, such as a vehicle, a building, or a machine.
- Vibration control can be achieved by passive or active methods, depending on the source and nature of the vibration.
- Passive vibration control involves the use of damping, isolation, or absorption devices that do not require external power or feedback. Examples of passive vibration control devices are springs, dampers, rubber mounts, or mass dampers.
- Active vibration control involves the use of sensors, actuators, and controllers that apply forces or torques to counteract the vibration. Examples of active vibration control devices are piezoelectric actuators, electromagnetic actuators, or smart materials.
- Vibration energy harvesting is the concept of converting vibration energy to electrical energy, which can be used to power wireless sensors, microelectronic devices, or other applications. Vibration energy harvesting can be achieved by different technologies, such as electromagnetic induction, piezoelectric effect, or electrostatic effect.
- Steady state cases are the situations where the vibration response of a system reaches a constant amplitude and frequency, regardless of the initial conditions. Steady state cases can occur in free or forced vibrations, depending on the damping and excitation of the system.
- Free vibration is the vibration of a system that occurs naturally without any external force. Free vibration can be undamped or damped, depending on the presence of energy dissipation in the system. Undamped free vibration has a constant amplitude and frequency, while damped free vibration has a decreasing amplitude and frequency.
- Forced vibration is the vibration of a system that occurs due to an external force. Forced vibration can be harmonic or non-harmonic, depending on the periodicity of the force. Harmonic forced vibration has a constant frequency, while non-harmonic forced vibration has a varying frequency. Forced vibration can also be resonant or non-resonant, depending on the relation between the natural frequency and the forcing frequency. Resonant forced vibration has a maximum amplitude, while non-resonant forced vibration has a lower amplitude.



## Unit 4 - ENERGY HARVESTING WIRELESS SENSORS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy from their environment into electrical energy for powering themselves and transmitting data  .
- Energy harvesting wireless sensors can use various sources of energy, such as solar, thermal, kinetic, electromagnetic, or radio frequency  .
- Energy harvesting wireless sensors have several advantages over battery-powered sensors, such as:
  - They are maintenance-free, flexible and inexpensive to install .
  - They can operate in harsh or inaccessible environments where battery replacement is difficult or impossible .
  - They can reduce the environmental impact of battery waste and disposal .
- Energy harvesting wireless sensors have many applications in various domains, such as:
  - Smart buildings: They can monitor and control temperature, humidity, lighting, occupancy, air quality, security, etc .
  - Industrial IoT: They can measure and optimize parameters such as pressure, vibration, flow, level, etc .
  - Healthcare: They can monitor and track vital signs, activity, posture, etc .
  - Agriculture: They can monitor and control soil moisture, irrigation, crop growth, etc .
- Energy harvesting wireless sensors face some challenges and limitations, such as:
  - The availability and intensity of ambient energy sources may vary over time and space .
  - The energy conversion efficiency and storage capacity may be low or insufficient for some applications .
  - The communication range and reliability may be affected by interference, noise, or obstacles .
  - The design and optimization of energy harvesting wireless sensors may require trade-offs between performance, cost, and complexity .



### Power sources for wireless sensor networks

- Wireless sensor networks (WSNs) are composed of small, low-power devices that can sense, process, and communicate data wirelessly.
- WSNs have many applications in environmental monitoring, industrial automation, health care, smart buildings, etc.
- One of the main challenges in WSNs is to provide adequate and reliable power for the sensor nodes, which have limited energy resources and often operate in remote or inaccessible locations.
- Power sources for WSNs can be classified into three categories :
  - Energy reservoirs: These are devices that store energy on the node, such as batteries, capacitors, or fuel cells. They have high energy density but limited lifetime and need to be replaced or recharged periodically.
  - Power distribution: These are methods that deliver power to the node from an external source, such as wires, electromagnetic induction, or radio frequency. They have high power density but require infrastructure and maintenance, and may not be feasible in some environments.
  - Power scavenging: These are techniques that harvest ambient energy from the surroundings, such as solar, thermal, vibration, or wind. They have low power density but can provide continuous and renewable power, and can extend the lifetime of the node significantly.
- The choice of the power source depends on several factors, such as the power consumption and duty cycle of the node, the availability and variability of the ambient energy, the size and cost of the device, and the environmental conditions and constraints.
- Some examples of power sources for WSNs are  :
  - Batteries: They are the most common and widely used energy reservoirs for WSNs. They have high energy density and low cost, but they suffer from self-discharge, limited lifetime, and environmental issues. Some types of batteries are primary (non-rechargeable), secondary (rechargeable), or hybrid (rechargeable with primary backup).
  - Capacitors: They are devices that store electric charge on two conductive plates separated by a dielectric material. They have high power density and fast charging and discharging rates, but they have low energy density and high leakage current. They can be used as energy buffers or backup power sources for WSNs.
  - Fuel cells: They are devices that convert chemical energy from a fuel (such as hydrogen, methanol, or glucose) and an oxidant (such as oxygen or air) into electrical energy. They have high energy density and long lifetime, but they have high cost, low power density, and complex operation and maintenance. They can be used as primary or secondary power sources for WSNs.
  - Wires: They are the simplest and most reliable way of delivering power to the node from an external source, such as a power grid or a generator. They have high power density and low cost, but they require infrastructure and maintenance, and may not be feasible in some environments. They can be used as primary or secondary power sources for WSNs.
  - Electromagnetic induction: It is a method of transferring power wirelessly by using a magnetic field generated by a coil or a magnet. It has high power density and low cost, but it requires close proximity and alignment between the transmitter and the receiver, and may cause interference and losses. It can be used as a secondary power source for WSNs.
  - Radio frequency: It is a method of transferring power wirelessly by using electromagnetic waves in the radio spectrum. It has low power density and high cost, but it can operate over long distances and does not require alignment between the transmitter and the receiver. It can be used as a secondary power source for WSNs.
  - Solar: It is the most common and widely used power scavenging technique for WSNs. It converts light energy from the sun or artificial sources into electrical energy by using photovoltaic cells. It has high power density and low cost, but it depends on the availability and variability of the light source, and may require energy storage and conversion devices. It can be used as a primary or secondary power source for WSNs.
  - Thermal: It is a power scavenging technique that converts heat energy from the environment or the node itself into electrical energy by using thermoelectric generators or thermocouples. It has low power density and high cost, but it can operate in a wide range of temperatures and does not require light or motion. It can be used as a primary or secondary power source for WSNs.
  - Vibration: It is a power scavenging technique



### Power generation for the notes of the Unit 4 - ENERGY HARVESTING WIRELESS SENSORS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Power generation is the process of converting ambient energy sources into electrical energy that can be used to power wireless sensor nodes (WSNs) in the Internet of Things (IoT) applications.
- Power generation methods for energy harvesting wireless sensors can be classified into four categories: solar, mechanical, thermal, and electromagnetic.
- Solar power generation uses photovoltaic cells to convert light energy into electrical energy. Solar power generation is suitable for outdoor applications where there is sufficient sunlight, but it has limitations in indoor or low-light environments. Solar power generation can also be affected by weather conditions, seasons, and shadows.
- Mechanical power generation uses piezoelectric, triboelectric, or electroactive polymers to convert mechanical vibrations, motions, or deformations into electrical energy. Mechanical power generation is suitable for applications where there is frequent or periodic mechanical activity, such as industrial machines, human body movements, or wind turbines. Mechanical power generation can also harvest energy from ambient acoustic or seismic waves .
- Thermal power generation uses thermoelectric or thermophotovoltaic devices to convert heat gradients or infrared radiation into electrical energy. Thermal power generation is suitable for applications where there is a significant temperature difference between the sensor node and its surroundings, such as body heat, waste heat, or combustion engines. Thermal power generation can also harvest energy from ambient thermal fluctuations or infrared sources.
- Electromagnetic power generation uses antennas, coils, or rectennas to convert radio frequency (RF) waves or magnetic fields into electrical energy. Electromagnetic power generation is suitable for applications where there is a strong or constant RF or magnetic source, such as wireless power transfer, RFID, or wireless communication. Electromagnetic power generation can also harvest energy from ambient RF or magnetic sources, such as TV, radio, or cellular signals .
- The choice of power generation method depends on the characteristics of the energy source, the power consumption and duty cycle of the sensor node, the environmental conditions, and the cost and size of the energy harvesting device. The power generation method should match the energy source in terms of frequency, amplitude, and duration, and should provide enough power to meet the sensor node's requirements. The power generation method should also be reliable, efficient, and scalable.



### Conversion for the notes of the Unit 4 - ENERGY HARVESTING WIRELESS SENSORS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy from their environment into electrical energy for powering themselves and transmitting data .
- Energy harvesting wireless sensors can use various sources of energy, such as solar, thermal, kinetic, electromagnetic, or piezoelectric .
- Energy harvesting wireless sensors have several advantages over battery-powered sensors, such as:
  - They are maintenance-free, flexible and inexpensive to install .
  - They can be placed practically anywhere, even in hard-to-reach or hazardous locations .
  - They can extend the lifetime and reliability of wireless sensor networks .
  - They can reduce the environmental impact and waste of batteries .
- Energy harvesting wireless sensors also have some challenges and limitations, such as:
  - They depend on the availability and intensity of the energy source, which can be intermittent or variable .
  - They require efficient energy conversion, storage and management techniques to optimize the energy usage and performance of the sensor nodes .
  - They may have lower data rates, higher latency and lower security than battery-powered sensors .
- Energy harvesting wireless sensors can be applied to various domains and applications, such as:
  - Smart buildings and homes, where they can monitor and control temperature, humidity, lighting, occupancy, air quality, etc .
  - Industrial IoT, where they can monitor and optimize the operation of machines, equipment, pipelines, etc .
  - Healthcare, where they can monitor and track the vital signs, activity and location of patients and staff .
  - Environmental monitoring, where they can measure and report the parameters of soil, water, air, etc .
  - Agriculture, where they can monitor and improve the crop growth, irrigation, pest control, etc .



### Examples for the notes of the Unit 4 - ENERGY HARVESTING WIRELESS SENSORS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy from their environment into electrical energy for powering themselves and transmitting data  .
- Energy harvesting wireless sensors can be powered by various sources of energy, such as solar, thermal, vibration, radio frequency, wind, etc  .
- Energy harvesting wireless sensors have several advantages over battery-powered sensors, such as:
  - They are maintenance-free, flexible and inexpensive to install .
  - They can be placed practically anywhere, even in hard-to-reach or hazardous locations .
  - They can extend the lifetime and reliability of wireless sensor networks .
  - They can reduce the environmental impact and waste of batteries .
- Energy harvesting wireless sensors have various applications in different domains, such as:
  - Smart buildings: They can monitor and control temperature, humidity, lighting, occupancy, air quality, etc .
  - Industrial IoT: They can measure and optimize parameters such as pressure, flow, level, vibration, etc .
  - Healthcare: They can monitor and track vital signs, activity, posture, etc .
  - Agriculture: They can monitor and control soil moisture, irrigation, crop growth, etc .
  - Environmental: They can monitor and detect parameters such as pollution, noise, radiation, etc .
- Energy harvesting wireless sensors have some challenges and limitations, such as:
  - The availability and intensity of ambient energy sources may vary over time and space .
  - The energy conversion efficiency and storage capacity may be low or insufficient .
  - The data transmission rate and range may be limited by the power budget .
  - The design and optimization of energy harvesting wireless sensors may require trade-offs among performance, cost, size, etc .



### Case studies for the notes of the Unit 4 - ENERGY HARVESTING WIRELESS SENSORS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy sources, such as light, heat, vibration, or radio frequency, into electrical energy to power themselves and transmit data wirelessly .
- Energy harvesting can address the energy-scarcity problem of wireless sensor networks (WSNs), which are widely used in various applications of the Internet of Things (IoT), such as smart buildings, industrial monitoring, healthcare, and environmental sensing.
- Energy harvesting can also reduce the maintenance cost and environmental impact of replacing batteries for wireless sensors, and enable new applications that require long-term or remote sensing.
- Some case studies of energy harvesting wireless sensors are:

  - **EnOcean**: EnOcean is a company that provides energy harvesting wireless solutions for building automation, smart homes, and industrial applications. EnOcean's products use solar, thermal, motion, and vibration energy harvesters to power wireless switches, sensors, and actuators that communicate using EnOcean's radio protocol or other standards such as Bluetooth or ZigBee.
  - **Everactive**: Everactive is a company that develops batteryless wireless sensors for industrial IoT applications, such as steam trap monitoring, machine health monitoring, and flare gas monitoring. Everactive's sensors use thermoelectric and electromagnetic energy harvesters to power ultra-low-power integrated circuits and wireless transceivers that can operate continuously and autonomously.
  - **Solar harvesting system for WSNs**: A research paper by Khan et al. (2021) presents a comprehensive study of solar harvesting systems and their applications in WSNs. The paper reviews the components, architectures, and challenges of solar harvesting systems, and discusses some recent applications in agriculture, healthcare, smart cities, and disaster management.



### Harvesting Microelectronic Circuits

- Harvesting microelectronic circuits are circuits that can extract and convert ambient energy sources, such as light, heat, vibration, or radio waves, into electrical energy for powering low-power devices, such as wireless sensors, biomedical implants, or wearable electronics .
- Harvesting microelectronic circuits typically consist of three main components: a transducer, a power converter, and a power management unit .
  - A transducer is a device that converts one form of energy into another, such as a photovoltaic cell, a thermoelectric generator, a piezoelectric element, or an antenna .
  - A power converter is a circuit that adapts the output voltage and current of the transducer to the input requirements of the load, such as a boost converter, a buck converter, or a charge pump .
  - A power management unit is a circuit that regulates and controls the power flow between the source, the storage, and the load, such as a voltage regulator, a battery charger, or a power switch .
- Harvesting microelectronic circuits face several challenges and trade-offs, such as low and variable input power, high conversion efficiency, low quiescent power, small size and weight, and compatibility with the application .
- Harvesting microelectronic circuits require careful design and optimization of the transducer, the power converter, and the power management unit, as well as the integration and coordination of these components, to achieve the best performance and reliability .
- Harvesting microelectronic circuits have many advantages and applications, such as extending the battery life or eliminating the need for batteries, reducing the maintenance and environmental costs, enabling new functionalities and features, and enhancing the mobility and autonomy of the devices .



### Power conditioning and losses for energy harvesting wireless sensors

- Power conditioning is the process of converting the harvested energy from various sources (such as solar, thermal, vibration, etc.) into a suitable form for the wireless sensor nodes (WSNs)  .
- Power conditioning typically involves voltage regulation, rectification, filtering, and storage .
- Power conditioning is essential for ensuring the reliability, efficiency, and functionality of the WSNs, especially in machine condition monitoring (MCM) applications  .
- Power losses can occur in different stages of power conditioning, such as in the transducer, the converter, the storage, and the load .
- Power losses can reduce the amount of usable energy for the WSNs and affect their performance and lifetime .
- Some of the factors that can cause power losses are:
  - Mismatch between the source impedance and the load impedance .
  - Non-ideal characteristics of the components (such as resistance, capacitance, inductance, etc.) .
  - Leakage currents and self-discharge of the storage devices .
  - Switching losses and conduction losses of the converter .
  - Parasitic effects and noise .
- Some of the techniques that can reduce power losses are:
  - Impedance matching and maximum power point tracking (MPPT) .
  - Using high-efficiency and low-power components .
  - Choosing appropriate storage devices and charging/discharging strategies .
  - Optimizing the converter topology and control .
  - Minimizing the parasitic effects and noise .



## Unit 5 - SELECTED APPLICATIONS OF ENERGY HARVESTING SYSTEMS

- Energy harvesting systems are devices that collect ambient energy from the environment and convert it into electrical energy for powering wireless devices or autonomous systems.
- Energy harvesting systems can extend the battery life, reduce the maintenance cost, and improve the reliability of remote sensors and devices that are impractical or inconvenient to replace batteries.
- Energy harvesting systems can find applications in various sectors such as industrial, consumer electronics, building and home automation, wireless sensor networks, security systems, and others.
- Some of the common sources of ambient energy for energy harvesting systems are solar, thermal, kinetic, radio frequency, and piezoelectric.
- Some of the examples of energy harvesting systems applications are:

  - Remote monitoring, predictive maintenance, and energy-efficient solutions for industrial applications.
  - Body sensor networks, wearable electronic devices, and biomedical implants for medical applications.
  - Smart lighting, HVAC control, and occupancy detection for building and home automation applications.
  - Environmental sensing, asset tracking, and structural health monitoring for wireless sensor networks applications.
  - Intrusion detection, access control, and surveillance for security systems applications.
  - Oceanographic monitoring, seismic sensing, and wind turbine control for environmental applications.



### Case studies for Implanted medical devices

- Implantable medical devices (IMDs) are electronic devices that are inserted into the human body to monitor, diagnose, or treat various medical conditions.
- IMDs include pacemakers, defibrillators, cochlear implants, neurostimulators, drug delivery systems, biosensors, and artificial organs.
- IMDs require a reliable and long-lasting power source to function properly and safely. However, conventional batteries have several limitations, such as limited lifespan, risk of leakage, infection, or inflammation, and the need for surgical replacement.
- Energy harvesting is an alternative approach to power IMDs by converting ambient energy sources, such as mechanical, thermal, or chemical energy, into electrical energy.
- Energy harvesting can potentially extend the lifetime of IMDs, reduce the size and weight of the devices, and eliminate the need for invasive surgeries and wires.
- Some examples of energy harvesting techniques for IMDs are:

  - Piezoelectric energy harvesting: This technique converts mechanical vibrations or deformations into electrical voltage using piezoelectric materials, such as ceramics or polymers. Piezoelectric energy harvesters can be attached to organs or tissues that undergo periodic motions, such as the heart, lungs, diaphragm, or blood vessels, and generate power from the heartbeat, respiration, or blood flow. For instance, a piezoelectric energy harvester was developed to power a pacemaker by harvesting energy from the heartbeats.
  - Thermoelectric energy harvesting: This technique converts temperature gradients into electrical voltage using thermoelectric materials, such as bismuth telluride or lead telluride. Thermoelectric energy harvesters can be placed near organs or tissues that have a higher or lower temperature than the surrounding environment, such as the skin, muscles, or brain, and generate power from the body heat. For example, a thermoelectric energy harvester was developed to power a cochlear implant by harvesting energy from the temperature difference between the ear canal and the mastoid bone.
  - Biofuel cell energy harvesting: This technique converts chemical energy into electrical energy using biofuel cells, which are electrochemical devices that use enzymes or microorganisms as catalysts. Biofuel cells can harvest energy from the glucose or oxygen in the body fluids, such as blood, interstitial fluid, or cerebrospinal fluid, and generate power from the redox reactions. For instance, a biofuel cell energy harvester was developed to power a glucose sensor by harvesting energy from the glucose in the interstitial fluid.



### Bio-MEMS based applications

- Bio-MEMS stands for biomedical micro-electro-mechanical systems, which are devices that integrate biological components with microfabrication technologies.
- Bio-MEMS can be used for various applications in medicine, such as surgical tools, diagnostic devices, therapeutic devices, and tissue engineering.
- Some examples of Bio-MEMS based applications are:

  - Biomedical transducers: These are devices that convert one form of energy into another, such as electrical, mechanical, optical, or chemical. For example, a piezoelectric transducer can generate an electric signal from a mechanical vibration, or vice versa. Biomedical transducers can be used for sensing, actuation, or stimulation of biological systems, such as blood pressure, heart rate, muscle contraction, or nerve impulses.
  - Microfluidics: These are devices that manipulate small volumes of fluids, such as blood, saliva, or urine, using channels, valves, pumps, or mixers. Microfluidics can be used for sample preparation, separation, detection, and analysis of biological molecules, such as DNA, proteins, antibodies, or cells. For example, a biochip is a microfluidic device that can perform multiple biochemical reactions or assays on a single chip, such as polymerase chain reaction (PCR), enzyme-linked immunosorbent assay (ELISA), or DNA microarray.
  - Medical implants: These are devices that are implanted into the body to replace, restore, or enhance a biological function, such as a pacemaker, cochlear implant, or artificial organ. Medical implants can be made of biocompatible materials, such as metals, ceramics, polymers, or composites, and can incorporate sensors, actuators, or drug delivery systems. For example, a glucose sensor can be implanted under the skin to monitor the blood glucose level of a diabetic patient, and a drug delivery actuator can release insulin when needed.
  - Microsurgical tools: These are devices that are used for performing minimally invasive surgery, such as endoscopy, laparoscopy, or microsurgery. Microsurgical tools can be made of flexible or rigid materials, and can have various functions, such as cutting, grasping, suturing, or cauterizing. For example, a microgripper can be used to manipulate or remove a tissue or a foreign object from a small incision.
  - Tissue engineering: This is a field that aims to create artificial tissues or organs from living cells, biomaterials, and growth factors. Tissue engineering can be used for repairing, replacing, or enhancing a damaged or diseased tissue or organ, such as skin, bone, cartilage, or heart. For example, a bioreactor is a device that can provide a suitable environment for the growth and differentiation of cells on a scaffold, such as temperature, nutrients, oxygen, or mechanical stimuli.



### Harvesting for RF Sensors and ID Tags

- RF sensors and ID tags are devices that use radio frequency (RF) signals to communicate data, such as identification, location, temperature, or motion, to a reader or a network.
- RF sensors and ID tags can be classified into passive, semi-passive, or active, depending on their power source and functionality.
- Passive RF sensors and ID tags have no battery and rely on the RF energy from the reader to power up their circuitry and transmit their data. They have a limited range and functionality, but they are low-cost and maintenance-free.
- Semi-passive RF sensors and ID tags have a battery that powers their circuitry, but they still use the RF energy from the reader to transmit their data. They have a longer range and more functionality than passive tags, but they are more expensive and require battery replacement.
- Active RF sensors and ID tags have a battery that powers both their circuitry and their transmission. They have the longest range and the most functionality, but they are the most expensive and require frequent battery replacement.
- Energy harvesting is a technique that enables RF sensors and ID tags to collect energy from the environment, such as light, heat, vibration, or RF signals, and convert it into electrical power for their operation.
- Energy harvesting can extend the battery life or eliminate the need for batteries in RF sensors and ID tags, thus reducing the cost, maintenance, and environmental impact of these devices.
- Energy harvesting can also enable new applications and functionalities for RF sensors and ID tags, such as sensing, computation, encryption, or localization.
- Energy harvesting for RF sensors and ID tags can be achieved by using different types of transducers, such as solar cells, thermoelectric generators, piezoelectric elements, or RF rectifiers, depending on the available energy source and the power requirement of the device.
- Energy harvesting for RF sensors and ID tags can be integrated into the device design or added as an external module, depending on the compatibility and feasibility of the solution.
- Energy harvesting for RF sensors and ID tags can be optimized by using efficient power conversion and management circuits, such as DC-DC converters, voltage regulators, or power switches, to match the output voltage and current of the transducer to the input voltage and current of the device.
- Energy harvesting for RF sensors and ID tags can be enhanced by using adaptive or cooperative techniques, such as impedance matching, load modulation, or multiple-input multiple-output (MIMO), to maximize the power transfer and communication performance of the device.



### Powering Wireless SHM Sensor Nodes through Energy Harvesting

- Wireless sensor nodes (WSNs) are devices that can sense, process, and communicate data wirelessly.
- Structural health monitoring (SHM) is an application of WSNs that aims to detect and assess the damage or degradation of structures such as bridges, buildings, pipelines, etc.
- One of the main challenges of WSNs for SHM is the power supply, as batteries have limited lifetime and may be difficult or costly to replace.
- Energy harvesting is a technique that can provide power to WSNs by converting ambient energy sources such as solar, thermal, vibration, wind, etc. into electrical energy.
- Energy harvesting can enable WSNs for SHM to operate autonomously and indefinitely, without the need for batteries or external power sources.
- Some of the advantages of energy harvesting for WSNs for SHM are:
  - Reduced maintenance cost and environmental impact of batteries.
  - Increased reliability and availability of the sensor network.
  - Enhanced scalability and flexibility of the sensor network.
  - Improved performance and functionality of the sensor network.
- Some of the challenges of energy harvesting for WSNs for SHM are:
  - The variability and unpredictability of the ambient energy sources.
  - The mismatch between the energy supply and demand of the sensor node.
  - The trade-off between the size, weight, and efficiency of the energy harvesting device.
  - The integration and compatibility of the energy harvesting device with the sensor node and the structure.
- Some of the examples of energy harvesting techniques for WSNs for SHM are:
  - Solar energy harvesting, which uses photovoltaic cells to convert sunlight into electricity.
  - Thermal energy harvesting, which uses thermoelectric generators to convert temperature gradients into electricity.
  - Vibration energy harvesting, which uses piezoelectric, electromagnetic, or electrostatic transducers to convert mechanical vibrations into electricity.
  - Wind energy harvesting, which uses micro-turbines or flapping wings to convert air flow into electricity.
  - Microwave energy harvesting, which uses rectennas to convert microwave signals into electricity    .

