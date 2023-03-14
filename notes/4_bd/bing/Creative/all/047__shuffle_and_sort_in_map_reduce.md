#### Shuffle and sort in map reduce

- Shuffle and sort is the process of transferring the intermediate key-value pairs from the mappers to the reducers in a map reduce framework.
- Shuffle and sort ensures that all the values associated with the same key are sent to the same reducer, and that the keys are sorted in ascending order.
- Shuffle and sort consists of the following steps:

  1. Partitioning: The mapper divides the output key-value pairs into partitions based on a hash function of the key. Each partition corresponds to a reducer.
  2. Sorting: The mapper sorts the key-value pairs within each partition by the key. This is done to facilitate merging later.
  3. Spilling: The mapper writes the sorted partitions to the local disk as spill files. The mapper may spill multiple times if the output data is larger than the available memory.
  4. Merging: The mapper merges the spill files into a single sorted file per partition. The mapper then notifies the master node about the location of the files.
  5. Copying: The reducer fetches the files from the mappers and copies them to its local disk.
  6. Merging: The reducer merges the files from different mappers into a single sorted file per partition. The reducer then iterates over the file and passes each key and its list of values to the reduce function.

- A possible mnemonic to remember the steps of shuffle and sort is: **P**arties **S**hould **S**pill **M**ore **C**ocktails **M**errily (Partitioning, Sorting, Spilling, Merging, Copying, Merging).
- An example of shuffle and sort in map reduce is:

  - Suppose we have two mappers and two reducers, and the input data is:

    ```
    hello world
    hello map reduce
    goodbye world
    goodbye map reduce
    ```

  - The mappers apply a word count function and produce the following intermediate key-value pairs:

    ```
    Mapper 1:
    (hello, 1)
    (world, 1)
    (hello, 1)
    (map, 1)
    (reduce, 1)

    Mapper 2:
    (goodbye, 1)
    (world, 1)
    (goodbye, 1)
    (map, 1)
    (reduce, 1)
    ```

  - The mappers partition the key-value pairs based on a hash function of the key. Suppose the hash function assigns odd keys to reducer 1 and even keys to reducer 2. The partitions are:

    ```
    Mapper 1:
    Partition 1: (hello, 1), (hello, 1)
    Partition 2: (world, 1), (map, 1), (reduce, 1)

    Mapper 2:
    Partition 1: (goodbye, 1), (goodbye, 1)
    Partition 2: (world, 1), (map, 1), (reduce, 1)
    ```

  - The mappers sort the key-value pairs within each partition by the key. The sorted partitions are:

    ```
    Mapper 1:
    Partition 1: (hello, 1), (hello, 1)
    Partition 2: (map, 1), (reduce, 1), (world, 1)

    Mapper 2:
    Partition 1: (goodbye, 1), (goodbye, 1)
    Partition 2: (map, 1), (reduce, 1), (world, 1)
    ```

  - The mappers write the sorted partitions to the local disk as spill files. The spill files are:

    ```
    Mapper 1:
    Spill file 1: (hello, 1), (hello, 1)
    Spill file 2: (map, 1), (reduce, 1), (world, 1)

    Mapper 2:
    Spill file 1: (goodbye, 1), (goodbye, 1)
    Spill file 2: (map, 1), (reduce, 1), (world, 1)
    ```

  - The mappers merge the spill files into a single sorted file per partition. The merged files are:

    ```
    Mapper 1:
    Merged file 1: (hello, 1), (hello, 1)
    Merged file 2: (map, 1), (reduce, 1), (world, 1)

    Mapper 2:
    Merged file 1: (goodbye, 1),