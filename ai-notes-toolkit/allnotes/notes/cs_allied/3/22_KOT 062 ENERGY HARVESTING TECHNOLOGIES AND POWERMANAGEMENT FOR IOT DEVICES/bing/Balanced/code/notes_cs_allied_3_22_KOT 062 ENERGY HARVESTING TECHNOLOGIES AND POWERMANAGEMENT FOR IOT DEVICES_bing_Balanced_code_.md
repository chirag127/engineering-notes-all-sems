

# KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES

- Energy harvesting is a promising solution to power IoT devices especially when they are installed in inaccessible areas and regular battery maintenance is not possible.
- Energy harvesting captures energy from ambient sources such as RF waves, light, thermal gradients, or mechanical motion to power IoT devices.
- Energy harvesting based on a renewable source enables IoT devices to generate electrical energy by absorbing energy from the environment.
- Energy harvesting approach extends the life cycle of the device and eliminates the constraint of fixed charge batteries as an energy source.
- Energy harvesting also reduces the environmental impact of battery disposal and enhances the sustainability of the IoT.
- Energy harvesting and power management techniques at the circuit, device, and system levels are the most crucial segment of IoT devices.
- Energy harvesting and power management requirements vary depending on the application, environment, and network of the IoT devices.
- Energy harvesting and power management techniques should be optimized for low power consumption, high efficiency, and robustness.
- Energy harvesting and power management techniques should also consider the trade-offs between performance, complexity, and cost.
- Energy harvesting and power management techniques should be compatible with the 5G network standards and protocols.



# KCS

- KCS stands for Knowledge-Centered Service, a methodology for creating and maintaining knowledge as a key asset of an organization.
- KCS is based on four basic principles: 
  - Integrate the creation and maintenance of knowledge into the problem-solving process.
  - Evolve content based on demand and usage.
  - Develop a knowledge base of collective experience to enable reuse and improvement.
  - Reward learning, collaboration, sharing, and improvement.
- KCS has two main processes: the Solve Loop and the Evolve Loop.
  - The Solve Loop focuses on capturing, structuring, and reusing knowledge at the point of interaction with customers or users.
  - The Evolve Loop focuses on analyzing, improving, and governing the knowledge base and the KCS practices.
- KCS has six core practices that support the principles and processes: 
  - Capture: Capturing knowledge in the context of the customer's situation and in the customer's words.
  - Structure: Structuring knowledge using a standard template and metadata to make it easy to find and use.
  - Reuse: Reusing existing knowledge to solve problems and avoid recreating content.
  - Improve: Improving the quality and effectiveness of knowledge based on feedback and usage patterns.
  - Search: Searching the knowledge base before solving a problem or creating new content.
  - Link: Linking related knowledge articles to create a network of knowledge.
- KCS has four maturity levels that describe the evolution of an organization's adoption and performance of KCS: 
  - Level 1: Reactive. Knowledge is captured and reused as a by-product of solving problems, but with low consistency and quality.
  - Level 2: Repeatable. Knowledge is captured and reused with some standards and guidelines, but with limited scope and impact.
  - Level 3: Defined. Knowledge is captured and reused with clear roles and responsibilities, and with measurable outcomes and benefits.
  - Level 4: Optimized. Knowledge is captured and reused with continuous improvement and innovation, and with strategic alignment and value.



## Unit 1 - Energy Harvesting Systems

- Energy harvesting systems are devices or systems that are used to convert ambient energy, which is derived from external sources existing in the atmosphere, into electrical energy.
- Energy harvesting systems are attractive alternatives to battery-operated systems, especially for long-term, low-power, and self-sustaining electronic systems.
- Energy harvesting systems can scavenge energy from various sources, such as mechanical load, vibrations, temperature gradients, light, etc., and convert them into small levels of power in the nW-mW range .
- Energy harvesting systems require interface circuits to control and regulate the flows of energy and to match the impedance between the energy source and the load.
- Energy harvesting systems have various applications, such as body sensor networks, oceanographic monitoring sensors, wireless sensor networks, etc .
- Energy harvesting systems can be classified into different types based on the energy source, such as solar, thermal, piezoelectric, electromagnetic, etc .
- Energy harvesting systems can also be classified into different types based on the energy conversion mechanism, such as electrostatic, electromagnetic, piezoelectric, etc.
- Energy harvesting systems face some challenges, such as low efficiency, high cost, environmental variability, etc .



### Introduction for the notes of the Unit 1 - ENERGY HARVESTING SYSTEMS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting is the process of capturing energy from one or more renewable energy sources and converting them into usable electrical energy.
- Energy harvesting is useful for powering wireless IoT devices that have limited battery life or are difficult to replace or recharge.
- Energy harvesting can reduce the environmental impact and maintenance cost of IoT devices, as well as enable new applications and functionalities.
- Energy harvesting IoT devices have the potential to harvest different forms of ambient energy as well as energy from external sources.
- Ambient energy sources include solar, thermal, flow, and radio frequency, while external sources can be categorized as mechanical and human sources.
- Energy harvesting systems for IoT devices consist of four main components: energy transducer, energy storage, power management, and load.
- Energy transducer is the device that converts the harvested energy into electrical energy, such as photovoltaic cells, thermoelectric generators, piezoelectric elements, etc.
- Energy storage is the device that stores the electrical energy for later use, such as batteries, capacitors, supercapacitors, etc.
- Power management is the circuit that regulates and optimizes the energy flow between the transducer, the storage, and the load.
- Load is the device that consumes the electrical energy, such as sensors, microcontrollers, wireless transceivers, etc.
- Energy harvesting systems for IoT devices face many challenges, such as low and variable power output, mismatch between energy supply and demand, efficiency and reliability issues, etc.
- Energy harvesting systems for IoT devices require careful design and optimization to achieve the best performance and functionality.
- Energy harvesting systems for IoT devices can benefit from the advances in nanotechnology, materials science, and artificial intelligence .
- Energy harvesting systems for IoT devices have many applications in various domains, such as smart buildings, smart cities, smart agriculture, smart health, smart transportation, etc .



### Energy sources for the notes of the Unit 1 - ENERGY HARVESTING SYSTEMS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting is the process by which energy is derived from external sources (e.g., solar power, thermal energy, wind energy, salinity gradients, and kinetic energy, also known as ambient energy), and then stored for use by small, wireless autonomous devices, like sensors, microcontrollers, and actuators.
- Energy sources for energy harvesting include:
  - Motion/mechanical energy: This is the energy from vibrations, movements, rotations, or deformations of materials or structures. It can be converted into electricity using piezoelectric, electromagnetic, or electrostatic mechanisms .
  - Light energy: This is the energy from natural or artificial light sources. It can be converted into electricity using photovoltaic (PV) cells, which are made of materials that convert light into an electrical current .
  - Thermal energy: This is the energy from temperature differences or heat flows between two points or materials. It can be converted into electricity using thermoelectric, thermionic, or pyroelectric mechanisms .
  - RF energy: This is the energy from radio frequency (RF) waves, such as those from TV, radio, or cellular signals. It can be converted into electricity using RF energy harvesters, which are devices that transform RF energy into electrical energy .
  - Chemical energy: This is the energy from chemical reactions or processes, such as those from batteries, fuel cells, or biodegradable materials. It can be converted into electricity using electrochemical, enzymatic, or microbial mechanisms .



# Energy Harvesting Based Sensor Networks

- Energy harvesting based sensor networks are wireless sensor networks that use ambient energy sources such as solar, wind, thermal, vibration, etc. to power the sensor nodes and extend their lifetime .
- Energy harvesting based sensor networks have several advantages over battery-powered sensor networks, such as:
  - Reduced maintenance cost and environmental impact of replacing batteries.
  - Increased reliability and availability of sensor nodes.
  - Enhanced scalability and flexibility of network deployment and expansion.
  - Improved security and privacy of data transmission and storage.
- Energy harvesting based sensor networks have several challenges, such as:
  - Intermittent and unpredictable nature of energy sources.
  - Trade-off between energy harvesting efficiency and sensor performance.
  - Coordination and synchronization of sensor nodes with different energy levels and states.
  - Routing and communication protocols that adapt to dynamic network conditions and energy constraints.
- Energy harvesting based sensor networks require the following components  :
  - Energy harvesting unit: A device that converts ambient energy into electrical energy, such as solar cells, piezoelectric generators, thermoelectric generators, etc.
  - Energy storage unit: A device that stores the harvested energy for later use, such as batteries, capacitors, supercapacitors, etc.
  - Energy management unit: A device that monitors and controls the energy flow between the energy harvesting unit, the energy storage unit, and the sensor node, such as voltage regulators, power converters, switches, etc.
  - Sensor node: A device that performs sensing, processing, and communication tasks, such as microcontrollers, sensors, transceivers, etc.
