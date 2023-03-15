### Concept of Hashing & Collision resolution Techniques used in Hashing

- Hashing is a technique of mapping a set of keys to a set of values using a hash function.
- A hash function is a function that takes a key as input and returns an integer value, called a hash value or a hash code, as output.
- A hash table is a data structure that stores key-value pairs in an array, using the hash values as indices.
- Hashing is useful for fast and efficient searching, insertion and deletion of data in a large collection of items.
- However, hashing may cause collisions, which occur when two or more keys have the same hash value and map to the same slot in the hash table.
- Collision resolution techniques are methods to handle collisions and avoid data loss or corruption in the hash table.
- There are two main types of collision resolution techniques: open hashing and closed hashing.

#### Open Hashing (Separate Chaining)

- In open hashing, each slot in the hash table contains a pointer to a linked list of key-value pairs that have the same hash value.
- To insert a new key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, a new linked list is created and the key-value pair is added as the first node. If the slot is not empty, the key-value pair is appended to the existing linked list.
- To search for a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the linked list is traversed until the key is found or the end of the list is reached.
- To delete a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the linked list is traversed until the key is found or the end of the list is reached. If the key is found, the node is removed from the list and the memory is freed. If the key is not found, no action is taken.
- The advantage of open hashing is that it can handle any number of collisions and the hash table size does not need to be fixed or large.
- The disadvantage of open hashing is that it requires extra space for the linked lists and the performance may degrade if the lists become too long.

#### Closed Hashing (Open Addressing)

- In closed hashing, each slot in the hash table can store only one key-value pair and there are no pointers or linked lists.
- To insert a new key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key-value pair is stored in the slot. If the slot is not empty, a collision has occurred and a different slot is probed until an empty slot is found or the entire table is full.
- To search for a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the key is compared with the stored key. If they match, the value is returned. If they do not match, a collision has occurred and a different slot is probed until the key is found or an empty slot is reached.
- To delete a key-value pair, the hash function is applied to the key and the corresponding slot is located. If the slot is empty, the key is not found. If the slot is not empty, the key is compared with the stored key. If they match, the slot is marked as deleted. If they do not match, a collision has occurred and a different slot is probed until the key is found or an empty slot is reached.
- The advantage of closed hashing is that it does not require extra space and the access time is constant if there are no collisions.
- The disadvantage of closed hashing is that it has a limited capacity and the performance may degrade if the load factor (the ratio of the number of keys to the table size) is high.

##### Collision Resolution Techniques in Closed Hashing

- There are different ways to probe for an empty slot in closed hashing, such as linear probing, quadratic probing, double hashing, etc.
- Linear probing: In linear probing, the next slot in the hash table is probed if the current slot is occupied. If the end of the table is reached, the probing wraps around to the beginning of the table. The probe sequence is given by:

    ```
    h(k