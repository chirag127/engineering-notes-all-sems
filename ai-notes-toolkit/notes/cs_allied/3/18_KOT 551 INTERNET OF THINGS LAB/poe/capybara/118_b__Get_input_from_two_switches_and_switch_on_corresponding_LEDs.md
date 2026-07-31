## Get Input from Two Switches and Switch on Corresponding LEDs

In this topic, we will discuss how to get input from two switches and switch on corresponding LEDs. This process can be done using a microcontroller such as Arduino, Raspberry Pi or any other microcontroller.

### Steps to Get Input from Two Switches and Switch on Corresponding LEDs

1. Connect the switches to the microcontroller's input pins. The switches can be connected in parallel or in series. 

2. Declare the input pins as digital inputs in the code. 

3. Read the input from the switches using the `digitalRead()` function. This function returns either HIGH or LOW depending on whether the switch is pressed or not.

4. Assign the output pins for the LEDs. 

5. Declare the output pins as digital outputs in the code. 

6. Use the `digitalWrite()` function to switch on or off the LED. 

7. Use `if` statements to check the state of each switch and switch on the corresponding LED. For example, if switch 1 is pressed, switch on LED 1. 

8. Use a delay function to slow down the program and prevent it from executing too quickly. 

### Example Code

```cpp
const int switchPin1 = 2;
const int switchPin2 = 3;
const int ledPin1 = 4;
const int ledPin2 = 5;

void setup() {
  pinMode(switchPin1, INPUT);
  pinMode(switchPin2, INPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() {
  int switchState1 = digitalRead(switchPin1);
  int switchState2 = digitalRead(switchPin2);

  if (switchState1 == HIGH) {
    digitalWrite(ledPin1, HIGH);
  } else {
    digitalWrite(ledPin1, LOW);
  }

  if (switchState2 == HIGH) {
    digitalWrite(ledPin2, HIGH);
  } else {
    digitalWrite(ledPin2, LOW);
  }

  delay(100);
}
```

### Conclusion

In conclusion, getting input from two switches and switching on corresponding LEDs is a simple process that can be done using a microcontroller. By following the steps outlined above and using the example code provided, you can easily incorporate this functionality into your own projects.