- Energy harvesting based sensor networks require the following techniques  :
  - Energy-aware sensing: A technique that adjusts the sensing frequency, resolution, and accuracy according to the available energy and the application requirements.
  - Energy-aware processing: A technique that optimizes the computation complexity, memory usage, and data compression according to the available energy and the application requirements.
  - Energy-aware communication: A technique that adapts the transmission power, modulation scheme, coding rate, and packet size according to the available energy and the channel conditions.
  - Energy-aware routing: A technique that selects the optimal path for data delivery based on the energy level, location, and connectivity of the sensor nodes.
  - Energy-aware medium access control: A technique that coordinates the access of multiple sensor nodes to the shared wireless channel based on the energy level, traffic load, and collision probability.
  - Energy-aware cross-layer optimization: A technique that jointly optimizes the performance of multiple layers of the network protocol stack based on the energy level and the application requirements.



### Photovoltaic cell technologies

- Photovoltaic (PV) cells are devices that absorb energy from sunlight and convert it into electrical energy through semiconducting materials.
- PV cells are based on the photovoltaic effect, which is the process of generating voltage and electric current in a material upon exposure to light.
- PV cells are connected to form larger power-generating units known as modules or panels, which can be installed on rooftops, buildings, or ground-mounted systems.
- There are three main types of PV cell technologies that dominate the world market: monocrystalline silicon, polycrystalline silicon, and thin film.
  - Monocrystalline silicon (mono-Si) cells are made from a single crystal of high-purity silicon. They have a uniform dark appearance and a high efficiency of about 15-20%.
  - Polycrystalline silicon (poly-Si) cells are made from multiple crystals of silicon that are melted and cast into a square shape. They have a speckled blue appearance and a lower efficiency of about 13-16% than mono-Si cells, but they are cheaper to produce.
  - Thin film cells are made from thin layers of semiconductor materials, such as amorphous silicon, cadmium telluride, or copper indium gallium selenide, deposited on a substrate. They have a flexible and lightweight appearance and a low efficiency of about 7-13%, but they are cheaper and more adaptable to different applications than crystalline silicon cells.
- PV cell technologies are constantly evolving and improving, with new materials, designs, and processes being developed to increase the performance, reliability, and cost-effectiveness of solar power generation .
- PV cell technologies are one of the most promising and widely used forms of renewable energy, as they offer environmental, economic, and social benefits, such as reducing greenhouse gas emissions, creating jobs, and providing electricity to remote areas .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of generation of electric power in semiconductor PV cells:

### Generation of electric power in semiconductor PV cells

- PV cells are devices that convert light energy into electrical energy using the photovoltaic effect .
- The photovoltaic effect is the phenomenon of generating electric voltage or current in a material when it is exposed to light .
- The material used in PV cells is usually a semiconductor, such as silicon, which has the property of changing its electrical conductivity when light is absorbed .
- A semiconductor has two types of charge carriers: electrons and holes. Electrons are negatively charged particles that can move freely in the material, while holes are positively charged regions that can accept electrons .
- A PV cell consists of two layers of semiconductor with different doping levels. Doping is the process of adding impurities to a semiconductor to change its electrical properties .
- The layer with more electrons is called the n-type layer, while the layer with more holes is called the p-type layer. The junction between the two layers is called the p-n junction .
- When light strikes the p-n junction, it creates electron-hole pairs in the semiconductor. The electrons and holes are separated by the electric field at the junction, creating a potential difference or voltage across the cell .
- The voltage can be measured by connecting an external circuit to the cell. The current that flows in the circuit is proportional to the intensity of the light and the area of the cell  .
- The power generated by a single PV cell is typically only about two watts. To increase the power output, multiple cells can be connected in series or parallel to form a PV module or panel .
- The efficiency of a PV cell is the ratio of the electrical power output to the light power input. The efficiency depends on several factors, such as the type and quality of the semiconductor, the wavelength and angle of the light, the temperature and the circuit design .
- The average efficiency of commercial PV cells is around 15-20%, while the theoretical maximum efficiency is around 33% for a single-junction cell .
- PV cells can be used for various applications, such as powering homes, buildings, vehicles, satellites, and remote devices. PV cells are a renewable and clean source of energy, as they do not emit greenhouse gases or pollutants .



### Types of Energy Harvesting Systems

Energy harvesting systems are devices or systems that are used to convert ambient energy, which is derived from external resources existing in the atmosphere, into electrical energy. Energy harvesting systems can be classified into different types based on the source of ambient energy, such as:

- **Mechanical energy harvesting systems**: These systems harvest energy from mechanical vibrations, motions, or forces, such as ocean waves, wind, human movements, etc. They usually employ piezoelectric, electromagnetic, or electrostatic transducers to convert mechanical energy into electrical energy. Examples of mechanical energy harvesting systems are piezoelectric shoes, wind turbines, ocean wave energy converters, etc.   

- **Thermal energy harvesting systems**: These systems harvest energy from temperature gradients or variations, such as body heat, solar radiation, waste heat, etc. They usually employ thermoelectric, thermophotovoltaic, or thermionic transducers to convert thermal energy into electrical energy. Examples of thermal energy harvesting systems are thermoelectric generators, solar cells, thermophotovoltaic devices, etc.  

- **Electromagnetic energy harvesting systems**: These systems harvest energy from electromagnetic waves, such as radio waves, microwaves, light, etc. They usually employ antennas, rectifiers, or photovoltaic transducers to convert electromagnetic energy into electrical energy. Examples of electromagnetic energy harvesting systems are radio frequency identification (RFID) tags, wireless power transfer devices, photovoltaic cells, etc.  

- **Chemical energy harvesting systems**: These systems harvest energy from chemical reactions, such as oxidation, reduction, combustion, etc. They usually employ electrochemical, fuel cell, or biofuel transducers to convert chemical energy into electrical energy. Examples of chemical energy harvesting systems are batteries, fuel cells, biofuel cells, etc.  

- **Other types of energy harvesting systems**: These systems harvest energy from other sources of ambient energy, such as acoustic noise, magnetic fields, etc. They usually employ piezoelectric, magnetostrictive, or magnetoelectric transducers to convert these types of energy into electrical energy. Examples of other types of energy harvesting systems are acoustic energy harvesters, magnetic energy harvesters, etc.   

Energy harvesting systems can be used for various applications, such as wireless sensor networks, wearable devices, remote monitoring systems, etc. They can provide long-term, low-power, and self-sustaining operation for these applications, without the need for batteries or external power sources.



# Unit 2 - Piezo-electric Energy Harvesting and Electromechanical Modeling

- Piezo-electric energy harvesting is the process of converting mechanical energy, such as vibration, into electrical energy using piezoelectric materials .
- Piezoelectric materials are materials that exhibit the piezoelectric effect, which is the generation of electric charge or voltage in response to mechanical stress or strain .
- Piezoelectric energy harvesters are devices that utilize piezoelectric materials to scavenge energy from ambient sources, such as wind, waves, traffic, human motion, etc .
- Piezoelectric energy harvesters can be used to power low-power electronic devices, such as wireless sensors, microcontrollers, LED lights, etc .
- Electromechanical modeling of piezoelectric energy harvesters is the process of developing mathematical models that describe the coupled mechanical and electrical behavior of the harvesters under various forms of excitation .
- Electromechanical modeling of piezoelectric energy harvesters can help to optimize the design, performance, and efficiency of the harvesters, as well as to understand the underlying physics and phenomena involved .
- Electromechanical modeling of piezoelectric energy harvesters can be done using different approaches, such as lumped-parameter models, distributed-parameter models, finite element models, etc .
- Lumped-parameter models are models that assume the harvester as a single degree of freedom system with equivalent mass, stiffness, damping, and capacitance parameters .
- Distributed-parameter models are models that account for the spatial variation of the mechanical and electrical properties of the harvester along its length, width, and thickness .
- Finite element models are models that discretize the harvester into small elements and apply the governing equations of mechanics and electricity to each element .
- The choice of the modeling approach depends on the complexity, accuracy, and computational cost required for the analysis .
- Some examples of piezoelectric energy harvesters are cantilever beams, bimorphs, unimorphs, diaphragms, plates, shells, etc .
- Some examples of excitation sources are base excitation, tip excitation, airflow excitation, acoustic excitation, moving load excitation, etc .
- Some examples of applications of piezoelectric energy harvesting are structural health monitoring, environmental monitoring, biomedical implants, wearable devices, smart buildings, etc .



### Piezoelectric materials

- Piezoelectric materials are materials that can convert mechanical stress into electrical charge, or vice versa. This phenomenon is called the piezoelectric effect .
- Piezoelectric materials can be classified into the following categories:
  - Crystalline materials, such as quartz, which have a natural piezoelectric property and a high stability and reliability.
  - Ceramic materials, such as lead zirconate titanate (PZT), which have a high piezoelectric coefficient and a wide range of applications.
  - Semiconductor materials, such as zinc oxide, which have a piezoelectric effect due to their asymmetric crystal structure and can be used as sensors and actuators.
  - Polymer materials, such as polyvinylidene fluoride (PVDF), which have a flexible and lightweight structure and can be used as energy harvesters and transducers.
  - Composite materials, which combine different types of piezoelectric materials to enhance their performance and functionality.
  - Glass-ceramic materials, which have a fine-grained structure and a high piezoelectric coefficient and can be used as resonators and filters.
