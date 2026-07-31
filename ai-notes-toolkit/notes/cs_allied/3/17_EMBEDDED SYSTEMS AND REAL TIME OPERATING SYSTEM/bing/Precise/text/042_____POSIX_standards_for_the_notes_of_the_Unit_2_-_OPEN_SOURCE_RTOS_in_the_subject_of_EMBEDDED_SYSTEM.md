### POSIX standards for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- POSIX is the acronym for Portable Operating System Interface.
- It is a proposed operating system interface standard based on the popular UNIX operating system.
- Its main goal is to support application portability at the source-code level.
- POSIX is an IEEE standard and is published by The Open Group.
- Using the POSIX standard for your application development frees you from having to rely on proprietary documentation from a single-source vendor.
- Many larger microprocessor (MPU) designs are built using embedded Linux.
- Real-time operating systems (RTOSes) are used only in cases where hard real-time performance is required.
- Regardless of the MPU operating system – either embedded Linux or an MPU RTOS – all use POSIX as the standard for application programming interface (API) calls.
- Its real-time extension (RT-POSIX) is one of the most successful standards in the area of real-time systems, adopted by all major kernel vendors.
- Since NuttX is a POSIX RTOS, you can write an application in a POSIX operating system such as Linux or MacOS and validate it and compile it to run on NuttX without learning a new API.
- NuttX also has many parallel subsystems to Linux.