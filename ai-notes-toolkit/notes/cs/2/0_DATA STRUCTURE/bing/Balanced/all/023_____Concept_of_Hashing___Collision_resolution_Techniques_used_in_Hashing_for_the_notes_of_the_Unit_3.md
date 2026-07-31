# Concept of Hashing & Collision resolution Techniques used in Hashing

## Hashing
- Hashing is a technique of mapping a set of keys to a set of values using a hash function.
- A hash function is a function that takes a key as input and returns an integer value, called a hash value or a hash code, as output.
- The hash value is used as an index to store the key-value pair in an array, called a hash table or a hash map.
- The hash table has a fixed size, usually a prime number, and each slot in the hash table can store one or more key-value pairs.
- The advantage of hashing is that it allows fast access to the values associated with the keys, as the hash function can compute the index in constant time.
- The disadvantage of hashing is that it may cause collisions, which occur when two or more keys have the same hash value and map to the same slot in the hash table.

## Collision resolution Techniques
- Collision resolution techniques are methods to handle the collisions in the hash table and to ensure that every key can be inserted and retrieved successfully.
- There are two main types of collision resolution techniques: open hashing and closed hashing.

### Open hashing (Separate chaining)
- Open hashing, also known as separate chaining, is a technique that uses a linked list to store the key-value pairs that have the same hash value in the same slot of the hash table.
- Each slot in the hash table is either empty or contains a pointer to the head of a linked list.
- To insert a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. Then, the key-value pair is added to the front of the linked list in that slot.
- To search for a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. Then, the linked list in that slot is traversed until the key is found or the end of the list is reached.
- The advantage of open hashing is that it can handle any number of collisions, as the linked list can grow dynamically.
- The disadvantage of open hashing is that it requires extra space for the pointers and the linked list, and it may cause long search time if the linked list is too long.

### Closed hashing (Open addressing)
- Closed hashing, also known as open addressing, is a technique that stores the key-value pairs directly in the hash table, without using any pointers or linked lists.
- Each slot in the hash table can store at most one key-value pair, and the hash table size is equal to or larger than the number of keys.
- To insert a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. If the slot is empty, the key-value pair is stored in that slot. If the slot is occupied, a different slot is probed until an empty slot is found or the entire hash table is scanned.
- To search for a key-value pair, the hash function is applied to the key and the hash value is used as the index to locate the slot in the hash table. If the slot is empty, the key is not in the hash table. If the slot is occupied, the key is compared with the key in that slot. If they match, the value is returned. If they do not match, a different slot is probed until the key is found or an empty slot is encountered.
- The advantage of closed hashing is that it does not require extra space for the pointers or the linked lists, and it may cause faster access time if the hash table is not too full.
- The disadvantage of closed hashing is that it may cause insertion failure if the hash table is full, and it may cause clustering, which occurs when many keys have the same or similar hash values and map to the same or adjacent slots in the hash table.

#### Probing methods
- Probing methods are the methods to find a different slot in the hash table when a collision occurs in closed hashing.
- There are three common probing methods: linear probing, quadratic probing, and double hashing.

##### Linear probing
- Linear probing is a probing method that uses a linear function to find the next slot in the hash table.
- The linear function is of the form: h'(k, i) = (h(k) + i) mod m, where h(k) is the original hash value, i is the probe number, and m is the hash table size.
- To