- Piezoelectric materials have various applications in different fields, such as  :
  - Sensors and actuators, which can measure and control physical parameters such as pressure, force, acceleration, vibration, temperature, etc.
  - Energy harvesting, which can convert ambient mechanical energy into electrical energy for powering low-power devices such as wireless sensors and microsystems.
  - Medical imaging and therapy, which can generate and detect ultrasound waves for diagnosis and treatment of diseases and injuries.
  - Acoustic and ultrasonic devices, which can produce and receive sound waves for communication, navigation, and entertainment.
  - Tilt sensing, which can detect the orientation and inclination of an object or a surface.
  - Power monitoring, which can measure and regulate the power output and consumption of high-power applications such as medical treatment, sonochemistry, and industrial processing.
  - Chemical and biological sensors, which can detect and analyze the presence and concentration of various substances and organisms.
  - Strain gauges, which can measure the deformation and stress of a material or a structure.



### Transducers for Piezoelectric Energy Harvesting

- A transducer is a device that converts one form of energy into another. In the context of piezoelectric energy harvesting, a transducer converts mechanical energy (such as vibration, pressure, or strain) into electrical energy (such as voltage or current).
- The piezoelectric energy harvesting technique is based on the materials' property of generating an electric field when a mechanical force is applied. This phenomenon is known as the direct piezoelectric effect .
- Piezoelectric transducers can be of different shapes and materials, making them suitable for a multitude of applications. Some common shapes are cantilever beams, cylindrical rods, plates, and rings  .
- Piezoelectric transducers can be classified into two types based on their mode of operation: resonant and non-resonant. Resonant transducers operate at a specific frequency that matches their natural frequency, and produce a high output voltage. Non-resonant transducers operate over a wide frequency range, and produce a low output voltage.
- Piezoelectric transducers can be modeled as electromechanical systems that consist of mechanical, electrical, and coupling elements. The mechanical elements represent the mass, stiffness, and damping of the transducer. The electrical elements represent the capacitance, resistance, and load of the transducer. The coupling elements represent the piezoelectric coefficient, which relates the mechanical and electrical variables.
- Piezoelectric transducers can be connected to different types of circuits to extract and store the electrical energy. Some common circuits are AC-DC converters, voltage multipliers, and impedance matching networks.
- Piezoelectric transducers can be used for energy harvesting in various applications, such as wireless sensors, biomedical implants, structural health monitoring, and wearable devices. The advantages of piezoelectric energy harvesting are its high power density, low cost, and environmental compatibility  .



### Harvesters

- Harvesters are devices that convert ambient energy sources, such as mechanical vibrations, into electrical energy that can be used to power sensors, wireless transmitters, or other low-power devices.
- Piezoelectric harvesters are a type of harvester that use piezoelectric materials, which generate electric charge when subjected to mechanical stress or strain.
- Piezoelectric harvesters can be designed in various configurations, such as cantilevers, beams, plates, or shells, depending on the shape and size of the piezoelectric material and the mode of vibration.
- Piezoelectric harvesters can be excited by different forms of mechanical energy, such as base excitation, airflow excitation, impact excitation, or moving loads.

### Electromechanical Modeling

- Electromechanical modeling is the process of developing mathematical models that describe the coupled mechanical and electrical behavior of piezoelectric harvesters.
- Electromechanical modeling can be used to predict the output voltage, power, and efficiency of piezoelectric harvesters under various operating conditions and design parameters.
- Electromechanical modeling can be classified into two main approaches: lumped-parameter modeling and distributed-parameter modeling.
- Lumped-parameter modeling assumes that the piezoelectric harvester can be represented by a single degree of freedom system with equivalent mass, stiffness, damping, and capacitance parameters. This approach is simple and convenient, but may not capture the higher-order modes and effects of the piezoelectric material.
- Distributed-parameter modeling considers the spatial variation of the displacement, stress, strain, and electric potential fields in the piezoelectric harvester. This approach is more accurate and general, but may require complex partial differential equations and numerical methods to solve.



# Microgenerators for Piezoelectric Energy Harvesting

- Piezoelectric energy harvesting is a technique that converts mechanical vibrations into electrical energy using piezoelectric materials.
- Piezoelectric materials are materials that generate electric charges when subjected to mechanical stress or strain.
- Piezoelectric energy harvesting devices can be classified into two types: MEMS generators and nanogenerators.
- MEMS generators are micro-scale devices that use thin-film piezoelectric materials to harvest energy from ambient vibrations.
- Nanogenerators are nano-scale devices that use piezoelectric nanowires or nanorods to harvest energy from body movements, wind, or water flow.
- Piezoelectric energy harvesting devices can be used as alternative or supplementary power sources for wireless sensor networks, wearable electronics, biomedical implants, and other low-power applications .
- Piezoelectric energy harvesting devices can operate in different modes, such as d31 mode, d33 mode, or hybrid mode, depending on the direction of the mechanical stress and the electric field .
- Piezoelectric energy harvesting devices can be integrated with other materials, such as composite materials, to enhance their performance and functionality.
- Piezoelectric energy harvesting devices face some challenges, such as low power density, low efficiency, high impedance, and environmental effects .
- Piezoelectric energy harvesting devices require power management circuits, such as rectifiers, voltage regulators, and energy storage units, to condition and store the harvested energy .



### Strategies for enhancing the performance of energy harvesters

Energy harvesters are devices that can convert ambient energy sources, such as vibration, wind, light, heat, etc., into electrical energy. Energy harvesters can be used to power low-power consumption devices, such as sensors, wireless communication modules, wearable electronics, etc., without the need for batteries or external power supply. Energy harvesters can also reduce the environmental impact of energy consumption and improve the reliability and lifetime of devices.

One of the most widely used types of energy harvesters is the piezoelectric energy harvester (PEH), which can convert mechanical vibration into electrical voltage by using the piezoelectric effect of certain materials. PEHs can be designed with different configurations, such as cantilever, bridge, bimorph, unimorph, etc., depending on the application and the vibration source.

However, the performance of energy harvesters, especially PEHs, is often limited by several factors, such as low power output, narrow frequency bandwidth, nonlinear behavior, environmental conditions, etc. Therefore, various strategies have been proposed to enhance the performance of energy harvesters and overcome these limitations. Some of the common strategies are:

- **Material and structure optimization**: The choice of material and structure can affect the mechanical and electrical properties of the energy harvester, such as stiffness, damping, resonance frequency, coupling coefficient, output voltage, etc. Therefore, by selecting suitable materials and structures, the performance of the energy harvester can be improved. For example, using piezoelectric materials with high piezoelectric coefficients, such as PZT, PMN-PT, PVDF, etc., can increase the output voltage of the PEH. Similarly, using structures with high aspect ratio, such as thin and long cantilevers, can increase the deflection and strain of the PEH. Moreover, using composite or hybrid structures, such as sandwich, multilayer, or functionally graded structures, can enhance the mechanical and electrical properties of the PEH by combining different materials with different properties .

- **Frequency tuning and bandwidth widening**: The power output of the energy harvester is usually maximized when the resonance frequency of the device matches the frequency of the ambient vibration. However, the ambient vibration frequency is often random and broadband, which means that the energy harvester can only operate efficiently in a narrow frequency range. Therefore, by tuning the resonance frequency of the device to match the ambient vibration frequency, or by widening the frequency bandwidth of the device, the performance of the energy harvester can be enhanced. For example, using frequency tuning mechanisms, such as magnets, springs, masses, etc., can adjust the resonance frequency of the PEH by changing the stiffness or the effective mass of the device. Similarly, using frequency bandwidth widening mechanisms, such as nonlinearities, bistability, multimode, etc., can increase the frequency range of the PEH by inducing complex or multiple vibration modes  .

- **Power management and hybridization**: The power output of the energy harvester is also affected by the electrical load and the storage device connected to the device. Therefore, by using power management techniques, such as impedance matching, rectification, regulation, etc., the power output of the energy harvester can be optimized and delivered to the load or the storage device efficiently. Moreover, by using hybridization techniques, such as combining different types of energy harvesters, such as piezoelectric, electromagnetic, electrostatic, triboelectric, etc., or combining different energy sources, such as vibration, wind, light, heat, etc., the performance of the energy harvester can be enhanced by exploiting the advantages of each type of harvester or source .



### Electromechanical modeling of Lumped parameter model and coupled distributed parameter models and closed-form solutions

