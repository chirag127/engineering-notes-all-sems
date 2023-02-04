Blockchain: Implement a simple blockchain application using a decentralized database to store transactions securely. Technologies: Python, Blockchain, Ethereum, Solidity.

Sure, here's a code example for a simple blockchain application using Ethereum and Solidity:

```
pragma solidity ^0.8.0;

contract SimpleBlockchain {
    // Event to log a new transaction
    event NewTransaction(
        uint256 index,
        address from,
        address to,
        uint256 value
    );

    // Struct to store a transaction
    struct Transaction {
        address from;
        address to;
        uint256 value;
    }

    // Array to store all transactions
    Transaction[] public transactions;

    // Function to add a new transaction
    function addTransaction(address _from, address _to, uint256 _value) public {
        transactions.push(Transaction(_from, _to, _value));
        emit NewTransaction(transactions.length - 1, _from, _to, _value);
    }
}
```

This code is a simple Solidity contract for a blockchain application. The contract defines a `Transaction` struct to store information about a transaction, and an array of transactions to store all transactions. The `addTransaction` function is used to add a new transaction to the blockchain, and the `NewTransaction` event is used to log the new transaction.

You can deploy this contract on the Ethereum blockchain using a tool like Remix, and interact with it using a tool like Web3.js or a Python library like web3.py. You can also add more functionality to this contract, such as the ability to validate transactions or to mine new blocks.
