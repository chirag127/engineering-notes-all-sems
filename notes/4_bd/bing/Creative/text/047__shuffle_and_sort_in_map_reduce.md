#### Shuffle and Sort in MapReduce

- Shuffle and sort are two phases in the MapReduce framework that occur between the map and the reduce tasks.
- Shuffle is the process of transferring the intermediate data from the mappers to the reducers. Each reducer receives one or more keys and their associated values depending on the number of reducers and the partitioning function. Shuffling can start even before the map phase has finished, to save some time.
- Sort is the process of merging and sorting the map outputs by key. Data from the mappers are grouped by the key, split among reducers and sorted by the key. Every reducer obtains all values associated with the same key. Sorting helps the reducer to easily distinguish when a new reduce task should start.
- Secondary sort is a technique to sort the values associated with each key in the reducer input. This can be useful for some applications that require the values to be ordered in some way.
- Shuffle and sort are performed by the MapReduce framework automatically and are not visible to the user. However, the user can customize the partitioning, grouping and sorting functions to achieve different results.

: https://stackoverflow.com/questions/22141631/what-is-the-purpose-of-shuffling-and-sorting-phase-in-the-reducer-in-map-reduce
: https://data-flair.training/blogs/shuffling-and-sorting-in-hadoop/