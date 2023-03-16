# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can be used to control the flow of electric current in a circuit. It can be either open or closed, meaning that it either allows or blocks the current.
- An LED is a light-emitting diode, which is a type of semiconductor that emits light when an electric current passes through it. It has two terminals, an anode and a cathode, and it only allows current to flow in one direction, from the anode to the cathode.
- To get input from two switches and switch on corresponding LEDs, we need to connect them in a certain way, as shown in the diagram below.

```text
    +5V
     |
     |
    [ ] S1
     |
     |
    [ ] LED1
     |
     |
    GND

    +5V
     |
     |
    [ ] S2
     |
     |
    [ ] LED2
     |
     |
    GND
```

- In this diagram, S1 and S2 are the switches, and LED1 and LED2 are the LEDs. They are connected to a +5V power source and a ground (GND) terminal, which complete the circuit.
- When S1 is closed, it allows current to flow from +5V to LED1, which turns it on. When S1 is open, it blocks the current, and LED1 turns off. Similarly, when S2 is closed, it allows current to flow from +5V to LED2, which turns it on. When S2 is open, it blocks the current, and LED2 turns off.
- Therefore, the input from the switches determines the output of the LEDs. We can summarize the logic of this circuit in a truth table, as shown below.

```text
    S1 | S2 | LED1 | LED2
    ---------------------
    0  | 0  |  0   |  0
    0  | 1  |  0   |  1
    1  | 0  |  1   |  0
    1  | 1  |  1   |  1
```

- In this table, 0 means open or off, and 1 means closed or on. The table shows that for each combination of inputs from S1 and S2, there is a corresponding combination of outputs from LED1 and LED2.
- This is an example of a simple logic circuit, which can be used to perform basic operations or functions based on the input signals. Logic circuits are the building blocks of digital electronics, which are widely used in computers, communication devices, and other applications.