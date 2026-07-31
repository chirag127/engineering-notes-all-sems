### Differential and Common-Mode Operation for the notes of the Unit 4 - Operational Amplifiers in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

Operational amplifiers (op-amps) are essential components in electronic circuits. They are used in signal processing, filtering, amplification, and many other applications. Understanding the differential and common-mode operation of op-amps is crucial for designing and analyzing electronic circuits.

Here are some key points to understand about the differential and common-mode operation of op-amps:

#### Differential Operation

- An op-amp has two input terminals: the inverting (-) and non-inverting (+) terminals.
- The voltage difference between these two terminals is called the differential input voltage (VID).
- The output voltage of the op-amp is proportional to the differential input voltage, and the proportionality factor is called the open-loop gain (A).
- Ideally, the open-loop gain of an op-amp is very high (infinite), which means that even a small differential input voltage can produce a large output voltage.
- The differential gain of an op-amp can be expressed as Ad = A*(RF/R1), where RF and R1 are the feedback and input resistors, respectively.
- In differential operation, the op-amp amplifies the difference between the two input voltages and rejects any common-mode voltage (i.e., voltage that is present at both inputs).

#### Common-Mode Operation

- Common-mode operation refers to the voltage that is present at both input terminals of an op-amp.
- Ideally, an op-amp should have no output voltage when there is no differential input voltage and only a common-mode voltage.
- However, due to imperfections in the op-amp's design, it may produce a small output voltage even in common-mode operation.
- The common-mode rejection ratio (CMRR) is a measure of an op-amp's ability to reject common-mode voltage. It is defined as the ratio of the differential gain to the common-mode gain.
- A high CMRR indicates a good rejection of common-mode voltage, while a low CMRR indicates poor rejection.

In conclusion, understanding the differential and common-mode operation of op-amps is crucial for designing and analyzing electronic circuits. The differential input voltage is amplified in differential operation, while the common-mode voltage is rejected. The common-mode rejection ratio indicates an op-amp's ability to reject common-mode voltage.