### Half and Full Wave Rectification

- Rectification is the process of converting an alternating current (AC) into a direct current (DC) by using one or more diodes.
- A diode is a semiconductor device that allows current to flow in one direction only. It has two terminals: anode and cathode.
- When the anode is positive with respect to the cathode, the diode is forward biased and conducts current. When the anode is negative with respect to the cathode, the diode is reverse biased and blocks current.
- There are two types of rectification: half wave and full wave.

#### Half Wave Rectification

- A half wave rectifier uses a single diode to convert only one half cycle of the AC input into a pulsating DC output.
- The positive half cycle of the AC input passes through the diode and appears as the output. The negative half cycle of the AC input is blocked by the diode and does not appear as the output.
- The output frequency of a half wave rectifier is equal to the input frequency.
- The output voltage of a half wave rectifier is half of the peak input voltage.
- The output current of a half wave rectifier is proportional to the input voltage.
- The output power of a half wave rectifier is low and the ripple factor is high.
- The efficiency of a half wave rectifier is 40.6%.
- The circuit diagram of a half wave rectifier is shown below:

```
    AC Input
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |
    |  |  |  +-----+
    |  |  |  |     |
    |  |  |  |     | Load
    |  |  |  |     |
    |  |  |  +-----+
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |
    |  |  |    |  |
    |  |  |    |  | Diode
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  |    |  |
    |  |  +----+  |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    |  |         |
    +--+---------+
    AC Input
```

#### Full Wave Rectification

- A full wave rectifier uses two or four diodes to convert both half cycles of the AC input into a pulsating DC output.
- The positive half cycle of the AC input passes through one pair of diodes and appears as the output. The negative half cycle of the AC input passes through another pair of diodes and is inverted to appear as the output.
- The output frequency of a full wave rectifier is twice the input frequency.
- The output voltage of a full wave rectifier is equal to the peak input voltage.
- The output current of a full wave rectifier is proportional to the input voltage.
- The output power of a full wave rectifier is high and the ripple factor is low.
- The efficiency of a full wave rectifier is 81.2%.
- There are two types of full wave rectifier: center-tapped and bridge.
- The circuit diagram of a center-tapped