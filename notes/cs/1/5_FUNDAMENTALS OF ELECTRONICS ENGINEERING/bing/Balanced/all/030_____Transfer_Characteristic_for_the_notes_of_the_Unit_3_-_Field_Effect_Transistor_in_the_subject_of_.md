# Transfer Characteristic of Field Effect Transistor

- A field effect transistor (FET) is a type of transistor that uses an electric field to control the flow of current in the channel between the source and the drain terminals.
- The gate terminal is the input of the FET and it is insulated from the channel by a thin layer of oxide or semiconductor material.
- The transfer characteristic of a FET is the curve that shows the relationship between the gate voltage (V<sub>GS</sub>) and the drain current (I<sub>D</sub>) for a given value of drain-source voltage (V<sub>DS</sub>).
- The transfer characteristic can be obtained by measuring the drain current for different values of gate voltage while keeping the drain-source voltage constant.
- The shape and slope of the transfer characteristic depend on the type and mode of operation of the FET.
- There are two main types of FETs: junction field effect transistors (JFETs) and metal oxide semiconductor field effect transistors (MOSFETs).
- JFETs have a channel that is doped with either n-type or p-type impurities and a gate that is formed by a reverse-biased pn junction.
- MOSFETs have a channel that is either n-type or p-type and a gate that is separated from the channel by a thin layer of metal oxide.
- JFETs can operate in either depletion mode or enhancement mode, depending on the polarity of the gate voltage.
- MOSFETs can operate in either enhancement mode or depletion mode, depending on the polarity and magnitude of the gate voltage.
- In depletion mode, the channel is normally conductive and the gate voltage reduces the channel width and the drain current.
- In enhancement mode, the channel is normally non-conductive and the gate voltage increases the channel width and the drain current.
- The transfer characteristic of a JFET in depletion mode is shown in the figure below. It is a nonlinear curve that starts from a maximum value of drain current (I<sub>DSS</sub>) when the gate voltage is zero and decreases as the gate voltage becomes more negative. The curve reaches zero when the gate voltage is equal to the pinch-off voltage (V<sub>P</sub>), which is the minimum voltage required to completely deplete the channel.

![Transfer characteristic of a JFET in depletion mode](https://www.electrical4u.com/wp-content/uploads/2018/11/Transfer-Characteristic-of-JFET.png)

- The transfer characteristic of a MOSFET in enhancement mode is shown in the figure below. It is a nonlinear curve that starts from zero when the gate voltage is below the threshold voltage (V<sub>T</sub>), which is the minimum voltage required to create a conductive channel. The curve increases as the gate voltage becomes more positive and reaches a saturation region when the drain-source voltage is equal to the gate-source voltage minus the threshold voltage (V<sub>DS</sub> = V<sub>GS</sub> - V<sub>T</sub>).

![Transfer characteristic of a MOSFET in enhancement mode](https://www.electrical4u.com/wp-content/uploads/2018/11/Transfer-Characteristic-of-MOSFET.png)

- The slope of the transfer characteristic is called the transconductance (g<sub>m</sub>) and it is a measure of the gain or amplification of the FET. The transconductance is defined as the ratio of the change in drain current to the change in gate voltage for a small variation around a given operating point.

g<sub>m</sub> = dI<sub>D</sub>/dV<sub>GS</sub>

- The transconductance is usually higher for MOSFETs than for JFETs and it depends on the channel length, width, doping, and temperature.