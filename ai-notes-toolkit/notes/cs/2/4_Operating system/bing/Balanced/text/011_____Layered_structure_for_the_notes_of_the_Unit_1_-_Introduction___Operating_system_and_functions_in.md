### Layered structure for the notes of the Unit 1 - Introduction : Operating system and functions in the subject of Operating system

- An operating system (OS) is a software that manages the hardware and software resources of a computer system and provides common services for the execution of various application programs.
- An OS can be viewed as a layered structure, where each layer provides a set of functions and services to the higher-level layers and uses the functions and services of the lower-level layers.
- The layered structure of an OS can be classified into four main categories: user interface, system services, system calls, and hardware abstraction layer.

#### User interface
- The user interface is the layer that interacts with the users and allows them to access the OS functions and services.
- The user interface can be graphical (GUI) or command-line (CLI) based, depending on the preference and needs of the users.
- The user interface provides features such as windows, menus, icons, buttons, keyboards, mice, touchscreens, etc. for GUI, and commands, arguments, options, prompts, etc. for CLI.
- The user interface also handles the input and output devices, such as monitors, printers, scanners, speakers, etc.

#### System services
- The system services are the layer that provides the core functionality of the OS, such as process management, memory management, file system management, device management, security, networking, etc.
- The system services are responsible for creating, scheduling, terminating, and synchronizing processes, allocating and deallocating memory, organizing and accessing files and directories, controlling and communicating with devices, enforcing access control and authentication, enabling data transmission and reception, etc.
- The system services are implemented as a set of system programs or daemons that run in the background and perform various tasks.

#### System calls
- The system calls are the layer that provides the interface between the system services and the application programs.
- The system calls are the requests made by the application programs to the OS to use the system services and resources.
- The system calls are usually implemented as a library of functions that are invoked by the application programs using a specific syntax and semantics.
- The system calls can be classified into five main categories: process control, file manipulation, device manipulation, information maintenance, and communication.

#### Hardware abstraction layer
- The hardware abstraction layer (HAL) is the layer that provides the interface between the system calls and the hardware devices.
- The HAL is responsible for hiding the details and differences of the hardware devices from the higher-level layers and presenting a uniform and consistent view of the hardware to the OS.
- The HAL also handles the device drivers, which are the software components that communicate with the hardware devices and translate the system calls into device-specific commands.
- The HAL enables the OS to support a variety of hardware devices and platforms without modifying the higher-level layers.