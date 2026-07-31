Serialization in Hadoop io is the process of converting structured objects into byte streams for transmission over the network or permanent storage on disk  . Hadoop provides a serialization framework that allows different serialization libraries to be plugged in . One of the serialization libraries that Hadoop supports is Writable, which is a custom serialization format for Hadoop .

A detailed ascii diagram for serialization in Hadoop io using Writable is as follows:

##### Serialization in Hadoop io

```
+-----------------+       +-----------------+       +-----------------+
| Structured data |       | Byte stream     |       | Structured data |
| (Writable)      |       | (DataOutput)    |       | (Writable)      |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Field 1     | |       | | Field 1     | |       | | Field 1     | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Field 2     | |       | | Field 2     | |       | | Field 2     | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | ...         | |       | | ...         | |       | | ...         | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Field n     | |       | | Field n     | |       | | Field n     | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       | write(DataOutput out)   |                         | readFields(DataInput in)
       +------------------------>+                         +<------------------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
```