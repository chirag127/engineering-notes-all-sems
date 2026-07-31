### Concept of Hashing & Collision resolution Techniques used in Hashing

Hashing is a technique used to map a large set of data into a smaller, fixed-size table, called a hash table. The process of mapping the data into the hash table is done using a hash function. The hash function takes the data as input and returns an index into the hash table where the data can be stored or retrieved.

Collision resolution is the process of handling situations where two or more data elements map to the same index in the hash table. There are several techniques used to resolve collisions in hashing, including:

1. **Chaining**: In this technique, each element in the hash table is a linked list. When a collision occurs, the new data element is added to the linked list at the index where the collision occurred.

2. **Open Addressing**: In this technique, when a collision occurs, the data element is stored in the next available slot in the hash table. There are several methods for finding the next available slot, including linear probing, quadratic probing, and double hashing.

3. **Coalesced Hashing**: This technique is a combination of chaining and open addressing. When a collision occurs, the data element is stored in the next available slot in the hash table, but a pointer is also added to the original index to point to the new location of the data element.

These are some of the common collision resolution techniques used in hashing. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.