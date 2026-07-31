# Raspberry Pi based Weather Reporting Over IOT

## Introduction

- The Internet of Things (IoT) is a network of physical objects that can communicate and exchange data over the internet.
- IoT applications can be used for various purposes, such as smart home, smart city, smart agriculture, smart health, etc.
- One of the applications of IoT is weather monitoring and reporting, which can provide accurate and real-time information about the environmental conditions of a specific location.
- Weather monitoring and reporting can be useful for various sectors, such as agriculture, tourism, transportation, disaster management, etc.

## Objective

- The objective of this project is to design and implement a Raspberry Pi based weather reporting system over IoT.
- The system can monitor and update weather parameters, such as temperature, humidity, and rainfall, using different sensors and display them on an LCD screen and also on a web page.
- The system can also send alerts to the user via email or SMS if the weather conditions exceed a certain threshold.

## Components

- The main components of the system are:

  - Raspberry Pi: It is a single-board computer that acts as the central processing unit and the web server of the system. It can communicate with the sensors and the LCD using GPIO pins and with the internet using Wi-Fi or Ethernet.
  - DHT11 sensor: It is a digital temperature and humidity sensor that can measure the ambient temperature and relative humidity with high accuracy and reliability. It can communicate with the Raspberry Pi using a single-wire protocol.
  - Rain sensor: It is an analog sensor that can detect the presence and intensity of rainfall by measuring the resistance between two conductive tracks on a PCB. It can communicate with the Raspberry Pi using an analog-to-digital converter (ADC) module.
  - LCD screen: It is a 16x2 character LCD that can display the weather parameters on the system. It can communicate with the Raspberry Pi using an I2C interface.
  - IoT Gecko: It is a cloud-based platform that can provide web services for IoT applications. It can store and visualize the weather data collected by the system and also send alerts to the user via email or SMS.

## Working

- The working of the system is as follows:

  - The DHT11 sensor and the rain sensor are connected to the Raspberry Pi using GPIO pins and an ADC module respectively.
  - The LCD screen is connected to the Raspberry Pi using an I2C interface.
  - The Raspberry Pi is connected to the internet using Wi-Fi or Ethernet.
  - The Raspberry Pi reads the sensor data periodically and displays them on the LCD screen.
  - The Raspberry Pi also sends the sensor data to the IoT Gecko platform using an HTTP request.
  - The IoT Gecko platform stores and visualizes the sensor data on a web page that can be accessed by the user from any device.
  - The IoT Gecko platform also sends alerts to the user via email or SMS if the sensor data exceeds a certain threshold that can be set by the user.

## Advantages

- The advantages of the system are:

  - It is cost-effective and has low power consumption.
  - It is easy to carry around and work with.
  - It provides accurate and real-time weather information of a specific location.
  - It can be useful for various sectors, such as agriculture, tourism, transportation, disaster management, etc.