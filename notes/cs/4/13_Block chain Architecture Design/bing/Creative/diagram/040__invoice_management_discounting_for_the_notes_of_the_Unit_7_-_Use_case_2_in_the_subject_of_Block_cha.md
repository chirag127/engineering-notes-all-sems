The following is a detailed ASCII diagram for invoice management discounting for the notes of the Unit 7 - Use case 2 in the subject of Block chain Architecture Design. The diagram is based on the information from the web search results    .

### Invoice management discounting

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Supplier     |       |    Customer     |       |    Financier    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |       +-----------------+
       |                       |                       |       |                 |
       |                       |                       |       |    Blockchain   |
       |                       |                       |       |                 |
       +---------------------->|                       +------>|                 |
       |   Purchase order      |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |<----------------------+                       |       |                 |
       |   Proof of delivery   |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       |                 |
       |                       |                       |       +-----------------+
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       +------------------------------------------------------------->|
       |   Invoice             |                       |   Invoice     |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |<-------------------------------------------------------------+
       |   Advance payment     |                       |   Advance payment
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |<----------------------+               |
       |                       |   Invoice payment     |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |<-------------------------------------------------------------+
       |   Final payment       |                       |   Final payment
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       +---------------------->|                       +------>|       |
       |   Invoice status      |                       |   Invoice status
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       |                       |                       |               |
       +---------------------->|                       +------>|       |