- Electromechanical modeling is the process of describing the dynamic behavior of systems that involve both electrical and mechanical components, such as piezoelectric devices.
- Piezoelectric devices are materials that can convert mechanical strain into electrical charge and vice versa, and are widely used for energy harvesting, sensing, and actuation applications.
- There are two main approaches for electromechanical modeling of piezoelectric devices: lumped parameter modeling and distributed parameter modeling.
- Lumped parameter modeling assumes that the piezoelectric device can be represented by a network of discrete elements, such as resistors, capacitors, inductors, and voltage or current sources, that are connected at nodes with zero electrical length and capacitance to ground.
- Lumped parameter modeling is simpler and faster than distributed parameter modeling, but it may not capture the effects of geometry, boundary conditions, and material properties on the device performance.
- Distributed parameter modeling considers the spatial variation of the physical quantities, such as displacement, stress, electric potential, and charge density, along the piezoelectric device, and uses partial differential equations (PDEs) to describe the coupled electromechanical fields.
- Distributed parameter modeling is more accurate and general than lumped parameter modeling, but it may require numerical methods, such as finite element analysis (FEA), to solve the PDEs, which can be computationally expensive and complex.
- A common example of distributed parameter modeling is the transmission line model, which treats the piezoelectric device as a series of infinitesimal segments, each with its own electrical and mechanical properties, and applies Kirchhoff's laws and constitutive relations to derive the governing equations.
- Closed-form solutions are analytical expressions that can be obtained for the electromechanical variables of the piezoelectric device, without using numerical methods, under certain assumptions and simplifications.
- Closed-form solutions are useful for understanding the physical phenomena, validating the numerical results, and optimizing the design parameters of the piezoelectric device.
- However, closed-form solutions are not always available or easy to derive, especially for complex geometries, nonlinearities, and boundary conditions.
- One example of closed-form solution is the Euler-Bernoulli beam theory, which can be used to model the electromechanical behavior of a cantilevered piezoelectric beam under base excitation, assuming small deflections, linear elasticity, and uniform cross-section.



# Unit 3 - ELECTROMAGNETIC ENERGY HARVESTING AND NON-LINEAR TECHNIQUES

- Electromagnetic energy harvesting is the process of converting ambient electromagnetic waves into electrical energy for powering low-power devices, such as wireless sensors, implantable devices, wearable devices, etc.
- Electromagnetic energy harvesting can be classified into two types: far-field and near-field. Far-field harvesting captures the radiated electromagnetic waves from sources such as radio, TV, cellular, and satellite signals. Near-field harvesting exploits the magnetic or electric coupling between the source and the harvester, such as inductive or capacitive coupling.
- Non-linear techniques are used to enhance the performance of electromagnetic energy harvesting systems, such as increasing the output power, widening the bandwidth, or improving the efficiency. Non-linear techniques can be applied to the mechanical, electrical, or magnetic components of the system, such as using non-linear springs, non-linear circuits, or magnetic levitation.
- Some examples of non-linear electromagnetic energy harvesting systems are:

  - A nonlinear electromagnetic harvester with a small magnet moving in an isolating tube surrounded by a coil attached to an electrical circuit. In the nonlinear case, the magnet vibrates between two fixed magnets attached to both ends of the tube. Additionally, two springs are used to limit the movement of the small magnet .
  - A nonlinear electromagnetic harvester with a magnetic levitation mechanism, where a permanent magnet is suspended above a coil by the repulsive force of another magnet. The levitated magnet can oscillate in a large amplitude and frequency range, and induce a voltage in the coil .
  - A nonlinear electromagnetic harvester with a nonlinear interface circuit and a power management circuit. The interface circuit uses a buck-boost DC-DC converter to match the load resistance of the harvester, and the power management circuit uses a supercapacitor and a low-dropout regulator to store and regulate the harvested energy.



### Basic principles for the notes of the Unit 3 - ELECTROMAGNETIC ENERGY HARVESTING AND NON-LINEAR TECHNIQUES in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Electromagnetic energy harvesting (EMEH) is a technique to convert ambient mechanical vibrations into electrical energy using electromagnetic induction .
- EMEH devices typically consist of a coil and a magnet, which can be arranged in different configurations depending on the design and application  .
- EMEH devices can be classified into four categories based on the magnetic levitation principle:
  - Linear: the magnet is suspended by a spring or a flexible beam and moves linearly along the coil axis.
  - Rotary: the magnet is mounted on a rotating shaft and spins around the coil axis.
  - Pendulum: the magnet is attached to a pendulum and swings around the coil axis.
  - Hybrid: the magnet can move in more than one direction or mode, such as linear and rotary, or linear and pendulum.
- EMEH devices can also be classified into linear and nonlinear based on the restoring force of the system  :
  - Linear: the restoring force is proportional to the displacement of the magnet, such as a linear spring or a simple pendulum.
  - Nonlinear: the restoring force is not proportional to the displacement of the magnet, such as a magnetic spring or a Duffing oscillator.
- Nonlinear EMEH devices have some advantages over linear ones, such as wider bandwidth, higher output voltage, and better robustness to environmental variations.
- Nonlinear EMEH devices require nonlinear interface circuits to optimize the power transfer from the harvester to the load. These circuits can be passive or active, depending on the use of external power sources or control signals.
- Nonlinear EMEH devices and circuits can be used for self-powered wireless sensor nodes, which are devices that can sense, process, and communicate data without batteries or wires.
- Nonlinear EMEH devices and circuits face some challenges, such as complex modeling, low efficiency, and high cost .



### Micro fabricated coils and magnetic materials

- Micro fabricated coils are miniature coils that are made using micro fabrication techniques such as lithography, electroplating, etching, etc.  
- Micro fabricated coils can be used for various applications such as magnetooptical data storage, electromagnetic energy harvesting, magnetic neurostimulation, etc.   
- Micro fabricated coils can be classified into two types: planar and three-dimensional. Planar coils have a flat structure with a transparent center, while three-dimensional coils have a cylindrical or spiral structure with a solid core.  
- Micro fabricated coils can be integrated with magnetic materials to form magnetic circuits that enhance the performance of the coils. Magnetic materials can be either soft or hard, depending on their coercivity and remanence. Soft magnetic materials have low coercivity and remanence, and can be easily magnetized and demagnetized by external fields. Hard magnetic materials have high coercivity and remanence, and can retain their magnetization even without external fields.  
- The characteristics of micro fabricated coils depend on several parameters such as the coil geometry, the number of turns, the wire width and thickness, the coil spacing, the magnetic material properties, etc. These parameters affect the coil resistance, inductance, capacitance, quality factor, magnetic flux density, etc.   
- The design of micro fabricated coils and magnetic circuits should consider the trade-offs between the performance and the fabrication constraints. For example, increasing the number of turns can increase the inductance and the magnetic flux density, but also increase the resistance and the fabrication complexity. Similarly, increasing the wire width and thickness can decrease the resistance and increase the power efficiency, but also increase the capacitance and the fabrication cost.



### Scaling of electromagnetic energy harvesting devices

- Electromagnetic energy harvesting devices convert mechanical vibrations into electrical energy using electromagnetic induction.
- The power output of electromagnetic energy harvesting devices depends on several factors, such as the size, mass, frequency and acceleration of the device, as well as the magnetic field strength and coil resistance.
- Scaling laws can be used to compare the performance of different electromagnetic energy harvesting devices and to optimize the design parameters for a given application.
- According to the literature review by T. M. Mitcheson et al.  , the power density metrics of electromagnetic energy harvesting devices can be expressed as follows:

  - Power density per unit volume: $$P_V = \frac{P}{V} \propto \frac{B^2}{R} \omega^4 \xi^2$$
  - Power density per unit mass: $$P_M = \frac{P}{M} \propto \frac{B^2}{R} \omega^2 \xi^2$$
  - Power density per unit acceleration: $$P_A = \frac{P}{A} \propto \frac{B^2}{R} \omega^2 \xi$$

  where $P$ is the power output, $V$ is the volume, $M$ is the mass, $B$ is the magnetic flux density, $R$ is the coil resistance, $\omega$ is the angular frequency, $\xi$ is the displacement amplitude and $A$ is the acceleration amplitude.

- The scaling laws show that the power density of electromagnetic energy harvesting devices increases with the frequency and acceleration of the vibration source, and decreases with the coil resistance and the device size and mass.
- The scaling laws also imply that there are trade-offs between different power density metrics, such as volume, mass and acceleration. For example, increasing the magnetic field strength can increase the power density per unit volume and mass, but decrease the power density per unit acceleration.
- The scaling laws can be used to guide the design and optimization of electromagnetic energy harvesting devices for different applications, such as wireless sensor networks, biomedical implants, wearable devices, etc.
- The scaling laws can also be used to evaluate the limitations and challenges of electromagnetic energy harvesting devices, especially at the micro-scale, where the fabrication processes, the material properties and the environmental factors can affect the performance and reliability of the devices.



### Power Maximization Techniques for Electromagnetic Energy Harvesting

