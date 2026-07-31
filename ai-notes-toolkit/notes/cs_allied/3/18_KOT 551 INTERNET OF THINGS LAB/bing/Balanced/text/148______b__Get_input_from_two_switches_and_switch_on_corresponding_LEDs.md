#### b) Get input from two switches and switch on corresponding LEDs

- The objective of this task is to design a circuit that can read the input from two switches and turn on the corresponding LEDs based on the switch states.
- The circuit requires the following components:
  - Two switches (S1 and S2) that can be toggled between ON and OFF positions.
  - Two LEDs (L1 and L2) that can emit light when powered by a voltage source.
  - A power supply (Vcc) that can provide a constant voltage to the circuit.
  - Four resistors (R1, R2, R3, and R4) that can limit the current flowing through the LEDs and protect them from damage.
- The circuit diagram is shown below:

```
    Vcc
     |
     |
    R1
     |
     +-----> L1
     |
    S1
     |
     |
    R2
     |
     +-----> L2
     |
    S2
     |
     |
    R3
     |
     +-----> L3
     |
    S3
     |
     |
    R4
     |
     +-----> L4
     |
    GND
```

- The circuit works as follows:
  - When both switches are OFF, no current flows through the LEDs and they are OFF.
  - When S1 is ON and S2 is OFF, current flows from Vcc through R1, L1, S1, R2, and GND. This turns on L1 and L2.
  - When S1 is OFF and S2 is ON, current flows from Vcc through R3, L3, S2, R4, and GND. This turns on L3 and L4.
  - When both switches are ON, current flows from Vcc through R1, L1, S1, R2, L2, S2, R4, L4, R3, L3, and GND. This turns on all four LEDs.