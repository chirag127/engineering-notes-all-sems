# Concept of Hashing & Collision resolution Techniques used in Hashing

## Hashing
- Hashing is a technique of mapping a set of keys to a set of values using a hash function.
- A hash function is a function that takes a key as input and returns an integer value, called a hash value or a hash code, as output.
- The hash value is used as an index to store the key-value pair in an array, called a hash table or a hash map.
- The hash table has a fixed size, usually a prime number, and each slot in the hash table can store one or more key-value pairs.
- The advantage of hashing is that it allows fast access to the values associated with the keys, as the hash function can compute the index in constant time.
- The disadvantage of hashing is that it may cause collisions, which occur when two or more keys have the same hash value and map to the same slot in the hash table.

## Collision resolution Techniques
- Collision resolution techniques are methods to handle the collisions in the hash table and to store the key-value pairs in a proper way.
- There are two main types of collision resolution techniques: open hashing and closed hashing.

### Open hashing (Separate chaining)
- Open hashing is a technique that uses a linked list to store the key-value pairs that have the same hash value in the same slot of the hash table.
- Each slot in the hash table is a pointer to the head of a linked list, which contains the key-value pairs that have the same hash value.
- To insert a new key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the key-value pair is added to the front of the linked list at the corresponding slot in the hash table.
- To search for a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the linked list at the corresponding slot in the hash table is traversed until the key is found or the end of the list is reached.
- To delete a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the linked list at the corresponding slot in the hash table is traversed until the key is found and removed from the list.
- The advantage of open hashing is that it can handle any number of collisions, as the linked list can grow dynamically.
- The disadvantage of open hashing is that it requires extra space for the pointers and the linked list, and it may cause long chains that degrade the performance.

### Closed hashing (Open addressing)
- Closed hashing is a technique that uses the hash table itself to store the key-value pairs, without using any extra space or pointers.
- Each slot in the hash table can store only one key-value pair, and the hash table size is usually larger than the number of keys to avoid collisions.
- To insert a new key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the slot at the hash value is checked. If it is empty, the key-value pair is stored there. If it is occupied, a different slot is probed until an empty slot is found or the hash table is full.
- To search for a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the slot at the hash value is checked. If it is empty, the key is not in the hash table. If it is occupied, the key is compared with the stored key. If they match, the value is returned. If they do not match, a different slot is probed until the key is found or an empty slot is reached.
- To delete a key-value pair, the hash function is applied to the key and the hash value is obtained. Then, the slot at the hash value is checked. If it is empty, the key is not in the hash table. If it is occupied, the key is compared with the stored key. If they match, the slot is marked as deleted. If they do not match, a different slot is probed until the key is found or an empty slot is reached.
- The advantage of closed hashing is that it does not require extra space or pointers, and it can achieve better cache performance.
- The disadvantage of closed hashing is that it may cause clustering, which occurs when many keys have the same or nearby hash values and occupy the same or adjacent slots in the hash table, making the probing more difficult.

#### Probing methods
- Probing methods are the ways to find a different slot in the hash table when a collision occurs in closed