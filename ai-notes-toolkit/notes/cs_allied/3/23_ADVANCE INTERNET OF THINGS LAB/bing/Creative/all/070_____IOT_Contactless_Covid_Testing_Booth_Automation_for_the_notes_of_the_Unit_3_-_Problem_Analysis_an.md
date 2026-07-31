# IOT Contactless Covid Testing Booth Automation

## Introduction

- Covid-19 is a highly contagious disease that has caused a global pandemic.
- Covid testing is a key measure to control the spread of the virus and identify infected individuals.
- Covid testing booths are designed to provide a safe and isolated environment for collecting samples from suspected cases.
- However, the conventional testing process involves manual registration of the person's details, contact with the health workers, and potential exposure to the virus.
- Therefore, there is a need for an advanced system that can automate and contactless the covid testing process using IoT technology.

## Problem Analysis

- The main problem of the conventional covid testing process is the risk of cross-infection and human error.
- The manual registration of the person's details is time-consuming, prone to mistakes, and requires physical contact with the paper or device.
- The health workers who collect the samples have to wear personal protective equipment (PPE) and follow strict protocols to avoid contamination.
- The samples have to be transported and stored properly to ensure their validity and quality.
- The test results have to be communicated to the person and the authorities in a timely and accurate manner.

## Designing a Solution

- The proposed solution is to design a completely automated and contactless covid testing booth system using IoT technology.
- The system consists of the following components:
  - An RFID reader and tag to identify and register the person's details.
  - A microcontroller to control the booth operations and communicate with the cloud server.
  - A MATLAB program to analyze the person's face and temperature using a camera and a thermal sensor.
  - A GSM modem to send SMS alerts to the person and the authorities.
  - A robotic arm to collect the nasal swab sample from the person and place it in a container.
  - A barcode scanner and printer to label and track the sample.
  - A cloud server to store and process the data and test results.
- The system works as follows:
  - The person enters the booth and scans their RFID tag to register their details.
  - The camera and the thermal sensor capture the person's face and temperature and send them to the MATLAB program for analysis.
  - If the person's face is detected and their temperature is normal, the system proceeds to the sample collection stage.
  - If the person's face is not detected or their temperature is high, the system sends an SMS alert to the person and the authorities and terminates the process.
  - The robotic arm moves to the person's nose and collects the swab sample and places it in a container.
  - The barcode scanner and printer generate and print a barcode label for the sample and attach it to the container.
  - The container is ejected from the booth and ready for transportation and storage.
  - The test results are obtained from the cloud server and sent to the person and the authorities via SMS.
  - The booth is sanitized and ready for the next person.