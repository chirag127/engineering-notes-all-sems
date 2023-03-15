### Concept of Hashing & Collision resolution Techniques used in Hashing

Hashing is a technique used to map a large set of data elements, such as a list of names or phone numbers, to a smaller, more manageable set of addresses or indices. This is done by using a hash function, which takes a data element as input and returns an address or index where the data element can be found.

Collision resolution is the process of resolving conflicts that arise when two or more data elements are mapped to the same address or index by the hash function. There are several techniques used to resolve collisions in hashing, including:

1. **Chaining**: In this technique, each address or index in the hash table is associated with a linked list. When a collision occurs, the new data element is added to the linked list at the address or index where the collision occurred.

2. **Open Addressing**: In this technique, when a collision occurs, the algorithm searches for the next available address or index in the hash table to store the new data element. This can be done using linear probing, quadratic probing, or double hashing.

3. **Rehashing**: In this technique, when a collision occurs, a second hash function is used to generate a new address or index for the data element. This process can be repeated with additional hash functions if necessary.

These are some of the most commonly used collision resolution techniques in hashing. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.