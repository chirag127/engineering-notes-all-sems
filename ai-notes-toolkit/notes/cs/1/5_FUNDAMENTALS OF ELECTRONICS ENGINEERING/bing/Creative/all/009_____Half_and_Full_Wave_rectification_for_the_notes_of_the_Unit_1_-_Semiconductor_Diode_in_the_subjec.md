# Half and Full Wave Rectification

## Introduction

Rectification is the process of converting an alternating current (AC) into a direct current (DC) by using one or more diodes. A diode is a semiconductor device that allows current to flow in one direction only. Rectification is important for many applications that require a steady and constant DC voltage, such as power supplies, battery chargers, LED lights, etc.

## Half Wave Rectification

- A half wave rectifier is a rectifier that uses only one diode to convert one half cycle of the AC input into a pulsating DC output.
- The other half cycle of the AC input is blocked by the diode and does not contribute to the output.
- The output voltage and current are proportional to the input voltage and current, but only for the positive half cycle.
- The output frequency is the same as the input frequency, but the output has a lot of ripple, which is the variation of the output voltage around the average value.
- The advantage of a half wave rectifier is its simplicity and low cost, but the disadvantage is its low efficiency and high ripple.

![Half wave rectifier circuit and output waveform](https://electronicsdesk.com/wp-content/uploads/2019/01/Half-Wave-Rectifier.png)

## Full Wave Rectification

- A full wave rectifier is a rectifier that uses two or four diodes to convert both half cycles of the AC input into a pulsating DC output.
- There are two types of full wave rectifiers: center-tapped and bridge.
- A center-tapped full wave rectifier uses a transformer with a center-tapped secondary winding and two diodes to rectify the AC input. The center tap provides a common ground for the two diodes, which conduct alternately during each half cycle of the input. The output voltage and current are twice that of a half wave rectifier, but the output frequency is also doubled.
- A bridge full wave rectifier uses four diodes arranged in a bridge configuration to rectify the AC input. No transformer is required, but the diodes must have a higher voltage rating than the input. The output voltage and current are the same as that of a center-tapped full wave rectifier, but the output frequency is also the same as the input frequency.

![Center-tapped and bridge full wave rectifier circuits and output waveforms](https://electronicsdesk.com/wp-content/uploads/2019/01/Full-Wave-Rectifier.png)

## Comparison

- The main difference between half wave and full wave rectifiers is their efficiency. Efficiency is the ratio of the output power to the input power. A half wave rectifier has a low efficiency of about 40.6%, while a full wave rectifier has a high efficiency of about 81.2%.
- Another difference is the ripple factor, which is the ratio of the root mean square (RMS) value of the ripple voltage to the DC value of the output voltage. A lower ripple factor means a smoother output voltage. A half wave rectifier has a high ripple factor of about 1.21, while a full wave rectifier has a low ripple factor of about 0.482.
- A third difference is the transformer utilization factor (TUF), which is the ratio of the output power to the AC rating of the transformer. A higher TUF means a better utilization of the transformer. A half wave rectifier has a low TUF of about 0.287, while a full wave rectifier has a high TUF of about 0.693.

## Summary

- Rectification is the process of converting AC into DC by using diodes.
- A half wave rectifier uses one diode to convert one half cycle of the AC input into a pulsating DC output. It has a low efficiency, high ripple, and low TUF.
- A full wave rectifier uses two or four diodes to convert both half cycles of the AC input into a pulsating DC output. It has a high efficiency, low ripple, and high TUF.
- A full wave rectifier is preferred over a half wave rectifier for most applications that require a steady and constant DC voltage.