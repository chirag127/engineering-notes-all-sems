## Get input from two switches and switch on corresponding LEDs

In embedded systems, switches are commonly used as input devices to provide user interaction. In this topic, we will learn how to get input from two switches and switch on corresponding LEDs using a microcontroller.

### Hardware Requirements
- Microcontroller (such as Arduino)
- Breadboard
- Two switches
- Two LEDs
- Resistors
- Jumper wires

### Circuit Diagram

![Switch and LED circuit diagram](https://i.imgur.com/L1nJVmR.png)

### Steps
1. Connect the switches to the microcontroller pins. One switch will be connected to pin 2 and the other to pin 3.
2. Connect the LEDs to the microcontroller pins. One LED will be connected to pin 4 and the other to pin 5.
3. Connect a resistor to each LED to limit the current flowing through them.
4. Connect the other end of each resistor to the ground pin of the microcontroller.
5. Set the pin mode of pins 2 and 3 to input, and pins 4 and 5 to output using the pinMode() function.
6. In the main loop function, use digitalRead() function to read the status of the switches.
7. If switch 1 is pressed, turn on LED 1 by setting pin 4 to HIGH using digitalWrite() function.
8. If switch 2 is pressed, turn on LED 2 by setting pin 5 to HIGH.
9. If both switches are pressed, turn on both LEDs.
10. If neither switch is pressed, turn off both LEDs by setting pins 4 and 5 to LOW.

### Sample Code
```c++
void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop() {
  if (digitalRead(2) == HIGH && digitalRead(3) == LOW) {
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
  } else if (digitalRead(2) == LOW && digitalRead(3) == HIGH) {
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);
  } else if (digitalRead(2) == HIGH && digitalRead(3) == HIGH) {
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
  } else {
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
  }
}
```

### Conclusion
In this topic, we learned how to get input from two switches and switch on corresponding LEDs using a microcontroller. By following the steps and using the sample code provided, you can create your own switch and LED circuit and expand it to include more switches and LEDs.