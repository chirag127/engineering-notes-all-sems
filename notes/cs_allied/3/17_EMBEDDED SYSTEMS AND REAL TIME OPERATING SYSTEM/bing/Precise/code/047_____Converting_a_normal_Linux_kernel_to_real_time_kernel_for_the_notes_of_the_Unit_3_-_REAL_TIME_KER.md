### Converting a normal Linux kernel to real time kernel for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. A real-time kernel is a kernel that provides real-time capabilities, such as deterministic response times and the ability to prioritize tasks.
2. The Linux kernel can be converted into a real-time kernel by applying a set of patches known as the PREEMPT_RT patch set.
3. The PREEMPT_RT patch set modifies the Linux kernel to reduce the maximum latency of the kernel and to make the scheduling of tasks more deterministic.
4. To convert a normal Linux kernel to a real-time kernel, the following steps can be followed:
    1. Download the latest version of the Linux kernel source code and the corresponding PREEMPT_RT patch set.
    2. Apply the PREEMPT_RT patch set to the Linux kernel source code.
    3. Configure the kernel to enable the real-time options.
    4. Compile the kernel and install it on the target system.
5. After the real-time kernel is installed, the system can be configured to use real-time scheduling policies and priorities to ensure that real-time tasks are executed with the desired level of determinism.