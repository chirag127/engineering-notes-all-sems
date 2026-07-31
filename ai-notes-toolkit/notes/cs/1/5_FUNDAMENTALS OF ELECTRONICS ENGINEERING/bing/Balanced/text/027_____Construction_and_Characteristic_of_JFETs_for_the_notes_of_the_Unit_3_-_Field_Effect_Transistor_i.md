### Construction and Characteristic of JFETs

- A JFET (Junction Field Effect Transistor) is a three-terminal semiconductor device that can be used as a voltage-controlled resistor, switch or amplifier .
- A JFET is constructed using a long channel of semiconductor material, either N-type or P-type, with two ohmic contacts at the ends, called the source (S) and the drain (D), and a reverse-biased PN junction on each side, called the gate (G)   .
- The symbols and basic construction for both N-channel and P-channel JFETs are shown below:

![JFET symbols and construction](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/transistor-tran5.gif)

- The current flow in a JFET is controlled by the voltage applied between the gate and the source, VGS, which modulates the width of the channel and thus the resistance of the device   .
- The JFET has two operating regions: the ohmic region and the saturation region  .
- In the ohmic region, the JFET behaves like a linear resistor, with a low drain-source voltage, VDS, and a high channel width  .
- In the saturation region, the JFET behaves like a constant current source, with a high VDS and a low channel width  .
- The transition from the ohmic region to the saturation region occurs when VDS reaches a value called the pinch-off voltage, VP, which depends on the doping level and the geometry of the device  .
- The characteristic curves of a JFET show the relationship between the drain current, ID, and the drain-source voltage, VDS, for different values of VGS  .
- The characteristic curves of an N-channel JFET are shown below:

![JFET characteristic curves](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/transistor-tran51.gif)

- The transfer characteristic of a JFET shows the relationship between the drain current, ID, and the gate-source voltage, VGS, for a constant value of VDS  .
- The transfer characteristic of an N-channel JFET is shown below:

![JFET transfer characteristic](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/transistor-tran52.gif)

- The transfer characteristic of a JFET is nonlinear and can be approximated by a quadratic equation of the form: ID = IDSS(1 - VGS/VP)^2, where IDSS is the maximum drain current when VGS = 0 and VP is the pinch-off voltage  .
- The JFET has some advantages over the BJT, such as high input impedance, low noise, low power consumption and high temperature stability   .
- The JFET also has some disadvantages, such as low gain, limited frequency response and susceptibility to damage by static electricity   .