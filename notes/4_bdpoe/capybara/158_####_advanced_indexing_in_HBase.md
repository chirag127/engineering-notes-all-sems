### Advanced Indexing in HBase

HBase is a NoSQL database that is built on top of the Hadoop Distributed File System (HDFS). It is designed to store and manage large amounts of structured data. HBase provides several indexing mechanisms to improve query performance. In this section, we will discuss some of the advanced indexing techniques used in HBase.

#### Bloom Filters

Bloom filters are probabilistic data structures that are used to test whether an element is a member of a set. Bloom filters are used in HBase to speed up lookups by reducing the number of disk accesses. Bloom filters work by creating a bit vector of a fixed size, and then hashing each element to a set of positions in the bit vector. 

When a query is made, HBase checks the bloom filter to see if the element is likely to be in the set. If the bloom filter returns false, the query is aborted, and if it returns true, HBase looks up the element in the relevant column family. Bloom filters can be used to speed up queries that access a small subset of the data.

#### Block Cache

The block cache is a memory cache that is used to speed up lookups by reducing the number of disk accesses. The block cache stores frequently accessed HBase blocks in memory, so that they can be accessed faster. The block cache can be configured to use a fixed amount of memory, or to use a percentage of the total available memory.

#### Secondary Indexes

Secondary indexes are indexes that are created on columns other than the row key. Secondary indexes can be used to speed up queries that search for rows based on non-key columns. In HBase, secondary indexes are implemented using Apache Phoenix, which is a SQL layer that sits on top of HBase. 

#### Mnemonics and Learning Tricks

One mnemonic that can be used to remember the benefits of advanced indexing techniques in HBase is "BSS". BSS stands for Bloom Filters, Secondary Indexes, and Block Cache. Remembering BSS can help you understand the different types of indexing techniques available in HBase, and the benefits they provide.

Another learning trick that can be used is to remember that Bloom Filters work by creating a bit vector of a fixed size, and then hashing each element to a set of positions in the bit vector. This can help you understand how Bloom Filters reduce the number of disk accesses in HBase.

#### Conclusion

In conclusion, HBase provides several advanced indexing techniques to improve query performance. Bloom Filters, Block Cache, and Secondary Indexes are some of the techniques that can be used to speed up lookups in HBase. Remembering BSS and the way Bloom Filters work can help you understand the benefits of these techniques.