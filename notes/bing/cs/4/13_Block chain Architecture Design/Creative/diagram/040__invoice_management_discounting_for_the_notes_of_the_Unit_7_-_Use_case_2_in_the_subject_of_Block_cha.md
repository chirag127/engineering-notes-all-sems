The following diagram illustrates the basic architecture of a blockchain-based invoice discounting system:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    Supplier     |        |     Bank        |        |    Buyer        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   Blockchain    |        |   Blockchain    |        |   Blockchain    |
|   Node          |        |   Node          |        |   Node          |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   Invoice       |        |   Invoice       |        |   Invoice       |
|   Management    |        |   Management    |        |   Management    |
|   Application   |        |   Application   |        |   Application   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   Smart         |        |   Smart         |        |   Smart         |
|   Contract      |        |   Contract      |        |   Contract      |
|   (Invoice      |        |   (Invoice      |        |   (Invoice      |
|   Discounting)  |        |   Discounting)  |        |   Discounting)  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

The basic steps of the invoice discounting process are as follows:

1. The supplier and the buyer agree on a purchase order and the supplier delivers the goods or services to the buyer.
2. The supplier uploads the invoice and the proof of delivery to the blockchain network, where it is verified by the smart contract and stored as a transaction.
3. The supplier requests an advance payment from the bank, which is also a node on the blockchain network. The bank checks the invoice and the creditworthiness of the buyer and the supplier, and decides whether to approve or reject the request.
4. If the request is approved, the bank transfers the funds to the supplier's account, minus a discount fee. The smart contract records the transfer and updates the status of the invoice.
5. The buyer pays the full invoice amount to the bank on the due date. The smart contract records the payment and closes the invoice.
6. The bank, the supplier and the buyer can access the invoice history and status on the blockchain network at any time. The blockchain network ensures the security, transparency and immutability of the invoice data.