### Concept of Hashing & Collision Resolution Techniques Used in Hashing

Hashing is a technique used to store and retrieve data effectively. It is a process of mapping a large and complex data set into a smaller and more manageable data set. In hashing, a hash function is used to map the data set into a smaller data set, known as the hash table. The hash table is then used to store and retrieve data quickly and efficiently.

#### Hash Function

A hash function is a mathematical function that takes an input (or key) and produces a fixed-size output, known as the hash value. The hash value is used to index the hash table. A good hash function distributes the keys uniformly across the hash table, minimizing collisions.

#### Collision Resolution Techniques

Collisions occur when two or more keys have the same hash value. There are several techniques used to resolve collisions:

- **Separate Chaining:** In this technique, each hash table entry is a linked list. If a collision occurs, the new key is added to the linked list at the corresponding hash table entry.
- **Open Addressing:** In this technique, the hash table entries are probed sequentially until an empty slot is found. There are several methods for probing, such as linear probing, quadratic probing, and double hashing.
- **Robin Hood Hashing:** In this technique, the hash table entries are probed sequentially until an empty slot is found. If a collision occurs, the probe distance is measured. The new key is inserted in the empty slot only if its probe distance is less than or equal to that of the existing key. If the probe distance is greater, the existing key is shifted to the empty slot, and the new key is inserted in the existing key's slot.

#### Advantages of Hashing

- Fast access and retrieval of data
- Efficient use of memory
- Uniform distribution of data
- Easy insertion and deletion of data

#### Disadvantages of Hashing

- Collisions can occur, reducing the efficiency of the hash table
- Hash functions may not distribute the data uniformly
- Hash tables may need to be resized if the data set increases or decreases significantly

### Conclusion

Hashing is a powerful technique used to store and retrieve data quickly and efficiently. Collision resolution techniques are used to handle collisions that occur when two or more keys have the same hash value. Hashing has advantages and disadvantages, and it is essential to choose the right hash function and collision resolution technique for the data set to achieve optimal performance.