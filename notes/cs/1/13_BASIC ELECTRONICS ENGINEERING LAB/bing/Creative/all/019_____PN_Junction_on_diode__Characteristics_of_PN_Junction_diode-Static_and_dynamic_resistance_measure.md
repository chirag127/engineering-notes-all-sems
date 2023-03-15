# PN Junction Diode: Characteristics of PN Junction Diode-Static and Dynamic Resistance Measurement from Graph

A PN junction diode is a semiconductor device that allows current to flow in one direction only. It is formed by joining a p-type semiconductor and an n-type semiconductor, creating a depletion region at the junction. The depletion region acts as a potential barrier that prevents the flow of electrons from the n-type to the p-type, and holes from the p-type to the n-type, unless an external voltage is applied.

## VI Characteristics of PN Junction Diode

The VI characteristics of a PN junction diode are the graphs that show the relationship between the voltage applied across the diode and the current flowing through it. There are two types of VI characteristics: forward bias and reverse bias.

### Forward Bias

When a positive voltage is applied to the p-type terminal and a negative voltage to the n-type terminal, the diode is said to be forward biased. In this condition, the external voltage reduces the potential barrier at the junction, allowing the electrons and holes to cross the depletion region and create a current. The forward current increases exponentially with the increase in the forward voltage, as shown in the graph below.

![Forward bias VI characteristics](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio3.gif)

### Reverse Bias

When a negative voltage is applied to the p-type terminal and a positive voltage to the n-type terminal, the diode is said to be reverse biased. In this condition, the external voltage increases the potential barrier at the junction, preventing the flow of charge carriers across the depletion region. The reverse current is very small and almost constant, as shown in the graph below. However, if the reverse voltage exceeds a certain value, called the breakdown voltage, the diode will conduct a large reverse current, which may damage the device.

![Reverse bias VI characteristics](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio4.gif)

## Static and Dynamic Resistance of PN Junction Diode

The resistance of a PN junction diode is the ratio of the voltage applied across it to the current flowing through it. However, the resistance of a diode is not constant, but varies with the applied voltage and the operating condition. Therefore, we can define two types of resistance: static and dynamic.

### Static Resistance

The static resistance of a diode is the resistance at a particular operating point on the VI characteristics curve. It is calculated by dividing the voltage at that point by the current at that point. For example, in the forward bias condition, the static resistance at point A on the graph below is given by:

![Static resistance in forward bias](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio5.gif)

R<sub>static</sub> = V<sub>A</sub> / I<sub>A</sub>

Similarly, in the reverse bias condition, the static resistance at point B on the graph below is given by:

![Static resistance in reverse bias](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio6.gif)

R<sub>static</sub> = V<sub>B</sub> / I<sub>B</sub>

The static resistance of a diode is not very useful, as it does not reflect the actual behavior of the device over a range of voltages and currents.

### Dynamic Resistance

The dynamic resistance of a diode is the resistance at a small change in the voltage and current around a particular operating point. It is calculated by dividing the change in voltage by the change in current. For example, in the forward bias condition, the dynamic resistance at point A on the graph below is given by:

![Dynamic resistance in forward bias](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio7.gif)

R<sub>dynamic</sub> = ΔV / ΔI

Similarly, in the reverse bias condition, the dynamic resistance at point B on the graph below is given by:

![Dynamic resistance in reverse bias](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/diode-dio8.gif)

R<sub>dynamic</sub> = ΔV / ΔI

The dynamic resistance of a diode is more useful, as it reflects the actual behavior of the device over a small range of voltages and currents. The dynamic resistance of a diode is inversely proportional to the slope of the VI characteristics curve at a given