Measurement is a crucial operation in quantum computation, as it allows one to extract information from a quantum system and to manipulate its state. There are different models of quantum computation that use measurement as the main tool, such as measurement-based quantum computation, one-way quantum computer, and teleportation-based quantum computation. In these models, the computation is driven by local measurements on qubits that are prepared in a highly entangled state, such as a cluster state or a graph state. The outcome of each measurement determines the next measurement to be performed, and the final result is obtained by combining all the measurement outcomes.

The following diagram illustrates the basic architecture of a measurement-based quantum computation:

```
    |<----------------- Cluster state ----------------->|
    |                                                  |
    |  o---o---o---o---o---o---o---o---o---o---o---o   |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  o---o---o---o---o---o---o---o---o---o---o---o   |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  o---o---o---o---o---o---o---o---o---o---o---o   |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  o---o---o---o---o---o---o---o---o---o---o---o   |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  o---o---o---o---o---o---o---o---o---o---o---o   |
    |                                                  |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  v   v   v   v   v   v   v   v   v   v   v   v   |
    |  M   M   M   M   M   M   M   M   M   M   M   M   |
    |                                                  |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  v   v   v   v   v   v   v   v   v   v   v   v   |
    |  x   x   x   x   x   x   x   x   x   x   x   x   |
    |                                                  |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  v   v   v   v   v   v   v   v   v   v   v   v   |
    |  C   C   C   C   C   C   C   C   C   C   C   C   |
    |                                                  |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  v   v   v   v   v   v   v   v   v   v   v   v   |
    |  R   R   R   R   R   R   R   R   R   R   R   R   |
    |                                                  |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  v   v   v   v   v   v   v   v   v   v   v   v   |
    |  F   F   F   F   F   F   F   F   F   F   F   F   |
    |                                                  |
    |  |   |   |   |   |   |   |   |   |   |   |   |   |
    |  v   v   v   v   v   v   v   v   v   v   v   v   |
    |  O   O   O   O   O   O   O   O   O   O   O   O   |
    |                                                  |
    |<----------------- Output state ----------------->|
```

In