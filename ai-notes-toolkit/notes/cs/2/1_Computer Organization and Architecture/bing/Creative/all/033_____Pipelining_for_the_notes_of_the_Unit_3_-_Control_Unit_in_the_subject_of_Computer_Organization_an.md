# Pipelining

Pipelining is a technique for improving the performance of a computer system by overlapping the execution of multiple instructions in different stages of a processor. Pipelining can be used for instruction processing or for any complex operation that can be divided into sub-operations.

## Basic Concepts of Pipelining

- A pipeline is a sequence of stages that process data or instructions in parallel. Each stage performs a specific function and passes the output to the next stage. The input and output of each stage are stored in registers called interface registers or pipeline registers.
- The number of stages in a pipeline is called the pipeline depth. The time required for a stage to complete its operation is called the stage delay. The time interval between the initiation of two successive instructions in a pipeline is called the pipeline cycle time or clock cycle.
- The performance of a pipeline is measured by its throughput, which is the number of instructions or operations completed per unit time. The ideal throughput of a pipeline is equal to the inverse of the pipeline cycle time. The speedup of a pipeline is the ratio of the throughput of a pipeline to the throughput of a single-stage processor.
- The efficiency of a pipeline is the ratio of the actual throughput to the ideal throughput. The efficiency of a pipeline depends on the balance of the stage delays, the frequency of hazards, and the degree of parallelism in the instruction stream.

## Types of Pipelining

- Instruction pipelining is a technique for processing multiple instructions in different stages of a processor. The stages of an instruction pipeline typically include fetch, decode, execute, memory access, and writeback. Instruction pipelining increases the instruction level parallelism (ILP) in a program by overlapping the execution of independent instructions.
- Data pipelining is a technique for processing multiple data elements in different stages of a processor. The stages of a data pipeline typically include load, operate, store, and repeat. Data pipelining increases the data level parallelism (DLP) in a program by overlapping the execution of independent data elements.
- Arithmetic pipelining is a technique for processing multiple arithmetic operations in different stages of a processor. The stages of an arithmetic pipeline typically include fetch operands, perform operation, normalize result, and round result. Arithmetic pipelining increases the arithmetic level parallelism (ALP) in a program by overlapping the execution of independent arithmetic operations.

## Advantages and Disadvantages of Pipelining

- The main advantage of pipelining is that it improves the performance of a computer system by increasing the throughput and reducing the latency of the processor. Pipelining also reduces the cost and power consumption of the processor by using simpler and smaller components for each stage.
- The main disadvantage of pipelining is that it introduces complexity and overhead in the design and implementation of the processor. Pipelining also increases the possibility of hazards, which are situations that prevent the smooth execution of instructions or operations in a pipeline. Hazards can be classified into three types: structural, data, and control hazards.
- Structural hazards occur when two or more instructions or operations require the same resource at the same time. For example, a structural hazard can occur when two instructions try to access the same memory unit or register file in the same cycle. Structural hazards can be resolved by increasing the number of resources, using buffers or queues, or stalling the pipeline.
- Data hazards occur when an instruction or operation depends on the result of a previous instruction or operation that has not yet completed. For example, a data hazard can occur when an instruction tries to read a register that is being written by a previous instruction in the pipeline. Data hazards can be resolved by using forwarding or bypassing, reordering or scheduling, or stalling the pipeline.
- Control hazards occur when the flow of instructions or operations is altered by a branch or a jump instruction. For example, a control hazard can occur when the target address of a branch or a jump instruction is not known until the execute stage of the pipeline. Control hazards can be resolved by using branch prediction, branch target buffering, or delaying the branch.