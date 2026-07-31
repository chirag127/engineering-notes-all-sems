Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

##### 4. Measurement of power in 3- phase circuit by two wattmeter method and determination of its power factor for star as well as delta connected load.

- The two wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The two wattmeters are connected across two of the three phase voltages, and their currents are taken from the third phase.
- The total power is given by the sum of the readings of the two wattmeters, and the power factor is given by the ratio of the difference and the sum of the readings.
- The two wattmeter method can be applied to both star and delta connected loads, with some modifications in the connections and calculations.
- For a star connected load, the wattmeters are connected across the line voltages, and their currents are taken from the line currents. The power factor angle is equal to the phase angle between the voltage and the current of the load.
- For a delta connected load, the wattmeters are connected across the phase voltages, and their currents are taken from the line currents. The power factor angle is equal to the phase angle between the line voltage and the line current minus 30 degrees.
- The two wattmeter method can be represented by a phasor diagram, as shown below.

![Two wattmeter method phasor diagram](https://i.imgur.com/4w4LZ9a.png)

- In the diagram, V<sub>AB</sub>, V<sub>BC</sub>, and V<sub>CA</sub> are the line voltages, I<sub>A</sub>, I<sub>B</sub>, and I<sub>C</sub> are the line currents, W<sub>1</sub> and W<sub>2</sub> are the wattmeter readings, P is the total power, and θ is the power factor angle.
- The wattmeter readings are given by:

W<sub>1</sub> = V<sub>AB</sub> I<sub>C</sub> cos(θ + 30°)

W<sub>2</sub> = V<sub>BC</sub> I<sub>A</sub> cos(θ - 30°)

- The total power and the power factor are given by:

P = W<sub>1</sub> + W<sub>2</sub> = V<sub>AB</sub> I<sub>C</sub> cos(θ + 30°) + V<sub>BC</sub> I<sub>A</sub> cos(θ - 30°)

cos θ = (W<sub>1</sub> - W<sub>2</sub>) / (W<sub>1</sub> + W<sub>2</sub>) = (V<sub>AB</sub> I<sub>C</sub> cos(θ + 30°) - V<sub>BC</sub> I<sub>A</sub> cos(θ - 30°)) / (V<sub>AB</sub> I<sub>C</sub> cos(θ + 30°) + V<sub>BC</sub> I<sub>A</sub> cos(θ - 30°))

- If the load is balanced, then V<sub>AB</sub> = V<sub>BC</sub> = V<sub>CA</sub> = V<sub>L</sub> and I<sub>A</sub> = I<sub>B</sub> = I<sub>C</sub> = I<sub>L</sub>, and the equations simplify to:

W<sub>1</sub> = V<sub>L</sub> I<sub>L</sub> cos(θ + 30°)

W<sub>2</sub> = V<sub>L</sub> I<sub>L</sub> cos(θ - 30°)

P = 3 V<sub>L</sub> I<sub>L</sub> cos θ

cos θ = (W<sub>1</sub> - W<sub>2</sub>) / (W<sub>1</sub> + W<sub>2</sub>) = cos(θ + 30°) - cos(θ - 30°) / cos(θ + 30°) + cos(θ - 30°)

- If the load is star connected, then V<sub>L</