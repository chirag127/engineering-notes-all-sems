# Common Collector Configuration

- Common collector configuration is one of the three basic single-stage bipolar junction transistor (BJT) amplifier topologies, along with common emitter and common base configurations.
- In common collector configuration, the base terminal of the transistor serves as the input, the emitter terminal is the output and the collector terminal is common for both input and output. Hence, it is named as common collector configuration .
- The collector terminal is grounded so the common collector configuration is also known as grounded collector configuration. Sometimes common collector configuration is also referred to as emitter follower, voltage follower, common collector amplifier, CC amplifier, or CC configuration .
- The common collector amplifier is often used as a voltage buffer, because it has a high input impedance, a low output impedance and a non-inverting voltage gain of approximately one .
- The input circuit is connected between emitter and base and the output is taken from the collector and emitter. The input signal is applied to the base-emitter junction and the output signal is taken from the emitter-collector junction.
- The common collector amplifier has the following characteristics :
  - Voltage gain: The voltage gain is the ratio of the output voltage to the input voltage. The voltage gain of the common collector amplifier is slightly less than one, because the output voltage is the input voltage minus the base-emitter voltage drop. The voltage gain is given by:

  ```
  A_v = \frac{V_o}{V_i} = \frac{V_e}{V_b} = \frac{R_e}{R_e + r_e} \approx 1
  ```

  where `V_o` is the output voltage, `V_i` is the input voltage, `V_e` is the emitter voltage, `V_b` is the base voltage, `R_e` is the external emitter resistance, and `r_e` is the internal emitter resistance.

  - Current gain: The current gain is the ratio of the output current to the input current. The current gain of the common collector amplifier is equal to the current gain of the transistor, which is typically very high. The current gain is given by:

  ```
  A_i = \frac{I_o}{I_i} = \frac{I_e}{I_b} = \beta
  ```

  where `I_o` is the output current, `I_i` is the input current, `I_e` is the emitter current, `I_b` is the base current, and `β` is the current gain of the transistor.

  - Power gain: The power gain is the ratio of the output power to the input power. The power gain of the common collector amplifier is the product of the voltage gain and the current gain. The power gain is given by:

  ```
  A_p = \frac{P_o}{P_i} = A_v \times A_i = \beta \times \frac{R_e}{R_e + r_e} \approx \beta
  ```

  where `P_o` is the output power and `P_i` is the input power.

  - Input impedance: The input impedance is the ratio of the input voltage to the input current. The input impedance of the common collector amplifier is very high, because the input current is very small compared to the output current. The input impedance is given by:

  ```
  Z_i = \frac{V_i}{I_i} = \frac{V_b}{I_b} = (\beta + 1) \times r_e
  ```

  where `Z_i` is the input impedance.

  - Output impedance: The output impedance is the ratio of the output voltage to the output current. The output impedance of the common collector amplifier is very low, because the output voltage is very close to the input voltage. The output impedance is given by:

  ```
  Z_o = \frac{V_o}{I_o} = \frac{V_e}{I_e} = \frac{R_e}{\beta + 1}
  ```

  where `Z_o` is the output impedance.

- The common collector amplifier has the following advantages :
  - It provides a high input impedance and a low output impedance, which makes it suitable for impedance matching and voltage buffering applications.
  - It has a non-inverting voltage gain of approximately one, which means it does not alter the phase or amplitude of the input signal.