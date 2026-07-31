# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

When working with microcontroller-based projects, it is often necessary to control an LED with a specific on and off time cycle. In this tutorial, we will learn how to flash an LED at a given on time and off time cycle, where the two times are taken from a file.

## Required Components
- Arduino Uno or any other compatible board
- LED
- 220 ohm resistor
- Breadboard
- Jumper wires

## Circuit Diagram
![Circuit Diagram](https://i.imgur.com/D6HE9U6.png)

## Code Explanation
The code for this project is fairly simple. We will be reading the on and off times from a file named "times.txt" and then using those values to control the LED.

First, we declare the pins for the LED and set them as outputs:
```c
int ledPin = 13;
void setup() {
  pinMode(ledPin, OUTPUT);
}
```

Next, we open the file and read the on and off times:
```c
File file = SD.open("times.txt");
int onTime = file.parseInt();
int offTime = file.parseInt();
```

We then use a loop to continuously turn the LED on and off based on the on and off times read from the file:
```c
while (true) {
  digitalWrite(ledPin, HIGH);
  delay(onTime);
  digitalWrite(ledPin, LOW);
  delay(offTime);
}
```

## Conclusion
Controlling an LED with a specific on and off time cycle is a common task in microcontroller-based projects. By reading the values from a file, we can easily modify the on and off times without having to modify the code. This can be useful when experimenting with different timings or when using the same code for multiple projects with different timing requirements.