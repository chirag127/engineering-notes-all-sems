 Here are the notes in markdown format without any emojis or external links:

### Real Time Kernel

- A real-time operating system (RTOS) is an operating system (OS) intended to serve real-time applications that process data as it comes in, typically without buffer delays.
- Real-time operating systems are used when lack of response can cause a system failure or damage. Real-time applications include:

› Industrial control systems
› Robotics
› Space probes
› Life-critical systems

- Features of a real-time kernel:

› Determinism: Predictable response to events.
› Strict priorities: Some processes much have precedence over others.
› Multitasking: Ability to execute multiple tasks concurrently with constraints.
› Efficiency: Fast context switches, minimal latency, optimize for speed.
› Small footprint: Take up minimal memory and processing power.
› Resource locking: Prevent deadlocks and ensure resources are allocated properly.

- Some popular real-time kernels:

› FreeRTOS
› VxWorks
› QNX
› Linux (with real-time extensions/patches)

- Applications of real-time kernels:

› Automotive systems (braking, engine control)
› Factory automation and robotics
› Medical devices (heart monitors)
› Avionics and space systems
› Telecommunications systems

- The key challenges with real-time systems are:

› Guaranteeing deadlines will be met
› Accounting for worst-case scenarios
› Preventing unexpected delays or "jitter"
› Handling priorities and resource conflicts
› Programming predictably without delays or bugs