The basic crypto primitives for blockchain development are the low-level algorithms that are used to build secure and distributed systems. They include hash functions, digital signatures, and encryption schemes. The following diagram illustrates the basic architecture of a blockchain system using these crypto primitives:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Block 1       |     |   Block 2       |     |   Block 3       |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| |             | |     | |             | |     | |             | |
| |  Header     | |     | |  Header     | |     | |  Header     | |
| |             | |     | |             | |     | |             | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| |             | |     | |             | |     | |             | |
| |  Data       | |     | |  Data       | |     | |  Data       | |
| |             | |     | |             | |     | |             | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hash Function  |     |  Hash Function  |     |  Hash Function  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hash Value     |     |  Hash Value     |     |  Hash Value     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Digital        |     |  Digital        |     |  Digital        |
|  Signature      |     |  Signature      |     |  Signature      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Signature      |     |  Signature      |     |  Signature      |
|  Value          |     |  Value          |     |  Value          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

A hash function is a mathematical function that