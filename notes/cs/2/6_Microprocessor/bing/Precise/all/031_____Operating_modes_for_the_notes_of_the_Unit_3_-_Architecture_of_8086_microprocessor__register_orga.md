# Operating Modes

The 8086 microprocessor has two operating modes: minimum mode and maximum mode.

1. **Minimum mode**: In minimum mode, the 8086 microprocessor operates as a single microprocessor system. This mode is used when the system has only one microprocessor. In this mode, the 8086 microprocessor generates all the control signals required for memory and I/O operations.

2. **Maximum mode**: In maximum mode, the 8086 microprocessor operates as part of a multi-processor system. This mode is used when the system has more than one microprocessor. In this mode, the 8086 microprocessor does not generate all the control signals required for memory and I/O operations. Instead, an external bus controller is used to generate the control signals.

The operating mode of the 8086 microprocessor is selected by the MN/MX# pin. If the MN/MX# pin is connected to ground, the 8086 microprocessor operates in minimum mode. If the MN/MX# pin is connected to +5V, the 8086 microprocessor operates in maximum mode.