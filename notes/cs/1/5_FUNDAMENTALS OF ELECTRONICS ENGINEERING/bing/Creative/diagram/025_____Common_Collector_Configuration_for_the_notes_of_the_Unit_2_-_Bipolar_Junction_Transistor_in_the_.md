### Common Collector Configuration

- In this configuration, the base terminal of the transistor serves as the input, the emitter terminal is the output and the collector terminal is common for both input and output.
- The collector terminal is grounded so the common collector configuration is also known as grounded collector configuration .
- Sometimes common collector configuration is also referred to as emitter follower, voltage follower, common collector amplifier, CC amplifier, or CC configuration .
- The common collector configuration is typically used as a voltage buffer, which means it has a high input impedance, a low output impedance and a non-inverting voltage gain of approximately one .
- The input circuit is connected between emitter and base and the output is taken from the collector and emitter.
- The basic NPN common collector circuit (neglecting biasing details) is shown in Figure 1.

![Figure 1: Basic NPN common collector circuit (neglecting biasing details)](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Common_collector.svg/1200px-Common_collector.svg.png)

- The load resistor in the common-collector amplifier circuit receives both the base and collector currents, being placed in series with the emitter.
- The voltage gain of the common collector amplifier is given by the formula:

![Voltage gain formula](https://latex.codecogs.com/png.latex?A_v%20%3D%20%5Cfrac%7BV_o%7D%7BV_i%7D%20%5Capprox%20%5Cfrac%7BR_E%7D%7BR_E%20&plus;%20r_e%7D)

- Where V_o is the output voltage, V_i is the input voltage, R_E is the emitter resistance and r_e is the emitter resistance of the transistor.
- The input impedance of the common collector amplifier is given by the formula:

![Input impedance formula](https://latex.codecogs.com/png.latex?Z_i%20%3D%20%5Cbeta%20%28R_E%20&plus;%20r_e%29)

- Where Z_i is the input impedance and beta is the current gain of the transistor.
- The output impedance of the common collector amplifier is given by the formula:

![Output impedance formula](https://latex.codecogs.com/png.latex?Z_o%20%3D%20%5Cfrac%7Br_e%7D%7B1%20&plus;%20%5Cbeta%7D)

- Where Z_o is the output impedance.