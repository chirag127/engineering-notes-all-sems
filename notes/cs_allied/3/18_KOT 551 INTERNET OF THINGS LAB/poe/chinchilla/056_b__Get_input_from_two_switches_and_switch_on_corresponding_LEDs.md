## Get input from two switches and switch on corresponding LEDs

When working with microcontrollers, it is common to need to read input from switches and control output to LEDs. In this section, we will discuss how to get input from two switches and switch on corresponding LEDs using a microcontroller.

### Required components

To get input from two switches and switch on corresponding LEDs, we will need the following components:

- A microcontroller (such as an Arduino)
- Two switches (such as push buttons)
- Two LEDs (with corresponding resistors)
- Breadboard and jumper wires

### Circuit diagram

The circuit diagram for getting input from two switches and switching on corresponding LEDs is shown below:

```
                +5V
                 |
                 -
                 |
                 |
          Switch 1
                 |
                 -
                 |
                 |
            Digital pin 2     Resistor     LED 1
                 |             |           |
                 -             -           -
                 |             |           |
                 |             |           |
          Switch 2             |           |
                 -             -           |
                 |             |           |
                 |             |           |
                GND            |           |
                                -           -
                                |           |
                                |           |
                            Resistor        |
                                |           |
                                -           -
                                |           |
                                |           |
                            LED 2          GND
```

### Programming

To read input from the switches and control output to the LEDs, we will need to write a program for the microcontroller. The following steps outline the basic program:

1. Set up the digital pins for input (for the switches) and output (for the LEDs).

```c
int switch1 = 2; // digital pin 2 for switch 1
int switch2 = 3; // digital pin 3 for switch 2
int led1 = 4;    // digital pin 4 for LED 1
int led2 = 5;    // digital pin 5 for LED 2

void setup() {
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}
```

2. Read the input from the switches and switch on the corresponding LEDs.

```c
void loop() {
  if (digitalRead(switch1) == HIGH) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led1, LOW);
  }

  if (digitalRead(switch2) == HIGH) {
    digitalWrite(led2, HIGH);
  } else {
    digitalWrite(led2, LOW);
  }
}
```

In this program, we are using the `digitalRead` function to read the input from the switches. If the switch is pressed (i.e., if `digitalRead` returns `HIGH`), we switch on the corresponding LED using the `digitalWrite` function. Otherwise, we switch off the LED.

### Conclusion

In this section, we have discussed how to get input from two switches and switch on corresponding LEDs using a microcontroller. We have seen the required components, the circuit diagram, and the basic program. With this knowledge, you should be able to implement similar circuits and programs for your own projects.