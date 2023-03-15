## Design of an 8-bit Input/ Output system with four 8-bit Internal Registers

- An 8-bit input/output system is a device that can read or write 8-bit data from or to an external source, such as a keyboard, a monitor, or a memory.
- An 8-bit internal register is a storage element that can hold 8-bit data temporarily within the device.
- A typical 8-bit input/output system with four 8-bit internal registers consists of the following components :
  - A data bus (D0-D7) that connects the input/output system to the external source and carries the 8-bit data.
  - An address bus (A0-A3) that selects one of the four internal registers to read from or write to.
  - A control bus that consists of three signals: clear (CLR), read enable (RE), and write enable (WE).
    - CLR clears the contents of all the internal registers to zero.
    - RE enables the input/output system to read data from the external source and store it in the selected internal register.
    - WE enables the input/output system to write data from the selected internal register to the external source.
  - Four 8-bit D flip-flops (FF0-FF3) that act as the internal registers. Each flip-flop has a data input (D), a data output (Q), a clock input (CLK), and a reset input (RST).
    - D receives the data from the data bus or the external source.
    - Q outputs the data to the data bus or the external source.
    - CLK receives the clock signal from the control bus and triggers the data transfer on the rising edge.
    - RST receives the clear signal from the control bus and resets the data to zero.
  - Four 2-input AND gates (G0-G3) that act as the address decoders. Each AND gate has two inputs (A and B) and one output (Y).
    - A and B receive the address bits from the address bus and select one of the four internal registers.
    - Y outputs a high signal to the clock input of the selected flip-flop and a low signal to the others.
- The following table shows the truth table of the address decoder :

| A3 | A2 | A1 | A0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 0  | 0  | 1  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 1  | 1  | 0  | 0  | 0  | 1  |
| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  | 0  | 0  | 0  | 0  |
| 0  | 1  | 1  | 0  | 0  | 0  | 0  | 0  |
| 0  | 1  | 1  | 1  | 0  | 0  | 0  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 1  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 1  | 0  | 1  | 1  | 0  | 0  | 0  | 0  |
| 1  | 1  | 0  | 0  | 0  | 0  |