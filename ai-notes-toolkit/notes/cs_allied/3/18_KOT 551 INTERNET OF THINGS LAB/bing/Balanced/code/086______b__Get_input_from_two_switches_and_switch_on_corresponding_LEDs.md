#### b) Get input from two switches and switch on corresponding LEDs

- The objective of this task is to design a circuit that can read the input from two switches and turn on the corresponding LEDs based on the switch state.
- The circuit requires the following components:
  - Two switches (S1 and S2) that can be toggled between ON and OFF positions.
  - Two LEDs (L1 and L2) that can emit light when powered by a voltage source.
  - A power supply (Vcc) that can provide a constant voltage to the circuit.
  - Four resistors (R1, R2, R3, and R4) that can limit the current flow through the LEDs and protect them from damage.
- The circuit diagram is shown below:

```
    Vcc
     |
     |
    R1
     |
     +----+----+
     |         |
     |        S1
     |         |
    L1        R2
     |         |
     +----+----+
     |
     |
    R3
     |
     +----+----+
     |         |
     |        S2
     |         |
    L2        R4
     |         |
     +----+----+
     |
    GND
```

- The circuit works as follows:
  - When both switches are OFF, no current flows through the LEDs and they remain off.
  - When S1 is ON and S2 is OFF, current flows from Vcc through R1, L1, R3, and S1 to GND. This turns on L1 and off L2.
  - When S1 is OFF and S2 is ON, current flows from Vcc through R1, R3, L2, R4, and S2 to GND. This turns on L2 and off L1.
  - When both switches are ON, current flows from Vcc through R1, L1, R2, S1, R3, L2, R4, and S2 to GND. This turns on both L1 and L2.