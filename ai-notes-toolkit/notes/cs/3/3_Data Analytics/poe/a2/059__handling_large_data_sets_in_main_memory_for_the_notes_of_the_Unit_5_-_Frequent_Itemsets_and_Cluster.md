 Here is the content in Markdown format without any emojis or external links and in formal tone:

### Handling Large Data Sets in Main Memory

1. Sorting - When data is loaded into memory, it is often useful to sort it. This allows for more efficient searching and processing. However, sorting large amounts of data can be computationally expensive. Various efficient sorting algorithms should be used to sort big data.
2. Pruning - When working with large data sets, it is common to prune, or trim down the data to only the most relevant parts. This may involve removing outliers or selecting specific columns of data to work with. Pruning the data can make processing more efficient and feasible on limited hardware.
3. Sampling - For very large data sets, it may not be possible to load and process all of the data at once. In these cases, sampling a subset of the data can be sufficient. Whether a random sample or more advanced sampling techniques are used, sampling allows big data sets to be summarized and analyzed without being constrained by memory limitations.
4. Distributed Processing - For data sets that are too large to process on a single machine, distributed processing can be used. This involves splitting up the work across multiple computers or servers so that the data can be processed in parallel. Hadoop and MapReduce are common frameworks for distributed processing of large data sets.

The above points should cover the key ways to handle large data sets that do not fit into the memory of a single machine. By sorting, pruning, sampling, and distributing the data across multiple machines, big data can be efficiently stored and processed.