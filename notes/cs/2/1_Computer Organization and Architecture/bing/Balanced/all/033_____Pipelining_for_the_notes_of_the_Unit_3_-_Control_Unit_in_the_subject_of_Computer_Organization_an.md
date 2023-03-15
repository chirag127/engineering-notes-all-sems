# Pipelining

- Pipelining is a technique for breaking down a sequential process into various sub-operations and executing each sub-operation in its own dedicated segment that runs in parallel with all other segments.
- Pipelining defines the temporal overlapping of processing. Pipelines are emptiness greater than assembly lines in computing that can be used either for instruction processing or, in a more general method, for executing any complex operations.
- Pipelining is the process of accumulating instruction from the processor through a pipeline. It allows storing and executing instructions in an orderly process. It is also known as pipeline processing.
- A pipeline has two ends, the input end and the output end. Between these ends, there are several stages that perform different operations on the data or instructions.
- Interface registers are used to hold the intermediate output between two stages. These interface registers are also known as pipeline registers or pipeline latches.
- All the stages in the pipeline along with the interface registers are connected in a linear fashion. The output of one stage is fed as the input to the next stage.
- The stages in the pipeline are synchronized by a common clock. Each stage performs its operation in one clock cycle and passes the result to the next stage in the next clock cycle.
- The main advantage of pipelining is that it increases the throughput of the processor, i.e., the number of instructions executed per unit time. This is because multiple instructions are processed simultaneously at different stages of the pipeline .
- The main disadvantage of pipelining is that it introduces some overheads and complexities, such as pipeline hazards, stalls, and bubbles. These are the situations that prevent the pipeline from operating at its full capacity and cause delays or inefficiencies .
- There are different types of pipelining, such as instruction pipelining, data pipelining, arithmetic pipelining, and superscalar pipelining. Each type has its own characteristics and applications .