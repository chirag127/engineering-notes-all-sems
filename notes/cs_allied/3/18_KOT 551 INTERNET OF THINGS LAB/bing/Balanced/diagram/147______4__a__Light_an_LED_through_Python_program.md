#### 4. a) Light an LED through Python program

- To light an LED through Python program, one needs to have a Raspberry Pi, an LED, a breadboard, a resistor, and some jumper wires.
- The Raspberry Pi is a small computer that can run Python code and interact with external devices through its GPIO (General Purpose Input Output) pins.
- The LED is a light-emitting diode that can be turned on and off by applying a voltage across its terminals.
- The breadboard is a prototyping board that allows one to connect different components without soldering.
- The resistor is a component that limits the current flow and protects the LED from burning out.
- The jumper wires are used to connect the components on the breadboard and to the Raspberry Pi.

- The following diagram shows how to connect the LED, the resistor, and the jumper wires on the breadboard and to the Raspberry Pi.

```
    +3.3V (pin 1)  o----+----o  LED  o----+----o  Resistor  o----+----o  GND (pin 6)
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+
                        |    |       |    |       |    |       |    |
                        o    o       o    o       o    o       o    o
                        |    |       |    |       |    |       |    |
                        +----+       +----+       +----+       +----+