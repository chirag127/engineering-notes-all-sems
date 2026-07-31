# b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- A switch is a device that can open or close a circuit, allowing current to flow or stop. A LED is a light-emitting diode that can emit light when current passes through it.
- We can use the digital pins of the Arduino to read the state of the switches and control the state of the LEDs. For example, we can use pin 2 and 3 for the switches, and pin 4 and 5 for the LEDs.
- We need to use resistors to limit the current that flows through the switches and the LEDs, to prevent damage to the components or the Arduino. For example, we can use 10k ohm resistors for the switches, and 220 ohm resistors for the LEDs.
- We also need to connect the ground (GND) pins of the Arduino to the negative terminals of the switches and the LEDs, and the 5V pin of the Arduino to the positive terminals of the switches.
- The circuit diagram for this project is shown below:

```
  +5V
   |
   |
  [ ] 10k ohm
   |
   |       +--------+
   +-------|  pin 2 | Arduino
   |       +--------+
   |
  [ ] switch 1
   |
   |
  GND

  +5V
   |
   |
  [ ] 10k ohm
   |
   |       +--------+
   +-------|  pin 3 | Arduino
   |       +--------+
   |
  [ ] switch 2
   |
   |
  GND

       +--------+
       |  pin 4 | Arduino
       +--------+
         |
         |
        [ ] 220 ohm
         |
         |     LED 1
        [ ]<|---|>
         |
         |
        GND

       +--------+
       |  pin 5 | Arduino
       +--------+
         |
         |
        [ ] 220 ohm
         |
         |     LED 2
        [ ]<|---|>
         |
         |
        GND
```

- To program the Arduino, we need to use the Arduino IDE and write the code in C++. The code should do the following steps:
  - Declare the pin numbers for the switches and the LEDs as constants.
  - Set the pin modes for the switches as inputs and the LEDs as outputs in the setup function.
  - Read the state of the switches using digitalRead function in the loop function.
  - Write the state of the LEDs using digitalWrite function in the loop function, based on the state of the switches.
  - Add some delay between each iteration of the loop function to avoid flickering of the LEDs.
- The code for this project is shown below:

```c++
// define the pin numbers for the switches and the LEDs
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 4;
const int led2 = 5;

void setup() {
  // set the pin modes for the switches as inputs and the LEDs as outputs
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // read the state of the switches
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);

  // write the state of the LEDs based on the state of the switches
  digitalWrite(led1, state1);
  digitalWrite(led2, state2);

  // add some delay to avoid flickering
  delay(100);
}
```

- To test the project, we need to upload the code to the Arduino and connect it to the computer using a USB cable. Then, we can open the serial monitor and observe the output of the LEDs. We can also change the state of the switches and see how the LEDs respond accordingly. The expected output is shown below:

```
switch 1 | switch 2 | LED 1 | LED 2
-----------------------------------
   off   |   off    |  off  |  off
   on    |   off    |  on   |  off
   off   |   on     |  off  |  on
   on    |   on     |  on   |  on
```

- This project demonstrates how to get input from two switches and switch on corresponding