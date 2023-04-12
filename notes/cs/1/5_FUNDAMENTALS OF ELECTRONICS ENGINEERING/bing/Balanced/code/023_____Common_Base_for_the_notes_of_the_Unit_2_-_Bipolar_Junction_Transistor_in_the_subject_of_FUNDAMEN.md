# Common Base Configuration of BJT

- The common base configuration is one of the three basic ways to connect a bipolar junction transistor (BJT) as an amplifier.
- In this configuration, the base terminal of the transistor is a common terminal to both the input and output signals, hence its name common base (CB).
- The input signal is applied between the emitter and the base, and the output signal is taken from the collector and the base.
- The common base configuration is less common as an amplifier than compared to the more popular common emitter (CE) or common collector (CC) configurations, but it is still used due to its unique input/output characteristics.
- Some of the advantages of the common base configuration are:
  - It has a high voltage gain, which is the ratio of output voltage to input voltage.
  - It has a high input impedance, which means it does not load the input source too much.
  - It has a low output impedance, which means it can drive a low resistance load easily.
  - It has a high frequency response, which means it can amplify high frequency signals without much attenuation.
- Some of the disadvantages of the common base configuration are:
  - It has a low current gain, which is the ratio of output current to input current.
  - It has a low power gain, which is the product of voltage gain and current gain.
  - It has a low input-output isolation, which means the output signal can affect the input signal and cause feedback or instability.
- The common base configuration can be analyzed using the following formulas and equations :
  - The current gain, alpha, is given by: alpha = IC / IE, where IC is the collector current and IE is the emitter current.
  - The voltage gain, AV, is given by: AV = alpha * RL / RE, where RL is the load resistance and RE is the emitter resistance.
  - The input impedance, Zin, is given by: Zin = 1 / (alpha * gm), where gm is the transconductance of the transistor, which is given by: gm = IC / VT, where VT is the thermal voltage, which is about 26 mV at room temperature.
  - The output impedance, Zout, is given by: Zout = r0 / (1 + alpha), where r0 is the output resistance of the transistor, which is given by: r0 = VA / IC, where VA is the Early voltage, which is a parameter that depends on the transistor type and fabrication.
- The common base configuration can be implemented using different biasing schemes, such as two-supply emitter bias, self-bias, or voltage divider bias. The biasing scheme determines the operating point of the transistor, which affects its performance and stability.
- An example of a common base amplifier using two-supply emitter bias is shown in the figure below :

```
+VCC
  |
  |
  R1
  |
  |
  C1
  |
  |
  Emitter
  |   |
  |   |  BJT
  |   |  NPN
  |   |
  |   Base
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   Collector
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   C2
  |   |
  |   |
  |   RL
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |   |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |
  |

```
