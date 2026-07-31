# Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or loss of data due to network or site failures  .
- There are different types of commit protocols, such as one-phase, two-phase, and three-phase commit protocols, each with its own advantages and disadvantages    .

## One-phase commit protocol
- A one-phase commit protocol involves a coordinator site that initiates a transaction and communicates with the participating sites to execute it .
- The coordinator site sends a commit request to all the participating sites and waits for their replies .
- If all the participating sites reply with an OK message, the coordinator site commits the transaction and informs the participating sites to do the same .
- If any of the participating sites reply with an ABORT message or fail to reply, the coordinator site aborts the transaction and informs the participating sites to do the same .
- The advantages of this protocol are simplicity and efficiency, as it requires only one round of message exchange between the coordinator and the participating sites .
- The disadvantages of this protocol are lack of fault tolerance and concurrency control, as it does not handle the cases where the coordinator site fails or the participating sites have conflicting transactions .

## Two-phase commit protocol
- A two-phase commit protocol is an extension of the one-phase commit protocol that adds a voting phase to improve the fault tolerance and concurrency control    .
- The two phases of this protocol are the prepare phase and the commit phase    .
- In the prepare phase, the coordinator site sends a prepare request to all the participating sites and waits for their votes    .
- The participating sites execute the transaction locally and write a log record of their decision (commit or abort) before sending their votes to the coordinator site    .
- If all the participating sites vote to commit, the coordinator site decides to commit the transaction and enters the commit phase    .
- In the commit phase, the coordinator site sends a commit request to all the participating sites and waits for their acknowledgments    .
- The participating sites commit the transaction and send an acknowledgment to the coordinator site    .
- If any of the participating sites vote to abort or fail to reply in the prepare phase, the coordinator site decides to abort the transaction and enters the abort phase    .
- In the abort phase, the coordinator site sends an abort request to all the participating sites and waits for their acknowledgments    .
- The participating sites abort the transaction and send an acknowledgment to the coordinator site    .
- The advantages of this protocol are fault tolerance and concurrency control, as it handles the cases where the coordinator or the participating sites fail or have conflicting transactions    .
- The disadvantages of this protocol are blocking and overhead, as it requires two rounds of message exchange and the sites