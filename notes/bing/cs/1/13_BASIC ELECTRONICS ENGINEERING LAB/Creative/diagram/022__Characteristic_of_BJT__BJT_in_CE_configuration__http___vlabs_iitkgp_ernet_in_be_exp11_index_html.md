The characteristic of BJT in CE configuration is the relation between the input current (base current, I_B) and the output current (collector current, I_C) for different values of the input voltage (base-emitter voltage, V_BE) and the output voltage (collector-emitter voltage, V_CE). The characteristic can be divided into two parts: the input characteristic and the output characteristic.

The input characteristic is the plot of I_B versus V_BE for different values of V_CE. It shows how the base current varies with the base-emitter voltage for a given collector-emitter voltage. The input characteristic is similar to that of a forward-biased diode, as the base-emitter junction is forward-biased in CE configuration. The input characteristic can be approximated by the following equation:

I_B = I_S * (exp(V_BE / V_T) - 1)

where I_S is the reverse saturation current, V_T is the thermal voltage, and exp is the exponential function.

The output characteristic is the plot of I_C versus V_CE for different values of I_B. It shows how the collector current varies with the collector-emitter voltage for a given base current. The output characteristic can be divided into three regions: the cutoff region, the active region, and the saturation region.

The cutoff region is the region where both the base-emitter and the collector-base junctions are reverse-biased, and the collector current is negligible. The cutoff region is defined by the condition:

V_CE > V_BE + V_CB

where V_CB is the collector-base voltage.

The active region is the region where the base-emitter junction is forward-biased and the collector-base junction is reverse-biased, and the collector current is proportional to the base current. The active region is defined by the condition:

V_BE + V_CB > V_CE > V_BE

The collector current in the active region can be approximated by the following equation:

I_C = beta * I_B

where beta is the current gain of the transistor.

The saturation region is the region where both the base-emitter and the collector-base junctions are forward-biased, and the collector current is limited by the supply voltage. The saturation region is defined by the condition:

V_CE < V_BE + V_CB

The collector current in the saturation region can be approximated by the following equation:

I_C = (V_CC - V_CE) / R_C

where V_CC is the supply voltage and R_C is the collector resistance.

The following diagram illustrates the basic architecture of a BJT in CE configuration:

```
    V_CC
     |
     |
    R_C
     |
     |-------------------+
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   V_CE
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     +-------------------+
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |  N
     |                   |  P
     |                   |  N
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   V_BE
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     +-------------------+
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
    R_B                 R_E
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     |                   |
     +-------------------+
     |
     |
    V_BB
```

The following diagram illustrates the input and output characteristics of a BJT in CE configuration:

```
Input