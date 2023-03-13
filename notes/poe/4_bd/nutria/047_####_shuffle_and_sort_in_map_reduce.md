

#### Shuffle and Sort in Map Reduce

Map Reduce is a programming model used to process large datasets in a parallel and distributed manner. It is a two-step process:

1. **Map**: The map step is responsible for taking an input dataset and transforming it into a set of data, where individual elements are broken down into tuples (key/value pairs).

2. **Reduce**: The reduce step is responsible for taking the output from the map step and combining those tuples into a smaller set of tuples.

In order to make sure that the data is processed correctly, the Map Reduce framework provides two key operations: shuffle and sort.

**Shuffle**: The shuffle operation is responsible for taking the output from the map step and rearranging it so that all tuples with the same key are grouped together. This allows for the reduce step to process each group of tuples with the same key simultaneously.

**Sort**: The sort operation is responsible for taking the output from the shuffle step and ordering the tuples based on their keys. This ensures that all tuples with the same key are processed in the same order.

Mnemonics and Learning Tricks:

- **M**ap **R**educe: **M**ove **R**epeated **K**eys **T**ogether
- **S**huffle: **S**eparate **K**eys
- **S**ort: **S**ort **K**eys