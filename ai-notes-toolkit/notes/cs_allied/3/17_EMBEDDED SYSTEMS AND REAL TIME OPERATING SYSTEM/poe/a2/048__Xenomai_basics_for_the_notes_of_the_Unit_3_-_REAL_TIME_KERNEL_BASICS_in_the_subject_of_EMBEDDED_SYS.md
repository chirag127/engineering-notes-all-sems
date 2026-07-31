 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Xenomai basics for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. Xenomai is a real-time development framework cooperating with the Linux kernel. It turns the Linux kernel into a POSIX-compliant RTOS.
2. Xenomai provides two execution contexts -
	- SVC (Supervisor Calls) context - Has higher priority than Linux and is used for real-time tasks.
	- Secondary mode - Runs Linux tasks and has lower priority than SVC mode.
3. Xenomai uses a dual kernel approach -
	- The primary kernel is the standard Linux kernel which takes care of non real-time tasks.
	- The secondary kernel is the real-time kernel (based on RTDM) which runs real-time tasks.
4. The Xenomai architecture has the following main components -
	- Xenomai core - The real-time core which extends Linux.
	- RTDM - The real-time driver model.
	- Real-time applications - The user-space real-time applications.
	- Services - Additional services such as real-time networking.
5. The benefits of Xenomai are -
	- Uses the Linux ecosystem and drivers.
	- Supports multiprocessor systems.
	- Provides resource protection between real-time and non-real-time tasks.
	- Supports a large number of architectures.
	- Has a small footprint.

Does this look okay? Let me know if you would like me to modify or expand the content in any way.