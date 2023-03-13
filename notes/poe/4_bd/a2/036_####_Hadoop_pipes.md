 Here is the content on #### Hadoop pipes in markdown format:

#### Hadoop pipes

Hadoop pipes refer to the way components in a Hadoop job can be connected to each other to process data. Some key points about Hadoop pipes:

- Data flows through pipes from one component to the next. Each component reads data from its input pipe, processes it and writes the output to its output pipe.
- Pipes are unidirectional and data flows in only one direction through the pipe.
- The output of one component is the input to the next component. The components are connected in a sequence to form pipelines.
- Data is processed in batches and a batch of data must be fully processed by a component before the next batch is retrieved.
- Types of pipes:

-- File pipe: Reads/writes data from/to the file system.
-- STDIN/STDOUT pipe: Reads/writes data from/to standard input/output.
-- Custom pipe: Built to enable data exchange with a custom data source or sink.

Advantages:

- Components can be reused and combined in different ways.
- Pipelines are easy to construct and maintain. New components can be added easily.
- Fault tolerance is increased as if one component fails, only that component needs to be rerun. The rest of the pipeline is unaffected.
- Performance is increased as components process data in parallel.

Disadvantages:

- Troubleshooting is harder as the exact component causing an issue is harder to identify.
- Data may get out of order if multiple inputs are being read in parallel.
- Deadlocks can occur if not designed properly.

[Include additional details/diagrams/examples/codes/applications as needed]