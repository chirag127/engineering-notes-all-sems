# CO2 Sensor Arduino

## Introduction

A CO2 sensor is a device that can measure the concentration of carbon dioxide (CO2) in the air. CO2 is a greenhouse gas that affects the climate and the quality of life on Earth. CO2 sensors can be used for various applications, such as monitoring indoor air quality, plant growth, fermentation, and environmental science experiments.

There are different types of CO2 sensors, such as electrochemical, infrared, and metal oxide. Each type has its own advantages and disadvantages, such as accuracy, sensitivity, response time, power consumption, and cost. One of the most common and affordable types of CO2 sensors is the MQ series, which uses a metal oxide semiconductor (MOS) to detect the presence of CO2.

Arduino is an open-source platform that consists of a microcontroller board and a software environment that allows users to program and control the board. Arduino can be used to interface with various sensors, actuators, and modules, such as LCD displays, motors, LEDs, and buttons. Arduino can also communicate with other devices, such as computers, smartphones, and other Arduino boards, using serial, Bluetooth, Wi-Fi, or radio frequency protocols.

In this topic, we will learn how to interface various CO2 sensors with Arduino or Raspberry Pi, and how to read and display the CO2 values. We will also learn some basic concepts and principles of CO2 sensing, such as calibration, compensation, and conversion.

## Learning Outcomes

By the end of this topic, you should be able to:

- K4: Explain the working principle and characteristics of different types of CO2 sensors.
- K5: Demonstrate how to connect and program CO2 sensors with Arduino or Raspberry Pi using various libraries and examples.

## Content

### 1. Working Principle and Characteristics of CO2 Sensors

#### 1.1 Electrochemical CO2 Sensors

- Electrochemical CO2 sensors use a chemical reaction between CO2 and an electrolyte to generate a small electric current that is proportional to the CO2 concentration.
- Electrochemical CO2 sensors have high accuracy, sensitivity, and selectivity, but they also have high power consumption, short lifespan, and need frequent calibration and maintenance.
- Electrochemical CO2 sensors are suitable for applications that require precise and continuous measurement of CO2, such as medical, industrial, and scientific fields.
- An example of an electrochemical CO2 sensor is the Gravity: Analog CO2 Gas Sensor (MG-811 Sensor) , which is compatible with Arduino and has a range of 0-10000 ppm.

#### 1.2 Infrared CO2 Sensors

- Infrared CO2 sensors use a light source and a detector to measure the absorption of infrared radiation by CO2 molecules in the air.
- Infrared CO2 sensors have low power consumption, long lifespan, and high stability, but they also have high cost, large size, and need temperature and humidity compensation.
- Infrared CO2 sensors are suitable for applications that require low-power and long-term measurement of CO2, such as smart home, HVAC, and agriculture fields.
- An example of an infrared CO2 sensor is the Adafruit SCD-30 - NDIR CO2 Temperature and Humidity Sensor , which is compatible with Arduino and has a range of 400-10000 ppm.

#### 1.3 Metal Oxide CO2 Sensors

- Metal oxide CO2 sensors use a heated metal oxide semiconductor (MOS) to detect the change in resistance caused by the adsorption and desorption of CO2 molecules on the surface of the MOS.
- Metal oxide CO2 sensors have low cost, small size, and fast response time, but they also have low accuracy, sensitivity, and selectivity, and need calibration and preheating.
- Metal oxide CO2 sensors are suitable for applications that require qualitative and indicative measurement of CO2, such as educational, hobby, and DIY fields.
- An example of a metal oxide CO2 sensor is the MQ-135 Air Quality Sensor , which is compatible with Arduino and has a range of 10-1000 ppm.

### 2. Interfacing CO2 Sensors with Arduino or Raspberry Pi

#### 2.1 Hardware Connections

- To interface a CO2 sensor with Arduino or Raspberry Pi, you need to connect the sensor to the board using jumper wires and a breadboard. The sensor may have different pins depending on the type and model, but the most common ones are VCC, GND, AOUT, and DOUT.
- VCC is the power supply pin, which needs to be connected to