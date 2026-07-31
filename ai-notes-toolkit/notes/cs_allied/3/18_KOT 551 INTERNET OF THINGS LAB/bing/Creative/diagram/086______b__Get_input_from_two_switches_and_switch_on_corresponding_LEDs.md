Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use to study and learn from:

#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, you need to use a microcontroller, such as Arduino, and connect it to the switches and LEDs using wires and resistors.
- A switch is a device that can open or close a circuit, allowing current to flow or stop. A LED (light-emitting diode) is a device that emits light when current passes through it.
- You can use the digital pins of the Arduino to read the state of the switches and control the state of the LEDs. For example, you can use pin 2 and 3 for the switches, and pin 8 and 9 for the LEDs.
- You need to declare the pin numbers as constants and set them as input or output using the pinMode() function in the setup() function. For example:

```c
// define the pin numbers
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 8;
const int led2 = 9;

void setup() {
  // set the pins as input or output
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}
```

- You need to read the state of the switches using the digitalRead() function and store them in variables in the loop() function. For example:

```c
void loop() {
  // read the state of the switches
  int switch1State = digitalRead(switch1);
  int switch2State = digitalRead(switch2);
}
```

- You need to use conditional statements to check the state of the switches and turn on or off the corresponding LEDs using the digitalWrite() function. For example:

```c
void loop() {
  // read the state of the switches
  int switch1State = digitalRead(switch1);
  int switch2State = digitalRead(switch2);

  // check the state of switch1 and turn on or off led1
  if (switch1State == HIGH) {
    // switch1 is pressed, turn on led1
    digitalWrite(led1, HIGH);
  } else {
    // switch1 is not pressed, turn off led1
    digitalWrite(led1, LOW);
  }

  // check the state of switch2 and turn on or off led2
  if (switch2State == HIGH) {
    // switch2 is pressed, turn on led2
    digitalWrite(led2, HIGH);
  } else {
    // switch2 is not pressed, turn off led2
    digitalWrite(led2, LOW);
  }
}
```

- This is the basic logic of getting input from two switches and switching on corresponding LEDs. You can modify the code and the circuit according to your needs and preferences.