- Electromagnetic energy harvesting is the process of converting ambient mechanical vibrations into electrical energy using electromagnetic induction.
- The basic principle of electromagnetic energy harvesting is that a coil of wire moves relative to a permanent magnet, generating an electromotive force (EMF) across the coil terminals.
- The EMF depends on the number of turns of the coil, the magnetic flux density, and the velocity of the coil.
- The power output of the electromagnetic energy harvester depends on the load resistance, the coil resistance, and the damping factor of the mechanical system.
- To maximize the power output, the following techniques can be applied:

  - Matching the load resistance to the coil resistance, which maximizes the power transfer efficiency.
  - Tuning the natural frequency of the mechanical system to the frequency of the vibration source, which maximizes the displacement of the coil and the EMF.
  - Reducing the damping factor of the mechanical system, which increases the quality factor and the amplitude of the vibration.
  - Increasing the number of turns of the coil, which increases the EMF.
  - Increasing the magnetic flux density, which increases the EMF.
  - Using a nonlinear spring or a bistable mechanism, which can increase the bandwidth and the power output of the harvester under stochastic or broadband vibrations.
  - Using a rectifier circuit, which can convert the alternating current (AC) output of the harvester into direct current (DC) for powering electronic devices.

- Some examples of electromagnetic energy harvesting applications are:

  - Harvesting energy from human motion, such as walking, running, or cycling, for powering wearable devices or biomedical implants.
  - Harvesting energy from environmental vibrations, such as wind, water, or traffic, for powering wireless sensors or actuators.
  - Harvesting energy from electromagnetic waves, such as Wi-Fi, radio, or microwave, for powering communication devices or smart grids.



### Micro and Macro Scale Implementations of Electromagnetic Energy Harvesting

- Electromagnetic energy harvesting is a technique that converts ambient mechanical vibrations into electrical energy by using electromagnetic induction.
- Electromagnetic energy harvesters can be classified into two categories based on their size: micro and macro scale.
- Micro scale electromagnetic energy harvesters are typically fabricated using microelectromechanical systems (MEMS) technology and have dimensions in the order of micrometers to millimeters. They can scavenge energy from micro scale vibrations such as air flow, acoustic noise, or human motion.
- Macro scale electromagnetic energy harvesters are usually composed of discrete coils and magnets and have dimensions in the order of centimeters to meters. They can scavenge energy from macro scale vibrations such as machinery, vehicles, or bridges.
- The design and optimization of both micro and macro scale electromagnetic energy harvesters require the understanding of the basic mechanics, mechatronics, and electrodynamics of the vibration scenario, the harvester structure, and the electrical load.
- Some of the key parameters that affect the performance of electromagnetic energy harvesters are the natural frequency, the damping ratio, the electromagnetic coupling coefficient, the output power, and the power density.
- The natural frequency of the harvester should match the frequency of the vibration source to achieve resonance and maximize the output power.
- The damping ratio of the harvester determines the bandwidth and the quality factor of the resonance. A high damping ratio means a wide bandwidth and a low quality factor, while a low damping ratio means a narrow bandwidth and a high quality factor.
- The electromagnetic coupling coefficient is a measure of how efficiently the mechanical energy is converted into electrical energy by the harvester. It depends on the geometry and the material properties of the coil and the magnet.
- The output power of the harvester is the electrical power delivered to the load. It depends on the vibration amplitude, the natural frequency, the damping ratio, the electromagnetic coupling coefficient, and the load resistance.
- The power density of the harvester is the output power per unit volume or mass of the harvester. It is an important figure of merit for comparing different harvesters and evaluating their suitability for different applications.
- Some of the challenges and opportunities for micro and macro scale electromagnetic energy harvesters are:
  - Scaling down the size of the harvester while maintaining a high output power and power density.
  - Increasing the bandwidth and the robustness of the harvester to cope with variable and unpredictable vibration sources.
  - Integrating the harvester with other components such as energy storage, power management, and wireless communication for autonomous and self-powered systems.
  - Exploring new materials, structures, and fabrication methods for improving the performance and functionality of the harvester.
  - Developing novel applications and markets for electromagnetic energy harvesting in various fields such as biomedical, environmental, industrial, and consumer electronics   .



### Non-linear techniques for electromagnetic energy harvesting

- Electromagnetic energy harvesting (EMEH) is a technique that converts ambient mechanical vibrations into electrical energy using electromagnetic induction.
- Non-linear techniques are used to optimize the harvested energy from EMEH by exploiting the non-linear dynamics of the system, such as bistability, snap-through, magnetic levitation, etc.
- Non-linear techniques can enhance the bandwidth, output voltage, and power density of EMEH, as well as reduce the dependency on the resonance frequency and the initial conditions.
- Some examples of non-linear techniques for EMEH are:

  - Non-linear interface circuit: A circuit that uses a diode bridge rectifier and a capacitor to store the harvested energy and provide a non-linear load to the EMEH. This circuit can improve the power transfer efficiency and the output voltage of the EMEH .
  - Non-linear magnetic spring: A spring that consists of a small magnet moving in a tube surrounded by a coil and two fixed magnets at the ends of the tube. This spring can exhibit bistability and snap-through behavior, which can increase the energy harvesting potential and the bandwidth of the EMEH .
  - Non-linear multi-stable EMEH: An EMEH that has multiple stable equilibrium positions due to the interaction of magnetic forces and mechanical springs. This EMEH can harvest energy from low-frequency and random vibrations, as well as switch between different stable states to adapt to the vibration environment.



# Vibration Control and Steady State Cases

- Vibration control is the process of reducing or eliminating unwanted vibrations in mechanical systems, such as machines, structures, vehicles, etc.
- Vibration control can be achieved by passive or active methods, or a combination of both.
- Passive vibration control involves the use of damping, isolation, or absorption devices that do not require external power or feedback.
- Active vibration control involves the use of sensors, actuators, and controllers that apply forces or moments to counteract the vibrations.
- Steady state cases are the situations where the vibration response of a system reaches a constant amplitude and phase after a transient period.
- Steady state cases can be classified into two types: free vibration and forced vibration.
- Free vibration is the vibration of a system under its natural frequency and damping, without any external excitation.
- Forced vibration is the vibration of a system under an external periodic force or displacement, such as a harmonic, periodic, or random excitation.
- The steady state response of a forced vibration system depends on the frequency ratio, the damping ratio, and the excitation amplitude and phase.
- The frequency ratio is the ratio of the excitation frequency to the natural frequency of the system.
- The damping ratio is the ratio of the damping coefficient to the critical damping coefficient of the system.
- The critical damping coefficient is the minimum damping required to prevent oscillations in the system.
- The steady state response of a forced vibration system can be expressed in terms of the amplitude and phase of the displacement, velocity, or acceleration of the system.
- The amplitude and phase of the steady state response can be obtained by using the complex notation, the phasor diagram, or the trigonometric identities.
- The amplitude and phase of the steady state response can also be plotted as a function of the frequency ratio, which is called the frequency response function or the transfer function of the system.
- The frequency response function can be used to analyze the resonance, bandwidth, and sharpness of the system.
- Resonance is the condition where the frequency ratio is equal to one, and the amplitude of the steady state response reaches a maximum value.
- Bandwidth is the range of frequencies where the amplitude of the steady state response is greater than or equal to a certain fraction of the maximum amplitude.
- Sharpness is the ratio of the maximum amplitude to the amplitude at a certain frequency ratio away from the resonance.



## Unit 4 - ENERGY HARVESTING WIRELESS SENSORS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy from their environment into electrical energy for powering themselves and transmitting data  .
- Energy harvesting wireless sensors can use various sources of energy, such as solar, thermal, kinetic, electromagnetic, or piezoelectric  .
- Energy harvesting wireless sensors have several advantages over battery-powered sensors, such as:
  - They do not require battery replacement or recharging, which reduces maintenance costs and environmental impact  .
  - They can be deployed in remote, inaccessible, or hazardous locations where battery replacement is difficult or impossible  .
  - They can operate for longer periods of time and have higher reliability and availability  .
- Energy harvesting wireless sensors also have some challenges and limitations, such as:
  - They depend on the availability and intensity of the ambient energy sources, which may vary over time and space .
  - They have to balance the trade-off between energy consumption and data quality, such as sampling rate, transmission range, and data rate .
  - They have to deal with the uncertainty and variability of the harvested energy, which may affect the performance and stability of the sensor network .
- Energy harvesting wireless sensors have many potential applications in various domains, such as smart buildings, industrial IoT, environmental monitoring, healthcare, and agriculture   .



### Power sources for WSN

Wireless sensor networks (WSNs) are composed of small, low-power devices that can sense, process, and communicate data wirelessly. WSNs have many applications in environmental monitoring, industrial automation, health care, security, and smart cities. However, one of the main challenges of WSNs is the limited energy supply of the sensor nodes, which affects their lifetime and performance. Therefore, finding suitable power sources for WSNs is an important research topic.

