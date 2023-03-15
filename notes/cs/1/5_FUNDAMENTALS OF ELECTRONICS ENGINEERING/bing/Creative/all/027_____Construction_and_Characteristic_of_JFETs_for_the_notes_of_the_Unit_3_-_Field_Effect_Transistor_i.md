# Construction and Characteristic of JFETs

- A JFET (Junction Field Effect Transistor) is a three-terminal semiconductor device that can be used as a voltage-controlled resistor, switch, or amplifier .
- A JFET is constructed using a long channel of semiconductor material, either N-type or P-type, with two ohmic contacts at the ends, called the source (S) and the drain (D), and a reverse-biased PN junction on each side, called the gate (G)  .
- The symbols and basic construction for both N-channel and P-channel JFETs are shown below:

![JFET symbols and construction](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/transistor-tran5.gif)

- The operation of a JFET is based on the modulation of the channel resistance by the gate voltage. When the gate voltage is zero, the channel is fully open and the JFET conducts the maximum current from source to drain, called the drain saturation current (IDSS) .
- When the gate voltage is negative for an N-channel JFET, or positive for a P-channel JFET, the depletion regions around the PN junctions expand, reducing the effective width of the channel and increasing its resistance. This reduces the drain current for a given drain voltage .
- When the gate voltage reaches a certain value, called the pinch-off voltage (VP), the depletion regions touch each other and the channel is closed, resulting in zero drain current. The pinch-off voltage is negative for an N-channel JFET, and positive for a P-channel JFET .
- The relationship between the drain current and the gate voltage is called the transfer characteristic of the JFET. It is usually expressed as a function of the normalized drain current (ID/IDSS) and the normalized gate voltage (VGS/VP) .
- The transfer characteristic of a JFET is shown below:

![JFET transfer characteristic](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/transistor-tran51.gif)

- The relationship between the drain current and the drain voltage is called the drain characteristic of the JFET. It depends on the gate voltage and the channel resistance .
- The drain characteristic of a JFET has two regions: the ohmic region, where the drain current is linearly proportional to the drain voltage, and the saturation region, where the drain current is independent of the drain voltage and determined by the gate voltage .
- The drain characteristic of a JFET is shown below:

![JFET drain characteristic](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/transistor-tran52.gif)

- The advantages of JFETs over BJTs are: lower power consumption, higher input impedance, lower noise, better thermal stability, and simpler biasing circuits  .
- The disadvantages of JFETs are: lower gain, lower frequency response, higher distortion, and more sensitivity to temperature and radiation  .