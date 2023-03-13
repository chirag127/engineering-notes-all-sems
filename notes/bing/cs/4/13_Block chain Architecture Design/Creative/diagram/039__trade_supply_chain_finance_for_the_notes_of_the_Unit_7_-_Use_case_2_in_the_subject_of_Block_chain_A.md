The following is a detailed ASCII diagram for trade/supply chain finance for the notes of the Unit 7 - Use case 2 in the subject of Block chain Architecture Design.

### Trade/Supply Chain Finance

```
+-----------------+      +-----------------+      +-----------------+
| Buyer           |      | Seller          |      | Bank            |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| 1. Order goods  |----->| 2. Ship goods   |      |                 |
|                 |      |                 |      |                 |
|                 |      | 3. Issue invoice|----->| 4. Finance      |
|                 |      |                 |      |                 |
|                 |      |                 |      | 5. Record on    |
|                 |      |                 |      |    blockchain   |
|                 |      |                 |      |                 |
|                 |      |                 |<-----| 6. Notify       |
|                 |      |                 |      |                 |
| 7. Receive goods|<-----|                 |      |                 |
|                 |      |                 |      |                 |
| 8. Pay invoice  |----->| 9. Receive payment|<---| 10. Receive     |
|                 |      |                 |      |     payment     |
+-----------------+      +-----------------+      +-----------------+
```

The diagram illustrates the basic architecture of a blockchain-based platform for trade/supply chain finance. The main actors are the buyer, the seller, and the bank. The steps are as follows:

1. The buyer orders goods from the seller.
2. The seller ships the goods to the buyer.
3. The seller issues an invoice to the bank for the goods.
4. The bank finances the invoice and pays the seller in advance.
5. The bank records the invoice and the payment on the blockchain, creating a transparent and immutable record of the transaction.
6. The bank notifies the buyer and the seller of the invoice and the payment on the blockchain.
7. The buyer receives the goods from the seller.
8. The buyer pays the invoice to the bank according to the agreed terms.
9. The seller receives the payment from the bank.
10. The bank receives the payment from the buyer.

The benefits of using blockchain for trade/supply chain finance are:

- Reduced complexity and risk of fraud, as the transactions are verified and recorded on a distributed ledger that is shared by all participants.
- Increased efficiency and speed, as the transactions are executed automatically and securely using smart contracts and digital signatures.
- Enhanced transparency and trust, as the transactions are visible and traceable by all participants, and the data is encrypted and protected from tampering.
- Expanded access and opportunities, as the platform enables new financing products and services for small and medium enterprises (SMEs) and companies that would traditionally use open account trading.