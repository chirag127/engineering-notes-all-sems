# Half and Full Wave Rectification

## Introduction

Rectification is the process of converting an alternating current (AC) into a direct current (DC) by using one or more diodes. A diode is a semiconductor device that allows current to flow in one direction only. Rectification is an important application of diodes in electronics.

## Half Wave Rectification

- A half wave rectifier is a circuit that uses a single diode to convert only one half cycle of the AC input into a pulsating DC output.
- The diode is connected in series with the AC source and the load resistor. The diode conducts only when the input voltage is positive and blocks the negative voltage.
- The output voltage across the load resistor is therefore a series of positive pulses with a frequency equal to the input frequency.
- The main disadvantage of half wave rectification is that it wastes half of the input power and produces a low output voltage and current.
- The output also contains a large amount of AC ripple, which is the variation of the output voltage around the DC value. This ripple can cause noise and distortion in the output devices.
- The efficiency of half wave rectification is low, as it is the ratio of the output power to the input power. The efficiency is given by the formula:

  $$\eta = \frac{P_{dc}}{P_{ac}} = \frac{V_{dc}^2}{V_{rms}^2} = \frac{(\frac{V_m}{\pi})^2}{(\frac{V_m}{\sqrt{2}})^2} = \frac{2}{\pi^2} \approx 0.406$$

  where $V_m$ is the peak value of the input voltage, $V_{dc}$ is the average value of the output voltage, and $V_{rms}$ is the root mean square value of the input voltage.

- The output voltage and current can be increased by using a transformer to step up the input voltage before the rectifier. However, this also increases the cost and size of the circuit.

## Full Wave Rectification

- A full wave rectifier is a circuit that uses two or four diodes to convert both half cycles of the AC input into a pulsating DC output.
- There are two types of full wave rectifiers: center-tapped and bridge.
- A center-tapped full wave rectifier uses a transformer with a center-tapped secondary winding and two diodes. The diodes are connected to the opposite ends of the secondary winding and the load resistor is connected between the center tap and the common point of the diodes. The diodes conduct alternately, one for each half cycle of the input voltage, and produce a pulsating DC output across the load resistor.
- A bridge full wave rectifier uses four diodes arranged in a bridge configuration. The diodes are connected to the input voltage and the load resistor is connected across the diagonal of the bridge. The diodes conduct in pairs, two for each half cycle of the input voltage, and produce a pulsating DC output across the load resistor.
- The main advantage of full wave rectification is that it utilizes both halves of the input power and produces a higher output voltage and current.
- The output also contains less AC ripple, as the frequency of the output pulses is twice the input frequency. This ripple can be reduced further by using a filter capacitor in parallel with the load resistor.
- The efficiency of full wave rectification is higher, as it is the ratio of the output power to the input power. The efficiency is given by the formula:

  $$\eta = \frac{P_{dc}}{P_{ac}} = \frac{V_{dc}^2}{V_{rms}^2} = \frac{(\frac{2V_m}{\pi})^2}{(\frac{V_m}{\sqrt{2}})^2} = \frac{8}{\pi^2} \approx 0.812$$

  where $V_m$ is the peak value of the input voltage, $V_{dc}$ is the average value of the output voltage, and $V_{rms}$ is the root mean square value of the input voltage.

- The output voltage and current can be increased by using a transformer to step up the input voltage before the rectifier. However, this also increases the cost and size of the circuit.
- The bridge full wave rectifier has the