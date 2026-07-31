### Resident monitor

- A resident monitor is a type of system software program that was used in many early computers from the 1950s to 1970s  .
- It can be considered a precursor to the operating system  .
- The name is derived from a program which is always present in the computer's memory, thus being "resident"  .
- The resident monitor's main functions are:
  - To quickly load the next task to be executed in a batch environment.
  - To control the instructions and perform all necessary functions.
  - To work as a job sequencer that schedules the jobs and sends them to the processor.
  - To load the programs one by one into the main memory according to their sequences.
- The resident monitor is usually divided into two parts:
  - The transient part, which is loaded into the memory when needed and contains the user programs and data .
  - The resident part, which is always in the memory and contains the monitor routines and data .
- The resident monitor uses a technique called overlaying, which allows the transient part to be swapped in and out of the memory as needed .
- The resident monitor also uses a technique called relocation, which allows the programs to be loaded into any available memory location without changing their addresses .