According to    , power sources for WSNs can be classified into three categories:

- **Energy reservoirs**: These are devices that store energy on the node, such as batteries, capacitors, or fuel cells. They have the advantage of being simple, reliable, and widely available, but they have the drawback of being finite, bulky, and costly to replace or recharge.
- **Power distribution**: These are methods that deliver power to the node from an external source, such as wires, electromagnetic waves, or ultrasound. They have the advantage of providing continuous and unlimited power, but they have the drawback of being complex, intrusive, and dependent on the infrastructure and environment.
- **Power scavenging**: These are methods that harvest ambient energy from the surroundings of the node, such as solar, thermal, mechanical, or biochemical energy. They have the advantage of being self-sustaining, scalable, and environmentally friendly, but they have the drawback of being intermittent, variable, and low-power.

Some examples of power sources for WSNs in each category are:

- **Energy reservoirs**: Alkaline batteries, lithium-ion batteries, supercapacitors, micro fuel cells, nuclear batteries.
- **Power distribution**: Power line communication, inductive coupling, radio frequency identification, acoustic power transmission.
- **Power scavenging**: Photovoltaic cells, thermoelectric generators, piezoelectric harvesters, electromagnetic harvesters, biofuel cells.

The choice of the best power source for a WSN depends on several factors, such as the power consumption and duty cycle of the sensor nodes, the size and topology of the network, the availability and quality of the ambient energy sources, the cost and maintenance of the power devices, and the environmental and safety constraints. A trade-off analysis between these factors is necessary to optimize the design and performance of the WSN.    

: Roundy, S., Wright, P. K., & Rabaey, J. (2004). Power sources for wireless sensor networks. In Wireless sensor networks (pp. 1-17). Springer, Berlin, Heidelberg.
: Roundy, S., & Wright, P. K. (2004). Power sources for wireless sensor networks. In European Workshop on Wireless Sensor Networks (pp. 1-17). Springer, Berlin, Heidelberg.
: Roundy, S., & Wright, P. K. (2004). Power sources for wireless sensor networks. In Wireless Sensor Networks (pp. 1-17). Springer, Berlin, Heidelberg.
: Roundy, S., & Wright, P. K. (2004). Power sources for wireless sensor networks. In Wireless Sensor Networks (pp. 1-17). Springer, Berlin, Heidelberg.



### Power generation for the notes of the Unit 4 - ENERGY HARVESTING WIRELESS SENSORS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting wireless sensors are devices that can capture ambient energy from their surroundings and convert it into usable electrical power for wireless communication and sensing applications .
- Energy harvesting can provide a sustainable and reliable power source for wireless sensors, eliminating the need for batteries or wires, and reducing maintenance and environmental costs  .
- Energy harvesting wireless sensors can be classified into four categories based on the type of ambient energy they harvest :
  - Solar harvesting: using photovoltaic cells to convert light energy into electrical energy .
  - Thermal harvesting: using thermoelectric generators to convert heat gradients or waste heat into electrical energy .
  - Vibration harvesting: using piezoelectric, electromagnetic, or electrostatic transducers to convert mechanical vibrations or motions into electrical energy  .
  - Radio frequency (RF) harvesting: using antennas or rectennas to capture electromagnetic waves from wireless transmissions or ambient sources and convert them into electrical energy  .
- Energy harvesting wireless sensors have various applications in different domains, such as industrial, environmental, biomedical, smart buildings, and smart cities   .
- Energy harvesting wireless sensors face some challenges and limitations, such as low and variable power output, power management and storage issues, efficiency and reliability trade-offs, and interference and security risks    .
- Energy harvesting wireless sensors are expected to play a key role in the development of the Internet of Things (IoT), enabling ubiquitous and pervasive sensing and communication with minimal environmental impact and operational cost   .



# Unit 4 - ENERGY HARVESTING WIRELESS SENSORS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy from their environment into electrical energy for powering themselves and transmitting data  .
- Energy harvesting wireless sensors have several advantages over conventional battery-powered sensors, such as:
  - They eliminate the need for battery replacement and maintenance, which reduces the cost and environmental impact of sensor networks  .
  - They enable the deployment of sensors in hard-to-reach or hazardous locations, where battery replacement is impractical or dangerous .
  - They increase the reliability and lifetime of sensor networks, as they do not depend on the availability and capacity of batteries  .
  - They allow the integration of sensors with various energy sources, such as solar, thermal, vibration, radio frequency, etc., which can enhance the functionality and adaptability of sensor networks  .
- Energy harvesting wireless sensors typically consist of four main components :
  - An energy harvester, which captures and converts ambient energy into electrical energy.
  - An energy storage unit, which stores the harvested energy for later use or provides a stable power supply for the sensor.
  - A sensor, which measures a physical or environmental parameter, such as temperature, humidity, motion, etc.
  - A wireless transceiver, which communicates the sensor data to a base station or other nodes in the network.
- Energy harvesting wireless sensors can be classified into two types based on their energy management strategy:
  - Energy-neutral sensors, which operate continuously by balancing the energy consumption and generation. They require a sufficient and stable energy source to meet the power demand of the sensor and the transceiver.
  - Intermittently-powered sensors, which operate periodically by switching between active and sleep modes. They can tolerate a variable and intermittent energy source, but they may suffer from data loss or inconsistency due to power interruptions.
- Energy harvesting wireless sensors can be applied to various domains, such as smart buildings, industrial automation, environmental monitoring, healthcare, etc. Some examples of energy harvesting wireless sensors are  :
  - Solar-powered temperature and humidity sensors for indoor climate control.
  - Thermoelectric-powered vibration sensors for machine condition monitoring.
  - Piezoelectric-powered pressure sensors for tire pressure monitoring.
  - Radio frequency-powered RFID tags for asset tracking and identification.



### Examples for the notes of the Unit 4 - ENERGY HARVESTING WIRELESS SENSORS in the subject of KOT 062 ENERGY HARVESTING TECHNOLOGIES AND POWERMANAGEMENT FOR IOT DEVICES KCS

- Energy harvesting wireless sensors are devices that can collect and convert ambient energy from their environment into electrical energy for powering themselves and transmitting data  .
- Energy harvesting wireless sensors can use various sources of energy, such as solar, thermal, kinetic, electromagnetic, or radio frequency  .
- Energy harvesting wireless sensors have several advantages over battery-powered sensors, such as:
  - They are maintenance-free, flexible and inexpensive to install .
  - They can operate in harsh or inaccessible environments where battery replacement is difficult or impossible .
  - They can extend the lifetime and reliability of wireless sensor networks .
  - They can reduce the environmental impact of battery disposal .
- Energy harvesting wireless sensors have various applications in smart building, industrial, environmental, biomedical, and security domains   .
- Energy harvesting wireless sensors face some challenges, such as:
  - The variability and unpredictability of the energy sources .
  - The trade-off between energy consumption and data quality .
  - The need for efficient energy management and storage techniques .
  - The compatibility and interoperability issues with different wireless standards and protocols  .
- Energy harvesting wireless sensors require novel design approaches and optimization methods to address these challenges and improve their performance .



### Case Studies for the Notes of the Unit 4 - Energy Harvesting Wireless Sensors in the Subject of KOT 062 Energy Harvesting Technologies and Power Management for IoT Devices KCS

- Energy harvesting wireless sensors (EHWS) are devices that can collect ambient energy from their surroundings and convert it into electrical energy to power themselves and perform sensing tasks.
- EHWS can reduce the dependency on batteries, which have limited lifetime, environmental impact, and maintenance cost.
- EHWS can enable new applications and scenarios for wireless sensor networks (WSN), such as industrial monitoring, environmental sensing, smart buildings, and health care.
- Some examples of energy harvesting sources are solar, thermal, kinetic, vibration, electromagnetic, and radio frequency.
- Some examples of energy harvesting technologies are photovoltaic, thermoelectric, piezoelectric, electrostatic, electromagnetic, and RF rectification.
- Some examples of energy harvesting wireless sensors case studies are:

  - Energy Prediction and Energy Management in Kinetic Energy-Harvesting Wireless Sensors for Industry 4.0
    - This case study presents a kinetic energy harvesting system using piezoelectric transducers to power a wireless sensor node for industrial monitoring.
    - The system consists of a piezoelectric cantilever beam, a rectifier circuit, a supercapacitor, a wireless sensor node, and a base station.
    - The system uses a machine learning algorithm to predict the energy harvested from the vibrations and to optimize the duty cycle of the wireless sensor node.
    - The system achieves an energy autonomy of 99.8% and a data transmission rate of 99.9% in a real industrial scenario.
  - Powering nodes of wireless sensor networks with energy harvesters for environmental monitoring
    - This case study presents a solar energy harvesting system to power a wireless sensor node for environmental monitoring.
    - The system consists of a solar panel, a charge controller, a battery, a wireless sensor node, and a base station.
    - The system uses a maximum power point tracking (MPPT) algorithm to maximize the energy harvested from the solar panel and to regulate the battery charging.
    - The system achieves an energy autonomy of 100% and a data transmission rate of 100% in a real outdoor scenario.
  - Energy harvesting in wireless sensor networks: A taxonomic survey
    - This case study presents a comprehensive survey of the state-of-the-art energy harvesting techniques and algorithms for wireless sensor networks.
    - The survey categorizes the energy harvesting sources, technologies, architectures, and protocols according to different criteria and metrics.
    - The survey analyzes the advantages and disadvantages of each category and provides some open challenges and future directions for research and development.



