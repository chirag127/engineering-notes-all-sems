### Converting a normal Linux kernel to real time kernel

In this unit, we will learn about the basics of real-time kernel and how to convert a normal Linux kernel to a real-time kernel. Here are the steps to convert a normal Linux kernel to a real-time kernel:

1. Download the latest stable version of the Linux kernel from the official website of Linux.

2. Extract the downloaded file using the following command:

    ```
    tar -xvf linux-x.x.x.tar.xz
    ```

    Replace "x.x.x" with the version number of the downloaded kernel.

3. Configure the kernel using the following command:

    ```
    cd linux-x.x.x
    make menuconfig
    ```

    This will open a configuration window, where you can select the real-time option.

4. In the configuration window, navigate to "General setup" > "Kernel Features" > "Preemption Model" and select the "Fully Preemptible Kernel (RT)" option.

5. Save the configuration and exit the window.

6. Compile the kernel using the following command:

    ```
    make -jX
    ```

    Replace "X" with the number of cores in your system.

7. Install the kernel using the following command:

    ```
    make install
    ```

8. Update the bootloader to load the new kernel at startup. This step may vary depending on the bootloader used in your system.

9. Reboot your system to start using the real-time kernel.

By following these steps, you can convert a normal Linux kernel to a real-time kernel and take advantage of its features for real-time applications.