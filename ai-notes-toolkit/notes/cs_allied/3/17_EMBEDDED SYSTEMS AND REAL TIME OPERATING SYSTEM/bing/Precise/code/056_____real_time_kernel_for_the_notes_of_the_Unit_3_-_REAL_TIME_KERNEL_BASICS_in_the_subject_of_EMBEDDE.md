### Unit 3 - REAL TIME KERNEL BASICS

A real-time kernel is software that manages the time of a microprocessor to ensure that time-critical events are processed as efficiently as possible. The use of a kernel simplifies the design of embedded systems because it allows the system to be divided into multiple independent elements called tasks.

Most kernels are written in C and require a small portion of code written in assembly language in order to adapt the kernel to different CPU architectures.

The real-time kernel is also known as kernel-rt or preempt-rt. The simplest way to identify a real-time kernel is to execute the `uname -r` command on the terminal, and then look for the `rt` keyword in the kernel version. If `rt` is missing, then the system uses the standard kernel.

The new real-time kernel serves extreme latency-dependent use cases and provides deterministic response times to service events. By meeting stringent preemption specifications, real-time is suitable across a broad range of verticals, from telco applications to dedicated devices in industrial automation and robotics.