### Converting a normal Linux kernel to real time kernel

1. **Download the patch**: The first step in converting a normal Linux kernel to a real-time kernel is to download the real-time patch from the official website of the Linux kernel.
2. **Apply the patch**: Once the patch is downloaded, it needs to be applied to the kernel source code. This can be done using the `patch` command.
3. **Configure the kernel**: After the patch has been applied, the kernel needs to be configured to enable the real-time features. This can be done using the `make menuconfig` command.
4. **Compile the kernel**: Once the kernel has been configured, it needs to be compiled. This can be done using the `make` command.
5. **Install the kernel**: After the kernel has been compiled, it needs to be installed. This can be done using the `make install` command.
6. **Update the bootloader**: The final step is to update the bootloader to use the new real-time kernel. This can be done by editing the bootloader configuration file and adding an entry for the new kernel.

These are the basic steps involved in converting a normal Linux kernel to a real-time kernel. It is important to note that the exact steps may vary depending on the specific Linux distribution and version being used. It is always a good idea to consult the documentation for the specific distribution and version to ensure that the process is carried out correctly.