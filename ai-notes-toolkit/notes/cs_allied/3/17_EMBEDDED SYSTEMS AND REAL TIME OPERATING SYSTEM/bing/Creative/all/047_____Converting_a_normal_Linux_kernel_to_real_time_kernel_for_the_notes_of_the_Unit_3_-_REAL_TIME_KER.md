# Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that can guarantee a deterministic response time to events, such as interrupts, system calls, or user inputs.
- A normal Linux kernel is not designed for real time applications, as it may incur unpredictable delays due to factors such as process scheduling, memory management, or locking mechanisms.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a set of patches that modify the kernel behavior and configuration to enable full preemption, priority inheritance, and high resolution timers.
- The steps to convert a normal Linux kernel to a real time kernel are as follows:

  1. Download the source code of the normal Linux kernel and the corresponding real time patches from the official websites or repositories.
  2. Apply the real time patches to the kernel source code using the patch command or a graphical tool such as git or quilt.
  3. Configure the kernel options using the make menuconfig or make xconfig command. In the config options, set the ‘Fully Preemptible kernel (RT)’ option . You may also adjust other options related to real time performance, such as CPU frequency scaling, tickless kernel, or CPU isolation.
  4. Build the kernel using the make command. You may need to install some dependencies, such as gcc, ncurses, or openssl, before building the kernel.
  5. Install the kernel using the make install command. This will copy the kernel image and modules to the appropriate directories and update the boot loader configuration.
  6. Reboot the system and select the real time kernel from the boot menu. You can verify that you are running the real time kernel by executing the uname -r command and looking for the rt keyword in the kernel version  .

- By converting a normal Linux kernel to a real time kernel, you can improve the responsiveness and predictability of your system for real time applications, such as audio or video processing, robotics, or industrial control. However, you may also encounter some trade-offs, such as increased overhead, reduced throughput, or compatibility issues with some drivers or modules. Therefore, you should test and benchmark your system before and after the conversion to ensure that it meets your requirements and expectations.