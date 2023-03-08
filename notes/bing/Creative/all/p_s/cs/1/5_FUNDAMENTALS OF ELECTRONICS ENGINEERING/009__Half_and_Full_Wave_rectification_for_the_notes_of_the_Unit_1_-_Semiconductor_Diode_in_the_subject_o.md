### Half and Full Wave Rectification

- Rectification is the process of converting alternating current (AC) into direct current (DC) by using one or more diodes.
- Diodes are semiconductor devices that allow current to flow in one direction only, blocking the reverse direction.
- Rectification is used to power many electronic devices that require a steady DC supply, such as radios, TVs, computers, etc.

#### Half Wave Rectification

- A half wave rectifier is a rectifier that uses a single diode to convert only one half cycle of the AC input into DC output.
- The other half cycle of the AC input is blocked by the diode and does not appear in the output.
- The output of a half wave rectifier is a pulsating DC voltage with a lot of ripple (fluctuation).
- The advantages of a half wave rectifier are:
  - It is simple and cheap to construct.
  - It does not require a center-tapped transformer.
- The disadvantages of a half wave rectifier are:
  - It has a low efficiency (only 40.6% of the input power is converted to DC).
  - It has a high ripple factor (1.21), which means the output voltage is not smooth and constant.
  - It has a poor voltage regulation (the output voltage changes with the load resistance).
  - It wastes half of the input power.

- The circuit diagram of a half wave rectifier is shown below:

```
    AC input
      | 
      | 
      V
     ~ ~
    ~   ~
   ~     ~
  ~       ~
 ~         ~
+ - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - +
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
+                                                                               +
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
|                                                                               |
+                                                                               +
 ~         ~
  ~       ~
   ~     ~
    ~   ~
     ~ ~
      |
      |
      V
    DC output
```

- The waveform of the AC input and the DC output of a half wave rectifier is shown below:

```
AC input:     /|    /|    /|    /|    /|    /|    /|    /|    /|    /|    /|    /|    /|
             / |   / |   / |   / |   / |   / |   / |   / |   / |   / |   / |   / |   / |
            /  |  /  |  /  |  /  |  /  |  /  |  /  |  /  |  /  |  /  |  /  |  /  |  /  |
           /   | /   | /   | /   | /   | /   | /   | /   | /   | /   | /   | /   | /   |
          /    |/    |/    |/    |/    |/    |/    |/    |/    |/    |/    |/    |/    |
         /     |     |     |     |     |     |     |     |     |     |     |     |     |
        /      |     |     |     |     |     |     |     |     |     |     |     |     |
       /       |     |     |     |     |     |     |     |     |     |     |     |

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between half wave and full wave rectifiers, you can use the acronym HAFU: Half wave rectifier Allows only one half cycle of the input, Full wave rectifier Uses both halves of the input.
- To remember the formula for the efficiency of a half wave rectifier, you can use the rhyme: The efficiency of a half wave rectifier is 40.6, which is equal to 0.406, which is the square of 0.8 over pi.
- To remember the formula for the ripple factor of a half wave rectifier, you can use the wordplay: The ripple factor of a half wave rectifier is 1.21, which sounds like one to one, which is the ratio of the AC component to the DC component of the output voltage.