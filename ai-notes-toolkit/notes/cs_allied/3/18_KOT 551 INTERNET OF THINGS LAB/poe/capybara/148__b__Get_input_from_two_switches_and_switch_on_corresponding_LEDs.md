#### b) Get input from two switches and switch on corresponding LEDs

To control electronic devices, we can use switches. Switches are simple electrical components that can turn a circuit on or off. In this topic, we will learn how to get input from two switches and switch on corresponding LEDs.

Here are the steps to get input from two switches and switch on corresponding LEDs:

1. Connect the switches to the microcontroller: Connect two switches to the microcontroller. One switch should be connected to a digital pin, and the other should be connected to another digital pin on the microcontroller.

2. Connect the LEDs to the microcontroller: Connect two LEDs to the microcontroller. One LED should be connected to a digital pin, and the other should be connected to another digital pin on the microcontroller.

3. Set the pins for input and output: In the setup function of the code, set the pins for the switches as input and the pins for the LEDs as output.

```
void setup() {
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}
```

4. Read the state of the switches: In the loop function, read the state of the switches using the digitalRead function. If the switch is pressed, it will return a HIGH value, and if it is not pressed, it will return a LOW value.

```
void loop() {
  switch1State = digitalRead(switch1);
  switch2State = digitalRead(switch2);
}
```

5. Switch on the corresponding LED: Depending on the state of the switches, switch on the corresponding LED using the digitalWrite function. If the switch is pressed, set the corresponding LED pin to HIGH, and if it is not pressed, set the corresponding LED pin to LOW.

```
void loop() {
  switch1State = digitalRead(switch1);
  switch2State = digitalRead(switch2);

  if (switch1State == HIGH) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led1, LOW);
  }

  if (switch2State == HIGH) {
    digitalWrite(led2, HIGH);
  } else {
    digitalWrite(led2, LOW);
  }
}
```

6. Upload the code to the microcontroller: Finally, upload the code to the microcontroller using the Arduino software.

By following these steps, we can get input from two switches and switch on corresponding LEDs. This is a basic example of how to use switches and LEDs to control electronic devices.