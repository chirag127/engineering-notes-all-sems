### Concept of Hashing & Collision resolution Techniques used in Hashing

Hashing is a technique used for fast and efficient data retrieval. It is a process of converting a key into a hash code using a hash function. The hash code is used to index and retrieve data from a data structure called a hash table.

#### Hash Function

A hash function is a mathematical function that takes a key as input and produces a hash code as output. It should have the following properties:

- Deterministic: The same key should always produce the same hash code.
- Uniformity: The hash function should distribute keys uniformly across the hash table.
- Efficiency: The hash function should be efficient to compute.

#### Collision Resolution Techniques

Collision occurs when two or more keys produce the same hash code. There are several collision resolution techniques used in hashing:

- Open Addressing: In this technique, when a collision occurs, the algorithm searches for the next empty slot in the hash table and inserts the key there.
    - Linear Probing: In this technique, the algorithm checks the next slot in the hash table and inserts the key there if it is empty. If not, it checks the next slot and so on until an empty slot is found.
    - Quadratic Probing: In this technique, the algorithm uses a quadratic function to search for the next empty slot in the hash table. It first checks the next slot, then the slot after that, and so on.
    - Double Hashing: In this technique, the algorithm uses a second hash function to search for the next empty slot in the hash table.
- Chaining: In this technique, each slot in the hash table contains a linked list of keys that hash to that slot. When a collision occurs, the new key is added to the linked list.

#### Advantages of Hashing

- Fast and efficient data retrieval.
- Can handle large amounts of data.
- Easy to implement.
- Provides constant-time operation for lookup, insertion, and deletion.

#### Disadvantages of Hashing

- Hashing requires a good hash function to minimize collisions.
- Hashing can lead to memory wastage if the hash table is not sized appropriately.
- Chaining can lead to poor performance if the linked lists become too long.

Overall, hashing is a powerful technique used in many applications such as databases, compilers, and operating systems. It is essential to understand the concept of hashing and the collision resolution techniques used to implement it.