### Ideal and Practical Diodes

- A **diode** is a two-terminal electronic device that allows current to flow in one direction only.
- An **ideal diode** is a hypothetical device that has zero voltage drop when forward biased and zero current when reverse biased. It acts as a perfect switch that turns on and off instantly.
- A **practical diode** is a real device that has some non-ideal characteristics, such as a finite forward voltage drop, a small reverse leakage current, a finite switching speed, and a breakdown voltage.
- The **difference** between ideal and practical diodes can be summarized as follows  :

| Ideal diodes | Practical diodes |
| ------------ | ---------------- |
| Ideal diodes act as perfect conductor and perfect insulator. | Practical diodes cannot act as perfect conductor and perfect insulator. |
| Ideal diode draws no current when reverse biased. | Practical diode draws very low current when reverse biased, called reverse leakage current. |
| Ideal diode offers infinite resistance when reverse biased and zero resistance when forward biased. | Practical diode offers very high resistance when reverse biased and low resistance when forward biased. |
| Ideal diode has no voltage drop when forward biased. | Practical diode has a voltage drop when forward biased, called forward voltage drop. |
| Ideal diode has no breakdown voltage. | Practical diode has a breakdown voltage, beyond which it may be damaged. |
| Ideal diode has no switching time. | Practical diode has a switching time, which is the time required to turn on or off. |
| Ideal diode cannot be manufactured. | Practical diode can be manufactured. |

- The **V-I characteristics** of ideal and practical diodes are shown in the figure below  :

![V-I characteristics of ideal and practical diodes](https://i.imgur.com/8Q2y8n0.png)

- The **ideal diode equation** is a mathematical expression that relates the current and voltage of a diode. It is given by:

$$
i = I_S \left( e^{\frac{v}{\eta V_T}} - 1 \right)
$$

where

- $i$ is the diode current
- $v$ is the diode voltage
- $I_S$ is the reverse saturation current
- $\eta$ is the ideality factor
- $V_T$ is the thermal voltage

- The **reverse saturation current** is the current that flows through the diode when it is reverse biased. It is very small and depends on the temperature and the material of the diode.
- The **ideality factor** is a parameter that indicates how close the diode is to the ideal behavior. It is usually between 1 and 2 for most diodes.
- The **thermal voltage** is a constant that depends on the temperature and the charge of the electron. It is given by:

$$
V_T = \frac{kT}{q}
$$

where

- $k$ is the Boltzmann constant
- $T$ is the absolute temperature
- $q$ is the elementary charge

- The **forward voltage drop** is the voltage that must be applied across the diode to make it conduct. It is usually around 0.7 V for silicon diodes and 0.3 V for germanium diodes.
- The **breakdown voltage** is the voltage that causes the diode to conduct in the reverse direction. It is usually much higher than the forward voltage drop and depends on the type and structure of the diode.