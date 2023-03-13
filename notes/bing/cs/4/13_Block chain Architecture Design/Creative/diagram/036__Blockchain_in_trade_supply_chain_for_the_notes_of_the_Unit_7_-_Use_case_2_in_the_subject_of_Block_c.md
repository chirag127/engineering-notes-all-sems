The following diagram illustrates the basic architecture of a blockchain in trade/supply chain for the notes of the Unit 7 - Use case 2 in the subject of Block chain Architecture Design.

```
+-----------------+      +-----------------+      +-----------------+
| Supplier        |      | Manufacturer    |      | Retailer        |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | Product     | |      | | Product     | |      | | Product     | |
| | Information | |      | | Information | |      | | Information | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|       |         |      |       |         |      |       |         |
|       |         |      |       |         |      |       |         |
|       v         |      |       v         |      |       v         |
+-----------------+      +-----------------+      +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        v                         v                         v
+-------------------------------------------------------------------+
| Blockchain Network                                                |
|                                                                   |
| +------------------+ +------------------+ +------------------+    |
| | Supplier Node    | | Manufacturer Node| | Retailer Node    |    |
| |                  | |                  | |                  |    |
| | +--------------+ | | +--------------+ | | +--------------+ |    |
| | | Transactions | | | | Transactions | | | | Transactions | |    |
| | | (Product     | | | | (Product     | | | | (Product     | |    |
| | | Information) | | | | Information) | | | | Information) | |    |
| | +--------------+ | | +--------------+ | | +--------------+ |    |
| |                  | |                  | |                  |    |
| | +--------------+ | | +--------------+ | | +--------------+ |    |
| | | Blocks       | | | | Blocks       | | | | Blocks       | |    |
| | | (Hashes,     | | | | (Hashes,     | | | | (Hashes,     | |    |
| | | Signatures,  | | | | Signatures,  | | | | Signatures,  | |    |
| | | Timestamps)  | | | | Timestamps)  | | | | Timestamps)  | |    |
| | +--------------+ | | +--------------+ | | +--------------+ |    |
| +------------------+ +------------------+ +------------------+    |
+-------------------------------------------------------------------+
```

The diagram shows how each participant in the supply chain (supplier, manufacturer, retailer) can store and share product information on a blockchain network. Each participant has a node on the network that can create transactions (product information) and store them in blocks (hashes, signatures, timestamps). The blocks are linked by cryptographic hashes and validated by consensus mechanisms. The blockchain network provides traceability, transparency, and security for the product information across the supply chain.