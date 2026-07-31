### Concept of Hashing & Collision resolution Techniques used in Hashing

Hashing is a technique used to map a large set of data to a smaller set of data, called a hash table, using a hash function. The hash function takes an input and produces an output, called a hash value, which is used as an index to store the data in the hash table.

Collision resolution techniques are used to handle the situation when two or more data elements are mapped to the same index in the hash table. There are several collision resolution techniques, including:

1. **Chaining**: In this technique, each element in the hash table is a linked list. When a collision occurs, the new data element is added to the linked list at the corresponding index.

2. **Open Addressing**: In this technique, when a collision occurs, the data element is stored in the next available slot in the hash table. There are several methods for finding the next available slot, including linear probing, quadratic probing, and double hashing.

3. **Coalesced Hashing**: This technique is a combination of chaining and open addressing. When a collision occurs, the data element is stored in the next available slot in the hash table, and a pointer is added to the linked list at the original index to point to the new location.

These are some of the collision resolution techniques used in hashing. It is important to choose the appropriate technique based on the specific requirements of the data set and the application.