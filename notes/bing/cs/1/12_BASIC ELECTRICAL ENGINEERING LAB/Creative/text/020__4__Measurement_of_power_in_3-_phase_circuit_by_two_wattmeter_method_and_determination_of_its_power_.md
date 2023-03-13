##### 4. Measurement of power in 3- phase circuit by two wattmeter method and determination of its power factor for star as well as delta connected load.

- The two wattmeter method is a technique for measuring the total power in a three-phase circuit using two wattmeters.
- The two wattmeters are connected to the three-phase circuit as shown below:

```
    A   B   C
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    W1  W2  |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    N   N   N
```

- W1 is connected between phase A and neutral, and W2 is connected between phase B and neutral. Phase C is left open.
- The current coils of both wattmeters are connected in series with the respective phases, and the potential coils are connected across the line voltage.
- The readings of the two wattmeters are added to obtain the total power in the circuit.
- The power factor of the circuit can be determined by using the following formula:

```
power factor = (W1 + W2) / (sqrt(3) * VL * IL)
```

- Where W1 and W2 are the readings of the wattmeters, VL is the line voltage, and IL is the line current.
- The two wattmeter method can be applied to both star and delta connected loads, with some modifications.
- For a star connected load, the line voltage is equal to the phase voltage, and the line current is equal to the phase current times the square root of three. Therefore, the power factor formula becomes:

```
power factor = (W1 + W2) / (3 * VP * IP)
```

- Where VP and IP are the phase voltage and current, respectively.
- For a delta connected load, the line voltage is equal to the phase voltage times the square root of three, and the line current is equal to the phase current. Therefore, the power factor formula becomes:

```
power factor = (W1 + W2) / (VP * IP)
```

- The two wattmeter method is useful for measuring the power in balanced or unbalanced three-phase circuits, as well as for determining the power factor of the load. However, it has some limitations, such as:
  - It requires two wattmeters, which may be expensive or unavailable.
  - It cannot measure the power in a three-wire circuit without a neutral wire, such as a delta connected load without a neutral point.
  - It cannot measure the power in a four-wire circuit with a neutral wire, such as a star connected load with a neutral point.
  - It cannot measure the power in a circuit with a non-sinusoidal voltage or current waveform, such as a circuit with harmonics or distortion.
  - It cannot measure the reactive power or the apparent power in the circuit, only the active power.