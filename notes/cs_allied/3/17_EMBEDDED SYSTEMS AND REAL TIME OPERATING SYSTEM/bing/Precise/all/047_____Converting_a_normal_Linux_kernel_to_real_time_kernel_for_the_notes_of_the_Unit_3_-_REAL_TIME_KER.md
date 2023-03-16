# Converting a normal Linux kernel to real time kernel

1. The first step in converting a normal Linux kernel to a real-time kernel is to download and install the real-time patch. This patch is available from the Linux kernel archives and can be applied to the source code of the Linux kernel.

2. Once the patch is installed, the kernel must be recompiled with the real-time configuration options enabled. This can be done by running the `make menuconfig` command and selecting the appropriate options under the "Processor type and features" and "Real-time sub-system" menus.

3. After the kernel has been recompiled, it must be installed and the system must be rebooted in order to use the new real-time kernel.

4. It is important to note that not all hardware and software configurations are compatible with real-time kernels. It may be necessary to make additional changes to the system in order to ensure that it can operate correctly with a real-time kernel.

5. Additionally, it is important to carefully test and validate the system after converting to a real-time kernel to ensure that it meets the desired performance and reliability requirements.

6. In summary, converting a normal Linux kernel to a real-time kernel involves installing the real-time patch, recompiling the kernel with the appropriate configuration options, and making any necessary changes to the system to ensure compatibility and correct operation. It is important to carefully test and validate the system after conversion to ensure that it meets the desired performance and reliability requirements.