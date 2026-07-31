### Using Libraries for Programming the Arduino

Libraries are an integral part of programming the Arduino board. They contain pre-written code that can be easily imported into your program, saving you time and effort. By using libraries, you can focus on the main logic of your program instead of writing code for every little function. In this unit, we will discuss how to use libraries for programming the Arduino.

#### What are Libraries?

A library is a collection of pre-written code that can be used in your program. It contains functions that you can call to perform specific tasks, such as controlling motors or reading data from sensors. Libraries can be downloaded from the internet or created by other users. They are written in C++ language and can be easily imported into your Arduino sketch.

#### How to use Libraries in your Program?

To use a library in your program, you first need to include it in your code. This can be done by using the `#include` statement at the beginning of your program. For example, to include the `Servo` library, you would use the following code:

```
#include <Servo.h>
```

Once you have included the library, you can start using its functions in your program. For example, to control a servo motor using the `Servo` library, you would create a `Servo` object and use its functions to set the motor position. Here is an example code:

```
#include <Servo.h>

Servo myservo; // create a servo object

void setup() {
  myservo.attach(9); // attaches the servo on pin 9 to the servo object
}

void loop() {
  myservo.write(90); // sets the servo position to 90 degrees
  delay(1000); // waits for 1 second
  myservo.write(0); // sets the servo position to 0 degrees
  delay(1000); // waits for 1 second
}
```

#### Popular Libraries for Arduino

There are many libraries available for programming the Arduino, each with its own set of functions and capabilities. Here are some of the popular libraries that you can use:

- `Servo`: This library is used to control servo motors.
- `LiquidCrystal`: This library is used to control LCD displays.
- `Wire`: This library is used to communicate with I2C devices.
- `Adafruit_Sensor`: This library is used to read data from sensors.
- `WiFi`: This library is used to connect to Wi-Fi networks.

#### Conclusion

Using libraries is an essential part of programming the Arduino board. They can save you time and effort by providing pre-written code for specific functions. By including libraries in your program, you can focus on the main logic of your program and create more efficient and effective code.