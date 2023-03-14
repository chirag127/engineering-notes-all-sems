## Unit 2 - Software Requirement Specifications (SRS)

- A software requirement specification (SRS) is a document that describes what the software will do and how it will be expected to perform .
- It also describes the functionality the product needs to fulfill the needs of all stakeholders (business, users) .
- An SRS is a blueprint or roadmap for the software development process .
- An SRS helps to create, organize, and share requirements among the development team and other stakeholders .
- An SRS provides a single source of truth that every team involved in development will follow  .
- An SRS helps to ensure that each requirement is met and that the product meets the expectations of the stakeholders  .
- An SRS can also help to make decisions on the product’s lifecycle, such as when to retire an obsolete feature .
- An SRS is a living document that can be updated and validated as the product evolves .

A basic SRS document outline has four parts :

- An introduction: This section provides an overview of the product, its purpose, scope, objectives, and assumptions. It also defines the terms and acronyms used in the document and identifies the intended audience and stakeholders.
- System and functional requirements: This section describes the system and its features in detail. It specifies the inputs, outputs, processes, and behaviors of the system. It also defines the use cases, scenarios, and user stories that illustrate how the system will be used and what value it will provide.
- External interface requirements: This section describes the interfaces between the system and other systems, devices, or users. It specifies the communication protocols, data formats, user interfaces, hardware interfaces, and software interfaces of the system.
- Non-functional requirements: This section describes the quality attributes, constraints, and assumptions that affect the system’s performance, reliability, security, usability, maintainability, and portability. It also defines the standards, regulations, and compliance requirements that the system must adhere to.

A mnemonic to remember the four parts of an SRS document is **I SEE NON**:

- **I**ntroduction
- **S**ystem and functional requirements
- **E**xternal interface requirements
- **E**xternal interface requirements
- **N**on-functional requirements
- **O**n
- **N**on-functional requirements

An example of an SRS document for a simple calculator application is given below:

# Software Requirements Specification for Calculator Application

## 1. Introduction

### 1.1 Purpose

The purpose of this document is to provide a detailed description of the requirements for the calculator application. This document will define the scope, features, functionality, and quality attributes of the application. This document will also serve as a communication tool between the development team and the stakeholders.

### 1.2 Scope

The calculator application is a simple software that allows users to perform basic arithmetic operations, such as addition, subtraction, multiplication, and division. The application will also support the use of parentheses and decimal numbers. The application will have a graphical user interface (GUI) that displays the input and output of the calculations. The application will run on Windows, Linux, and Mac operating systems.

### 1.3 Definitions, Acronyms, and Abbreviations

- GUI: Graphical User Interface
- OS: Operating System
- SRS: Software Requirements Specification

### 1.4 References

- IEEE. IEEE Std 830-1998 IEEE Recommended Practice for Software Requirements Specifications. IEEE Computer Society, 1998.
- ISO. ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering. International Organization for Standardization, 2018.

### 1.5 Overview

The rest of this document is organized as follows:

- Section 2 describes the system and functional requirements of the calculator application.
- Section 3 describes the external interface requirements of the calculator application.
- Section 4 describes the non-functional requirements of the calculator application.

## 2. System and Functional Requirements

### 2.1 System Features

The calculator application will have the following features:

- The application will allow users to enter numbers and operators using the keyboard or the mouse.
- The application will display the input and output of the calculations on the GUI.
- The application will support the following arithmetic operators: +, -, *, /, (, and ).
- The application will follow the