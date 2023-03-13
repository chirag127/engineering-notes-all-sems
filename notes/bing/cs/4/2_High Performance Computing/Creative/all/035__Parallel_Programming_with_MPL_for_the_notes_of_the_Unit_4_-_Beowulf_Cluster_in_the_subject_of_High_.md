### Parallel Programming with MPL for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- A Beowulf cluster is a private network of computers (usually Alpha or Intel boxes) running a stripped down version of Linux .
- Acting together, with a parallel programming API like MPI or PVM, the cluster can function like a single massively parallel computer.
- MPI (Message Passing Interface) and PVM (Parallel Virtual Machine) are commonly used parallel processing libraries that permit the programmer to divide a task among a group of networked computers, and collect the results of processing .
- MPI is a standard for message-passing communication between processes in a parallel program. It provides a set of routines that can be used to send and receive messages, synchronize processes, broadcast data, and perform collective operations .
- PVM is a software system that enables a collection of heterogeneous computers to be used as a coherent and flexible concurrent computational resource, or a "parallel virtual machine". PVM consists of a run-time environment and a library of functions that allow message passing, process creation, and task synchronization.
- Beowulf clusters provide universities, often with limited resources, an excellent platform to teach parallel programming courses and provide cost-effective computing to their computational scientists as well.
- Beowulf clusters can be used for various applications that require high performance computing, such as scientific simulations, data analysis, image processing, machine learning, etc.
- A simple example of parallel programming with MPI on a Beowulf cluster is the "Hello World" program, which prints a message from each process in the cluster. The code is shown below:

```c
// hello.c: a simple MPI program
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    int rank, size;

    // Initialize MPI
    MPI_Init(&argc, &argv);

    // Get the rank (process ID) and size (number of processes) of the communicator
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Print a message from each process
    printf("Hello world from process %d of %d\n", rank, size);

    // Finalize MPI
    MPI_Finalize();

    return 0;
}
```

- To compile and run the program on a Beowulf cluster, the following commands can be used:

```bash
# Compile the program with mpicc, the MPI C compiler
mpicc -o hello hello.c

# Run the program with mpirun, the MPI launcher
# Specify the number of processes with -np option
# Specify the hostnames of the cluster nodes with -host option
mpirun -np 4 -host node1,node2,node3,node4 ./hello
```

- The output of the program may look like this:

```bash
Hello world from process 0 of 4
Hello world from process 1 of 4
Hello world from process 2 of 4
Hello world from process 3 of 4
```

- A possible mnemonic to remember the steps of parallel programming with MPI on a Beowulf cluster is:

**I C R P F**

- **I**nitialize MPI
- **C**ommunicate with other processes
- **R**un the program with mpirun
- **P**rint the output
- **F**inalize MPI

- A possible learning trick to understand the concept of a Beowulf cluster is to imagine a group of people working together on a project, each with their own laptop. They can communicate with each other by sending messages, and they can divide the work among themselves. The laptops are like the nodes of the cluster, and the people are like the processes. The project is like the parallel program, and the messages are like the MPI calls.