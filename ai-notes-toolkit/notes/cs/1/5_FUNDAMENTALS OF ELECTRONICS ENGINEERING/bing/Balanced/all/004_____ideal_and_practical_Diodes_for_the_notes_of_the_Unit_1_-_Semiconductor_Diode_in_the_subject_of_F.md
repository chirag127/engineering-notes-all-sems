# Ideal and Practical Diodes

- A **diode** is a two-terminal electronic device that allows current to flow in one direction only.
- An **ideal diode** is a hypothetical device that has the following characteristics  :
  - It acts as a **perfect conductor** when it is forward biased, meaning that it has zero voltage drop across it and allows any amount of current to flow through it.
  - It acts as a **perfect insulator** when it is reverse biased, meaning that it has infinite resistance and blocks any current from flowing through it.
  - It has a **sharp transition** between the conducting and insulating states, meaning that it switches instantly from one state to the other when the applied voltage changes polarity.
  - It has **no leakage current**, meaning that it does not draw any current when it is reverse biased.
  - It has **no capacitance**, meaning that it does not store any charge or energy when it is biased in either direction.
- A **practical diode** is a real device that has the following characteristics  :
  - It acts as a **near-perfect conductor** when it is forward biased, meaning that it has a small voltage drop across it (typically 0.7 V for silicon diodes and 0.3 V for germanium diodes) and allows a large amount of current to flow through it.
  - It acts as a **near-perfect insulator** when it is reverse biased, meaning that it has a very high resistance and blocks most of the current from flowing through it.
  - It has a **smooth transition** between the conducting and insulating states, meaning that it switches gradually from one state to the other as the applied voltage changes polarity.
  - It has a **small leakage current**, meaning that it draws a very low current (typically in the range of microamperes to nanoamperes) when it is reverse biased.
  - It has a **small capacitance**, meaning that it stores a small amount of charge or energy when it is biased in either direction (typically in the range of picofarads to nanofarads).
- The **V-I characteristics** of an ideal diode and a practical diode are shown in the figure below :

![V-I characteristics of ideal and practical diodes](https://i.imgur.com/9XZ1Q2f.png)

- The **ideal diode equation** is a mathematical expression that relates the current and voltage of a practical diode. It is given by:

  - I = I_s (e^(v/(ηV_T)) - 1)

  - where I is the diode current, I_s is the reverse saturation current, v is the diode voltage, η is the ideality factor, and V_T is the thermal voltage.
  - The ideal diode equation is very useful as a formula for current as a function of voltage. However, at times the inverse relation may be more useful; if the ideal diode equation is inverted and solved for voltage as a function of current, we find:

  - v = ηV_T ln((I/I_s) + 1)

- The **ideality factor** is a parameter that measures how closely a practical diode behaves like an ideal diode. It is typically in the range of 1 to 2, depending on the type and quality of the diode. A lower value of η means a more ideal diode.
- The **thermal voltage** is a parameter that depends on the temperature and the charge of the electron. It is given by:

  - V_T = kT/q

  - where k is the Boltzmann constant, T is the absolute temperature, and q is the elementary charge. At room temperature (25°C), V_T is approximately 0.026 V.