### Differential and Common-Mode Operation

Operational amplifiers (op-amps) are widely used in various electronic circuits due to their high gain, high input impedance, and low output impedance. However, to use op-amps effectively, it is important to understand their differential and common-mode operation.

#### Differential Amplifiers

A differential amplifier is an electronic circuit that amplifies the difference between two input signals while rejecting any common-mode signal present in the input. The differential amplifier can be implemented using an op-amp and two input resistors.

##### Differential Amplifier Circuit

The differential amplifier circuit consists of two inputs, labeled as `+` and `-`, and two output terminals. The input signals are applied to the `+` and `-` inputs, and the output voltage is taken between the two output terminals. The circuit diagram of the differential amplifier is shown below:

![Differential Amplifier Circuit](https://i.imgur.com/7VwQx4y.png)

##### Differential Amplifier Gain

The differential gain of the amplifier is defined as the ratio of the change in output voltage to the change in the difference between the input voltages. Mathematically, the differential gain can be expressed as:

```
Ad = ΔVout / ΔVin
```

##### Common-Mode Rejection Ratio (CMRR)

The common-mode rejection ratio (CMRR) is defined as the ratio of the differential gain to the common-mode gain. In other words, it represents the ability of the differential amplifier to reject any common-mode signal present in the input. Mathematically, the CMRR can be expressed as:

```
CMRR = Ad / Acm
```

#### Common-Mode Operation

In a common-mode operation, both the input signals are at the same voltage level with respect to ground. In other words, the difference between the input signals is zero. When a common-mode signal is present in the input, it can cause various issues such as distortion, noise, and signal interference.

##### Common-Mode Rejection

Common-mode rejection refers to the ability of an amplifier to reject any common-mode signal present in the input. The common-mode rejection ratio (CMRR) is a measure of the amplifier's ability to reject the common-mode signal. The higher the CMRR, the better the amplifier is at rejecting the common-mode signal.

##### Common-Mode Gain

Common-mode gain refers to the gain of the amplifier for a common-mode signal. Ideally, the common-mode gain of the amplifier should be zero, indicating that the amplifier does not amplify the common-mode signal.

#### Conclusion

In conclusion, differential and common-mode operation are important concepts in the operation of operational amplifiers. The differential amplifier is used to amplify the difference between two input signals while rejecting any common-mode signal present in the input. The common-mode operation, on the other hand, refers to the operation of the amplifier when both the input signals are at the same voltage level. Understanding these concepts is important for designing electronic circuits that use operational amplifiers effectively.