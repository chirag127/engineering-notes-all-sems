# CO2 Sensor Arduino

## Introduction

A CO2 sensor is a device that can measure the concentration of carbon dioxide (CO2) in the air. CO2 is a greenhouse gas that affects the climate and the quality of life. Measuring CO2 levels can be useful for various applications, such as monitoring indoor air quality, plant growth, fermentation, and environmental science.

There are different types of CO2 sensors, such as electrochemical, infrared, and metal oxide. Each type has its own advantages and disadvantages, such as accuracy, cost, power consumption, and response time. In this topic, we will focus on interfacing some common CO2 sensors with Arduino or Raspberry Pi, which are popular microcontroller platforms for hobbyists and makers.

## Interfacing CO2 Sensors with Arduino

Arduino is an open-source hardware and software platform that can be used to create interactive electronic projects. Arduino boards have digital and analog input/output pins that can be connected to various sensors, actuators, and modules. Arduino boards can be programmed using the Arduino IDE, which is a cross-platform application that supports C/C++ languages.

To interface a CO2 sensor with Arduino, we need to consider the following aspects:

- The output signal of the CO2 sensor: Some CO2 sensors provide analog voltage output, while others provide digital serial output. Depending on the output signal, we need to connect the sensor to the appropriate pins on the Arduino board and use the corresponding libraries and functions to read the data.
- The power supply of the CO2 sensor: Some CO2 sensors require 5V power supply, while others require 3.3V or lower. Depending on the power requirement, we need to connect the sensor to the appropriate power pins on the Arduino board and use a voltage regulator or a level shifter if needed.
- The calibration of the CO2 sensor: Some CO2 sensors require calibration before use, while others are pre-calibrated or self-calibrating. Depending on the calibration method, we need to follow the instructions provided by the sensor manufacturer and use the appropriate code and tools to calibrate the sensor.

In the following sections, we will provide some examples of interfacing different CO2 sensors with Arduino.

### Example 1: MQ-135 Sensor

The MQ-135 sensor is a low-cost metal oxide sensor that can detect various gases, including CO2, ammonia, benzene, alcohol, and smoke. The sensor has an analog voltage output that varies with the concentration of the gas. The sensor requires 5V power supply and a heating time of about 20 minutes before use. The sensor also needs to be calibrated in fresh air to obtain the baseline voltage.

To interface the MQ-135 sensor with Arduino, we need to connect the following pins:

- VCC pin of the sensor to the 5V pin of the Arduino board
- GND pin of the sensor to the GND pin of the Arduino board
- AOUT pin of the sensor to an analog input pin of the Arduino board, such as A0

We also need to add a 10K ohm resistor between the AOUT and GND pins of the sensor, as shown in the following diagram:

```
    +5V
     |
     |
    [ ] 10K ohm
     |
     +----- AOUT
     |
    [ ] MQ-135
     |
     +----- GND
     |
    GND
```

To read the analog voltage from the sensor, we can use the analogRead() function in the Arduino code, as shown in the following example:

```c
// Define the analog input pin
#define MQ135_PIN A0

// Define the baseline voltage of the sensor in fresh air
#define MQ135_BASELINE 0.5

// Define the conversion factor from voltage to ppm
#define MQ135_FACTOR 116.6020682

// Define the exponent factor from voltage to ppm
#define MQ135_EXPONENT -2.769034857

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read the analog voltage from the sensor
  int mq135_value = analogRead(MQ135_PIN);

  // Convert the analog value to voltage
  float mq135_voltage = mq135_value * (5.0 / 1023.0);

  // Calculate the ratio of the sensor voltage to the baseline voltage
  float mq135_ratio = mq135_voltage / MQ135_BASELINE;

  // Calculate the CO2 concentration in ppm using the formula
  float mq135_ppm = MQ135_FACTOR * pow(mq135_ratio, MQ135

```
