The two-wattmeter method is a technique for measuring the power in a three-phase circuit using two wattmeters. It can be applied to balanced or unbalanced loads, star or delta connected. The basic principle is to connect the current coils of the two wattmeters in series with any two line conductors, and the potential coils of each wattmeter to the third line conductor. The total power is then the sum of the two wattmeter readings.

The following diagram illustrates the two-wattmeter method for a star-connected load.

```
    A
    |
    V
    R
    |
    V
    W1
    |
    V
    B
   / \
  /   \
 /     \
V       V
W2      C
 \     /
  \   /
   \ /
    V
    N
```

In this diagram, A, B and C are the line conductors, N is the neutral, R is the load resistance, W1 and W2 are the wattmeters, and V is the voltmeter. The current coils of W1 and W2 are connected in series with A and B, respectively, and the potential coils of both wattmeters are connected to C. The voltmeter is connected across A and N to measure the phase voltage.

The power measured by W1 is given by:

`P1 = Vp * Ip * cos(30 - phi)`

where Vp is the phase voltage, Ip is the phase current, and phi is the power factor angle.

The power measured by W2 is given by:

`P2 = Vp * Ip * cos(30 + phi)`

The total power is then:

`P = P1 + P2 = 3 * Vp * Ip * cos(phi)`

The power factor can be calculated by:

`cos(phi) = (P1 + P2) / (3 * Vp * Ip)`

The following diagram illustrates the two-wattmeter method for a delta-connected load.

```
    A
   / \
  /   \
 /     \
V       V
W1      W2
 \     /
  \   /
   \ /
    V
    B
    |
    V
    R
    |
    V
    C
```

In this diagram, A, B and C are the line conductors, R is the load resistance, W1 and W2 are the wattmeters, and V is the voltmeter. The current coils of W1 and W2 are connected in series with A and B, respectively, and the potential coils of both wattmeters are connected to C. The voltmeter is connected across A and B to measure the line voltage.

The power measured by W1 is given by:

`P1 = Vl * Il * cos(30 - phi)`

where Vl is the line voltage, Il is the line current, and phi is the power factor angle.

The power measured by W2 is given by:

`P2 = Vl * Il * cos(30 + phi)`

The total power is then:

`P = P1 + P2 = 3 * Vl * Il * cos(phi)`

The power factor can be calculated by:

`cos(phi) = (P1 + P2) / (3 * Vl * Il)`