### Harvesting Microelectronic Circuits

- Harvesting microelectronic circuits are circuits that can extract and convert ambient energy sources, such as light, heat, vibration, or radio waves, into electrical energy for powering low-power devices, such as wireless sensors, biomedical implants, or wearable electronics   .
- Harvesting microelectronic circuits typically consist of four main components: a transducer, a rectifier, a voltage regulator, and a storage element  .
  - A transducer is a device that converts one form of energy into another, such as a photovoltaic cell, a thermoelectric generator, a piezoelectric element, or an antenna  .
  - A rectifier is a circuit that converts an alternating current (AC) output from the transducer into a direct current (DC) output, such as a diode bridge, a voltage doubler, or a synchronous rectifier  .
  - A voltage regulator is a circuit that maintains a constant output voltage level regardless of the input voltage variations, such as a linear regulator, a switched-capacitor regulator, or a buck-boost converter  .
  - A storage element is a device that stores electrical energy for later use, such as a capacitor, a battery, or a supercapacitor  .
- Harvesting microelectronic circuits face several challenges and trade-offs, such as low and variable input power, high conversion efficiency, low quiescent power, small size and weight, and long lifetime   .
- Harvesting microelectronic circuits require careful design and optimization of each component and the overall system to achieve the best performance and reliability   .
- Harvesting microelectronic circuits have many potential applications and benefits, such as reducing the need for batteries, enabling self-powered and autonomous devices, enhancing environmental sustainability, and improving quality of life   .



### Power Conditioning and Losses for Energy Harvesting Wireless Sensors

- Power conditioning is the process of converting the raw electrical output of an energy harvester into a suitable form for powering a wireless sensor node or charging a storage device.
- Power conditioning circuits typically include rectifiers, voltage regulators, DC-DC converters, and maximum power point trackers (MPPTs).
- The main objectives of power conditioning are to:
  - Match the impedance of the energy harvester to the load or storage device for optimal power transfer.
  - Provide a stable and regulated voltage or current output for the wireless sensor node or storage device.
  - Minimize the losses and quiescent power consumption of the power conditioning circuit.
  - Maximize the utilization and efficiency of the energy harvester.
- Power losses in energy harvesting systems can be classified into three types:
  - Real power losses: These are the losses due to the resistance of the components, wires, and traces, and the switching losses of the transistors and diodes. Real power losses reduce the amount of useful power delivered to the load or storage device.
  - Reactive power losses: These are the losses due to the parasitic capacitance and inductance of the components, wires, and traces, and the non-ideal behavior of the energy harvester. Reactive power losses cause power oscillations and phase shifts between the voltage and current, which reduce the power factor and the efficiency of the system.
  - Harmonic power losses: These are the losses due to the distortion of the voltage and current waveforms caused by the non-linear behavior of the components, especially the rectifiers and converters. Harmonic power losses increase the total harmonic distortion (THD) and the harmonic power factor (HPF) of the system, which reduce the quality and reliability of the power output.
- Power conditioning techniques for energy harvesting systems can be divided into two categories:
  - Passive techniques: These are the techniques that use passive components, such as resistors, capacitors, inductors, and diodes, to perform power conditioning functions. Passive techniques are simple, low-cost, and robust, but they have limited performance and flexibility, and they may not be able to achieve optimal power transfer or regulation for different energy harvesters and loads.
  - Active techniques: These are the techniques that use active components, such as transistors, integrated circuits, and microcontrollers, to perform power conditioning functions. Active techniques are more complex, costly, and sensitive, but they have higher performance and flexibility, and they can adapt to different energy harvesters and loads using feedback and control algorithms.
- Some examples of power conditioning techniques for energy harvesting systems are:
  - Peak rectifier: This is a passive technique that uses a diode bridge and a capacitor to rectify and smooth the AC output of an energy harvester. The peak rectifier is simple and widely used, but it has high losses due to the diode voltage drop and the capacitor leakage, and it does not provide any voltage regulation or MPPT function.
  - Synchronous rectifier: This is an active technique that uses transistors and a control circuit to replace the diodes in the peak rectifier. The synchronous rectifier reduces the losses by turning on and off the transistors in synchrony with the AC output of the energy harvester, eliminating the diode voltage drop. The synchronous rectifier can also provide some voltage regulation and MPPT function by adjusting the duty cycle of the transistors.
  - Buck converter: This is an active technique that uses a transistor, a diode, an inductor, and a capacitor to step down the voltage output of an energy harvester. The buck converter is efficient and widely used, but it has some losses due to the switching and conduction of the transistor and the diode, and the parasitics of the inductor and the capacitor. The buck converter can also provide voltage regulation and MPPT function by adjusting the duty cycle of the transistor using a feedback and control circuit.
  - Boost converter: This is an active technique that uses a transistor, a diode, an inductor, and a capacitor to step up the voltage output of an energy harvester. The boost converter is useful for low-voltage energy harvesters, such as thermoelectric generators, but it has higher losses than the buck converter due to the higher current and voltage stress on the components. The boost converter can also provide voltage regulation and MPPT function by adjusting the duty cycle of the transistor using a feedback and control circuit.
  - Synchronized switch harvesting on inductor (SSHI): This is an active technique that uses a transistor, a diode



# Unit 5 - SELECTED APPLICATIONS OF ENERGY HARVESTING SYSTEMS

Energy harvesting systems are devices that collect ambient energy from the environment and convert it into electrical energy for powering low-power electronic components. Energy harvesting systems can extend the battery life of wireless sensors and wearable devices, enable autonomous operation of remote systems, and provide energy-efficient solutions for various sectors.

Some of the selected applications of energy harvesting systems are:

- **Industrial applications**: Energy harvesting systems can be used for remote monitoring, predictive maintenance, and energy management of industrial equipment and processes. For example, vibration energy harvesters can power wireless sensors that measure the condition and performance of rotating machinery, such as motors, pumps, and turbines. Thermal energy harvesters can power sensors that monitor the temperature and pressure of pipelines, boilers, and reactors.
- **Consumer electronics applications**: Energy harvesting systems can be used for powering portable and wearable devices, such as smart watches, fitness trackers, and medical implants. For example, piezoelectric energy harvesters can convert the mechanical stress and strain from human motion, such as walking, running, or breathing, into electrical energy for charging batteries or directly powering devices. Photovoltaic energy harvesters can capture the solar or ambient light and convert it into electrical energy for powering devices or displays.
- **Building and home automation applications**: Energy harvesting systems can be used for controlling and optimizing the lighting, heating, ventilation, and air conditioning (HVAC) systems of buildings and homes. For example, electromagnetic energy harvesters can power wireless switches and sensors that detect the occupancy, motion, and ambient light levels of rooms and adjust the lighting and HVAC accordingly. Thermoelectric energy harvesters can power sensors that measure the indoor and outdoor temperature and humidity and optimize the energy consumption of HVAC systems.
- **Wireless sensor network (WSN) applications**: Energy harvesting systems can be used for powering wireless sensors that collect and transmit data from various environments, such as forests, oceans, bridges, and roads. For example, acoustic energy harvesters can power underwater sensors that monitor the marine life, water quality, and seismic activity. Wind energy harvesters can power sensors that measure the wind speed, direction, and turbulence on bridges and buildings.
- **Security system applications**: Energy harvesting systems can be used for powering security devices, such as cameras, alarms, and locks. For example, radio frequency (RF) energy harvesters can power wireless cameras and sensors that detect the presence and movement of intruders and transmit the images and signals to a central station. Kinetic energy harvesters can power locks and alarms that are activated by the touch or motion of a user or an intruder.



### Case studies for Implanted medical devices

- Implantable medical devices (IMDs) are electronic devices that are inserted into the human body for various purposes, such as monitoring, diagnosis, therapy, or enhancement.
- IMDs require a reliable and long-lasting power source to function properly and safely. However, conventional batteries have limitations such as limited lifespan, toxicity, infection risk, and need for replacement surgery.
- Energy harvesting is an alternative approach to power IMDs by converting ambient energy sources from the human body or the environment into electrical energy. Energy harvesting can potentially extend the lifetime of IMDs, reduce the size and weight of the devices, and eliminate the need for invasive procedures.
- Some examples of energy sources that can be harvested for IMDs are:

  - **Biomechanical energy**: This is the energy generated by the movement of muscles, organs, blood, or body fluids. For example, a piezoelectric device can harvest energy from the heartbeat, respiration, or blood flow .
  - **Biochemical energy**: This is the energy derived from the chemical reactions of biomolecules, such as glucose, oxygen, or ATP. For example, a biofuel cell can harvest energy from the oxidation of glucose and oxygen in the blood or interstitial fluid .
  - **Thermal energy**: This is the energy produced by the temperature difference between the body and the environment. For example, a thermoelectric device can harvest energy from the heat dissipation of the skin or the core body temperature .
  - **Electromagnetic energy**: This is the energy radiated by electromagnetic waves, such as radiofrequency, microwave, or light. For example, a wireless power transfer system can harvest energy from an external transmitter or a solar cell can harvest energy from ambient light .

