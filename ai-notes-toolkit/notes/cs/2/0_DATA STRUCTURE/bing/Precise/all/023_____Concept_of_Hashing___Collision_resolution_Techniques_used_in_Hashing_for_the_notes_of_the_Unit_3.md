# Concept of Hashing & Collision resolution Techniques used in Hashing

Hashing is a technique used to map a large set of data elements, such as a list of names or phone numbers, to a smaller, fixed-size table, called a hash table. The goal of hashing is to allow for fast and efficient data retrieval.

The basic idea behind hashing is to use a hash function to compute an index into the hash table for each data element. The hash function takes the data element as input and returns an integer, which is used as the index into the hash table.

Collision resolution is the process of handling situations where two or more data elements are mapped to the same index in the hash table. There are several techniques used to resolve collisions in hashing, including:

1. **Chaining**: In this technique, each slot in the hash table contains a linked list of data elements that are mapped to that slot. When a collision occurs, the new data element is simply added to the linked list.

2. **Open Addressing**: In this technique, when a collision occurs, the algorithm searches for the next available slot in the hash table to store the data element. There are several methods for searching for the next available slot, including linear probing, quadratic probing, and double hashing.

3. **Rehashing**: In this technique, when the hash table becomes too full, a new, larger hash table is created and all the data elements are rehashed into the new table.

Each collision resolution technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the application. It is important to choose a good hash function and an appropriate collision resolution technique to ensure that the hash table performs well.