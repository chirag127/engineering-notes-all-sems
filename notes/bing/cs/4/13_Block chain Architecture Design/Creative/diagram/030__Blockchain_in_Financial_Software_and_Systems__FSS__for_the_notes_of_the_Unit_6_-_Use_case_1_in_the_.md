### Blockchain in Financial Software and Systems (FSS) for the notes of the Unit 6 - Use case 1 in the subject of Block chain Architecture Design

Blockchain is a distributed ledger technology that enables secure and transparent transactions among multiple parties without intermediaries. Blockchain can be used in various financial software and systems to improve efficiency, security, trust and innovation. Some of the use cases of blockchain in financial software and systems are:

- Digital assets: Blockchain can enable the creation, issuance, transfer and exchange of digital representations of financial instruments, such as stocks, bonds, commodities, currencies, etc. Digital assets can be traded with more liquidity and speed at lower cost, and can also enable new business models and markets.
- Trade finance: Blockchain can streamline the complex and paper-intensive process of trade finance, which involves multiple parties, such as exporters, importers, banks, insurers, etc. Blockchain can provide a shared and immutable record of trade transactions, reducing fraud, errors, delays and costs, and enhancing trust and transparency.
- Stock transactions: Blockchain can facilitate faster and cheaper settlement of stock transactions, reducing the need for intermediaries and clearing houses. Blockchain can also provide a more secure and accurate record of ownership and transactions, reducing the risk of manipulation and disputes.
- Risk management: Blockchain can help financial institutions manage their risk exposure and compliance obligations, by providing a single source of truth and auditability for their transactions and data. Blockchain can also enable real-time monitoring and reporting of risk indicators, such as liquidity, credit, market, operational, etc., and facilitate the implementation of smart contracts and regulatory rules.
- Banking services: Blockchain can enable new and inclusive banking services, such as cross-border payments, remittances, peer-to-peer lending, microfinance, etc. Blockchain can reduce the cost and friction of these services, by eliminating intermediaries and currency conversions, and providing faster and more secure transactions. Blockchain can also increase the access and participation of unbanked and underbanked populations, by providing them with digital identities and wallets.

The following diagram illustrates the basic architecture of a blockchain-based financial software and system, using the example of digital assets:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Issuer         |      |  Investor       |      |  Exchange       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Create and     |      |  Buy and sell   |      |  Match and      |
|  issue digital  |      |  digital assets |      |  execute trades |
|  assets         |      |                 |      |                 |
|                 |      |                 |      |                 |
+--------+--------+      +--------+--------+      +--------+--------+
         |                       |                       |
         |                       |                       |
         +-----------------------+-----------------------+
                                 |
                                 |
                                 v
                          +-----------------+
                          |                 |
                          |  Blockchain     |
                          |                 |
                          +-----------------+
                          |                 |
                          |  Validate and   |
                          |  record         |
                          |  transactions   |
                          |                 |
                          +--------+--------+
                                   |
                                   |
                                   v
                          +-----------------+
                          |                 |
                          |  Ledger         |
                          |                 |
                          +-----------------+
                          |                 |
                          |  Store and      |
                          |  share          |
                          |  transactions   |
                          |                 |
                          +-----------------+
```