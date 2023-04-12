Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of equivalent circuit for the notes of the Unit 3 - Transformers in the subject of FUNDAMENTALS OF ELECTRICAL ENGINEERING.

### Equivalent Circuit

- An equivalent circuit is a simplified representation of a complex circuit or device that preserves its essential characteristics, such as voltage, current, power, impedance, etc.
- An equivalent circuit can be used to analyze the behavior and performance of the circuit or device under different conditions, such as load, frequency, temperature, etc.
- An equivalent circuit can also be used to compare and contrast different circuits or devices, such as different types of transformers, motors, generators, etc.

#### Equivalent Circuit of a Transformer

- A transformer is a device that transfers electrical energy from one circuit to another through electromagnetic induction, without changing the frequency.
- A transformer consists of two or more coils of wire, called the primary and secondary windings, that are wound around a common magnetic core, usually made of iron or steel.
- The primary winding is connected to the input voltage source, and the secondary winding is connected to the output load.
- When an alternating current (AC) flows through the primary winding, it produces an alternating magnetic flux in the core, which induces an alternating voltage in the secondary winding, according to Faraday's law of electromagnetic induction.
- The ratio of the primary and secondary voltages is equal to the ratio of the primary and secondary turns, according to the transformer equation: $$V_s = \frac{N_s}{N_p} V_p$$
- The ratio of the primary and secondary currents is inversely proportional to the ratio of the primary and secondary turns, according to the conservation of energy: $$I_s = \frac{N_p}{N_s} I_p$$
- The ratio of the primary and secondary turns is also called the turns ratio or the transformation ratio of the transformer: $$a = \frac{N_p}{N_s}$$
- The ideal transformer is a transformer that has no losses, no leakage flux, and no magnetizing current. In other words, it is a transformer that transfers all the input power to the output load, without any losses or inefficiencies.
- The ideal transformer can be represented by an equivalent circuit that consists of only an ideal transformer, as shown below:

```
+-----+     +-----+
|     |     |     |
|  Vp |     |  Vs |
|     |     |     |
+--+--+     +--+--+
   |           |
   |           |
   |           |
   |           |
   |           |
   |           |
+--+--+     +--+--+
|     |     |     |
|  Ip |     |  Is |
|     |     |     |
+-----+     +-----+
```

- The actual transformer is a transformer that has some losses, leakage flux, and magnetizing current. In other words, it is a transformer that transfers less than the input power to the output load, due to some losses or inefficiencies.
- The actual transformer can be represented by an equivalent circuit that consists of an ideal transformer and some additional elements, such as resistances, reactances, and sources, that account for the losses, leakage flux, and magnetizing current, as shown below:

```
+-----+     +-----+
|     |     |     |
|  Vp |     |  Vs |
|     |     |     |
+--+--+     +--+--+
   |           |
   |           |
   |           |
   |           |
   |           |
   |           |
+--+--+     +--+--+
|     |     |     |
|  Ip |     |  Is |
|     |     |     |
+--+--+     +--+--+
   |           |
   |           |
   |           |
   |           |
   |           |
   |           |
+--+--+     +--+--+
|     |     |     |
| Rp  |     | Rs  |
|     |     |     |
+--+--+     +--+--+
   |           |
   |           |
   |           |
   |           |
   |           |
   |           |
+--+--+     +--+--+
|     |     |     |
| Xp  |     | Xs  |
|     |     |     |
+--+--+     +--+--+
   |           |
   |           |
   |           |
   |           |
   |           |
   |           |
+--+--+     +--+--+
|     |     |     |
| Rc  |     |     |
|     |     |     |
+

```
