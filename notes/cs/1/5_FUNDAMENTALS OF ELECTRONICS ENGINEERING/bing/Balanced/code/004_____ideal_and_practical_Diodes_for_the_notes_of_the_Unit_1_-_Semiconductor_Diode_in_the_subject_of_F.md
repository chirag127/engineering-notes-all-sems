### Ideal and Practical Diodes

- A diode is a two-terminal electronic device that allows current to flow in one direction only.
- An ideal diode is a hypothetical device that has zero resistance when forward biased and infinite resistance when reverse biased.
- A practical diode is a real device that has some non-ideal characteristics, such as forward voltage drop, reverse leakage current, and breakdown voltage.
- The differences between ideal and practical diodes are summarized in the table below:

| Ideal diodes | Practical diodes |
| ------------ | ---------------- |
| Ideal diodes act as perfect conductor and perfect insulator. | Practical diodes cannot act as perfect conductor or insulator. |
| Ideal diode draws no current when reverse biased. | Practical diode draws very low current when reverse biased, called reverse leakage current. |
| Ideal diode offers infinite resistance when reverse biased. | Practical diode offers very high resistance when reverse biased, but not infinite. |
| Ideal diode has no voltage drop when forward biased. | Practical diode has a voltage drop when forward biased, called forward voltage drop. |
| Ideal diode has no breakdown voltage. | Practical diode has a breakdown voltage, beyond which it conducts in reverse direction. |
| Ideal diode cannot be manufactured. | Practical diode can be manufactured. |

- The V-I characteristics of ideal and practical diodes are shown in the figure below:

![V-I characteristics of ideal and practical diodes](https://circuitglobe.com/wp-content/uploads/2016/06/ideal-and-real-diode.png)

- The ideal diode equation is a mathematical expression that relates the current and voltage of a diode. It is given by:

$$
I = I_S (e^{\frac{V}{\eta V_T}} - 1)
$$

where

- $I$ is the diode current
- $I_S$ is the reverse saturation current
- $V$ is the diode voltage
- $\eta$ is the ideality factor
- $V_T$ is the thermal voltage

- The ideal diode equation is very useful as a formula for current as a function of voltage. However, at times the inverse relation may be more useful; if the ideal diode equation is inverted and solved for voltage as a function of current, we find:

$$
V = \eta V_T \ln \left(\frac{I}{I_S} + 1\right)
$$

- The ideal diode equation can be used to model the behavior of practical diodes, but it does not account for some non-ideal effects, such as series resistance, junction capacitance, and temperature dependence.