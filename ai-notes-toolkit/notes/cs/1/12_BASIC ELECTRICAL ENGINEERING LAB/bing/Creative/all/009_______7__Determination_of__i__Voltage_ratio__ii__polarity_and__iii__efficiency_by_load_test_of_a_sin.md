Hello, I am Sydney, your AI assistant. I can help you with your topic.

# 7. Determination of (i) Voltage ratio (ii) polarity and (iii) efficiency by load test of a single phase Transformer

A single phase transformer is a device that transfers electrical energy from one circuit to another through electromagnetic induction. The transformer consists of two windings, called the primary and the secondary, that are linked by a magnetic core. The primary winding is connected to the input voltage source, while the secondary winding is connected to the output load.

The voltage ratio, polarity and efficiency of a single phase transformer can be determined by performing a load test, which involves applying a known voltage to the primary winding and measuring the corresponding voltage, current and power in the secondary winding. The load test can be done using the following steps:

- Connect the primary winding of the transformer to a variable voltage source, such as an autotransformer, and the secondary winding to a resistive load, such as a rheostat. Also connect an ammeter, a voltmeter and a wattmeter to the secondary circuit, as shown in the figure below.

![Load test circuit diagram](https://i.imgur.com/2Q0QfZa.png)

- Adjust the input voltage to the rated value of the primary winding, and note down the readings of the voltmeter, ammeter and wattmeter in the secondary circuit. This is the no-load condition, where the secondary current is very small and the power factor is close to zero.
- Increase the load resistance gradually, and note down the corresponding readings of the voltmeter, ammeter and wattmeter in the secondary circuit. This is the loaded condition, where the secondary current and power factor increase as the load resistance decreases.
- Repeat the above step for different values of load resistance, until the rated current of the secondary winding is reached. Plot a graph of secondary voltage versus secondary current, and secondary power versus secondary current, using the recorded data.

The voltage ratio, polarity and efficiency of the transformer can be calculated from the load test data as follows:

- The voltage ratio is the ratio of the secondary voltage to the primary voltage, which can be obtained from the no-load condition. It is given by:

`Voltage ratio = V2 / V1`

where V2 is the secondary voltage and V1 is the primary voltage.

- The polarity is the relative direction of the induced voltages in the primary and secondary windings, which can be determined by the dot convention. The dot convention states that if the current enters the dotted terminal of one winding, the induced voltage in the other winding will have the same polarity at the dotted terminal. The polarity can be verified by connecting a low resistance across the secondary terminals, and observing the deflection of the ammeter in the primary circuit. If the ammeter deflects in the same direction as the no-load condition, the polarity is additive, otherwise it is subtractive. The polarity can be indicated by placing a plus sign (+) or a minus sign (-) near the dotted terminals of the windings, as shown in the figure below.

![Polarity diagram](https://i.imgur.com/0wZxkZ8.png)

- The efficiency is the ratio of the output power to the input power, which can be obtained from the loaded condition. It is given by:

`Efficiency = P2 / P1`

where P2 is the secondary power and P1 is the primary power.

The primary power can be calculated from the secondary power and the losses in the transformer, which are mainly due to the copper loss and the iron loss. The copper loss is the power dissipated in the resistance of the windings, which is proportional to the square of the current. The iron loss is the power dissipated in the core due to hysteresis and eddy currents, which is constant for a given input voltage and frequency. The losses can be estimated from the load test data as follows:

- The copper loss is the difference between the input power and the output power at full load, which is the maximum current of the secondary winding. It is given by:

`Copper loss = P1 - P2 (at full load)`

- The iron loss is the input power at no load, which is the minimum current of the secondary winding. It is given by:

`Iron loss = P1 (at no load)`

The primary power can then be calculated by adding the output power and the losses, as follows:

`P1 = P2 + Copper loss + Iron loss`

The efficiency can then be calculated by dividing the output power by the input power, as follows:

`Efficiency = P2 / (P2 + Copper loss + Iron loss)`

The efficiency can also be plotted as