- Some examples of IMDs that use energy harvesting are:

  - **Cardiac pacemakers**: These are devices that deliver electrical impulses to the heart to regulate its rhythm. A piezoelectric device can harvest energy from the heartbeat or the chest wall motion to power the pacemaker .
  - **Neural stimulators**: These are devices that stimulate the nerves or the brain to treat various neurological disorders, such as epilepsy, Parkinson's disease, or chronic pain. A biofuel cell can harvest energy from the glucose and oxygen in the cerebrospinal fluid to power the neural stimulator .
  - **Drug delivery systems**: These are devices that deliver drugs to specific locations in the body in a controlled manner. A thermoelectric device can harvest energy from the body heat to power the drug delivery system .
  - **Biosensors**: These are devices that measure various physiological parameters, such as blood pressure, glucose level, or oxygen saturation. A wireless power transfer system or a solar cell can harvest energy from external sources to power the biosensor .

- Energy harvesting for IMDs faces several challenges, such as:

  - **Low and variable power output**: The energy sources from the human body or the environment are often weak and intermittent, which limits the amount and quality of power that can be harvested. Therefore, efficient energy conversion, storage, and management techniques are needed to ensure stable and sufficient power supply for IMDs .
  - **Biocompatibility and safety**: The energy harvesting devices and materials should be compatible with the biological tissues and fluids, and should not cause any adverse effects, such as inflammation, infection, or toxicity. Moreover, the energy harvesting devices should not interfere with the normal functions of the body or the IMDs, such as the cardiac or neural signals .
  - **Miniaturization and integration**: The energy harvesting devices should be small and lightweight to reduce the invasiveness and discomfort of the implantation. Moreover, the energy harvesting devices should be integrated with the IMDs to form a compact and self-contained system .

- Energy harvesting for IMDs is a promising and emerging field that can enable self-powered and long-lasting IMDs for various medical applications. However, further research and development are needed to overcome the challenges and limitations of the current technologies and to demonstrate the feasibility and reliability of the energy harvesting devices in vivo  .

: Energy harvesting for the implantable biomedical devices: issues



### Bio-MEMS based applications

- Bio-MEMS stands for biomedical micro-electro-mechanical systems, which are devices that integrate mechanical, electrical, and biological components at the microscale.
- Bio-MEMS have many potential applications in clinical medicine, environmental monitoring, biological analysis, and chemical synthesis.
- Some of the main categories of bio-MEMS applications are:
  - Surgical: These devices are used to perform minimally invasive procedures, such as micro-needles, micro-catheters, micro-sensors, and micro-actuators.
  - Diagnostic: These devices are used to detect and quantify various biological entities, such as molecules, antibodies, DNA, bacteria, and viruses, using biochips, biosensors, microarrays, and microfluidics. Examples include next-generation sequencing of DNA (NGS) and point-of-care diagnostics.
  - Therapeutic: These devices are used to deliver drugs, genes, or cells to specific targets, using micro-pumps, micro-valves, micro-reservoirs, and micro-implants.
- Bio-MEMS devices offer several advantages over conventional methods, such as high sensitivity, specificity, speed, accuracy, portability, and low cost.
- Bio-MEMS devices also face some challenges, such as biocompatibility, sterilization, integration, and reliability.



### Harvesting for RF Sensors and ID Tags

- RF sensors and ID tags are devices that use radio frequency (RF) signals to communicate data, such as identification, location, temperature, etc.
- RF sensors and ID tags can be classified into passive, semi-passive, and active, depending on their power source and functionality.
- Passive RF sensors and ID tags have no battery and rely on the RF reader signal to deliver energy and power up their circuitry . They have a limited communication range and data rate, but a long lifetime and low cost.
- Semi-passive RF sensors and ID tags have a battery that powers the sensor and the logic circuit, but not the RF communication. They use the RF reader signal to transmit data back to the reader . They have a longer communication range and data rate than passive tags, but a shorter lifetime and higher cost.
- Active RF sensors and ID tags have a battery that powers the sensor, the logic circuit, and the RF communication. They can initiate communication with the reader or other tags, and have a high communication range and data rate . They have a short lifetime and high cost, and require frequent battery replacement or recharging.
- Energy harvesting is a technique that enables RF sensors and ID tags to collect energy from the environment, such as RF, motion, heat, light, etc., and store it in a capacitor or a battery for later use   . Energy harvesting can extend the lifetime, increase the functionality, and reduce the maintenance cost of RF sensors and ID tags, especially for active ones.
- Energy harvesting can be performed by using different types of transducers, such as antennas, piezoelectric, thermoelectric, photovoltaic, etc., depending on the type and availability of the ambient energy source   . The harvested energy can be conditioned by using rectifiers, voltage converters, regulators, etc., to match the requirements of the RF sensor or ID tag circuit   .
- Energy harvesting can also be performed by exploiting the power carried by the harmonic signals generated by the RFID chip. For example, the third harmonic signal of the UHF RFID chip can be used to power up an associated sensor to the RFID tag, without affecting the communication performance of the tag.
- Energy harvesting for RF sensors and ID tags is a critical design feature on the path to the grand vision of ubiquitous computing, where every object can be sensed, identified, and connected to the Internet of Things (IoT)   . Energy harvesting can enable self-powered, autonomous, and intelligent RF sensors and ID tags that can provide various applications, such as asset tracking, inventory management, environmental monitoring, health care, security, etc.   .



### Powering Wireless SHM Sensor Nodes

- Wireless sensor nodes (WSNs) are devices that can sense, process, and communicate data wirelessly, and are widely used for structural health monitoring (SHM) applications, such as detecting damage, cracks, or corrosion in buildings, bridges, pipelines, etc.
- However, one of the main challenges of WSNs is how to power them, as they typically rely on batteries that have limited lifetime, need periodic replacement, and may not be accessible or environmentally friendly.
- Energy harvesting (EH) is a promising solution to overcome this challenge, as it can convert ambient energy sources, such as solar, thermal, vibration, or electromagnetic radiation, into electrical energy that can be used to power the WSNs.
- EH can enable WSNs to operate autonomously, indefinitely, and maintenance-free, and can also reduce the size, weight, and cost of the nodes.
- However, EH also poses some challenges, such as the variability, intermittency, and low power density of the ambient energy sources, the mismatch between the harvested energy and the load demand, and the trade-off between the performance and the complexity of the EH system.
- Therefore, EH systems for WSNs need to be carefully designed, optimized, and integrated, taking into account the characteristics of the energy source, the energy conversion mechanism, the energy storage device, the power management circuit, and the WSN application.
- Some examples of EH systems for WSNs are:
  - Solar EH: using photovoltaic cells to convert sunlight into electricity. This is one of the most common and mature EH techniques, as it can provide high power density and long-term operation. However, it also depends on the availability and intensity of sunlight, which can vary with time, location, and weather conditions. Solar EH also requires a large surface area and a proper orientation of the photovoltaic cells, which may not be feasible or desirable in some SHM scenarios.
  - Thermal EH: using thermoelectric generators (TEGs) to convert temperature gradients into electricity. This can be useful for SHM applications where there is a significant difference between the temperature of the structure and the ambient air, such as pipelines, boilers, or engines. However, thermal EH also has some limitations, such as the low efficiency and power density of the TEGs, the need for good thermal contact and insulation, and the degradation of the TEGs over time.
  - Vibration EH: using piezoelectric, electromagnetic, or electrostatic transducers to convert mechanical vibrations into electricity. This can be suitable for SHM applications where the structure is subject to dynamic loads, such as wind, traffic, or machinery. However, vibration EH also faces some challenges, such as the narrow frequency bandwidth and low voltage output of the transducers, the need for resonance tuning and impedance matching, and the trade-off between the damping and the power generation of the system.
  - Electromagnetic EH: using antennas or rectennas to convert electromagnetic waves into electricity. This can be applicable for SHM applications where there is a strong and reliable source of electromagnetic radiation, such as radio, TV, or cellular signals, or where wireless energy transmission (WET) can be implemented. However, electromagnetic EH also has some drawbacks, such as the low efficiency and power density of the antennas or rectennas, the need for frequency and polarization matching, and the interference and safety issues of the electromagnetic radiation.

