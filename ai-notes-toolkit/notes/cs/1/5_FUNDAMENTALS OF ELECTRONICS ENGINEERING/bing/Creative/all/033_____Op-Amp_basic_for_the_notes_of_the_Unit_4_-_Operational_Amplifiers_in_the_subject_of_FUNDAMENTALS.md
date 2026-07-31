Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 4 - Operational Amplifiers in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING. Here is the content in markdown format:

# Op-Amp Basics

- An operational amplifier (op-amp) is a high-gain, direct-coupled, differential-input amplifier that can amplify AC or DC signals.
- An op-amp has two input terminals: the inverting input (-) and the non-inverting input (+), and one output terminal.
- An op-amp also has two power supply terminals: the positive supply (V+) and the negative supply (V-), which provide the voltage and current for the op-amp to operate.
- The basic symbol of an op-amp is shown below:

![op-amp symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Op-Amp.svg/1200px-Op-Amp.svg.png)

- The ideal characteristics of an op-amp are:
  - Infinite voltage gain (A)
  - Infinite input resistance (Ri)
  - Zero output resistance (Ro)
  - Zero input offset voltage (Vos)
  - Infinite bandwidth (B)
  - Zero noise
- The actual characteristics of an op-amp are:
  - Finite voltage gain (A)
  - High input resistance (Ri)
  - Low output resistance (Ro)
  - Small input offset voltage (Vos)
  - Finite bandwidth (B)
  - Some noise
- The voltage gain (A) of an op-amp is the ratio of the output voltage (Vo) to the differential input voltage (Vd), i.e., A = Vo/Vd.
- The differential input voltage (Vd) of an op-amp is the difference between the voltages at the two input terminals, i.e., Vd = V+ - V-.
- The input offset voltage (Vos) of an op-amp is the voltage that must be applied to the input terminals to make the output voltage zero, i.e., Vos = -Vo/A.
- The bandwidth (B) of an op-amp is the range of frequencies over which the op-amp can operate with a constant gain.
- The op-amp can be used in various configurations to perform different functions, such as amplification, buffering, filtering, summing, subtracting, integrating, differentiating, etc.
- The most common configuration of an op-amp is the negative feedback configuration, where a fraction of the output voltage is fed back to the inverting input terminal through a feedback resistor (Rf).
- The negative feedback configuration reduces the gain of the op-amp, but improves its stability, linearity, bandwidth, and input and output impedances.
- The closed-loop voltage gain (Af) of an op-amp in the negative feedback configuration is the ratio of the output voltage (Vo) to the input voltage (Vi), i.e., Af = Vo/Vi.
- The closed-loop voltage gain (Af) of an op-amp in the negative feedback configuration can be calculated using the formula: Af = A/(1 + AB), where A is the open-loop voltage gain and B is the feedback factor.
- The feedback factor (B) of an op-amp in the negative feedback configuration is the ratio of the feedback voltage (Vf) to the output voltage (Vo), i.e., B = Vf/Vo.
- The feedback factor (B) of an op-amp in the negative feedback configuration can be calculated using the formula: B = R1/(R1 + Rf), where R1 is the input resistor and Rf is the feedback resistor.
- The negative feedback configuration of an op-amp can be classified into two types: the inverting amplifier and the non-inverting amplifier.
- The inverting amplifier is a negative feedback configuration where the input voltage (Vi) is applied to the inverting input terminal (-) and the output voltage (Vo) is inverted with respect to the input voltage, i.e., Vo = -AfVi.
- The non-inverting amplifier is a negative feedback configuration where the input voltage (Vi) is applied to the non-inverting input terminal (+) and the output voltage (Vo) is in phase with the input voltage, i.e., Vo = AfVi.
- The circuit diagrams and the formulas for the closed-loop voltage gain (Af) of the inverting amplifier and the non-inverting amplifier are shown below:

![inverting amplifier](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp4.gif)

Af = -Rf/R1

![non-inverting amplifier](https://