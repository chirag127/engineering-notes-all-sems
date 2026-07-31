### 3. Applications of PN Junction diode: Half & Full wave rectifierMeasurement of Vrms, Vdc, and ripple factor.

- A PN junction diode is a semiconductor device that allows current to flow in one direction only. It has two terminals, anode and cathode, and a junction between them. When the anode is connected to a positive voltage and the cathode to a negative voltage, the diode is said to be forward biased and conducts current. When the polarity is reversed, the diode is said to be reverse biased and blocks current.
- A rectifier is a circuit that converts alternating current (AC) to direct current (DC). Rectifiers are used in power supplies, radio receivers, and other applications that require a steady DC voltage.
- A half-wave rectifier is a rectifier that uses only one diode and passes only one half of the AC cycle to the output. The other half is blocked by the diode. The output of a half-wave rectifier is a pulsating DC voltage with a frequency equal to the input AC frequency.
- A full-wave rectifier is a rectifier that uses two diodes and passes both halves of the AC cycle to the output. The diodes are connected in such a way that they reverse the polarity of the negative half-cycle and make it positive. The output of a full-wave rectifier is a pulsating DC voltage with a frequency equal to twice the input AC frequency.
- The advantages of a full-wave rectifier over a half-wave rectifier are: it has a higher output voltage, a higher output power, a smoother output waveform, and a lower ripple factor.
- The ripple factor is a measure of the amount of AC component in the output of a rectifier. It is defined as the ratio of the root mean square (RMS) value of the AC component to the DC component of the output voltage. The lower the ripple factor, the better the quality of the rectified output.
- The RMS value of a voltage is the equivalent DC voltage that would produce the same amount of heat in a resistor as the AC voltage. The RMS value of a sinusoidal voltage is equal to its peak value divided by the square root of two.
- The DC value of a voltage is the average value of the voltage over one cycle. The DC value of a sinusoidal voltage is zero, since the positive and negative halves cancel out. The DC value of a rectified voltage is equal to its peak value multiplied by a factor that depends on the type of rectifier.
- For a half-wave rectifier, the DC value of the output voltage is given by:

  Vdc = Vp / pi

  where Vp is the peak value of the input AC voltage and pi is the mathematical constant 3.14.

- For a full-wave rectifier, the DC value of the output voltage is given by:

  Vdc = 2 Vp / pi

  where Vp is the peak value of the input AC voltage and pi is the mathematical constant 3.14.

- For a half-wave rectifier, the RMS value of the output voltage is given by:

  Vrms = Vp / 2

  where Vp is the peak value of the input AC voltage.

- For a full-wave rectifier, the RMS value of the output voltage is given by:

  Vrms = Vp / sqrt(2)

  where Vp is the peak value of the input AC voltage and sqrt(2) is the square root of two.

- For a half-wave rectifier, the ripple factor is given by:

  r = sqrt(2) - 1

  which is approximately equal to 0.414.

- For a full-wave rectifier, the ripple factor is given by:

  r = sqrt(2) / 2 - 1

  which is approximately equal to 0.207.

- The ripple factor can be reduced by using a capacitor or an inductor in parallel with the load resistor. The capacitor or the inductor acts as a filter that smooths out the pulsations in the output voltage.

- The following diagrams show the circuit and the waveform of a half-wave rectifier and a full-wave rectifier :

  Half-wave rectifier:

  ```
  +Vp       +Vp
   |         |
   |         |
   |

```
