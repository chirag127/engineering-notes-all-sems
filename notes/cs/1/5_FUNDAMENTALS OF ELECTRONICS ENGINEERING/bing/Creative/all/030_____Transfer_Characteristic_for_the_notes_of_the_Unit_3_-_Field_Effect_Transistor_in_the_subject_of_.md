# Transfer Characteristic of Field Effect Transistor

- A field effect transistor (FET) is a type of transistor that uses an electric field to control the flow of current in the channel between the source and the drain terminals.
- The gate terminal is used to apply the electric field to the channel, and it is insulated from the channel by a thin layer of oxide or junction.
- The transfer characteristic of a FET is a curve that shows the relationship between the gate voltage (V<sub>GS</sub>) and the drain current (I<sub>D</sub>) for a given drain-source voltage (V<sub>DS</sub>).
- The transfer characteristic can be obtained experimentally by keeping V<sub>DS</sub> constant and measuring I<sub>D</sub> for different values of V<sub>GS</sub>.
- The shape of the transfer characteristic depends on the type and mode of operation of the FET. There are two main types of FETs: junction field effect transistors (JFETs) and metal oxide semiconductor field effect transistors (MOSFETs).
- JFETs have a channel that is doped with either n-type or p-type impurities, and a gate that is formed by a reverse-biased pn junction. JFETs can operate in either depletion mode or enhancement mode, depending on the polarity of V<sub>GS</sub>.
- MOSFETs have a channel that is either lightly doped or undoped, and a gate that is separated from the channel by a thin layer of oxide. MOSFETs can also operate in either depletion mode or enhancement mode, depending on the polarity and magnitude of V<sub>GS</sub>.
- The transfer characteristic of a JFET in depletion mode is shown in the figure below. It can be seen that I<sub>D</sub> decreases as V<sub>GS</sub> becomes more negative (for n-channel JFET) or more positive (for p-channel JFET). This is because the reverse-biased gate junction reduces the width of the channel and increases its resistance. When V<sub>GS</sub> reaches a certain value, called the pinch-off voltage (V<sub>P</sub>), the channel is completely closed and I<sub>D</sub> becomes zero. The maximum value of I<sub>D</sub> that can flow through the JFET when V<sub>GS</sub> is zero is called the shorted gate drain current (I<sub>DSS</sub>).

![Transfer characteristic of a JFET in depletion mode](https://www.electrical4u.com/wp-content/uploads/2018/11/transfer-characteristic-of-jfet.png)

- The transfer characteristic of a MOSFET in enhancement mode is shown in the figure below. It can be seen that I<sub>D</sub> increases as V<sub>GS</sub> becomes more positive (for n-channel MOSFET) or more negative (for p-channel MOSFET). This is because the applied gate voltage induces a channel of opposite polarity to the substrate under the oxide layer. When V<sub>GS</sub> reaches a certain value, called the threshold voltage (V<sub>T</sub>), the channel is formed and I<sub>D</sub> starts to flow. The slope of the transfer characteristic is called the transconductance (g<sub>m</sub>), and it measures the gain or amplification of the MOSFET.

![Transfer characteristic of a MOSFET in enhancement mode](https://chem.libretexts.org/@api/deki/files/230211/10.2.1.png)

- The transfer characteristic of a FET is useful for analyzing and designing circuits that use FETs as amplifiers, switches, or sensors. By knowing the transfer characteristic, one can determine the operating point, the input and output impedances, the voltage gain, and the frequency response of the FET circuit.