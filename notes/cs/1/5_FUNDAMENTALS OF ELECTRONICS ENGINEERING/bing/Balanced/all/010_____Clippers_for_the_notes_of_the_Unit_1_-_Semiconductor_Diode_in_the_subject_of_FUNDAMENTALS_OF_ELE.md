# Clippers for the notes of the Unit 1 - Semiconductor Diode in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A **semiconductor diode** is a device that allows current to flow in one direction, but blocks it in the opposite direction  .
- A semiconductor diode is made of two types of semiconductor materials: **p-type** and **n-type**. The p-type has a lot of holes (positive charge carriers), while the n-type has a lot of electrons (negative charge carriers) .
- The junction of the p-type and n-type materials is called the **pn junction**. The pn junction has two terminals: the **anode** (connected to the p-type) and the **cathode** (connected to the n-type) .
- The symbol of a semiconductor diode is shown below:

![diode symbol](https://www.fluke.com/sites/default/files/styles/asset_image_full_width/public/lead-images/what-is-a-diode-lead-image.jpg?itok=8y0l1w1A)

- The anode is marked with a triangle, while the cathode is marked with a line. The direction of the triangle indicates the direction of the forward current (from anode to cathode) .
- The characteristics of a semiconductor diode are shown in the following graph:

![diode characteristics](https://www.khanacademy.org/science/electrical-engineering/ee-semiconductor-devices/ee-diode/a/ee-diode-circuit-element/a/ee-diode-circuit-element/ee-diode-circuit-element_files/ee-diode-circuit-element-1.png)

- The horizontal axis is the voltage across the diode (**Vd**), while the vertical axis is the current through the diode (**Id**).
- The graph shows that when the voltage is positive (forward bias), the current increases rapidly after a certain threshold voltage (**Vt**), which is typically 0.7 V for silicon diodes and 0.3 V for germanium diodes .
- The graph also shows that when the voltage is negative (reverse bias), the current is very small (almost zero) until a certain breakdown voltage (**Vbr**), which is the maximum reverse voltage that the diode can withstand without being damaged .
- A **clipper** is a circuit that uses one or more diodes to limit the voltage of an input signal to a certain range.
- A clipper can be used to protect a circuit from overvoltage, to remove unwanted parts of a signal, or to shape a signal into a desired form.
- There are different types of clippers, such as series clippers, parallel clippers, biased clippers, and combinational clippers.
- The following diagram shows an example of a series clipper that clips the positive part of the input signal above 0.7 V:

![series clipper](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Series_clipper.svg/1200px-Series_clipper.svg.png)

- The diode is connected in series with the load resistor (**Rl**). When the input voltage (**Vin**) is positive and less than 0.7 V, the diode is reverse biased and the output voltage (**Vout**) is equal to the input voltage.
- When the input voltage is positive and greater than 0.7 V, the diode is forward biased and the output voltage is limited to 0.7 V, which is the voltage drop across the diode.
- When the input voltage is negative, the diode is reverse biased and the output voltage is equal to the input voltage.
- The following diagram shows an example of a parallel clipper that clips the negative part of the input signal below -0.7 V:

![parallel clipper](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Parallel_clipper.svg/1200px-Parallel_clipper.svg.png)

- The diode is connected in parallel with the load resistor. When the input voltage is positive, the diode is reverse biased and the output voltage is equal to the input voltage.
- When the input voltage is negative and less than -0