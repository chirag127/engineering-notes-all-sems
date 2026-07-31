 Here is the content in markdown format without any feeling or friendliness with formal tone and without any emojis or external links:

### Concept of Hashing & Collision resolution Techniques used in Hashing

**Hashing**: Hashing is a technique to assign a unique code (called hash code) to each data item. This makes searching, storing and retrieving data items efficient.

**How Hashing works?**

1. The key value of the data item is applied to a hash function to compute the hash code (index value)
2. The data item is stored at the index location in the table as pointed by the hash code
3. During searching, the same hash function is applied on the search key to get the hash code and search the item at the index location

**Advantages**:

- Searches, insertions and deletions are fast as they are of O(1) time complexity
- Dense data can be stored efficiently

**Disadvantages**:

- The hash function plays an important role in determining the performance. If the hash function is not good, it leads to frequent collisions which degrade the performance of hashing.
- Not suitable for dynamic data where frequent insertions and deletions occur. This leads to rehashing which is an expensive operation.

**Collision Resolution Techniques**:

When two keys map to the same index location, collision occurs. The following techniques are used to resolve collisions:

1. **Chaining**: Each cell of the table contains a pointer to a linked list of elements that have same hash function value. Searches are done in the chain to locate the element.
2. **Open Addressing**: Probing is done to resolve collisions.
    - **Linear Probing**: Probing is done sequentially to find an empty slot.
    - **Quadratic Probing**: Probing is done sequentially but using a quadratic function to find an empty slot.
    - **Double Hashing**: Two hash functions are used to probe for an empty slot.

The content is written in points and in a formal tone as per the given instructions. Let me know if you would like me to modify or add anything.