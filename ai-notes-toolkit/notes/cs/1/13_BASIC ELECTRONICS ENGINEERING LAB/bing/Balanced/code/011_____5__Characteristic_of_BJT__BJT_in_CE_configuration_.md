### 5. Characteristic of BJT: BJT in CE configuration

- BJT stands for bipolar junction transistor, which is a type of semiconductor device that can amplify or switch electrical signals.
- A BJT has three terminals: the base (B), the collector (C), and the emitter (E).
- The BJT can be classified into two types: NPN and PNP, depending on the arrangement of the N-type and P-type semiconductor materials in the device.
- In the CE configuration, the base terminal is the input, the collector terminal is the output, and the emitter terminal is the common terminal for both input and output circuits.
- The CE configuration is the most widely used configuration for BJT amplifiers, because it has high voltage gain, high current gain, high power gain, and high input impedance.
- The CE configuration can be analyzed using two characteristic curves: the input characteristic and the output characteristic.
- The input characteristic shows the relation between the base current (IB) and the base-emitter voltage (VBE) for a given collector-emitter voltage (VCE).
- The output characteristic shows the relation between the collector current (IC) and the collector-emitter voltage (VCE) for a given base current (IB).
- The input characteristic is nonlinear and exponential, because the base-emitter junction behaves like a forward-biased diode.
- The output characteristic is linear and has three regions: the cutoff region, the active region, and the saturation region.
- In the cutoff region, the base current is zero or very small, and the collector current is also zero or very small. The BJT is in the off state and acts like an open switch.
- In the active region, the base current is positive and the collector current is proportional to the base current. The BJT is in the on state and acts like a current-controlled current source.
- In the saturation region, the base current is large and the collector current reaches a maximum value. The BJT is in the on state and acts like a closed switch.
- The operating point or quiescent point (Q-point) of the BJT is the point on the output characteristic that corresponds to the DC bias conditions of the device.
- The Q-point determines the linear range of operation of the BJT and should be chosen in the middle of the active region for maximum signal swing and minimum distortion.
- The AC analysis of the BJT amplifier involves superimposing a small AC signal on the DC bias and finding the AC output voltage and current.
- The AC analysis can be simplified by using the hybrid-pi model, which is an equivalent circuit that represents the BJT using a controlled current source and resistors.
- The hybrid-pi model parameters are: the transconductance (gm), which is the ratio of the change in collector current to the change in base-emitter voltage; the output resistance (ro), which is the inverse of the slope of the output characteristic in the active region; and the input resistance (ri), which is the ratio of the change in base-emitter voltage to the change in base current.
- The voltage gain (Av) of the CE amplifier is the ratio of the AC output voltage to the AC input voltage. It can be found by applying the voltage divider rule and the Ohm's law to the hybrid-pi model.
- The voltage gain (Av) of the CE amplifier is given by:

```math
Av = -gm * RC / (1 + gm * re)
```

where RC is the collector resistance and re is the emitter resistance.
- The negative sign indicates that the output voltage is 180 degrees out of phase with the input voltage, which means that the CE amplifier is an inverting amplifier.
- The current gain (Ai) of the CE amplifier is the ratio of the AC output current to the AC input current. It can be found by applying the current divider rule and the Ohm's law to the hybrid-pi model.
- The current gain (Ai) of the CE amplifier is given by:

```math
Ai = -gm * RC / re
```

where RC and re are the same as before.
- The negative sign indicates that the output current is 180 degrees out of phase with the input current, which means that the CE amplifier is an inverting amplifier.
- The power gain (Ap) of the CE amplifier is the ratio of the AC output power to the AC input power. It can be found by multiplying the voltage gain and the current gain.
- The power gain (Ap) of the CE amplifier is given by:

```math
Ap = Av * Ai = gm^2 * RC^2
```

where RC and gm are the same as before.
- The power gain (Ap) of the CE amplifier