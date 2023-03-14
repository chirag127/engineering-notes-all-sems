### Invoice Management Discounting for the Notes of the Unit 7 - Use Case 2 in the Subject of Block Chain Architecture Design

- Invoice management discounting is a process of obtaining short-term financing from a bank or a financial institution by using the invoices or accounts receivable of a business as collateral .
- It helps businesses, especially small and medium enterprises (SMEs), to improve their cash flow and liquidity by getting advance payments from the bank, rather than waiting for the customers to pay .
- Invoice management discounting is a market with a double-digit potential growth rate in Europe and worldwide in the next years .
- However, one of the main challenges of invoice management discounting is how to prevent double spending, i.e., the same invoice being used to obtain financing from multiple sources, and how to reduce the risk and the cost for the banks .
- Blockchain technology has the potential to provide a solution for invoice management discounting by creating a transparent, secure, and decentralized ledger of invoices that can be verified and accessed by authorized parties  .
- A blockchain-based invoice management discounting system, called Distributed Ledger Invoice (DLI), has been proposed by Fabrizio et al.  as a use case for blockchain architecture design.
- The DLI system consists of the following components:
  - A blockchain network that stores the invoices and their status (e.g., issued, paid, discounted, etc.) as smart contracts.
  - A web application that allows the suppliers, customers, and banks to interact with the blockchain network and perform operations such as creating, sending, receiving, approving, and discounting invoices.
  - A decoupling layer that enables interoperability and access control across different blockchain platforms, based on the Attribute-Based Access Control (ABAC) language.
- The DLI system works as follows:
  - The supplier creates an invoice for the customer and sends it to the blockchain network, where it is stored as a smart contract with a unique identifier and a status of "issued".
  - The customer receives the invoice from the blockchain network and approves it, changing its status to "approved".
  - The supplier requests a discounting service from the bank, providing the invoice identifier and the amount of financing needed.
  - The bank verifies the invoice status and the customer's creditworthiness from the blockchain network and decides whether to accept or reject the discounting request.
  - If the bank accepts the request, it transfers the funds to the supplier's account and changes the invoice status to "discounted".
  - The customer pays the invoice amount to the bank on the due date and changes the invoice status to "paid".
- The DLI system offers the following benefits for the invoice management discounting process  :
  - It increases the transparency and the trust among the parties involved, as they can access the same source of truth and verify the invoice status and history on the blockchain network.
  - It reduces the risk and the cost for the banks, as they can prevent double spending and fraud, and eliminate the need for manual verification, reconciliation, and auditing of the invoices.
  - It improves the efficiency and the speed of the process, as the transactions are executed automatically by the smart contracts and the funds are transferred in real time.
  - It enhances the interoperability and the data security, as the decoupling layer allows different blockchain platforms to communicate and share information, and the ABAC language enables fine-grained access control to the sensitive data.

- A possible mnemonic to remember the main components and benefits of the DLI system is:

  - DLI = Decoupling Layer + Blockchain + Invoice
  - DLI = Decrease risk + Increase trust + Improve efficiency

- A possible learning trick to understand the DLI system is to compare it with a traditional invoice management discounting system, and identify the differences and the advantages of using blockchain technology. For example, the following table shows a comparison of the two systems:

| Traditional System | DLI System |
| ------------------ | ---------- |
| The invoices are stored in different databases or paper records, which may be inconsistent, incomplete, or tampered with. | The invoices are stored on a blockchain network, which is immutable, transparent, and verifiable. |
| The parties involved have to rely on intermediaries or third parties to verify, approve, and process the invoices, which may introduce