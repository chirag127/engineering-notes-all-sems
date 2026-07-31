##### 1. Verification of Kirchhoff’s laws

- Kirchhoff’s laws are two rules that relate the currents and voltages in an electrical circuit.
- Kirchhoff’s current law (KCL) states that the algebraic sum of the currents entering a node (or a closed boundary) is zero.
- Kirchhoff’s voltage law (KVL) states that the algebraic sum of the voltages around a loop (or a closed path) is zero.
- To verify Kirchhoff’s laws experimentally, one can use a simple circuit consisting of a battery, a resistor, and a voltmeter and an ammeter.
- The steps are as follows:
  - Connect the battery, the resistor, the voltmeter, and the ammeter in series, as shown in the figure below.
  - Measure the current (I) through the ammeter and the voltage (V) across the resistor using the voltmeter.
  - Apply KCL at the node where the battery, the resistor, and the ammeter are connected. The current entering the node is equal to the current leaving the node, which is equal to I. Therefore, KCL is verified.
  - Apply KVL around the loop formed by the battery, the resistor, the voltmeter, and the ammeter. The voltage around the loop is equal to the sum of the voltage drops across the components, which is equal to V - I*R, where R is the resistance of the resistor. Therefore, KVL is verified.

```
  +-----+     +-----+     +-----+
  |     |     |     |     |     |
  |     |     |     |     |     |
  |     |     |     |     |     |
  |     |     |     |     |     |
  |     |     |     |     |     |
  +-----+     +-----+     +-----+
    |           |           |
    |           |           |
    |           |           |
    |           |           |
    |           |           |
    +-----------+-----------+
        |               |
        |               |
        |               |
        |               |
        |               |
        V               I
      +---+           +---+
      |   |           |   |
      |   |           |   |
      |   |           |   |
      |   |           |   |
      |   |           |   |
      +---+           +---+
      Voltmeter      Ammeter
```