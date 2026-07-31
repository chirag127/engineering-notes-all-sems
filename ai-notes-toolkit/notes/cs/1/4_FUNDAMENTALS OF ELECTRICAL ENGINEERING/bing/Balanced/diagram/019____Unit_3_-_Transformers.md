## Unit 3 - Transformers

Transformers are electrical devices that transfer energy between two or more circuits through electromagnetic induction. Transformers can change the voltage, current, or impedance of an AC circuit without changing its frequency or power.

### Learning Objectives

By the end of this unit, you should be able to:

- Explain the principle of electromagnetic induction and how it is used in transformers.
- Identify the main components of a transformer and their functions.
- Distinguish between step-up and step-down transformers and their applications.
- Calculate the voltage, current, and power ratios of a transformer using the turns ratio and the conservation of energy.
- Describe the types of losses in a transformer and how to minimize them.
- Analyze the equivalent circuit of a transformer and its phasor diagram.

### Contents

- 3.1 Electromagnetic Induction
- 3.2 Transformer Construction and Operation
- 3.3 Transformer Ratings and Efficiency
- 3.4 Transformer Equivalent Circuit and Phasor Diagram
- 3.5 Summary and Review Questions

### 3.1 Electromagnetic Induction

Electromagnetic induction is the phenomenon of generating an electric current in a conductor by changing the magnetic flux linked with it. The electric current is proportional to the rate of change of magnetic flux, as given by Faraday's law of induction:

$$\varepsilon = -N \frac{d\phi}{dt}$$

where $\varepsilon$ is the induced electromotive force (emf), $N$ is the number of turns of the conductor, and $\phi$ is the magnetic flux.

The negative sign indicates that the induced emf opposes the change in magnetic flux, as stated by Lenz's law.

There are two ways to change the magnetic flux in a conductor:

- Moving the conductor in a stationary magnetic field, as in a generator.
- Varying the magnetic field around a stationary conductor, as in a transformer.

A transformer uses the second method, by applying an alternating current (AC) to a primary coil, which creates an alternating magnetic field around a secondary coil. The alternating magnetic field induces an alternating emf in the secondary coil, which can be connected to a load.

### 3.2 Transformer Construction and Operation

A transformer consists of two or more coils of insulated wire, called the primary and secondary windings, wound around a common core of magnetic material, such as iron or ferrite. The core provides a low reluctance path for the magnetic flux, and enhances the coupling between the windings.

The primary winding is connected to an AC source, such as a generator or a power grid, and the secondary winding is connected to a load, such as a motor or a lamp. The AC source produces an alternating current in the primary winding, which generates an alternating magnetic flux in the core. The alternating magnetic flux induces an alternating emf in the secondary winding, which drives an alternating current in the load.

The ratio of the number of turns in the primary and secondary windings determines the ratio of the voltages and currents in the transformer. If the secondary winding has more turns than the primary winding, the transformer is called a step-up transformer, because it increases the voltage and decreases the current. If the secondary winding has fewer turns than the primary winding, the transformer is called a step-down transformer, because it decreases the voltage and increases the current.

The diagram below shows a simple transformer with a primary winding of $N_1$ turns and a secondary winding of $N_2$ turns.

![A simple transformer with a primary winding of N1 turns and a secondary winding of N2 turns.](https://i.imgur.com/0pZ0X5N.png)

The voltage and current ratios of a transformer are given by:

$$\frac{V_2}{V_1} = \frac{N_2}{N_1} = a$$

$$\frac{I_1}{I_2} = \frac{N_2}{N_1} = a$$

where $V_1$ and $I_1$ are the voltage and current in the primary winding, $V_2$ and $I_2$ are the voltage and current in the secondary winding, and $a$ is the turns ratio of the transformer.

The power in the primary and secondary windings are equal, assuming no losses in the transformer, as given by the conservation of energy:

$$P_1 = P_2$$

$$V_1 I_1 = V_2 I_2$$

### 3.3 Transformer Ratings and Efficiency

A transformer has two main ratings: the voltage rating and the power rating. The voltage rating specifies the maximum voltage that can be applied to the primary and secondary windings