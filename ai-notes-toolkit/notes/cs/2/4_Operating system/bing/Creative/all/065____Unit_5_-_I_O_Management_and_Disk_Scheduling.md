# Unit 5 - I/O Management and Disk Scheduling

## Introduction

- I/O management and disk scheduling are two important aspects of operating systems that deal with the interaction between the CPU and the external devices, such as disks, terminals, printers, etc.
- I/O management is responsible for providing a uniform interface for different types of I/O devices, handling I/O requests from processes, buffering and caching data, and performing error handling and recovery.
- Disk scheduling is a specific type of I/O management that focuses on optimizing the performance of disk drives, which are one of the slowest and most frequently used I/O devices in a computer system.
- Disk scheduling algorithms aim to reduce the seek time, rotational latency, and transfer time of disk I/O operations, by ordering the pending requests in a queue according to some criteria.

## I/O Devices

- I/O devices can be classified into three categories based on their characteristics and functions:
  - Human-readable devices: These are devices that are suitable for communicating with the computer user, such as printers, terminals, video displays, keyboards, mice, etc. They typically have low data transfer rates and require formatted data.
  - Machine-readable devices: These are devices that are suitable for communicating with other machines or systems, such as disk drives, tape drives, sensors, actuators, etc. They typically have high data transfer rates and require unformatted data.
  - Communication devices: These are devices that are suitable for transmitting data over a network, such as modems, network adapters, routers, etc. They typically have varying data transfer rates and require data to be formatted according to some protocol.

## I/O Modules

- I/O modules are hardware components that connect the CPU and the main memory with the I/O devices. They perform the following functions:
  - Control and timing: They synchronize the data transfer between the CPU and the I/O device, using signals and commands.
  - Communication with the CPU: They exchange information with the CPU, such as status, commands, data, addresses, etc., using buses or channels.
  - Communication with the I/O device: They interface with the I/O device, using device-specific protocols and signals.
  - Data buffering: They temporarily store data that is being transferred between the CPU and the I/O device, using registers or memory.
  - Error detection and handling: They detect and correct errors that may occur during the data transfer, using techniques such as parity checking, checksum, etc.

## I/O Techniques

- There are three main techniques for performing I/O operations between the CPU and the I/O devices:
  - Programmed I/O: The CPU executes a program that contains instructions to read or write data from or to an I/O device. The CPU polls the status of the I/O device until it is ready, then transfers one data item at a time. The CPU is busy-waiting during the I/O operation and cannot perform other tasks.
  - Interrupt-driven I/O: The CPU executes a program that contains instructions to initiate an I/O operation, then continues with other tasks. When the I/O device is ready, it sends an interrupt signal to the CPU, which suspends the current program and executes an interrupt handler routine to transfer one or more data items. The CPU resumes the original program after the I/O operation is completed.
  - Direct memory access (DMA): The CPU executes a program that contains instructions to initiate an I/O operation, then continues with other tasks. The I/O device transfers data directly to or from the main memory, without involving the CPU, using a special hardware component called the DMA controller. The DMA controller sends an interrupt signal to the CPU when the I/O operation is completed.