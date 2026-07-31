### Real Time Kernel

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible .
- A real-time kernel is designed to provide low latency, consistent response time, and determinism .
- A real-time kernel is not necessarily superior or better than a standard kernel, but it meets different business or system requirements.
- A real-time kernel is also known as kernel-rt or preempt-rt.
- A real-time kernel can be identified by executing the `uname -r` command and looking for the `rt` keyword in the kernel version.
- A real-time kernel can be installed by downloading the ISO image from the Red Hat customer portal or by enabling the rhel-7-server-rt repository and performing a group installation.
- A real-time kernel requires some dependent packages, such as rt-setup, rt-tests, tuned-profiles-realtime, and kernel-rt-doc.
- A real-time kernel can be configured by using the `tuned-adm` command and selecting the appropriate profile.
- A real-time kernel can be tested by using the `cyclictest` command and observing the latency histogram.
- A real-time kernel can be optimized by tuning various parameters, such as CPU isolation, IRQ affinity, memory locking, and scheduler policies.