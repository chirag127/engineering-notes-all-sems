# Data Transfer Schemes

Data transfer schemes are the methods through which data can be transferred between the units of a microprocessor system, such as the CPU, memory, and I/O devices. Data transfer schemes are important for the efficient and smooth operation of the system. There are three main types of data transfer schemes:

- Programmed I/O Data Transfer
- Interrupt Driven Data Transfer
- Direct Memory Access (DMA) Data Transfer

## Programmed I/O Data Transfer

Programmed I/O Data Transfer is a simple and basic method of data transfer. In this scheme, the data transfer is controlled by a program that resides in the memory and is executed by the CPU. The CPU initiates and monitors the data transfer between the memory and the I/O device by using instructions and registers. This scheme is used when the speed of data transfer is not critical and the amount of data to be transferred is small. The advantages of this scheme are:

- It is easy to implement and understand.
- It does not require any additional hardware or circuitry.

The disadvantages of this scheme are:

- It consumes a lot of CPU time and resources, as the CPU has to constantly check the status of the I/O device and perform the data transfer.
- It reduces the performance of the system, as the CPU cannot perform any other task while the data transfer is in progress.

## Interrupt Driven Data Transfer

Interrupt Driven Data Transfer is an improved method of data transfer that overcomes some of the drawbacks of the programmed I/O data transfer. In this scheme, the data transfer is initiated by the I/O device, which sends an interrupt signal to the CPU when it is ready to send or receive data. The CPU then temporarily suspends its current task and executes an interrupt service routine (ISR) that performs the data transfer between the memory and the I/O device. After the data transfer is completed, the CPU resumes its previous task. This scheme is used when the speed of data transfer is moderate and the amount of data to be transferred is variable. The advantages of this scheme are:

- It reduces the CPU involvement and overhead, as the CPU only performs the data transfer when it is requested by the I/O device.
- It improves the performance of the system, as the CPU can perform other tasks while the I/O device is waiting for data.

The disadvantages of this scheme are:

- It requires additional hardware and software to handle the interrupt signals and the ISR.
- It may cause priority and synchronization issues, as multiple I/O devices may request data transfer at the same time.

## Direct Memory Access (DMA) Data Transfer

Direct Memory Access (DMA) Data Transfer is the most advanced and efficient method of data transfer. In this scheme, the data transfer is performed directly between the memory and the I/O device, without involving the CPU. A special hardware device called the DMA controller (DMAC) is used to control and coordinate the data transfer. The CPU only initiates the data transfer by sending the parameters such as the source and destination addresses, the amount of data, and the mode of transfer to the DMAC. The DMAC then takes over the data transfer and sends an interrupt signal to the CPU when the data transfer is completed. The CPU then resumes its normal operation. This scheme is used when the speed of data transfer is high and the amount of data to be transferred is large. The advantages of this scheme are:

- It frees the CPU from the data transfer task, as the CPU only sets up the data transfer and does not participate in it.
- It maximizes the performance of the system, as the CPU and the I/O device can operate in parallel.

The disadvantages of this scheme are:

- It requires a complex and expensive hardware device (the DMAC) to perform the data transfer.
- It may cause memory contention and bus arbitration issues, as the DMAC and the CPU may access the memory and the bus at the same time.