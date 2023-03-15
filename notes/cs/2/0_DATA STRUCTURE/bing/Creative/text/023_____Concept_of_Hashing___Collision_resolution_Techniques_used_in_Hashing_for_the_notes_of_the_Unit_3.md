### Concept of Hashing & Collision resolution Techniques used in Hashing

- Hashing is a technique of mapping a set of keys to a set of values using a hash function that assigns a unique hash value to each key.
- A hash function is a mathematical function that takes a key as input and returns a hash value as output, such that the hash value is in the range of the hash table size.
- A hash table is a data structure that stores key-value pairs in an array, where the index of each element is determined by the hash value of its key.
- Hashing is useful for fast and efficient searching, insertion and deletion of data in a large collection of items.
- Collision is a situation when two or more keys have the same hash value and map to the same slot in the hash table .
- Collision resolution is the process of handling the collisions and finding an alternative slot for the keys that cause collisions .
- There are two main types of collision resolution techniques: open hashing and closed hashing.

#### Open hashing (Separate chaining)

- This technique involves making a linked list out of the slot where the collision happened, then adding the new key to the list.
- Each slot in the hash table is a pointer to the head of the linked list that stores the keys with the same hash value.
- To search for a key, the hash function is applied to find the slot, then the linked list is traversed to find the key.
- To insert a key, the hash function is applied to find the slot, then the key is added to the front of the linked list.
- To delete a key, the hash function is applied to find the slot, then the key is removed from the linked list.
- The advantage of this technique is that it can handle any number of collisions, as long as there is enough memory to store the linked lists.
- The disadvantage of this technique is that it requires extra space for the pointers, and the performance may degrade if the linked lists become too long.

#### Closed hashing (Open addressing)

- This technique involves finding an alternative slot for the key that causes a collision, using a probe sequence that depends on the key and the hash function.
- There is no key stored outside of the hash table, therefore the size of the hash table is always greater than or equal to the number of keys.
- To search for a key, the hash function is applied to find the initial slot, then the probe sequence is followed until the key is found or an empty slot is reached.
- To insert a key, the hash function is applied to find the initial slot, then the probe sequence is followed until an empty slot is found or the table is full.
- To delete a key, the hash function is applied to find the initial slot, then the probe sequence is followed until the key is found, then the key is marked as deleted.
- The advantage of this technique is that it does not require extra space for the pointers, and the performance may be better if the load factor (the ratio of the number of keys to the table size) is low.
- The disadvantage of this technique is that it may cause clustering (the tendency of keys to cluster around certain slots), and the performance may degrade if the load factor is high.
- There are different methods of generating the probe sequence, such as linear probing, quadratic probing, double hashing, etc .