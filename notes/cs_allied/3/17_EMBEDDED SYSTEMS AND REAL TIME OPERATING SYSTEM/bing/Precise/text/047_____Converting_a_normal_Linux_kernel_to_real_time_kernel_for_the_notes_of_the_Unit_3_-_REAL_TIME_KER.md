### Converting a normal Linux kernel to real time kernel for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. A real-time kernel is a kernel that provides deterministic response times to events and supports real-time applications.
2. The Linux kernel can be converted into a real-time kernel by applying a set of patches known as the PREEMPT_RT patch set.
3. The PREEMPT_RT patch set modifies the Linux kernel to reduce the maximum latency of the kernel and improve its responsiveness to real-time events.
4. To convert a normal Linux kernel to a real-time kernel, the following steps can be followed:
    1. Download the latest version of the Linux kernel source code and the corresponding PREEMPT_RT patch set.
    2. Apply the PREEMPT_RT patch set to the Linux kernel source code.
    3. Configure the kernel with the `make menuconfig` command and enable the `CONFIG_PREEMPT_RT` option.
    4. Build the kernel with the `make` command and install it with the `make install` command.
    5. Reboot the system with the new real-time kernel.
5. After converting the Linux kernel to a real-time kernel, the system should be able to support real-time applications with deterministic response times. However, it is important to note that the performance of the system may be affected and some tuning may be required to achieve the desired performance.