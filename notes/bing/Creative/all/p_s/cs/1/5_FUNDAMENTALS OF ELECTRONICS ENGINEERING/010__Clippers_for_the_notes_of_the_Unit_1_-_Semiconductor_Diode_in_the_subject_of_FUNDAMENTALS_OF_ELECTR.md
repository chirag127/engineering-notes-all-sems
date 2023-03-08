### Clippers

- Clippers are electronic circuits that clip off or remove a portion of an input signal, without causing any distortion to the remaining part of the waveform   .
- Clippers are also known as clippers, clipping circuits, limiters, slicers, etc .
- Clippers are used to limit distortion and noise in digital signals by clipping off any sudden waveform peaks above or below a certain threshold level.
- Clippers are also used to protect circuits from overvoltage, to shape waveforms, to modulate signals, etc .
- Clippers consist of linear and non-linear elements, such as resistors, diodes, transistors, etc, but do not contain energy storing elements, such as capacitors or inductors.
- Clippers can be classified into different types based on the position, polarity, and number of diodes used in the circuit   .
- Some common types of clippers are:

  - Series clipper: A clipper in which the diode is connected in series with the load resistor   .
  - Shunt clipper: A clipper in which the diode is connected in parallel with the load resistor   .
  - Positive clipper: A clipper that clips off the positive half of the input signal   .
  - Negative clipper: A clipper that clips off the negative half of the input signal   .
  - Biased clipper: A clipper that uses a DC voltage source to shift the clipping level from zero to some desired value   .
  - Combinational clipper: A clipper that combines two or more clippers to clip off both the positive and negative halves of the input signal at different levels   .

- The basic operation of a diode clipping circuit is such that, in forward biased condition, the diode allows current to pass through it, clamping the voltage across it to a small value (usually 0.7 V for silicon diodes). In reverse biased condition, the diode blocks current, leaving the voltage across it unchanged .
- The output waveform of a clipper depends on the input waveform, the clipping level, the type and polarity of the diode, and the position of the diode in the circuit   .
- The following are some examples of clipper circuits and their output waveforms:

  - Series positive clipper:

    ```
    +Vcc
     |
     |
    ---  R1
    | |
    | |   R2
    | |   |
    | |   |   +Vi
    | |   |   |
    | |   |  ---  RL
    | |   |  | |
    | |   |  | |   +Vo
    | |   |  | |   |
    | |   |  | |  ---  GND
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  | |  | |
    | |   |  |

Some possible mnemonics and learning tricks for the topic are:

- To remember the types of clippers, use the acronym SPNSBC: Series, Parallel, Negative, Positive, Biased, Combinational.
- To remember the polarity of the diode in a clipper, use the rule of thumb: The diode points to the clipped half.
- To remember the output waveform of a clipper, use the analogy of a scissors: The diode acts like a scissors that cuts off the input waveform at the clipping level.
- To remember the clipping level of a biased clipper, use the formula: Vc = Vb + Vd, where Vc is the clipping level, Vb is the bias voltage, and Vd is the diode voltage drop.